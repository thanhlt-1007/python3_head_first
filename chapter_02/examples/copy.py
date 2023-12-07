first = [1, 2, 3, 4, 5]
print("first: ", first)

second = first
print("second: ", second)

second.append(6)
print("second: ", second)
print("first: ", first)

third = second.copy()
third.append(7)
print("third: ", third)
print("second: ", second)
