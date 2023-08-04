# string
s='Hello World'
# you can concat string like this
print('Hello'+'World') # HelloWorld
# but you can't concat string like this
# print('1'+2) # 2 is int 
# you must be change int to string
print('1'+str(2)) # 12
# if you want to use ' in string
print("let's go") # let's go
print('let\'s go') # let's go
# multiline string using triple quotes
print('''Hello World
I will learn python''')
# Hello World
# I will learn python

# spacial characters
# tap use \t
print('Hello\tWorld') # Hello   World
# new line use \n
print('Hello World\nI will learn python')
# Hello World
# I will learn python

# string index
print(s[0]) # H
print(s[-1]) # d

# string slicing
print(s[0:3]) # Hel
print(s[:3]) # Hel
print(s[-3:-1]) # rl
print(s[-3:]) # rld

# len function
# count number of characters
print(len(s)) # 11

# check string in string
s='Hello World'
print('Hello' in s) # True
print('hello' in s) # False
print('hello' not in s) # True

# replace function
s='Hello World'
s.replace('Hello','hello') # if you print -> hello World (but s doesn't change)
print(s) # Hello World
s=s.replace('Hello','hello')
print(s) # hello World
# you can't replace string like this
# s[0]='x'

# upper/lower function
s='Hello World'
s.upper() # if you print -> HELLO WORLD (but s doesn't change)
print(s) # Hello World
s=s.upper()
print(s) # HELLO WORLD
s.lower() # if you print -> hello world (but s doesn't change)
print(s) # HELLO WORLD
s=s.lower()
print(s) # hello world

# isdigit function
# check all characters is number
print('145'.isdigit()) # True
print('145a'.isdigit()) # False

#index function 
#return first character in string
s='hello world'
print(s.index('llo')) # 2
print(s.index('world')) # 6