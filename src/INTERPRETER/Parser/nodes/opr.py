class BinOpNode:
  def __init__(self, opr, left, right, line=0):
    self.opr = opr
    self.left = left
    self.right = right
    self.line = line

  def __repr__(self):
    return f"BinOpNode(opr={self.opr!r}, left={self.left!r}, right={self.right!r}, line={self.line})"


class BinCompNode:
  def __init__(self, comp, left, right, line=0):
    self.comp = comp
    self.left = left
    self.right = right
    self.line = line

  def __repr__(self):
    return f"BinCompNode(comp={self.comp!r}, left={self.left!r}, right={self.right!r}, line={self.line})"


class BinInNode:
  def __init__(self, val, var, line=0):
    self.val = val
    self.var = var
    self.line = line

  def __repr__(self):
    return f"BinInNode(val={self.val!r}, var={self.var!r} , line={self.line})"


class UnaryOpNode:
  def __init__(self, opr, val, line=0):
    self.opr = opr
    self.val = val
    self.line = line

  def __repr__(self):
    return f"UnaryOpNode(opr={self.opr!r}, val={self.val!r}, line={self.line})"