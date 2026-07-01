from . import definetask
SYNTEX = [
  "SHOW ",
  "VAR ",
  "TYPE ",
  "LEN ",
]
def find(code):
  if code.startswith(SYNTEX[0]):
    definetask.createshow(code)
  elif code.startswith(SYNTEX[1]):
    
    definetask.createvar(code)
  elif code.startswith(SYNTEX[2]):
    definetask.createtype(code)
  elif code.startswith(SYNTEX[3]):
    definetask.createlen(code)
  else:
    print(f"INVALID CODE : TASK NOT FOUND >> {code}")
  
  
  
  
  