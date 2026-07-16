from .tokens import TOKEN
from ..ToolKit.dataops import NUMBER_OPS, STRING_OPS


  
class Lexer:
  digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
  keywords = {'var', 'and', 'or', 'in', "not", 'stop', 'skip', 'return', "rm", "in"}
  equal = '='
  comment = '€'
  statements = {'if', 'elif', 'else', 'fun', 'while', 'for'}
  bools = {'TRUE', 'FALSE'}
  oprs = {'+', '-', '*', '/', '^'}
  comps = {'>', '<', '>_', '<_', 'is', 'isnot'}
  null = "NONE"
  symbs = {".", ",", '=', ':'}
  def __init__(self):
    self.code = None 
    self.idx = 0
    self.tokens = []
    self.memo = ''
    self.line = 1
    self.i = 0
  def tokenise(self, code):
    self.code = code 
    return self.get_tokens()
  #main loop
  def get_tokens(self):
    while self.idx < len(self.code):
   #   print(self.idx, repr(self.code[self.idx]), repr(self.memo))
      if self.code[self.idx] in Lexer.symbs:
        self.flush_memo()
        self.memo += self.code[self.idx]
        self.symb(self.memo, self.line)
        self.clear_memo()
      elif self.code[self.idx] in Lexer.oprs:
        self.flush_memo()
        self.memo += self.code[self.idx]
        self.opr(self.memo, self.line)
        self.clear_memo()
      elif self.code[self.idx] == '€':
        self.flush_memo()
        cmt = STRING_OPS(self.code).get_comment('€', self.idx)
        
        self.comment(cmt[0], self.line)
        self.clear_memo()
        if cmt[1] > len(self.code)-1:
          break 
        self.idx = cmt[1]
        continue
      elif self.code[self.idx] in Lexer.comps:
        self.flush_memo()
        a = self.get_comp()
        self.memo += a
        self.word(self.memo, self.line)
        self.clear_memo()
        continue
      elif self.code[self.idx] in Lexer.digits and  not self.memo:
        num = STRING_OPS(self.code).get_num(self.idx)
        self.number(num[0], self.line)
        self.clear_memo()
        if num[1] > len(self.code)-1:
          break 
        self.idx = num[1]
        continue
      elif self.code[self.idx] == '"' or self.code[self.idx] == "'":
        self.flush_memo()
        s = STRING_OPS(self.code).get_string(self.idx)
        self.string(s[0], self.line)
        if s[1] > len(self.code)-1:
          break 
        self.idx = s[1]
        continue
      elif self.code[self.idx] =='(' or self.code[self.idx] ==')':
        self.flush_memo()
        self.memo += self.code[self.idx]
        self.per(self.memo, self.line)
        self.clear_memo()
      elif self.code[self.idx] =='[' or self.code[self.idx] ==']':
        self.flush_memo()
        self.memo += self.code[self.idx]
        self.sqbrackets(self.memo, self.line)
        self.clear_memo()
      elif self.code[self.idx] =='{' or self.code[self.idx] =='}':
        self.flush_memo()
        self.memo += self.code[self.idx]
        self.qer(self.memo, self.line)
        self.clear_memo()
      elif self.code[self.idx] == '\n':
        self.flush_memo()
        self.memo += self.code[self.idx]
        self.new_line(self.memo, self.line)
        self.clear_memo()
      else:
        if self.code[self.idx] in ' ' :
          pass
        else:
          self.memo += self.code[self.idx]
      
      if self.code[self.idx].isspace():
        self.word(self.memo, self.line)
        self.clear_memo()
      self.next()
    self.flush_memo()
    self.tokens.append(TOKEN("END OF PROGRAME", "EOF", None))
    return self.tokens
    
  #Token making methods
  def symb(self, token, line):
    if token == '=':
      self.tokens.append(TOKEN(token, 'SYMB_EQ', line))
    elif token == ',':
      self.tokens.append(TOKEN(token, 'SYMB_COMMA', line))
    elif token == ':':
      self.tokens.append(TOKEN(token, 'SYMB_COLON', line))
    elif token == '.':
      self.tokens.append(TOKEN(token, 'SYMB_DOT', line))
    else:
      self.tokens.append(TOKEN(token, 'SYMB_UNDEFINED', line))
  def string(self, token, line):
    if not token:
      return
    if token.startswith(token[0]) and token.endswith(token[0]) and len(token)>1:
      fine_str = STRING_OPS(token).get_fine_str()
      self.tokens.append(TOKEN(rf'{fine_str}', 'STR_CLOSED', line))
    else:
      self.tokens.append(TOKEN(token, 'STR_UNCLOSED', line))
  def opr(self, token, line):
    if token == '+':
      self.tokens.append(TOKEN(token, 'OPR_PLUS', line))
    elif token == '-':
      self.tokens.append(TOKEN(token, 'OPR_MINUS', line))
    elif token == '*':
      self.tokens.append(TOKEN(token, 'OPR_MULTIPLY', line))
    elif token == '/':
      self.tokens.append(TOKEN(token, 'OPR_DIVIDE', line))
    elif token == '^':
      self.tokens.append(TOKEN(token, 'OPR_POW', line))
    else:
      self.tokens.append(TOKEN(token, 'OPR_UNDEFINED', line))
  def new_line(self, token, line):
    if self.tokens:
      if self.tokens[-1].value == '{' or self.tokens[-1].value == '['or self.tokens[-1].value == ';':
        pass
      else:
        self.tokens.append(TOKEN(';', 'NEW_LINE', line))
  def comment(self, token, line):
    self.tokens.append(TOKEN(token, 'COMMENT', line))
  def per(self, token, line):
    if token == '(':
      self.tokens.append(TOKEN(token, 'PRSTART', line))
    elif token == ')':
      self.tokens.append(TOKEN(token, 'PREND', line))
  def qer(self, token, line):
    if token == '{':
      self.tokens.append(TOKEN(token, 'CBSTART', line))
    elif token == '}':
      self.tokens.append(TOKEN(token, 'CBEND', line))
  def sqbrackets(self, token, line):
    if token == '[':
      self.tokens.append(TOKEN(token, 'SQBSTART', line))
    elif token == ']':
      self.tokens.append(TOKEN(token, 'SQBEND', line))
  def keyword(self, token, line):
    if token == 'var':
      self.tokens.append(TOKEN(token, 'KW_VAR', line))
    elif token == 'and':
      self.tokens.append(TOKEN(token, 'KW_AND', line))
    elif token == 'in':
      self.tokens.append(TOKEN(token, 'KW_IN', line))
    elif token == 'rm':
      self.tokens.append(TOKEN(token, 'KW_RM', line))
    elif token == 'return':
      self.tokens.append(TOKEN(token, 'KW_RETURN', line))
    elif token == 'not':
      self.tokens.append(TOKEN(token, 'KW_NOT', line))
    elif token == 'in':
      self.tokens.append(TOKEN(token, 'KW_IN', line))
    elif token == 'or':
      self.tokens.append(TOKEN(token, 'KW_OR', line))
    elif token == 'stop':
      self.tokens.append(TOKEN(token, 'KW_STOP', line))
    elif token == 'skip':
      self.tokens.append(TOKEN(token, 'KW_SKIP', line))
    else:
      self.tokens.append(TOKEN(token, 'KW_UNDEFINED', line))
  def statement(self, token, line):
    if token == 'if':
      self.tokens.append(TOKEN(token, 'ST_IF', line))
    elif token == 'elif':
      self.tokens.append(TOKEN(token, 'ST_ELIF', line))
    elif token == 'else':
      self.tokens.append(TOKEN(token, 'ST_ELSE', line))
    elif token == 'fun':
      self.tokens.append(TOKEN(token, 'ST_FUN', line))
    elif token == 'while':
      self.tokens.append(TOKEN(token, 'ST_WHILE', line))
    elif token == 'for':
      self.tokens.append(TOKEN(token, 'ST_FOR', line))
    else:
      self.tokens.append(TOKEN(token, 'ST_UNDEFINED', line))
  def compare(self, token, line):
    if token == 'is':
      self.tokens.append(TOKEN(token, 'CP_EQ', line))
    elif token == '>':
      self.tokens.append(TOKEN(token, 'CP_GT', line))
    elif token == '<':
      self.tokens.append(TOKEN(token, 'CP_LT', line))
    elif token == '>_':
      self.tokens.append(TOKEN(token, 'CP_GTE', line))
    elif token == '<_':
      self.tokens.append(TOKEN(token, 'CP_LTE', line))
    elif token == 'isnot':
      self.tokens.append(TOKEN(token, 'CP_NEQ', line))
    else:
      self.tokens.append(TOKEN(token, 'CP_UNDEFINED', line))
  def bool(self, token, line):
    if token == 'TRUE':
      self.tokens.append(TOKEN(token, 'BOOL_TRUE', line))
    elif token == 'FALSE':
      self.tokens.append(TOKEN(token, 'BOOL_FALSE', line))
    else:
      self.tokens.append(TOKEN(token, 'BOOL_UNDEFINED', line))
  def word(self, token, line):
    token = token.strip()
    if token in '\n \t ':
      pass 
    elif token in Lexer.keywords:
      self.keyword(token, line)
    elif token in Lexer.statements:
      self.statement(token, line)
    elif token in Lexer.comps:
      self.compare(token, line)
    elif token in Lexer.bools:
      self.bool(token, line)
    elif token == 'NONE':
      self.tokens.append(TOKEN(token, 'NONE', line))
    else:
      self.tokens.append(TOKEN(token, 'IDENTIFIER', line))
  def number(self, token, line):
    if type(token) == type(1):
      self.tokens.append(TOKEN(token, 'NUM_INT', line))
    elif type(token) == type(1.0):
      self.tokens.append(TOKEN(token, 'NUM_FLOAT', line))

  #Helper methods 
  def next(self):
    if repr(self.code[self.idx]) == repr('\n'):
      self.line += 1
    self.idx += 1
  def clear_memo(self):
    self.memo = ''
  def flush_memo(self):
    self.memo.strip()
    if self.memo:
      self.word(self.memo, self.line)
      self.memo = ""
  def get_comp(self):
    c = self.code[self.idx]
    if self.code[self.idx] in '<>' and self.idx + 1 < len(self.code):
      c = self.code[self.idx]+self.code[self.idx+1]
      if c == '>_':
        self.next()
        self.next()
        return c
      elif c == '<_':
        self.next()
        self.next()
        return c
      elif ( c[0] in '<>')  and( not c[1] == '_'):
        self.next()
        return c[0]
    else:
      self.next()
      return c
  def __str__(self):
    return "EGG LEXER"