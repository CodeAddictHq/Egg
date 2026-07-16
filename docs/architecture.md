

# EggLang Architecture Overview

Like most other languages, Egg follows a pretty standard architecture. First, the whole source file is read in as one big string. That string goes to the **lexer**, which identifies tokens and splits everything up into a token stream.

The token stream then goes to the **parser** — this is the hardest part, since the parser turns the tokens into an AST (Abstract Syntax Tree), using a bunch of algorithms you don't normally run into in day-to-day programming.

Finally comes the fun part: the **interpreter** creates an environment, adds variables and functions to it, and runs the code.

```
+------------------------+
|      Source Code       |
+------------------------+
             |
             v
+------------------------+
|         Lexer          |
+------------------------+
             |
             v
+------------------------+
|         Tokens         |
+------------------------+
             |
             v
+------------------------+
|         Parser         |
+------------------------+
             |
             v
+------------------------+
|          AST           |
+------------------------+
             |
             v
+------------------------+
|      Interpreter       |
+------------------------+
             |
             v
+------------------------+
|  Runtime / Environment |
+------------------------+
```

Explaining every single detail here would make this doc way too long, so instead I'll just walk through the overall idea using one small code snippet as an example:

```
var b = "This is a str"
show(b)
```

## Lexer

The lexer (short for lexical analysis) takes the massive source code string and turns it into tokens. It splits the input into small pieces, recognizes and matches them against reserved keywords and symbols, and turns each piece into a token.

If we run the two lines above through the lexer, the output looks like this:

```
TOKEN(value='var', type='KW_VAR', line=1)
TOKEN(value='b', type='IDENTIFIER', line=1)
TOKEN(value='=', type='SYMB_EQ', line=1)
TOKEN(value='This is a str', type='STR_CLOSED', line=1)
TOKEN(value=';', type='NEW_LINE', line=1)
TOKEN(value='show', type='IDENTIFIER', line=2)
TOKEN(value='(', type='PRSTART', line=2)
TOKEN(value='b', type='IDENTIFIER', line=2)
TOKEN(value=')', type='PREND', line=2)
TOKEN(value=';', type='NEW_LINE', line=2)
TOKEN(value='END OF PROGRAM', type='EOF', line=None)
```

Visually, it's basically chopping the raw string up into labeled chunks:

```
 var        b        =     "This is a str"     ;
  |         |        |            |            |
  v         v        v            v            v
KW_VAR  IDENTIFIER SYMB_EQ    STR_CLOSED    NEW_LINE
```

## Parser

This part takes the token list and checks each line against the grammar rules to build the AST.

When the parser hits a line that starts with the `KW_VAR` token, it expects a keyword, followed by an `IDENTIFIER`, followed by an `=` symbol, followed by a value. That value gets parsed through a precedence chain using recursion, and the result becomes a node in the AST for the interpreter to run later.

Every statement in Egg is defined the same way.

For our code snippet, the parser's output looks like this:

```
ProgramNode([
    VarDeclNode(name='b', value=StrNode('This is a str', line=1), line=1),
    FunCallNode(name=IdentifierNode('show', line=2), args=[IdentifierNode('b', line=2)], line=2)
])
```

If you draw that out as a tree, it looks like this:

```
ProgramNode
  |
  +-- VarDeclNode (name = "b")
  |     |
  |     +-- StrNode ("This is a str")
  |
  +-- FunCallNode (name = "show")
        |
        +-- IdentifierNode ("b")
```

## Interpreter / Evaluator

Once we have the AST, we just need to execute it. Since Egg is an interpreted language, we don't compile the code down to bytecode or any other intermediate form — we walk the tree and run one subtree at a time. We use **post-order traversal**, since most operations need their child values evaluated first before the operation itself can run.

So for our example, the flow of execution looks like this: the interpreter starts at the `ProgramNode`, then walks down to the first statement — a `VarDeclNode`. It evaluates the value in that node's subtree and saves it into the current environment.

Once it reaches the bottom of that subtree, it moves on to the next one. When it reaches the `FunCallNode`, it looks up a function with that name in the built-in environment, finds it, and executes it.

Here's that same tree again, but numbered in the order the interpreter actually visits each node (post-order — children before parents):

```
                ProgramNode [4]
               /              \
   VarDeclNode [2]          FunCallNode [3]
        |                        |
   StrNode [1]              IdentifierNode
   "This is a str"          "b" (looked up
   (evaluated first,         in env, then
   then stored as b)         passed to show)
```

So the leaf values get evaluated first, then that result gets used by the node above it — `StrNode` before `VarDeclNode`, `IdentifierNode` before `FunCallNode`, and both statements before `ProgramNode` is considered "done."

## Environment & Scoping

Scoping also works recursively. When a variable is accessed, Egg first searches the current environment. If it's found there, it's returned right away.

If not, Egg walks up to the parent environment and searches there instead. This continues until it either finds the variable or reaches the outermost environment — if it's still not found there, Egg raises an error.

```
+--------------------+
|     Block Env      |  <-- lookup starts here
+--------------------+
          |
          | not found -> check parent
          v
+--------------------+
|   Function Env     |
+--------------------+
          |
          | not found -> check parent
          v
+--------------------+
|     Global Env     |  <-- if not found here, raise error
+--------------------+
```

## Error Handling

This part isn't strictly necessary — a simple `print()` would technically work — but I built a custom error handler instead. It tracks line numbers and logs errors properly, and it's built on top of Python's `Exception` class.

## Project Structure

```
Errors
│   ├── __init__.py
│   ├── cli.py
│   ├── fun.py
│   ├── loop.py
│   ├── runtime.py
│   └── syntex.py
├── Interpreter
│   ├── __init__.py
│   ├── builtin.py
│   ├── env.py
│   └── main.py
├── Lexer
│   ├── __init__.py
│   ├── main.py
│   └── tokens.py
├── Parser
│   ├── __init__.py
│   ├── main.py
│   └── nodes
│       ├── __init__.py
│       ├── base.py
│       ├── opr.py
│       ├── programe.py
│       ├── statements.py
│       └── var.py
├── ToolKit
│   ├── __init__.py
│   └── dataops.py
└── __init__.py
```

This is packaged so that the `Lexer`, `Parser`, and `Interpreter` modules are all imported from one place, and that's what actually runs the operations.
