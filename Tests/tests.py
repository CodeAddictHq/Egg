from src.INTERPRETER import Lexer, Parser, Interpreter
from pathlib import Path

tests = [
  "forloop.egg.txt",
  "whileloop.egg.txt",
  "var.egg.txt",
  "ifstatement.egg.txt",
  "fun.egg.txt",
  "combined.egg.txt",
]

for file in tests:
  path = Path().cwd()/"Tests"/file
  print(f"\nRunning: {file}")

  source = path.read_text()
  lexer = Lexer()
  tokens = lexer.tokenise(source)
  parser = Parser()
  ast = parser.parse(tokens)
  interpreter = Interpreter()
  interpreter.interpret(ast)
  

