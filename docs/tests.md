```text
███████╗ ██████╗  ██████╗
██╔════╝██╔════╝ ██╔════╝
█████╗  ██║  ███╗██║  ███╗
██╔══╝  ██║   ██║██║   ██║
███████╗╚██████╔╝╚██████╔╝
╚══════╝ ╚═════╝  ╚═════╝
```

🧪 EggLang Testing Guide

## Overview

I have made some test code using the syntax of EggLang and run it.

The `tests/` directory contains both standard and stress tests. There are some files that show only one item in the test, and there is a combined file that contains 2800+ lines of Egg code, which Egg passes easily, from basic operations to recursion operations, etc.

---

## Test Structure

In the `tests/` folder, there is a main file that runs all tests.

---

## Running Tests

There is a directory called `tests`.

There, you will find `test.py`. Run that file to execute the tests.

To create your own test:

Create your own file for testing, add critical syntax, add it to the `tests` directory, then add it to the list of tests in `tests.py`, and run it to see all tests, including yours.

**Individual test:**

Keep the list containing only your file name and run that file to test your code.

---

## Writing New Tests

When adding new language features:

1. Create a new `.egg.txt` file inside the `tests/` directory. Yes, `.txt`, because to keep your tests on GitHub, you have to add `.txt`; otherwise, GitHub won't treat the file correctly as `.egg`, because Python has some built-in association with the `.egg` extension. That's why `.gitignore` ignores it.
2. Add test cases.
3. Add a simple test success log like:
   ```
   your_name_test_1...OK
   ```
4. Add comments explaining the purpose of complex test cases.

Example:

```egg
€Checking if Egg can parse list access expressions
var values = [10, 20, 30, 40,]
var calculation = values[0] + values[-1] * 2
fineshow("T7:", calculation, "...OK")
```

---

## Test Coverage

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