
# EGG Language Guide

This guide covers EGG's syntax and core language features — from variables and data types to loops, functions, and built-ins. It's meant to give you a clear picture of how to write EGG code.

## Table of Contents

1. [Comments](#1-comments)
2. [Variables](#2-variables)
3. [Data Types](#3-data-types)
4. [Operators](#4-operators)
5. [Conditions](#5-conditions)
6. [Loops](#6-loops)
7. [Functions](#7-functions)
8. [Lists / Arrays](#8-lists--arrays)
9. [Dictionaries / Objects](#9-dictionaries--objects)
10. [Built-in Functions](#10-built-in-functions)
11. [Reserved Items](#11-reserved-items)
12. [Rules](#12-rules)
13. [Current Limitations](#13-current-limitations)
14. [Full Example Program](#14-full-example-program)

---

## 1. Comments

Comments start with `€`.

```egg
€ This is a comment
var x = 5
```

> [!NOTE]
> Comments are stripped out by the lexer before parsing even starts, so they have zero effect on how your program runs.

---

## 2. Variables

Create a variable using the keyword `var`. It's accessible to every child scope.

```egg
var name = "Egg"
var a = 1
var b = 3
var c = a > b  € FALSE
var age = 10
```

You can use any algebraic or comparison expression here — EGG will parse it correctly.

> [!TIP]
> A variable declared in a parent scope (like the global scope) can be read from inside a function or loop below it. This is because scope lookup walks upward from the current environment to its parent until it finds the variable.

To redeclare a variable, just use the name — you can't redeclare using `var` again, it'll throw an error. Using `var` twice on the same name is treated as a mistake rather than an update, so EGG catches it early instead of letting you accidentally overwrite something.

```egg
a = 3
```

Delete a variable using `rm`:

```egg
rm var_name
```

---

## 3. Data Types

### Primitive Types

```
Data Types
  |
  +-- Primitive
  |     +-- Boolean   (TRUE / FALSE)
  |     +-- Null      (NONE)
  |     +-- String
  |     +-- Number    (int / float)
  |
  +-- Non-Primitive
        +-- List / Array
        +-- Dictionary / Object
```

#### Boolean Values

EGG has two boolean values: `TRUE` and `FALSE`.

```egg
var active = TRUE
show(active)
```

Output:
```
True
```

> [!NOTE]
> Booleans are written capitalized in EGG code (`TRUE`, `FALSE`), but they print out as `True` and `False`. That's because under the hood they're real Python bool values, not strings — Python just prints its booleans that way.

#### Null Value

The empty value is `NONE`.

```egg
var data = NONE
show(data)
```

Output:
```
None
```

Same idea as booleans: Python stores `NONE` as a real `None`, so it prints as `None`.

#### Strings

You can store strings with either double quotes or single quotes:

```egg
var str = "My first str"
```

> [!NOTE]
> In this version, strings only support the `\` escape character — newlines and tabs aren't supported yet.

#### Numbers

Numbers can only be stored as ints or floats.

### Non-Primitive Types

EGG also has two non-primitive types: **lists/arrays** and **dictionaries/objects**. See [Lists / Arrays](#8-lists--arrays) and [Dictionaries / Objects](#9-dictionaries--objects) below for details.

---

## 4. Operators

### Math Operators

| Operator | Meaning |
|----------|---------|
| `+` | Add |
| `-` | Subtract |
| `*` | Multiply |
| `/` | Divide |
| `^` | Power |

```egg
var total = 5 + 3
show(total)
```

Output:
```
8
```

### Comparison Operators

| Operator | Meaning |
|----------|---------|
| `>` | Greater than |
| `<` | Less than |
| `>_` | Greater than or equal to |
| `<_` | Less than or equal to |
| `is` | Equals |
| `isnot` | Not equals |

```egg
x > 5
x < 5
x is 5
x isnot 5
```

> [!NOTE]
> `is` and `isnot` are EGG's equality operators — they check if two values are equal, not whether they're the same object in memory.

### Logical Operators

| Operator | Meaning |
|----------|---------|
| `and` | Logical AND |
| `or` | Logical OR |
| `not` | Logical NOT |

```egg
if (age > 10 and age < 20) {
    show("Teen")
}
```

---

## 5. Conditions

Use `if`, `elif`, and `else` for conditions. Always wrap the condition in a pair of parentheses, otherwise it'll throw an error.

```egg
if (age > 18) {
    € Do something
} elif (age is 18) {
    € Do something
} else {
    € Do something
}
```

> [!NOTE]
> Code blocks are recognized by curly braces `{ }`, not indentation. Indentation is just for keeping your code clean — it doesn't affect how the parser reads your program.

Nested statements are allowed.

---

## 6. Loops

### While Loop

Make a while loop using the `while` keyword and a condition:

```egg
while (x < 5) {
    € some work
    x = x + 1
}
```

### For Loop

For loops can only be written like this:

```
(identifier in iterable)
```

No other form is allowed. Valid iterables are:

- lists/arrays
- dict/object keys or values
- strings

A dict on its own isn't iterable — you need to go through `keys(dict)` or `values(dict)`.

```egg
var nums = [1, 2, 3,]

for (num in nums) {
    show(num)
}
```

Output:
```
1
2
3
```

Use `stop` to exit a loop:

```egg
while (TRUE) {
    stop
}
```

Use `skip` to skip the current iteration:

```egg
for (x in nums) {
    if (x is 2) {
        skip
    }
    € work
}
```

> [!NOTE]
> Both `stop` and `skip` can only be used inside a loop. Using either one outside of a loop will throw an error.

---

## 7. Functions

Create a function using the keyword `fun`, return using `return`, and call it with parentheses.

```egg
fun greet() {
    € Do something
    return "Hello"
}

greet()
```

Nested functions are allowed, but they can only be used inside the block where they were declared (and that block's child scopes) — they can't be accessed from parent scopes.

```
Global Scope
   |
   +-- fun greet() scope
          |
          +-- nested fun scope
              (usable here and inside greet,
               not usable outside greet)
```

---

## 8. Lists / Arrays

Arrays/lists use square brackets, like normal.

```egg
var numbers = [1, 2, 3,]
```

Access a list item:

```egg
var first = numbers[0]
var last = numbers[-1]
```

Update a list item:

```egg
numbers[-1] = 0
```

You can't do this:

```egg
var num = [1, 2, 3][1]
```

> [!NOTE]
> That's invalid — you always have to store the array in a variable before accessing it. The parser currently only allows indexing on identifiers, not on a literal array written inline.

Some methods:

| Method | Description |
|--------|--------------|
| `numbers.push(0)` | Adds to the end |
| `numbers.pop()` | Removes from the end |
| `numbers.pushfirst(0)` | Adds to the start |
| `numbers.popfirst()` | Removes from the start |

> [!TIP]
> More list methods are planned for a future version — contributions welcome!

---

## 9. Dictionaries / Objects

Dictionaries store key-value pairs.

Dictionary iteration uses `keys(dict)` or `values(dict)`.

```egg
var di = {
  name:"Adib",
  age:10
}
show(di.name)
show(di.age)
```

> [!TIP]
> No dictionary methods yet, but more are planned — contributions welcome!

---

## 10. Built-in Functions

| Function | Description |
|----------|--------------|
| `show(x)` | Prints one item |
| `fineshow(...)` | Takes multiple arguments, combines them into one list, and prints them out |
| `type(var_name)` | Prints the type of a variable |
| `keys(dict)` | Returns dict keys |
| `values(dict)` | Returns dict values |
| `ask("prompt")` | Takes user input |
| `len("prompt")` | Retirns len of iterable |
### Type Casting Functions

| Function | Description |
|----------|--------------|
| `number(str)` | Returns a number |
| `string(any type)` | Returns a string |

---

## 11. Reserved Items

You can never use any of these as an identifier — doing so throws an error.

**Keywords**
`var`, `and`, `or`, `in`, `not`, `stop`, `skip`, `return`, `rm`

**Statement Keywords**
`if`, `elif`, `else`, `fun`, `while`, `for`

**Booleans**
`TRUE`, `FALSE`

**Null**
`NONE`

**Math Operators**
`+`, `-`, `*`, `/`, `^`

**Comparison Operators**
`>`, `<`, `>_`, `<_`, `is`, `isnot`

**Other Symbols**
`=`, `€`, `.`, `,`, `:`

---

## 12. Rules

- You can never use a reserved keyword or reserved symbol as an identifier — doing so throws an error.
- **Separation rule:** always use a space between elements. Commas are optional, since EGG recognizes elements by spaces, not commas — but commas can still be used to help readability.

---

## 13. Current Limitations

EGG is still early, so a few things are worth keeping in mind:

- Strings only support the `\` escape character — no newline or tab escapes yet.
- You can't index a literal array directly (`[1, 2, 3][1]`) — it has to be stored in a variable first.
- Lists only have four built-in methods so far: `push`, `pop`, `pushfirst`, and `popfirst`.
- Dictionaries don't have any built-in methods yet.
- For loops only support the single form `(identifier in iterable)` — no other loop syntax is supported.

> [!TIP]
> None of this is set in stone — EGG is an evolving hobby language, and contributions to close these gaps are welcome.

---

## 14. Full Example Program

Here's a small program that ties several features together: comments, a function, a condition chain, a list, a loop, and a built-in call.

```egg
€ EGG demo: temperature checker

fun classify(temp) {
    if (temp > 30) {
        return "Hot"
    } elif (temp is 30) {
        return "Warm"
    } else {
        return "Cold"
    }
}

var temps = [28, 30, 35, 15,]

for (t in temps) {
    var label = classify(t)
    show(label)
}
```

Output:
```
Cold
Warm
Hot
Cold
```

---

Check `example.md` for some basic example programs written in EGG, to get a clearer picture of the syntax.
