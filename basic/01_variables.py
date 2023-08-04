# variable naming rules
# no keywords: example True, for
# no special characters: foo+bar
# they must begin with a letter or _
# other characters can be letters (a to Z, A to Z) or numbers (0 to 9)
# names are case sensitive
num1=10
num_1=5
NUm_1X=1
print(num1)
print(num_1)
print(NUm_1X)

# variable also can defind any type of data
# integer variable
i=1
print('type :', type(i))
# float variable
f=1.0
print('type :', type(f))
# string variable
s='Hello'
print('type :', type(s))
# boolean variable
b=True
print('type :', type(b))

# you have to declare data type of a variable in advance
foo=5
# you can set new value and data type to variable
foo=10 # at this point foo=10 (same type) and 5 will be garbage collected
print(foo)
foo='ABC' # at this point foo='ABC' (new type) and 10 will be garbage collected
print(foo)
bar=foo # you can set like this
print("foo id",id(foo))
print("bar id",id(bar))