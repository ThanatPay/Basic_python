# if else

n=int(input("Enter a number:"))

if n%2==0:
    print("Number is even")
else:
    print("Number is odd")

# condition is boolean
# if the previous conditions were not true, then try elif condition
# after check all elif condition were not true, then try this else condition

# Python supports the usual logical conditions
# Equals: ==
# Not equals: !=
# grater than: >
# less than: <
# grater than or equal to: >=
# less than or equal to: <=
#
# _ and _
# _ or _
# not _


# Cousine checker. Explains if..elif..else
set1=[0,3,6,9]
set2=[1,4,7,10]
set3=[2,5,8,11]

n=int(input("Enter a number:"))

if n in set1:
    print(f"{n} is set1")
elif n in set2:
    print(f"{n} is set2")
elif n in set3:
    print(f"{n} is set3")
else:
    print(f"{n} is not all")
	

# Ternary operator
print("Ternary operator demo")
n=input("Enter a number:")
n=int(n)
message="Number is even" if n%2==0 else "Number is odd"
print(message)	