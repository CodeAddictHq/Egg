import sys
import os
sys.path.append(os.path.abspath("../functions"))

sys.path.append(os.path.abspath("../DB"))
from DB.db import VARS


def showcontent(code):
  print(code)
  
def showvar(name):
  var = str(name)

  if var in VARS.keys():
    print(VARS[var])
  else:
    print(f"INVALID CODE : VAR NOT FOUND >> '{name}'")
  