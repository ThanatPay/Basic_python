# tuple
Tuple=tuple((1,))
print(Tuple, type(Tuple))
Tuple=(1,2)
print(Tuple, type(Tuple))
Tuple=1,2,3
print(Tuple, type(Tuple))

# index of tuple
print(Tuple[0])
print(Tuple[-1])
# tuple slicing
print(Tuple[:2])
print(Tuple[1:2])
print(Tuple[1:])
print(Tuple[1:-1])

# tuples are immutable
Tuple = (3, 7, 4, 2)
# it is impossible to update individual items in a tuple
# z[1] = 5
tup1 = ('Python', 'SQL')
tup2 = ('R',)
# Create new tuple based on existing tuples
new_tuple = tup1 + tup2
print(new_tuple)

# tuple methods
tup = (3,7,4,3,'b')
# find index of 3
print(tup.index(3))
# count number of 3
print(tup.count(3))

# print all value in tuple using for loop
for item in tup:
    print(item)

tup = ('A', 'B', 'C', 'D')
for index, value in enumerate(tup):
    print(index,value)

# can set value in tuple to multiple variable like this
x, y = (7, 10)
print("Value of x is {}, the value of y is {}.".format(x, y))

# tuples are faster than list
import timeit 
print('Tuple time: ', 
      timeit.timeit('x=(1,2,3,4,5,6,7,8,9,10,11,12)', number=1000000))
print('List time: ', 
      timeit.timeit('x=[1,2,3,4,5,6,7,8,9,10,11,12]', number=1000000))