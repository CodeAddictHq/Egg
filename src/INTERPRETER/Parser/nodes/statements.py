class FunCallNode:
  def __init__(self, name, args=None, line=0):
    self.name = name
    self.args = args
    self.line = line

  def __repr__(self):
    return f"FunCallNode(name={self.name!r}, args={self.args!r}, line={self.line})"
class MethodCallNode:
  def __init__(self, name, args=None, line=0):
    self.name = name
    self.args = args
    self.line = line

  def __repr__(self):
    return f"MethodCallNode(name={self.name!r}, args={self.args!r}, line={self.line})"

class FunDefineNode:
  def __init__(self, name, params=None, statements=None, line=0):
    self.name = name
    self.params = params
    self.works = statements
    self.line = line

  def __repr__(self):
    return f"FunDefineNode(name={self.name!r}, params={self.params!r}, statements={self.works!r}, line={self.line})"




class FunReturnNode:
  def __init__(self, value, line=0):
    self.value = value
    self.line = line

  def __repr__(self):
    return f"FunReturnNode(value={self.value!r}, line={self.line})"


class ElifStatementNode:
  def __init__(self, con, works=None, line=0):
    self.con = con
    self.works = works or []
    self.line = line

  def __repr__(self):
    return f"ElifStatementNode(con={self.con!r}, works={self.works!r}, line={self.line})"

  

class ElseStatementNode:
  def __init__(self, works=None, line=0):
    self.works = works or []
    self.line = line

  def __repr__(self):
    return f"ElseStatementNode(works={self.works!r}, line={self.line})"




class IfStatementNode:
  def __init__(self, con, works=None, elif_nodes=None, else_node=None, line=0):
    self.con = con
    self.works = works or []
    self.elif_nodes = elif_nodes or []
    self.else_node = else_node
    self.line = line

  def __repr__(self):
    return (
      f"IfStatementNode("
      f"con={self.con!r}, "
      f"works={self.works!r}, "
      f"elif_nodes={self.elif_nodes!r}, "
      f"else_node={self.else_node!r}"
      f"line={self.line})"
      
    )

  


class ForLoopNode:
  def __init__(self, one, iterable, works=None, line=0):
    self.one = one
    self.iterable = iterable
    self.works = works or []
    self.line = line

  def __repr__(self):
    return f"ForLoopNode(one={self.one!r}, iterable={self.iterable!r}, works={self.works!r}, line={self.line})"


class WhileLoopNode:
  def __init__(self, condition, works=None, line=0):
    self.condition = condition
    self.works = works or []
    self.line = line

  def __repr__(self):
    return f"WhileLoopNode(condition={self.condition!r}, works={self.works!r}, line={self.line})"




class OneNode:
  def __init__(self, one, line=0):
    self.one = one
    self.line = line

  def __repr__(self):
    return f"OneNode(one={self.one!r}, line={self.line})"



class LoopStopNode:
  def __init__(self, line=0):
    self.line = line

  def __repr__(self):
    return f"LoopStopNode(line={self.line})"



class LoopSkipNode:
  def __init__(self, line=0):
    self.line = line

  def __repr__(self):
    return f"LoopSkipNode(line={self.line})"




class StatementNode:
  def __init__(self, statements=None, line=0):
    self.statements = statements or []
    self.line = line

  def append(self, val):
    self.statements.append(val)

  def __repr__(self):
    return f"StatementNode(statements={self.statements!r}, line={self.line})"

