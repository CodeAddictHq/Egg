from .nodes import (
  ProgrameNode,
  VarDeclNode,
  BinOpNode,
  BinInNode,
  VarAssignNode,
  IfStatementNode,
  FunCallNode,
  FunDefineNode,
  StatementNode,
  BinCompNode,
  ElifStatementNode,
  ElseStatementNode,
  FunReturnNode,
  ForLoopNode,
  WhileLoopNode,
  UnaryOpNode,
  LoopStopNode,
  LoopSkipNode,
  ListNode,
  DictNode,
  DictAccessNode,
  ListAccessNode,
  IdentifierNode,
  StrNode,
  IntNode,
  FloatNode,
  BoolNode,
  VarRmNode,
  OneNode,
  DictUpdateNode,
  ListUpdateNode,
  MethodCallNode,
)
from ..Lexer.tokens import TOKEN

from ..Errors.syntex import SyntexError


TOKENS = {
    # KEYWORDS
    "KW_VAR": "var",
    "KW_AND": "and",
    "KW_OR": "or",
    "KW_IN": "in",
    "KW_NOT": "not",
    "KW_STOP": "stop",
    "KW_SKIP": "skip",

    # STATEMENTS
    "ST_IF": "if",
    "ST_ELIF": "elif",
    "ST_ELSE": "else",
    "ST_FUN": "fun",
    "ST_WHILE": "while",
    "ST_FOR": "for",

    # COMPARISONS
    "CP_GT": ">",
    "CP_LT": "<",
    "CP_GTE": ">_",
    "CP_LTE": "<_",
    "CP_EQ": "is",

    # OPERATORS
    "OPR_PLUS": "+",
    "OPR_MINUS": "-",
    "OPR_MULTIPLY": "*",
    "OPR_DIVIDE": "/",
    "OPR_POW": "^",

    # LITERALS
    "NUM_INT": "[0-9]+",
    "NUM_FLOAT": "[0-9]+\\.[0-9]+",
    "STR_CLOSED": "'...'",
    "STR_UNCLOSED": None,
    "BOOL_TRUE": "TRUE",
    "BOOL_FALSE": "FALSE",

    # BRACKETS
    "PRSTART": "(",
    "PREND": ")",
    "CBSTART": "{",
    "CBEND": "}",

    # OTHERS
    "IDENTIFIER": "[a-zA-Z_][a-zA-Z0-9_]*",
    "COMMENT": "€",
    "NEW_LINE": "\\n",
    "EOF": "EOF",

    # SYMBOLS
    "SYMB_DOT": ".",
    "SYMB_EQ": "=",
    "SYMB_COMMA": ",",
    "SYMB_COLON": ":"
}
class Parser:
  mul_op_tokens = {'OPR_DIVIDE', 'OPR_MULTIPLY'}
  factor_tokens = {'NUM_INT', 'NUM_FLOAT', 'IDENTIFIER', 'BOOL_TRUE', 'BOOL_FALSE', 'STR_CLOSED', 'NONE'}
  add_opr_tokens = {'OPR_MINUS', 'OPR_PLUS'}
  bool_tokens = {'BOOL_TRUE', 'BOOL_FALSE'}
  comp_tokens = {'CP_GT', 'CP_LT', 'CP_GTE', 'CP_LTE', 'CP_EQ', 'CP_NEQ'} 
  unary_tokens = {'OPR_PLUS', 'OPR_MINUS', 'KW_NOT'}
  itarable_tokens = {'IDENTIFIER'}
  def __init__(self):
    self.tokens = None
    self.idx = None
    self.current_token = None
    self.tree = ProgrameNode([])
  
  #Helper functions 
  def next(self):
    if self.idx < len(self.tokens) - 1:
        self.idx += 1
        self.current_token = self.tokens[self.idx]
  def eat(self, type):
    if self.current_token.type == type:
      value = self.current_token.value
      self.next()
      return value
    else:
      line = self.current_token.line
      if not line:
        line = self.tokens[self.idx-1].line
      raise SyntexError(
    f"Expected {type}, got   {self.current_token.type}('{self.current_token.value}')",
    line)
  def parse(self, tokens):
    self.tokens = tokens
    self.idx = 0
    self.current_token = self.tokens[self.idx]
    self.statement()
    return self.tree

  
  
  #Main loops
  def statement(self):
    while self.current_token.type != "EOF":
      if self.current_token.type == "KW_VAR":
        node = self.varDeclear()
        self.tree.append(node)
      elif self.current_token.type == "COMMENT":
        self.next()
      elif self.current_token.type == "KW_RM":
        node = self.rm()
        self.tree.append(node)
      elif self.current_token.type == "IDENTIFIER":
        if self.tokens[self.idx+1].type== "PRSTART":
          node = self.funCall()
          self.tree.append(node)      
        elif self.tokens[self.idx+1].type== "SYMB_DOT" :
          try:
            if self.tokens[self.idx+3].type== "PRSTART":
              node =self.methodCall()
              self.tree.append(node)  
            else:
              node =self.dictUpdate()
              self.tree.append(node) 
          except IndexError:
            raise SyntexError(f"Invalid syntex >> {self.current_token.value}", self.current_token.line)
        elif self.tokens[self.idx+1].type== "SQBSTART":
          node = self.listUpdate()
          self.tree.append(node)      
        else:
          node = self.varAssign()
          self.tree.append(node)

      elif self.current_token.type == "NEW_LINE":
        self.next()
      elif self.current_token.type == "ST_FOR":
        node = self.forLoop()
        self.tree.append(node)
      elif self.current_token.type == "ST_WHILE":
        node = self.whileLoop()
        self.tree.append(node)
      elif self.current_token.type == "ST_FUN":
        node = self.defFun()
        self.tree.append(node)
      elif self.current_token.type == "ST_IF":
        node = self.ifStatement()
        self.tree.append(node)
      elif self.current_token.type == "NEW_LINE":
        self.next()
      else:
        lin = self.current_token.line
        if not self.current_token.line:
          lin = self.tokens[self.idx-1].line
        raise SyntexError(f"Invalid syntex >> {self.current_token.value}", lin)
  def block(self):
    sts = []
    while self.current_token.type != "CBEND":
      if self.current_token.type == "KW_VAR":
        sts.append(self.varDeclear())
      elif self.current_token.type == "KW_RM":
        node = self.rm()
        sts.append(node)
      elif self.current_token.type == "ST_FOR":
        node = self.forLoop()
        sts.append(node)
      elif self.current_token.type == "KW_STOP":
        node = LoopStopNode(self.current_token.line)
        self.next()
        sts.append(node)
      elif self.current_token.type == "KW_SKIP":
        node = LoopSkipNode(self.current_token.line)
        self.next()
        sts.append(node)
      elif self.current_token.type == "ST_WHILE":
        node = self.whileLoop()
        sts.append(node)
      elif self.current_token.type == "IDENTIFIER":
        if self.tokens[self.idx+1].type== "PRSTART":
          node = self.funCall()
          sts.append(node)      
        elif self.tokens[self.idx+1].type== "SYMB_DOT" :
          try:
            if self.tokens[self.idx+3].type== "PRSTART":
              node =self.methodCall()
              sts.append(node)  
            else:
              node =self.dictUpdate()
              sts.append(node) 
          except IndexError:
            raise SyntexError(f"Invalid syntex >> {self.current_token.value}", self.current_token.line)
        elif self.tokens[self.idx+1].type== "SQBSTART":
          node = self.listUpdate()
          sts.append(node)  
        else:
          node = self.varAssign()
          sts.append(node)
      elif self.current_token.type == "COMMENT":
        self.next()
      elif self.current_token.type == "KW_RETURN":
        sts.append(self.returnStatement())
      elif self.current_token.type == "ST_FUN":
        sts.append(self.defFun())
      elif self.current_token.type == "ST_IF":
        st = self.ifStatement()
        sts.append(st)
      elif self.current_token.type == "NEW_LINE":
        self.next()
      else:
        lin = self.current_token.line
        if not self.current_token.line:
          lin = self.tokens[self.idx-1].line
        raise SyntexError(f"Invalid syntex >> {self.current_token.value}", lin)
    return sts

  #specific cases
  def varDeclear(self):
    line = self.current_token.line  
    self.eat("KW_VAR")
    name = self.eat("IDENTIFIER")
    self.eat("SYMB_EQ")
    value =  self.expression()
    return VarDeclNode(name, value, line)
  def varAssign(self):
    line = self.current_token.line  
    parent = IdentifierNode(self.eat('IDENTIFIER'), line)
    while self.current_token.type == "SYMB_DOT":
      self.eat('SYMB_DOT')
      child = IdentifierNode(self.eat('IDENTIFIER'), line)
      parent = DictAccessNode(parent, child, line)
    if self.current_token.type =="SQBSTART":
      self.eat('SQBSTART')
      idx = self.expression()
      self.eat('SQBEND')
      parent = ListAccessNode(parent, idx, line)
    self.eat('SYMB_EQ')
    value =  self.expression()
    return VarAssignNode(parent, value, line)
  def ifStatement(self):
    line_if = self.current_token.line  
    elif_blocks = []
    else_block = None
    self.eat('ST_IF')
    self.eat('PRSTART')
    condition_if = self.expression()
    self.eat('PREND')
    self.eat('CBSTART')
    statements_if = self.block()
    self.eat('CBEND')
    while self.current_token.type == "NEW_LINE":
      self.eat('NEW_LINE')
    while self.current_token.type == "ST_ELIF":
      line_elf = self.current_token.line  
      self.eat('ST_ELIF')
      self.eat('PRSTART')
      condition_elif = self.expression()
      self.eat('PREND')
      self.eat('CBSTART')
      statements_elif = self.block()
      self.eat('CBEND')
      elif_blocks.append(ElifStatementNode(condition_elif, statements_elif, line_elf))
    while self.current_token.type == "NEW_LINE":
      self.eat('NEW_LINE')
    if self.current_token.type == "ST_ELSE":
      line_els = self.current_token.line 
      self.eat('ST_ELSE')
      self.eat('CBSTART')
      statements_else= self.block()
      self.eat('CBEND')
      else_block = ElseStatementNode( statements_else, self.current_token.line)
    return IfStatementNode(condition_if, statements_if, elif_blocks, else_block, line_if)
  def funCall(self):
    line = self.current_token.line  
    name = IdentifierNode(self.eat("IDENTIFIER"), line)
    self.eat("PRSTART")
    args = self.arg()
    self.eat("PREND")
    return FunCallNode(name, args, line)
  def defFun(self):
    line = self.current_token.line  
    self.eat("ST_FUN")
    name = IdentifierNode(self.eat("IDENTIFIER"), line)
    self.eat("PRSTART")
    params = self.params()
    self.eat("PREND")
    self.eat("CBSTART")
    statements = self.block()
    self.eat("CBEND")
    return FunDefineNode(name, params, statements, line)
  def forLoop(self):
    line = self.current_token.line  
    self.eat("ST_FOR")
    self.eat("PRSTART")
    one = OneNode(self.eat("IDENTIFIER"), line)
    self.eat("KW_IN")
    itarable = self.itarable()
    self.eat("PREND")
    self.eat("CBSTART")
    works = self.block()
    self.eat("CBEND")
    return ForLoopNode(one, itarable, works, line)
  def whileLoop(self):
    line = self.current_token.line  
    self.eat("ST_WHILE")
    self.eat("PRSTART")
    condition = self.expression()
    self.eat("PREND")
    self.eat("CBSTART")
    works = self.block()
    self.eat("CBEND")
    return WhileLoopNode(condition, works, line)
  def returnStatement(self):
    self.eat("KW_RETURN")
    a = FunReturnNode(self.expression(), self.current_token.line)
    return a
  def varAccess(self):
    line = self.current_token.line
    left = IdentifierNode(self.eat("IDENTIFIER"), self.current_token.line)
    while self.current_token.type == "SYMB_DOT" or self.current_token.type == "SQBSTART":
      if self.current_token.type == "SYMB_DOT":
        self.eat("SYMB_DOT")
        right = IdentifierNode(self.eat("IDENTIFIER"), self.current_token.line)
        left = DictAccessNode(left, right, self.current_token.line)
      elif self.current_token.type == "SQBSTART":
        self.eat("SQBSTART")
        idx = self.expression()
        self.eat("SQBEND")
        left = ListAccessNode(left, idx, self.current_token.line)
      else:
        raise SyntexError("Invalid syntex", line)
    return left
  def methodCall(self):
    var = IdentifierNode(self.eat("IDENTIFIER"))
    self.eat("SYMB_DOT")
    method = IdentifierNode(self.eat("IDENTIFIER"))
    self.eat("PRSTART")
    args = self.arg()
    args.append(var)
    self.eat("PREND")
    return MethodCallNode(method, args, self.current_token.line)
  def dictUpdate(self):
    line = self.current_token.line
    dic = self.varUpdate()
    self.eat("SYMB_EQ")
    val = self.expression()
    return DictUpdateNode(dic, None, val, line)
  def listUpdate(self):
    line = self.current_token.line
    lis = self.varUpdate()
    self.eat("SYMB_EQ")
    val = self.expression()
    return ListUpdateNode(lis, None, val, line)
  def varUpdate(self):
    line = self.current_token.line
    path = [self.eat("IDENTIFIER")]
    while self.current_token.type != "SYMB_EQ":
      if self.current_token.type == "SYMB_DOT":
        self.eat("SYMB_DOT")
        child = self.eat("IDENTIFIER")
        path.append(child)
      elif self.current_token.type == "SQBSTART":
        self.eat("SQBSTART")
        idx = self.expression()
        self.eat("SQBEND")
        path.append(idx)
      else:
        raise SyntexError(f"Invalid syntex >> {self.current_token.value}", line)
    return path
  

  #Main parsing  methods
  
  #fun 
  def arg(self):
    args = []
    while self.current_token.type != "PREND":
      while self.current_token.type in {'NEW_LINE', "COMMENT"}:
        self.next()
      args.append(self.expression())
      if self.current_token.type == "SYMB_COMMA":
        self.eat("SYMB_COMMA")
      while self.current_token.type in {'NEW_LINE', 'SYMB_COMMA'}:
        self.next()
    return args
    
    #expression chain 
     
    #list
  def params(self):
    params = []
    li =[]
    while self.current_token.type != "PREND":
      if self.current_token.value in li:
        raise SyntexError(f"Function params can't be duplicate >> {self.current_token.value}", self.current_token.line)
      li.append(self.current_token.value)
      params.append(IdentifierNode(self.eat("IDENTIFIER"), self.current_token.line))
      if self.current_token.type == "SYMB_COMMA":
        self.eat("SYMB_COMMA")
    return params
  
  #list and dict
  def li_els(self):
    els = []
    while self.current_token.type != "SQBEND":
      while self.current_token.type in {'NEW_LINE', "COMMENT"}:
        self.next()
      if self.current_token.type == "STR_UNCLOSED":
        raise SyntexError(f"Unclosed string is not valid >> {self.current_token.value}", self.current_token.line)
      else:
        els.append(self.expression())
      if self.current_token.type == "SYMB_COMMA":
        self.eat("SYMB_COMMA")
      while self.current_token.type in {'NEW_LINE', 'SYMB_COMMA'}:
        self.next()
    return els
  def di_els(self):
    els = {}
    while self.current_token.type != "CBEND":
      while self.current_token.type in {'NEW_LINE', 'COMMENT'}:
        self.next()
      name = self.eat("IDENTIFIER")
      self.eat("SYMB_COLON")
      value = self.expression()
      els[name] = value
      if self.current_token.type == "SYMB_COMMA":
        self.eat("SYMB_COMMA")
      while self.current_token.type in {'NEW_LINE', 'SYMB_COMMA'}:
        self.next()
    return els
    
    
    
    #expression chain 

  
  
  
  
  #main expressions
  def expression(self):
    val = self.parse_or()
    return val
  def parse_or(self):
    left = self.parse_and()
    while self.current_token.type  == "KW_OR":
      comp = self.current_token.value 
      self.next()
      right = self.parse_and()
      left = BinCompNode(comp, left, right, self.current_token.line)
    return left
  def parse_and(self):
    left = self.parse_in()
    while self.current_token.type  == "KW_AND":
      comp = self.current_token.value 
      self.next()
      right = self.parse_in()
      left = BinCompNode(comp, left, right, self.current_token.line)
    return left
  def parse_in(self):
    val = self.comparison()
    while self.current_token.type  == "KW_IN":
      self.eat("KW_IN")
      var = self.comparison()
      val = BinInNode(val, var, self.current_token.line)
    return val
  def comparison(self):
    left = self.algexpr()
    while self.current_token.type in Parser.comp_tokens:
        comp = self.current_token.value 
        self.next()
        right = self.algexpr()
        left = BinCompNode(comp, left, right, self.current_token.line)
    
    return left
  def algexpr(self):
    left = self.algeterm()
    while self.current_token.type in Parser.add_opr_tokens:
      opr = self.current_token.value
      self.next()
      right = self.algeterm()
      left = BinOpNode(opr, left, right, self.current_token.line)
    return left
  def algeterm(self):
    left = self.power()
    while self.current_token.type in Parser.mul_op_tokens:
      opr = self.current_token.value
      self.next()
      right = self.power()
      left = BinOpNode(opr, left, right, self.current_token.line)
    return left
  def power(self):
    base = self.unary()
    if self.current_token.type == "OPR_POW":
      symb = self.current_token.value
      self.next()
      power = self.power()
      base = BinOpNode(symb, base, power, self.current_token.line)
    return base
  def unary(self):
    if self.current_token.type in Parser.unary_tokens :
      opr = self.current_token.value
      self.next()
      val = self.unary()  
      return UnaryOpNode(opr, val, self.current_token.line)
    else:
        return self.atom()
  def atom(self):
    if self.current_token.type == "IDENTIFIER" :
      if self.tokens[self.idx + 1].type=="PRSTART" :
        value = self.funCall()
        return value
      elif self.tokens[self.idx + 1].type=="SYMB_DOT" and self.tokens[self.idx+3].type== "PRSTART" :
        node = self.methodCall()
        return node
      elif self.tokens[self.idx + 1].type=="SQBSTART" or self.tokens[self.idx + 1].type=="SYMB_DOT":
        node = self.varAccess()
        return node
      else: 
        node = IdentifierNode(self.eat("IDENTIFIER"), self.current_token.line)
        return node
    elif self.current_token.type in Parser.factor_tokens:
      if self.current_token.type == 'NUM_INT':
        return IntNode(int(self.eat('NUM_INT')), self.current_token.line)
      elif self.current_token.type == 'NUM_FLOAT':
        return FloatNode(float(self.eat('NUM_FLOAT')), self.current_token.line)
      elif self.current_token.type == 'IDENTIFIER':
        return IdentifierNode(self.eat('IDENTIFIER'), self.current_token.line)
      elif self.current_token.type == 'BOOL_TRUE':
        self.eat('BOOL_TRUE')
        return BoolNode(True, self.current_token.line)
      elif self.current_token.type == 'BOOL_FALSE':
        self.eat('BOOL_FALSE')
        return BoolNode(False, self.current_token.line)
      elif self.current_token.type == 'STR_CLOSED':
        return StrNode(self.eat('STR_CLOSED'), self.current_token.line)
      elif self.current_token.type == 'NONE':
        self.eat('NONE')
        return None
      else:
        raise SyntexError(f"Invalid syntex >> {self.current_token.value}", self.current_token.line)
      return value
    elif self.current_token.type == "PRSTART":
      self.eat("PRSTART")
      value = self.expression()
      self.eat("PREND")
      return value
    elif self.current_token.type == "SQBSTART":
      line = self.current_token.line  
      self.eat("SQBSTART")
      liels = self.li_els()
      self.eat("SQBEND")
      return ListNode(liels, line)
    elif self.current_token.type == "CBSTART":
      line = self.current_token.line  
      self.eat("CBSTART")
      di_els = self.di_els()
      self.eat("CBEND")
      return DictNode(di_els, line)
    else:
      lin = self.current_token.line
      if not self.current_token.line:
        lin = self.tokens[self.idx-1].line
      raise SyntexError(f"Invalid syntex >> {self.current_token.value}", lin)
      
      
    #itarable 
  def itarable(self):
    return self.atom()
  def rm(self):
    line = self.current_token.line
    self.eat("KW_RM")
    name = IdentifierNode(self.eat("IDENTIFIER"), self.current_token.line)
    return VarRmNode(name, line)