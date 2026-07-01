
import sys
import os
sys.path.append(os.path.abspath("../functions"))

sys.path.append(os.path.abspath("../DB"))
from DB import db

TYPES = [
  "STR",
  "NUM",
  "BOOL",
  "NONE"
]

from functions import show

def makestr(txt):
  a = txt[1:-1:]
  return a
  
def findvalue(txt):
  value = txt.split("=")
  try:
    value = value[-1].strip()
    return value
  except:
    print(f"invalid code : >>> '{txt}'")
def findname(txt):
  value = txt.split("=")
  return value[0].strip()
  
def valueconvert(val, tp):
  try:
    
    if tp=="STR" and val.startswith("'") and val.endswith("'"):
      return makestr(val)
    if tp=="STR" and val.startswith('"') and val.endswith('"'):
      return makestr(val)
    elif tp == "BOOL":
      return bool(makestr(val))
    elif tp == "NUM":
      return float(val)
    elif tp == "NONE":
      val = None
      return val
    else:
      print(f"INVALID CODE : TYPE DOESNT EXISTS>> '{tp}' ")
  except:
    print(f"INVALID CODE : CANT CONVERT'{val}>>>{tp}'")
  

def createshow(codes):
  code = codes.split(" ", 1)
  val = code[1]
  if val.startswith("'") and val.endswith("'"):
    show.showcontent(makestr(val))
  elif val.startswith('"') and val.endswith('"'):
    show.showcontent(makestr(val))
  else:
    show.showvar(val)
    
    
def createvar(codes):

  code = codes.split(" ", 2)

  for i in code:
    if i == "":
      code.remove(i)
  if len(code)==3:
    if "=" not in code[2]:
      code = []
    else:
    
      vartype = code[1]
      name = findname(code[-1])
      value = findvalue(code[-1])
      value = valueconvert(value, vartype)
      
      db.assignvar(name, value)
  
  else:
    print(f"INVALID CODE : ASSIGN ERROR >> {codes}")
  
  
  


def createtype(code):
  var = code.split(" ")[1]
  print("varname sent")
  db.showtype(var)
  
def createlen(code):
  var = code.split(" ")[1]
  db.showlen(var)

  
  