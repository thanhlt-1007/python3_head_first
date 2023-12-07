book = "The Hitchhiker's Guide to the Galaxy"
booklist = list(book)
print("booklist:", booklist)

print("booklist[0:3]:", booklist[0:3]) # ['T', 'h', 'e']
print("''.join(booklist[0:3]):", ''.join(booklist[0:3])) # 'The'
print("''.join(booklist[-6:]):", ''.join(booklist[-6:])) # 'Galaxy'
