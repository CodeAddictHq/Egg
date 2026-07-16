class NUMBER_OPS:
  symbs = {'0','1','2','3','4','5','6','7','8','9','+','-','.'}
  digits = {'0','1','2','3','4','5','6','7','8','9'}
  oprs = {'+', '-'}

  def __init__(self, main):
    main = main.strip()

    self.main = main
    self.opr = ''
    self.num = ['', '']   # [before-dot, after-dot]
    self.dot_count = 0
    self.typ = ''
    self.organise()

  def get_num(self):
    try:
      return int(self.main)
    except ValueError:
      return float(self.main)
  
  def organise(self):
    pass

  def is_int(self):
    return self.typ == 'int'

  def is_float(self):
    return self.typ == 'float'

  def in_float(self):
    return float(self.main)

  def in_int(self):
    if self.typ == 'float':
      raise ValueError(f'Cannot convert float to int >>> {self.main}')
    return int(self.main)

  def value(self):
    return self.in_float() if self.typ == 'float' else self.in_int()

  def __repr__(self):
    return f'NUMBER({self.main!r}, typ={self.typ})'



class TYPE:
  def __init__(self, code):
    self.code = code
    self.idx = 0


class STRING_OPS(TYPE):
  def __init__(self, code):
    self.code = code
    self.idx = 0
    
  def is_valid_str(self):
    if len(self.code) > 1 and self.code[0] == self.code[-1]:
      return True
    return False
    
    
  def get_fine_str(self):
    return self.code[1:-1]
    
    
  def get_num(self, idx):
    dot = False
    digit = ["", ""]

    while idx < len(self.code):
      ch = self.code[idx]

      if ch in NUMBER_OPS.digits:
        if not dot:
          digit[0] += ch
        else:
          digit[1] += ch

      elif ch == ".":
        if dot:
          break
        dot = True
      else:
        break
      idx += 1
    if dot:
      return NUMBER_OPS(digit[0] + "." + digit[1]).in_float(), idx
    return NUMBER_OPS(digit[0]).in_int(), idx

  def get_string(self, idx):
    quote_char = self.code[idx]
    start = idx
    idx += 1
    while idx < len(self.code):
      if self.code[idx] == quote_char:
        end = idx+1
        return self.code[start:end], end
      elif self.code[idx] == '\n':
        end = idx
        return self.code[start:end], end
      elif self.code[idx] == '\\':
        idx += 2
        continue
      idx += 1

    end = len(self.code)
    return self.code[start:end], end

  def get_comment(self, symb, idx):
    comment_char = symb
    start = idx
    idx += 1
    while idx < len(self.code):
      if self.code[idx] == '\n':
        end = idx
        
        return self.code[start:end], end
      elif self.code[idx] == '\\':
        idx += 2
        continue
      idx += 1

    end = len(self.code)
    self.code = self.code[start:end]
    return self.code[start:end], end
    
    