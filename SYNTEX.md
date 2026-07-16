EGG Syntax Guide (Simple English)

1. Variables

Create a variable using "var".

Example:

var name = "Egg"
var age = 10

Remove a variable using "rm".

Example:

rm age

---

2. Comments

Comments start with "€".

Example:

€ This is a comment
var x = 5

---

3. Output

Use "show()" to print something.

Example:

show("Hello")
show(x)

---

4. User Input

Use "ask()" to get input from the user.

Example:

var name = ask("Your name: ")
show(name)

---

5. Functions

Create a function using "fun".

Example:

fun hello() {
    show("Hello")
}

Return a value using "return".

Example:

fun add(a, b) {
    return a + b
}

Call a function:

hello()

Functions can be inside other functions.

---

6. Conditions

Use "if", "elif", and "else".

Example:

if (age > 18) {
    show("Adult")
} elif (age is 18) {
    show("Exactly 18")
} else {
    show("Child")
}

---

7. Loops

While Loop

Runs while a condition is TRUE.

Example:

while (x < 5) {
    show(x)
    x = x + 1
}

For Loop

Runs through items in a list.

Example:

var nums = [1, 2, 3,]

for (num in nums) {
    show(num)
}

---

8. Loop Controls

"stop" exits a loop.

Example:

while (TRUE) {
    stop
}

"skip" skips the current loop step.

Example:

for (x in nums) {
    if (x is 2) {
        skip
    }

    show(x)
}

---

9. Boolean Values

EGG has two boolean values:

TRUE
FALSE

Example:

var active = TRUE

---

10. Null Value

The empty value is:

NONE

Example:

var data = NONE

---

11. Lists

Lists use square brackets.

Example:

var numbers = [1, 2, 3,]

Access a list item:

var first = numbers[0]

Do not directly index a list literal.

Wrong:

[1, 2, 3,][0]

Correct:

var nums = [1, 2, 3,]
var first = nums[0]

---

12. Dictionaries

Dictionaries store key and value pairs.

Dictionary iteration uses:

keys(dict)

or

values(dict)

Example:

for (key in keys(data)) {
    show(key)
}

---

13. Operators

Math Operators

+
-
*
/
^

Example:

var total = 5 + 3

---

14. Comparison Operators

Use:

>
<
>_
<_
is
isnot

Examples:

x > 5
x < 5
x is 5
x isnot 5

---

15. Logical Operators

Use:

and
or
not

Examples:

if (age > 10 and age < 20) {
    show("Teen")
}

---

16. Keywords

EGG keywords:

var
and
or
in
not
stop
skip
return
rm

---

17. Statements

EGG statements:

if
elif
else
fun
while
for

---

18. Symbols

EGG symbols:

.
,
=
:

---

19. Numbers

Digits:

0 1 2 3 4 5 6 7 8 9

---

20. Basic EGG Program Example

€ Simple EGG program

var name = ask("Name: ")

fun greet(person) {
    show("Hello " + person)
}

greet(name)