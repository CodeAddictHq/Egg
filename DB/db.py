VARS = {
  "key":"value"
  
}

def assignvar(name, val):
  VARS[name] = val
  
def showtype(var):
  var = str(var)
  print(type(var), var)
  if var in VARS.keys():
    print(type(VARS[var]))
  else:
    print(f"INVALID CODE : VAR '{var}' DOESNT EXISTS")
def showlen(var):
  var = str(var)

  if var in VARS.keys():
    print(len(VARS[var]))
  else:
    print(f"INVALID CODE : VAR '{var}' DOESNT EXISTS")
  
def showle(var):
  if VARS[var]:
    print(len(VARS[var]))
  else:
    print(f"INVALID CODE : VAR '{var}' DOESNT EXISTS")