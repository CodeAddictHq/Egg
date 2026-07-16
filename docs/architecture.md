```text
███████╗ ██████╗  ██████╗
██╔════╝██╔════╝ ██╔════╝
█████╗  ██║  ███╗██║  ███╗
██╔══╝  ██║   ██║██║   ██║
███████╗╚██████╔╝╚██████╔╝
╚══════╝ ╚═════╝  ╚═════╝
```

# EggLang Architecture Overview
Like other languages egg also has  normal Architecture at first it takes whole code input as a massive string than ut gives it to lexer the lexer identifies the tokens and splits them into tokens than it gaves to the parser heres the most hard part the parser makes the ast 
and here used so much algorithm that really not used in day to day use 
than the most fun part the interpreter creates a env makes var and function to that env and runs the code 
Source Code
     │
     ▼
 Lexer
     │
     ▼
 Tokens
     │
     ▼
 Parser
     │
     ▼
 AST
     │
     ▼
 Interpreter
     │
     ▼
 Runtime / Environment

## Lexer
The lexer also known as lexical analysis it takes the massive code string and turns them token
actually i made a loop to itarate through this massive string when it stores temporarily and when finds space turns that prev tem memory into token and finds for ther els 
example 
var name = "Adib"
this will store the v a r in memo 

when he found space he will make the memory into token 
while making the token it will go through several chechmking wheather its a keyword or statements than it will store it 
after storing same process will also bw aplied in name it is not reserved keyword it will store as identifiwr 
and when it founds symb it imedietly checks wheather it is a reserved symb or not than if reserved makes it token and when it will come to str it wont verify itt will direct tokenize it a string token from starting qutote to end quto 
if end qutoe not found it will store it as unclosed string heres some lexer output examples soliek this verification and tge loop it will split the whole str into tokens he also tracks lines by adding ; as new line we dont use it in code and at last it adds eof token

code 

"""
var b = "This is a str"
show(b)
"""
tokens 
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
TOKEN(value='END OF PROGRAME', type='EOF', line=None)



## Parser
this part takes the tokens and checks the lines wuth grammer rule tmand makes ast 

for examples parser will take that tokens list and when he will find the line started with tolen kw_var he will expect keyword with a IDENTIFIER with a eq symb and wuth a value of that token he will parse that value in precedence chain expression by recursion and make the ast for excuter

for example that tokens ast gonna be 



## AST

## Interpreter / Evaluator

## Environment & Scoping

## Error Handling

## Project Structure
