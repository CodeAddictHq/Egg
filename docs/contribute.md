```text
███████╗ ██████╗  ██████╗
██╔════╝██╔════╝ ██╔════╝
█████╗  ██║  ███╗██║  ███╗
██╔══╝  ██║   ██║██║   ██║
███████╗╚██████╔╝╚██████╔╝
╚══════╝ ╚═════╝  ╚═════╝
```

# Contributing to EggLang

You can contribute by fixing a bug, improving documentation, adding a feature, writing tests, or anything else — I always welcome contributions.

---

## Getting Started

1. Fork the repo.
2. Clone your fork.
3. Create a new branch with a name that reflects what you're contributing.
4. Install the dependencies from `r.txt`.

---

## Development Guidelines

There are many places where you can contribute:

### 1. Creating a CLI Editor

Honestly, the biggest thing EGG is missing right now is a CLI editor. I found it boring to build and don't have much experience with it, so I skipped it for now — but you're welcome to build one.

Here's the catch: most language CLI editors save past syntax/history in memory and push it onto a stack for things like up-arrow history. I never built that functionality into the interpreter, so if you want to add a CLI editor with that kind of feature, let me know — I can help out with that part too.

### 2. Adding Built-in Methods and Functions

There's a class in `src/interpreter/interpreter/builtin.py` where you can add methods and functions. Just add a class method there, and it automatically becomes an EGG function.

**Logic:**

If you call a function in EGG code, it gets called with the argument list. For example:

```egg
fineshow("hi ", "Adib")
```

EGG internally calls:

```python
self.fineshow(["hi ", "Adib"])
```

That's it — that's how easy it is to add functions to EGG.

For methods (like list methods), name them like `method_methodname()`. The method takes 1 argument — a list — where the last element of the list is the instance the method was called on.

For example:

```egg
a = [1, 2]
a.push(3)
```

The `val` passed in will be `[3, [1, 2]]` — `3` is the argument, and `[1, 2]` is the actual list instance.

Wrap any exceptions in exception classes inside the `errors/` directory — everything else is handled by EGG itself, which will show the error along with the line number.

You could also try implementing a module import/export system for EGG using Python's `pathlib`.
 check out architecture.md to know more
 
### 3. Improving Error Logs

You could improve error logs — maybe by adding a file-tracking system so errors point back to the exact file they came from.

### 4. Writing Tests

Add tests to check EGG's behavior and help find bugs just add your tests to tests/ folder
check out tests from from main readme to know more

### 5. Bug Fixes

Fix any minor bugs you find in the parser or interpreter.

###6 Doc update 
you can also update or make doc in detail that other can understand egg easily


---

There are many ways to contribute to EGG — pick whatever interests you.


## Feature Requests

Please describe:
- The problem you're trying to solve.
- Your proposed solution.
- Possible alternatives.

---

## Code of Conduct

Be respectful and constructive.

---

## Questions

If you have questions, feel free to open a GitHub Issue — I'll be there for you.
