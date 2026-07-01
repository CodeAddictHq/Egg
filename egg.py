from process.validation import chekvalidation

print(r"""
███████╗ ██████╗  ██████╗ 
██╔════╝██╔════╝ ██╔════╝ 
█████╗  ██║  ███╗██║  ███╗
██╔══╝  ██║   ██║██║   ██║
███████╗╚██████╔╝╚██████╔╝
╚══════╝ ╚═════╝  ╚═════╝

""")
print("=" * 50)
print("  EGG INTERPRETER v1.0")
print("  'egg help'   -> Show syntax")
print("  'about egg'  -> Know about this language")
print("=" * 50)
def syntax():
   print(r"""
╠══════════════════════════════════════╣
║  Open the link and scroll down:      ║
║  https://github.com/CodeAddictHq/    ║
║  EGG_LANGUAGE_PYTHON                 ║
╚══════════════════════════════════════╝
""")


def about():
    print(r"""
╠══════════════════════════════════════╣
║  Source code:                        ║
║  https://github.com/CodeAddictHq/    ║
║  EGG_LANGUAGE_PYTHON/tree/main       ║
╚══════════════════════════════════════╝
""")


while True:
  a = input("/>")
  if a == "EXIT":
    break
  elif a == "about egg":
    about()
  elif a == "egg help":
    syntax()
  else:
    
    chekvalidation(a)
  
  
  

  

  