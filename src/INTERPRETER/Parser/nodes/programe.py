class ProgrameNode:
  def __init__(self, li):
    self.statements = []

  def append(self, statement):
    self.statements.append(statement)

  def __getitem__(self, i):
    return self.statements[i]

  def __repr__(self):
    return f"ProgrameNode({self.statements})"