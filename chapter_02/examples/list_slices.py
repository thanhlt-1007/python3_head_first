saying = "Don't panic!"
letters = list(saying)
print("letters:", letters)
print("letters[0:10:3]:", letters[0:10:3]) # ['D', "'", 'p', 'i']
print("letters[3:]:", letters[3:]) # ["'", 't', ' ', 'p', 'a', 'n', 'i', 'c', '!']
print("letters[:10]:", letters[:10])  # ['D', 'o', 'n', "'", 't', ' ', 'p', 'a', 'n', 'i']
print("letters[::2]:", letters[::2]) # ['D', 'n', 't', 'p', 'n', 'c']
