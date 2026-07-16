class IdentifierNode:
  def __init__(self, identifier, line=0):
    self.identifier = identifier
    self.line = line

  def __repr__(self):
    return f"IdentifierNode({self.identifier!r}, line={self.line})"
class DictUpdateNode:
  def __init__(self, di, key, val, line=0):
    self.dic = di
    self.key = di
    self.value = val
    self.line = line

  def __repr__(self):
    return f"DictUpdateNode(dic={self.dic!r}, key={self.key},value={self.value}, line={self.line})"
class ListUpdateNode:
  def __init__(self, lis, idx, val, line=0):
    self.lis = lis
    self.idx = idx
    self.value = val
    self.line = line

  def __repr__(self):
    return f"DictUpdateNode(dic={self.lis!r},idx={self.idx}, value={self.value}, line={self.line})"
class StrNode:
  def __init__(self, value, line=0):
    self.value = value
    self.line = line

  def __repr__(self):
    return f"StrNode({self.value!r}, line={self.line})"


class IntNode:
  def __init__(self, value, line=0):
    self.value = value
    self.line = line

  def __repr__(self):
    return f"IntNode({self.value!r}, line={self.line})"


class FloatNode:
  def __init__(self, value, line=0):
    self.value = value
    self.line = line

  def __repr__(self):
    return f"FloatNode({self.value!r}, line={self.line})"


class BoolNode:
  def __init__(self, value, line=0):
    self.value = value
    self.line = line

  def __repr__(self):
    return f"BoolNode({self.value!r}, line={self.line})"
    
class VarDeclNode:
  def __init__(self, name, value, line=0):
    self.name = name
    self.value = value
    self.line = line

  def __repr__(self):
    return f"VarDeclNode(name={self.name!r}, value={self.value!r}), line={self.line}"


class VarAssignNode:
  def __init__(self, name, value, line=0):
    self.name = name
    self.value = value
    self.line = line

  def __repr__(self):
    return f"VarAssignNode(name={self.name!r}, value={self.value!r}, line={self.line})"


class VarRmNode:
  def __init__(self, var, line=0):
    self.var = var
    self.line = line

  def __repr__(self):
    return f"VarRmNode(var={self.var!r}, line={self.line})"
class ListNode:
  def __init__(self, value, line=0):
    self.values = value
    self.line = line

  def __repr__(self):
    return f"ListNode(values={self.values!r}, line={self.line})"


class DictNode:
  def __init__(self, dict, line=0):
    self.dict = dict
    self.line = line

  def get(self, key):
    return self.dict.get(key)

  def __repr__(self):
    return f"DictNode(dict={self.dict!r}, line={self.line})"


class DictAccessNode:
  def __init__(self, parent, child, line=0):
    self.parent = parent
    self.child = child
    self.line = line

  def __repr__(self):
    return f"DictAccessNode(parent={self.parent!r}, child={self.child!r}, line={self.line})"


class ListAccessNode:
  def __init__(self, li, el, line=0):
    self.li = li
    self.idx = el
    self.line = line

  def __repr__(self):
    return f"ListAccessNode(li={self.li!r}, idx={self.idx!r}, line={self.line})"