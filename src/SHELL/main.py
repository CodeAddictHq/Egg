from pathlib import Path
import typer
from rich.console import Console
from rich.panel import Panel
from INTERPRETER import Lexer, Parser, Interpreter
from INTERPRETER.Errors.cli import UnknownCmdError, FileNotFoundError

app = typer.Typer()
console = Console()


@app.callback(invoke_without_command=True)
def fuck(v:bool=False, version:bool=False):
  if version or v:
    print("""
███████╗ ██████╗  ██████╗
██╔════╝██╔════╝ ██╔════╝
█████╗  ██║  ███╗██║  ███╗
██╔══╝  ██║   ██║██║   ██║
███████╗╚██████╔╝╚██████╔╝
╚══════╝ ╚═════╝  ╚═════╝
""")
    print("V 0.2.2")



@app.command()
def run(file:str, i:bool=False):
  file = Path(file)
  if file.suffix != ".egg":
    raise UnknownCmdError(f"File should always contain .egg extension >> {file}", file)
  if not file.exists():
    raise FileNotFoundError(f"File not found >> {file}", f"{file.cwd()}/{file}")
  code = file.read_text() +"\n"
  lexer = Lexer()
  tokens = lexer.tokenise(code)
  parser = Parser()
  ast = parser.parse(tokens)
  interpreter = Interpreter()
  interpreter.interpret(ast)


@app.command()
def help():
  """Show documentation links."""
  console.print(
    Panel(
      "[bold cyan]Documentation & Source[/bold cyan]\n\n"
      "📚 Docs:\n"
      "https://github.com/codeaddicthq/egg/SYNTEX.md",
      title="EGG Docs",
      border_style="cyan",
    )
  )


@app.command()
def info():
  console.print(
    Panel(
      """[bold cyan]EGG Programming Language[/bold cyan]

 EGG is a small, fun programming language created as a learning project.

When I started my coding journey, I was always curious about how programming languages actually work. 
It felt like magic — how code turns into something a computer understands.

In July 2026, I got three weeks of free time and decided to turn that curiosity into reality.

The first version of EGG (v1.0) was a simple experiment. I created a language that could take input and produce output, but it had no complex logic or real structure.

This time, I studied how programming languages are built — including:
• Lexer
• Parser
• AST (Abstract Syntax Tree)
• Interpreter design

While building EGG, I learned many complex algorithms and concepts that I never thought I could understand before.

EGG is built with Python, so it may not be the fastest language, but it provides many useful features:

✓ Variables
✓ Functions
✓ If statements
✓ For loops
✓ While loops
✓ Lists
✓ Dictionaries
✓ And other basic programming language features

My goal is not to compete with big languages, but to explore, learn, and share the process of creating a programming language.

Try EGG, explore it, and share your feedback!

[italic]Made with curiosity and a love for programming 🥚[/italic]
""",
      title="About EGG",
      border_style="cyan",
    )
  )



def main():
  app()
  
if __name__ =="__main__":
  main()