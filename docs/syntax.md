```text
███████╗ ██████╗  ██████╗
██╔════╝██╔════╝ ██╔════╝
█████╗  ██║  ███╗██║  ███╗
██╔══╝  ██║   ██║██║   ██║
███████╗╚██████╔╝╚██████╔╝
╚══════╝ ╚═════╝  ╚═════╝
```

# EGG Lang Guide

## 1. Variables

Create a variable using the keyword `var`. It's accessible to every child scope.

```egg
var name = "Egg"
var a = 1
var b = 3
var c = a > b  € FALSE
var age = 10
```

You can use any algebraic or comparison expression here, EGG should parse it correctly.

To redeclare a variable, just use the name — you can't redeclare using `var` again, it'll throw an error. Use only the name to redeclare:

```egg
a = 3
```

Delete a variable using `rm`:

```egg
rm var_name
```

---

## 2. Comments

Comments start with `€`.

```egg
€ This is a comment
var x = 5
```

---

## 3. Conditions

Use `if`, `elif`, and `else` for conditions. Always wrap the condition in a pair of parentheses, otherwise it'll throw an error. Code blocks are recognized by curly braces, not indentation — indentation is just for clean code. 

```egg
if (age > 18) {
    € Do something
} elif (age is 18) {
    € Do something
} else {
    € Do something
}
```

Nested statements are allowed.

---

## 4. Functions

Create a function using the keyword `fun`, return using `return`, and call it with parentheses.

```egg
fun greet() {
    € Do something
    return "Hello"
}

greet()
```

Nested functions are allowed, but they can only be used inside the block where they were declared (and that block's child scopes) — they can't be accessed from parent scopes.

---

## 5. Loops

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

A dict on its own isn't iterable.

```egg
var nums = [1, 2, 3,]

for (num in nums) {
    show(num)
}
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

Both `stop` and `skip` can only be used inside a loop.

---

## 6. Data Types

### Primitive Types

#### Boolean Values

EGG has two boolean values: `TRUE` and `FALSE`.

They're capitalized, but print out as `True` and `False` — since Python doesn't store them as strings, it treats them as actual bool values, which is why they print that way.

```egg
var active = TRUE
```

#### Null Value

The empty value is `NONE`.

Same idea as booleans — Python stores it as a real `None`, and it prints out as `None`.

```egg
var data = NONE
```

#### Strings

You can store strings with either double quotes or single quotes:

```egg
var str = "My first str"
```

In this version, strings only support the `\` escape character — newlines and tabs aren't supported yet.

#### Numbers

Numbers can only be stored as ints or floats.

### Non-Primitive Types

EGG also has two non-primitive types: **lists/arrays** and **dictionaries/objects**. See sections 7 and 8 below for details.

---

## 7. Lists/Arrays

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

That's invalid — you always have to store the array in a variable before accessing it.

Some methods:

- `numbers.push(0)` — adds to the end
- `numbers.pop()` — removes from the end
- `numbers.pushfirst(0)` — adds to the start
- `numbers.popfirst()` — removes from the start

More methods are coming in a future version — contributions welcome!

---

## 8. Dictionaries/Objects

Dictionaries store key-value pairs.

Dictionary iteration uses `keys(dict)` or `values(dict)`.

```egg
for (key in keys(data)) {

}
```

No methods yet, but more are planned — contributions welcome!

---

## 9. Operators

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

## 10. Built-in Functions

| Function | Description |
|----------|--------------|
| `show(x)` | Prints one item |
| `fineshow(...)` | Takes multiple arguments, combines them into one list, and prints them out |
| `type(var_name)` | Prints the type of a variable |
| `keys(dict)` | Returns dict keys |
| `values(dict)` | Returns dict values |
| `ask("prompt")` | Takes user input |

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

Check `example.md` for some basic example programs written in EGG, to get a clearer picture of the syntax.
