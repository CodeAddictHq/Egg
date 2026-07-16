from ..Errors.runtime import RuntimeError, NotFoundError, AlreadyExistsError


class Env:
  def __init__(self, parent=None):
    self.vars = {}
    self.funs = {}
    self.parent = parent 
  
  
  
  def getDicEl(self, name):
    if name in self.vars.keys():
      return self.vars[name]
    elif self.parent:
      return self.parent.getDicEl(name)
    else:
      raise NotFoundError(f"Hash not found >> {name}")

  def delitem(self, name):
    if name in self.vars.keys():
      del self.vars[name]
    elif self.parent:
      return self.parent.delitem(name)
    else:
      raise NotFoundError(f"Cannot delete the variable which does not exist >> {name}")

  def defFun(self, name, works, params):
    if name in self.funs.keys():
      raise AlreadyExistsError(f"Function already exists yet >> {name}")
    fun = {
      "works": works,
      "params": []
    }
    for i in params:
      fun['params'].append(i.identifier)
    self.funs[name] = fun

  def getFun(self, name):
    if name in self.funs.keys():
      return self.funs[name]
    elif self.parent:
      return self.parent.getFun(name)
    else:
      raise NotFoundError(f"Function is not defined >> {name}(...)")
    self.funs[name] = fun

  def exists(self, name):
    if name in self.vars:
      return True
    elif self.parent:
      return self.parent.exists(name)
    return False

  def define(self, name, value):
    if name in self.vars:
      print(name, value)
      raise AlreadyExistsError(f"Variable already exists >> {name}  assign instead of redeclar ")
    self.vars[name] = value

  def assign(self, name, value):
    if name in self.vars:
      self.vars[name] = value
    elif self.parent: 
      self.parent.assign(name, value)
    else:
      raise NotFoundError(f"Variable not found to assign >> {name}")

  def delete(self, name):
    if name in self.vars:
      del self.vars[name]
    elif self.parent:
      self.parent.delete(name)
    else:
      raise NotFoundError(f"Variable not found to delete >> {name}")

  def get(self, name):
    if name in self.vars:
      return self.vars[name]
    elif self.parent:
      return self.parent.get(name)
    else:
      raise NotFoundError(f"Variable not found to access >> {name}")

  def __str__(self):
    return str(self.vars)