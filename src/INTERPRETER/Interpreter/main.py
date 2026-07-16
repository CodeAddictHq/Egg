from .env import Env
from .builtin import Fun
from ..Errors.runtime import RuntimeError, NotFoundError, AlreadyExistsError, UnsupportedTypeError, TypeNotAllowed
from ..Errors.loop import StopNodeError, SkipNodeError
from ..Errors.fun import ReturnNodeError
#atu_call funcs

class Interpreter:
  def __init__(self):
    self.ast = None
    self.env = Env()

  def interpret(self, ast):
    self.ast = ast
    self.visit(ast)
    return self.env
  def visit(self, node):
    method = f"visit{node.__class__.__name__}"
    default_method = getattr(self, "visitDefault")
    """
    Get attr needs 3 args 
     1 --> a instance 
     2 --> the attr name what we are looking for 
     3 optional --> a default return if that attr not found. if not given its None
    """
    execute = getattr(self, method, default_method)
    return execute(node)




 #"""Method that does oparetions but not returns something"""
  def visitDefault(self, node):
    raise Exception(f'No visit{type(node).__name__} method found')
  def visitProgrameNode(self, node):
    for statement in node.statements:
      self.visit(statement)
    return None
  def visitVarDeclNode(self, node):
    try:
      var_name = node.name 
      var_val = self.visit(node.value)
      self.env.define(var_name, var_val )
      return None
    except AlreadyExistsError as e:
      raise AlreadyExistsError(e.msg, node.line)
  def visitVarAssignNode(self, node):
    try:
      name = (node.name.identifier)
      value = self.visit(node.value)
      self.env.assign(name, value)
      return None
    except NotFoundError as e:
      raise NotFoundError(e.msg, node.line)
  def visitWhileLoopNode(self, node):
    while self.visit(node.condition):
      self.env = Env(self.env)
      try:
        for i in node.works:
          self.visit(i)
      except StopNodeError:
        break
      except SkipNodeError:
        continue
      finally:
        self.env = self.env.parent
  def visitForLoopNode(self, node):
    typer = Fun()
    one = self.visitOneNode(node.one)
    itr = (node.iterable)
    print(self.visit(itr))
    if not typer.type([self.visit(itr)]) in {"STRING", "ARRAY", "HASH_KEYS", "HASH_VALUES"}:
      if typer.type([self.visit(itr)]) == "HASHMAP":
        raise RuntimeError("HASHMAP directly is not iterable", node.line)
      else:
        raise RuntimeError("Unsupported itareble", node.line)
    for i in self.visit(itr):
      nEnv = Env(self.env)
      self.env = nEnv
      self.env.define(one, i)
      try: 
        for val in node.works:
          self.visit(val)
      except SkipNodeError:
        self.env= self.env.parent
        pass
      except StopNodeError:
        self.env= self.env.parent
        break
      self.env= self.env.parent
  def visitIfStatementNode(self, node):
    try:
      con_if = self.visit(node.con)
    except NotFoundError:
      con_if = False
    if con_if:
      self.env = Env(self.env)
      for i in node.works:
        self.visit(i)
      self.env = self.env.parent
      return 
  
    for i in node.elif_nodes:
      try:
        con_elif = self.visit(i.con)
      except NotFoundError:
        con_elif = None
      if con_elif:
        self.env = Env(self.env)
        for n in i.works:
          self.visit(n)
        self.env = self.env.parent
        return
    if not node.else_node:
      return 
    self.env = Env(self.env)
    for i in node.else_node.works:

      self.visit(i)
    self.env = self.env.parent
    return
  def visitFunDefineNode(self, node):
    try:
      name = node.name.identifier
      works = node.works
      params = node.params 
      self.env.defFun(name, works, params)
    except AlreadyExistsError as e:
      raise AlreadyExistsError(e.msg, node.line)
  def visitVarRmNode(self, node):
    try:
      var = node.var.identifier
      self.env.delitem(var)
    except NotFoundError as e:
      raise NotFoundError(e.msg, node.line)
  def visitFunCallNode(self, node):
    try: 
      name = (node.name.identifier)
      values = []
      Funs = Fun()
      for i in (node.args):
        values.append(self.visit(i))
      found_fun = getattr(Funs, name, False)
      value = None
      if found_fun:
        value = found_fun(values)
      else:
        value = self.CALL(name, values)
      return value
    except NotFoundError as e:
      raise NotFoundError(e.msg, node.line)
  def visitMethodCallNode(self, node):
    try: 
      name = "method_"+str(node.name.identifier)
      values = []
      Funs = Fun()
      for i in (node.args):
        values.append(self.visit(i))
      found_fun = getattr(Funs, name, False)
      value = None
      if found_fun:
        value = found_fun(values)
      return value
    except NotFoundError as e:
      raise NotFoundError(e.msg, node.line)
    except TypeNotAllowed as e:
      raise TypeNotAllowed(e.msg, node.line)
  def CALL(self, name, values):
    fun = self.env.getFun(name)
    params = fun["params"]
    self.env = Env(self.env)
    if len(values) > len(params):
      raise RuntimeError(f"The function {name}(...) takes only {len(params)} arguments but {len(values)} were given ")
    try:
      for idx, i in enumerate(values):
        self.env.define(params[idx], i)
    except IndexError:
      raise RuntimeError()
    try:
      for n in fun["works"]:
        self.visit(n)
    except ReturnNodeError as e:
      self.env = self.env.parent
      return e.value
    self.env = self.env.parent
  def visitFunReturnNode(self, node):
    raise ReturnNodeError(self.visit(node.value), node.line)
  def visitBinInNode(self, node):
    try:
      val = self.visit(node.val)
      var = self.visit(node.var)
      if val in var:
        return True
      else:
        return False
    except TypeError:
      raise UnsupportedTypeError(f'Unsupported type for this oparetion >> {val} in {var}', node.line)
  def visitOneNode(self, node):
    return node.one
  def visitLoopStopNode(self, node):
    raise StopNodeError(node.line)
  def visitLoopSkipNode(self, node):
    raise SkipNodeError(node.line)
  def visitDictNode(self, node):
    dic = {}
    for i in node.dict.keys():
      dic[i] = self.visit(node.dict[i])
    return dic
  def visitListNode(self, node):
    values = []
    for i in node.values:
      values.append(self.visit(i))
    return values
  def visitIntNode(self, node):
    return int(node.value)
  def visitStrNode(self, node):
    return str(node.value)
  def visitFloatNode(self, node):
    return float(node.value)
  def visitBoolNode(self, node):
    return bool(node.value)
  def visitIdentifierNode(self, node):
    try:
      return self.env.get(node.identifier)
    except NotFoundError as e:
      raise NotFoundError(e.msg, node.line)
  def visitBinOpNode(self, node):
    left = self.visit(node.left)
    right = self.visit(node.right)
    opr = node.opr
    try:
      if opr=="+":
        return left+right
      elif opr=="-":
        return left-right
      elif opr=="*":
        return left*right
      elif opr=="^":
        return left**right
      elif opr=="/":
        return left/right
      else:
        raise RuntimeError("Unexpected oparetor", node.line)
    except TypeError as e:
      raise UnsupportedTypeError(f"unsupported operand types >> {left} {opr} {right}", node.line)
    except ZeroDivisionError as e:
      raise RuntimeError(f"(o≧▽≦)ﾉ Dont know basic math ? ZeroDivisionError >> {left} {opr} {right}", node.line)
  def visitBinCompNode(self, node):
    left = self.visit(node.left)
    right = self.visit(node.right)
    comp = node.comp
    try:
      if comp==">":
        return left>right
      elif comp=="<":
        return left<right
      elif comp=="and":
        return left and right
      elif comp=="or":
        return left or right
      elif comp==">_":
        return left>=right
      elif comp=="<_":
        return left<=right
      elif comp=="is":
        return left==right
      elif comp=="isnot":
        return left!=right
      else:
        raise UnsupportedTypeError(f"Unexpected comparison oparetor >> {left} {opr} {right}", node.line)
    except:
      raise UnsupportedTypeError(f"Unexpected comparison oparetor >> {left} {comp} {right}", node.line)
  def visitUnaryOpNode(self, node):
    opr = node.opr 
    value = None
    try:
      value = self.visit(node.val)
    except NotFoundError:
      value = False
      
    if opr == "-":
      try:
        return int(f'{opr}{value}')
      except ValueError:
        return float(f'{opr}{value}')
      except ValueError:
        raise RuntimeError()
    elif opr == "not":
      if value:
        return False
      elif not value:
        return True
    else :
      raise RuntimeError("Unexpected unary oparetor", node.line)
  def visitNoneType(self, node):
    return None
  def visitListAccessNode(self, node):
    li = self.visit(node.li)
    idx = self.visit(node.idx)
    try:
      return (li[idx])
    except IndexError as e:
      raise RuntimeError(f"List index out of range >> {node.li.identifier}[{idx}] not exists yet ")
  def visitDictAccessNode(self, node):
    try:
      child = node.child.identifier
      parent = self.visit(node.parent)
      return parent[child]
    except NotFoundError as e:
      raise NotFoundError(e.msg, node.line)
  def visitDictUpdateNode(self, node):
    path = []
    val = self.visit(node.value)
    for i in node.dic:
        if not isinstance(i, str):
          path.append(self.visit(i))
        else:
          path.append(i)
    try:
      self.Update(path, val, node)
    except KeyError:
      try:
        self.prev_env(node)
      except KeyError:
        st = str(path[0])
        for i in range(1, len(path)):
          if isinstance(path[i], int):
            st = st +f"[{path[i]}]"
          else:
            st = st +"."+path[i]
        raise NotFoundError(f"Element not found in var >> {st}", node.line)
  def visitListUpdateNode(self, node):
    path = []
    val = self.visit(node.value)
    for i in node.lis:
      if not isinstance(i, str):
        path.append(self.visit(i))
      else:
        path.append(i)
    try:
      self.Update(path, val, node)
    except KeyError:
      self.prev_env(node)
    except IndexError or NotFoundError:
      st = str(path[0])
      for i in range(1, len(path)):
        if isinstance(path[i], int):
          st = st +f"[{path[i]}]"
        else:
          st = st +"."+path[i]
          
      raise NotFoundError(f"Element not found in var >> {st}", node.line)
  def Update(self, path, val, node):
    try:
      memo = self.env.vars[path[0]]
      for i in range(1, len(path)-1):
        memo = memo[path[i]]
      memo[path[-1]] = val
    except TypeError:
      raise UnsupportedTypeError("Unsupported oparetion trying ", node.line)
  def prev_env(self, node):
    if not self.env.parent:
      raise NotFoundError()
    prev_env = self.env
    self.env = self.env.parent 
    self.visit(node)
    self.env = prev_env
