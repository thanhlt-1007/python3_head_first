# CHAPTER 02: LIST DATA

## 1. Numbers, strings ... and objects

### a. Numbers

```python
import random

wait_time = random.randint()
print("wait_time: ", wait_time)
```

### b. Strings

```python
word = "bottles"
```

### c. Objects

## 2. Everything is an object

## 3. Meet the four built-in data structures

## 4. Ordered collections are mutable / immutable

## 5. An undrdered data structure: dictionary

## 6. A data structure that avoids duplicates: set

## 7. A list is an ordered collection of objects

## a. How to spot a list in code

```python
odds = [
  1, 3, 5, 7, 9,
  11, 13, 15, 17, 19,
  21, 23, 25, 27, 29,
  31, 33, 35, 37, 39,
  41, 43, 45, 47, 49,
  51, 53, 55, 57, 59
]
```

## 8. Creating lists literally

```python
prices = []
temps = [32.0, 212.0, 0.0, 81.6, 100.0, 45.3]
words = ['hello', 'world']
car_details = ['Tokyo', 'RAV4', 2.2, 60807]
everything = [prices, temps, words, car_details]
odds_and_ends = [
  [1, 2, 3],
  ['a', 'b', 'c'],
  ['One', 'Two', 'Three']
]
```

## 9. Putting lists to work

### a. Working with lists

```python
vowels = ['a', 'e', 'i', 'o', 'u']
word = "Milliways"
```

### b. Is one object inside another? Check with "in"

```python
for letter in word:
  if letter in vowels:
    print(letter)
```

## 10. Use your editor when working on more than a few lines of code

## 11. "Growing" a list at runtime

```python
found = []
len(found)

found.append('a')
len(found)

found.append('e')
found.append('i')
found.append('o')
len(found)

found # ['a', 'e', 'i', 'o']
```

## 12. Checking for membership with "in"

## 13. It's time to update our code

```python
vowels = ['a', 'e', 'i', 'o', 'u']
word = "Milliways"
found = []

for letter in word:
  if letter in vowels:
    if leeter not in found:
      found.append(letter)

for vowel in found:
  print(vowel)
```

## 14. Removing objects from a list

```python
nums = [1, 2, 3, 4]
nums

nums.remove(3)
nums # [1, 2, 4]
```

## 15. Popping objects off a list

```python
nums = [1, 2, 4]
nums.pop # 4
nums # [1, 2]

nums.pop(0) # 1
nums # [2]
```

## 16. Extending a list with objects

```python
nums = [2]
nums.extend([3, 4])
nums.extend()
```

## 17. Inserting an object into a list

```python
nums = [2, 3, 4]
nums.insert(0, 1)
nums.insert(2, "two-and-a-half")
```

## 18. What about using square brackets

## 19. What Happened to "plist"?

## 20. What Happened to "plist", continued

## 21. Lists: what we know

## 22. What looks like a copy, but isn't

```python
first = [1, 2, 3, 4, 5]
first # [1, 2, 3, 4, 5]

second = first
second # [1, 2, 3, 4, 5]

second.append(6)
second # [1, 2, 3, 4, 5, 6]
first # [1, 2, 3, 4, 5, 6]
```

# 23. How to coppy a data structure

```python
third = second.copy()
third # [1, 2, 3, 4, 5, 6]

third.append(7)
third # [1, 2, 3, 4, 5, 6, 7]
second # [1, 2, 3, 4, 5, 6]
```

## 24. Square brackets are everywhere

## 25. Lists extend the square bracket notation

```python
saying = "Don't panic!"
letters = list(saying)
letters
letters[0] # D
letters[3] # '
letters[6] # p
letters[-1] # !
letters[-3] # i
letters[-6] # p
```
