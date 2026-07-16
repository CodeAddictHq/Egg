class TOKEN:
  def __init__(self, value, type, line):
    self.value = value
    self.type = type
    self.line = line
  def __repr__(self):
    return f"TOKEN(value={self.value!r}, type={self.type!r}, line={self.line})"


      
