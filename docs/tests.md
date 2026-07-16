

# 🧪 EggLang Testing Guide

## Overview

I have made some test code with the syntax of egg and run them.
The `tests/` directory contains both standard and stress tests. There are some files showing only one item in the test, and there is a combined file which contains 2800+ lines of egg code which egg passes easily, from basic operations to including recursion operations, etc.

---

## 🗂️ Test Structure

In the test folder there is a main file which runs all tests.

---

## ▶️ Running Tests

There is a dir called `tests`.
There I have `test.py`, run that file to see tests.

**To create your own test:**
Create your own file for testing, add critical syntaxes, and add that to that dir called `tests`, and add that to the list of `tests.py` file called `tests`, and run it to see all tests including yours.

**Individual test:**
Keep the list to only your file name and run that file to test the code.

---

## ✍️ Writing New Tests

When adding new language features:

1. Create a new `.egg.txt` file inside the `tests/` directory. Yes, `.txt`, because to keep your tests in GitHub you have to add `.txt`, else GitHub won't take the file as `.egg`, because Python has some built-in relation with the `.egg` extension, that's why `.gitignore` ignores it.
2. Add testcases.
3. Add a simple test success log like:
   ```
   your_name_test_1...OK
   ```
5. Add comments explaining the purpose of complex test cases.

**Example:**
```egg
€Checking if egg can parse list access expressions
var values = [10, 20, 30, 40,]
var calculation = values[0] + values[-1] * 2
fineshow("T7:", calculation, "...OK")
```

---

## ✅ Test Coverage

The current test suite covers:

- Variable declaration and assignment
- Primitive data types
- Arithmetic and comparison operators
- Logical expressions
- If / Elif / Else statements
- While loops
- For loops
- Function declaration and invocation
- Return statements
- Arrays
- HashMaps (Dictionaries)
- Index and property access
- Nested expressions
- Built-in functions
- Scope handling
- Runtime errors
- Parser validation
- Lexer tokenization
- Stress tests with deeply nested data structures and complex expressions
- Nested complex combined tests

---

As EggLang evolves, new language features should always be accompanied by corresponding tests to maintain reliability and prevent regressions.
