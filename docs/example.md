# 🥚 EggLang Examples

A collection of example programs that showcase the features and capabilities of **EggLang**—a simple, expressive programming language designed for learning and prototyping.

> **ℹ️ Note:** All examples use features currently available in EggLang v1.0+. As the language evolves, new examples and features may be added.

---

## 📖 Quick Navigation

- [Hello World](#-hello-world)
- [Calculator](#-calculator)
- [Word Counter](#-word-counter)
- [Password Checker](#-password-checker)
- [List Operations](#-list-operations)
- [Student Database](#-student-database)
- [Expense Calculator](#-expense-calculator)
- [Contact Manager](#-contact-manager)
- [Text Analyzer](#-text-analyzer)
- [Simple Bank Account](#-simple-bank-account)

---

## 👋 Hello World

The simplest EggLang program—a classic introduction that prints a message.

```egg
show("Hello, World!")
```

**Output:**
```
Hello, World!
```

---

## 🧮 Calculator

A simple interactive calculator that performs basic arithmetic operations based on user input.

```egg
var calc_a = number(ask("First Number: "))
var calc_b = number(ask("Second Number: "))
var calc_op = ask("Operator (+ - * / ^): ")

if (calc_op is "+") {
    show(calc_a + calc_b)
} elif (calc_op is "-") {
    show(calc_a - calc_b)
} elif (calc_op is "*") {
    show(calc_a * calc_b)
} elif (calc_op is "/") {
    show(calc_a / calc_b)
} elif (calc_op is "^") {
    show(calc_a ^ calc_b)
} else {
    show("Invalid Operator")
}
```

**Example run:**
```
First Number: 10
Second Number: 5
Operator (+ - * / ^): +
15
```

---

## 🔤 Word Counter

Counts the number of words in a user-provided sentence by iterating through characters.

```egg
var wc_text = ask("Enter Sentence: ")
var wc_words = 1

for (wc_char in wc_text) {
    if (wc_char is " ") {
        wc_words = wc_words + 1
    }
}

show("Words:")
show(wc_words)
```

**Example run:**
```
Enter Sentence: EggLang is fun
Words:
3
```

---

## 🔐 Password Checker

A simple password validation program using string comparison and conditional logic.

```egg
var pass = ask("Password: ")

if (pass is "egglang") {
    show("Correct Password")
} else {
    show("Wrong Password")
}
```

---

## 📋 List Operations

Demonstrates common list operations including push, pop, pushfirst, and popfirst methods.

```egg
var todos = []

todos.push("Study")
todos.push("Code")
todos.push("Sleep")

show(todos)

todos.pushfirst("Wake Up")
show(todos)

todos.pop()
show(todos)

todos.popfirst()
show(todos)
```

**Output:**
```
["Study", "Code", "Sleep"]
["Wake Up", "Study", "Code", "Sleep"]
["Wake Up", "Study", "Code"]
["Study", "Code"]
```

---

## 🎓 Student Database

Stores and retrieves structured student information using nested dictionaries and built-in utility functions.

```egg
var students = {
    alice: {
        age: 18,
        grade: "A",
    },
    bob: {
        age: 19,
        grade: "B",
    },
}

show(students.alice.grade)
show(students.bob.grade)

show(keys(students))
show(values(students))
```

**Output:**
```
A
B
[alice, bob]
[{age: 18, grade: A}, {age: 19, grade: B}]
```

---

## 💰 Expense Calculator

Calculates total expenses from a dictionary of expense categories.

```egg
var expenses = {
    food: 300,
    internet: 500,
    transport: 200,
}

var expense_total = expenses.food + expenses.internet + expenses.transport

show(expense_total)
```

**Output:**
```
1000
```

---

## 📇 Contact Manager

A simple contact storage system that organizes contact information in nested dictionaries.

```egg
var contacts = {
    alice: {
        phone: "01711111111",
        city: "Dhaka",
    },
    bob: {
        phone: "01822222222",
        city: "Rajshahi",
    },
}

show(contacts.alice.phone)
show(contacts.alice.city)

show(contacts.bob.phone)
show(contacts.bob.city)
```

**Output:**
```
01711111111
Dhaka
01822222222
Rajshahi
```

---

## 📝 Text Analyzer

Analyzes user input text by counting total characters and spaces.

```egg
var ta_text = ask("Enter Text: ")

var ta_chars = 0
var ta_spaces = 0

for (ta_char in ta_text) {
    ta_chars = ta_chars + 1

    if (ta_char is " ") {
        ta_spaces = ta_spaces + 1
    }
}

show("Characters")
show(ta_chars)

show("Spaces")
show(ta_spaces)
```

**Example run:**
```
Enter Text: EggLang rocks
Characters
14
Spaces
1
```

---

## 🏦 Simple Bank Account

Demonstrates dictionary updates, arithmetic operations, and conditional logic with a practical banking scenario.

```egg
var account = {
    owner: "Egg",
    balance: 1000,
}

show(account.owner)
show(account.balance)

var deposit = number(ask("Deposit: "))

account.balance = account.balance + deposit

show(account.balance)

var withdraw = number(ask("Withdraw: "))

if (withdraw <= account.balance) {
    account.balance = account.balance - withdraw
    show("Withdraw Success")
} else {
    show("Insufficient Balance")
}

show(account.balance)
```

**Example run:**
```
Egg
1000
Deposit: 500
1500
Withdraw: 300
Withdraw Success
1200
```

---

**EggLang** is actively evolving. More examples will be added as new language features are introduced. Happy coding! 🐣