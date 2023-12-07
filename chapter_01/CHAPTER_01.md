# CHAPTER 01: THE BASICS

## 1. Breaking with Tradition

## 2. Starting with a meatier example

## 3. Jump right in

## 4. Python's IDLE is all you need to get going

## 5. Understanding IDLE's Windows

## 6. What happens next ...

## 7. Presss F5 to run your code

## 8. Code Runs Immediately

### a. Oh, good catch. That is confusing.

## 9. Excuting code, one statement at a time

### a. Let's be the Python interpreter

## 10. Functions + modules = the standard library

## 11. Batteries included

### a. Yes. That's what they mean.

## 12. Data structures come built-in

### a. Python variables are dynamically assigned

## 13. Invoking methods obtains results

### a. Invoking built-in module functionality

## 14. Deciding when to run blocks of code

### a. Blocks in Python are easy to spot, as they are always indented

## 15. What happened to my curly braces?

### a. A colon introduces an indented suite of code

## 16. What "else" can you have with "if"?

### a. Neither. Python spells it elif

```python
if today == 'Saturday':
  print('Party!!')
elif today == 'Sunday':
  print('Recover.')
else:
  print('Work, work, work.')
```

## 17. Suites can contain embedded suites

```python
if  today == 'Saturday':
  println('Party!')
elif today == 'Sunday':
  if condition == 'Headache':
    println('Recover, then rest.')
  else:
    print('Rest.')
else:
  print('Work, work, work.')
```

## 18. What we already know

## 19. Extending our program to do more

## 20. What's the bét approach to solving this problem?

### a. Both approaches work with Python

## 21. Returning to the Python Shell

## 22. Experimenting at the shell

### a. Flip the page when you're ready. Let the experiments begin.

## 23. Iterating over a sequence of objects

```python
for i in [1, 2, 3]:
  print(i)

for ch in "Hi!"
  print(ch)
```

## 24. Iterating a specific number of times

```python
for num in range(5):
  print("Head First Rocks!")
```

## 25. Applying the outcome of task #1 to our code

## 26. Indent suites with format ... indent region

```python
import datetime

odds = [
  1, 3, 5, 7, 9,
  11, 13, 15, 17, 19,
  21, 23, 25, 27, 29,
  31, 33, 35, 37, 39,
  41, 43, 45, 47, 49,
  51, 53, 55, 57, 59
]

for i in range(5):
  minute = datetime.datetime.today().minute
  if minute in odds:
    print("This minute seems a little odd.")
  else:
    print("Not an odd minute.")
```

## 27. Arranging to pause execution

## 28. Importation Confusion

## 29. Generating random integers with python

## 30. Asking the interpreter for help

## 31. Reviewing our experiments

```python
import datetime
import random
import time

odds = [
  1, 3, 5, 7, 9,
  11, 13, 15, 17, 19,
  21, 23, 25, 27, 29,
  31, 33, 35, 37, 39,
  41, 43, 45, 47, 49,
  51, 53, 55, 57, 59
]

for i in range(5):
  minute = datetime.datetime.today().minute
  if minute in odds:
    print("This minute seems a little odd.")
  else:
    print("Not an odd minute.")
  wait_second = random.randint(1, 60)
  time.sleep(wait_second)
```

## 32. Updating what we already know

## 33. A few lines of code do a lot

## 34. Coding a serious business application

## 35. Python code is easy to read

## 36. Is indentation driving you crazy

## 37. Asking the interpreter for help on a function

### a. Starting, stopping, and stepping

## 38. Experimenting with Ranges

```python
range(5)
# range(0, 5)
# range(0, 5, 1)

list(range(5))
# [0, 1, 2, 3, 4]

list(range(5, 10))
# [5, 6, 7, 8, 9]

list(range(0, 10, 2))
# [0, 2, 4, 6, 8]

list(range(10, 0, -2))
# [10, 8, 6, 4, 2]

list(range(10, 0, 2))
# []
```

## 39. Don't forget to try the beer song code
