# list
a=[1,3,4,5,6,7,8]
print(type(a)) # list

# index of list
print(a[0]) # 1
print(a[3]) # 5
print(a[-1]) # 8
# list slicing
print(a[1:4]) # [3,4,5]
print(a[:3]) # [1,3,4]
print(a[5:]) # [7,8]
print(a[-3:]) # [6,7,8]

# len function
print(len(a)) # 7

# check in list
print(1 in a) # True
print(9 in a) # False

# append function
a.append(9) # add 9 after the last index
print(a) # [1,3,4,5,6,7,8,9]

# insert function
a.insert(1,2) # add 2 at index 1
print(a) # [1,2,3,4,5,6,7,8,9]

# concatenate 2 list
l1=['a','b','c']
l2=[1,2,3]
print(l1+l2) # ['a','b','c',1,2,3]
# you can't add like this
# l1+'d' # 'd' is't list

# list items can be changed
a[2]='d'
print(a) # [1,2,'d',4,5,6,7,8,9]
a[-3:]=['x']
print(a) # [1,2,'d',4,5,6,'x']
a[:2]=['a','b','c']
print(a) # ['a','b','c','d',4,5,6,'x']

# above shows all function in list 
print(dir(a))