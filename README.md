```text
███████╗ ██████╗  ██████╗
██╔════╝██╔════╝ ██╔════╝
█████╗  ██║  ███╗██║  ███╗
██╔══╝  ██║   ██║██║   ██║
███████╗╚██████╔╝╚██████╔╝
╚══════╝ ╚═════╝  ╚═════╝
```

> A basic interpreted programming language built with Python.

---

## 📚 Documentation

| Guide | Description |
|-------|-------------|
| [Language Syntax](./docs/syntax.md) | Learn the language grammar, keywords, data types, operators, and core syntax. |
| [Architecture Overview](./docs/architecture.md) | Explore how EggLang is implemented, from lexing and parsing to AST evaluation and runtime execution. |
| [Testing Guide](./docs/tests.md) | Review the project's test suite and the cases used to validate language features. |
| [Contributing Guide](./docs/contribute.md) | Learn how to contribute, report issues, and submit improvements. |

---

## Introduction

A basic programming language with support for common functionality like loops, variables, and data types. It just doesn't have OOP / classes.

---

## 📦 Installation

EggLang is published on PyPI, so you can install the interpreter with a single command — no advanced setup needed.

**Requirements:** Python and pip.

```bash
pip install egglang
```

After installation, verify it by running:

```bash
egg --v
```
or
```bash
egg --version
```

Both will print the EGG logo.

Now you can run simple `.egg` files.

> Note: a lot of functionality isn't implemented yet, since most of the effort so far has gone into the interpreter itself. That's why there's no CLI editor to test code directly in the terminal yet.

---

## 🚀 Quick Start

Once you've installed the interpreter, you can start running EGG code right away.

Create a simple `.egg` file and write your EGG code in it. Here's a "Hello, World!" example:

```egg
show("Hello, World!")
```

Save the file, open a terminal in that file's directory, and run:

```bash
egg run file.egg
```

Your EGG code will run smoothly.
# Calculator-without-built-in-functions
