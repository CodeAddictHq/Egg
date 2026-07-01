from . import findtask
SYNTEX = [
  "SHOW",
  "VAR",
  "TYPE",
  "FOR",
  "LEN ",
]



def chekvalidation(code):
  if code.startswith(SYNTEX[0]) or code.startswith(SYNTEX[1]) or code.startswith(SYNTEX[2]) or code.startswith(SYNTEX[3]) or code.startswith(SYNTEX[4]):
    findtask.find(code)
  else:
    print(f"INVALID CODE : SYNTEX ERROR >> {code}")