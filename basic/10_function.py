# Calculate sum of value in list without fuction
values1 = [1000,2000,3000,4000]
values2 = [500,1500,2500,3500]

total=0
for value in values1:
    total+=value
print("Total value of value1 :", total)

total=0
for value in values2:
    total+=value
print("Total value of value2 :", total)

# Calculate sum of value in list with fuction
values1 = [1000,2000,3000,4000]
values2 = [500,1500,2500,3500]

def find_total(values):
    total=0
    for value in values:
        total+=value
    return total

print("Total value of value1 :", find_total(values1))
print("Total value of value2 :", find_total(values2))

# Explain argument, return value, function body with visuals

# documentation strings
# print(help(find_total))

# function return value of cylinder
def cylinder_volume(radius=1,height=1):
    print("radius is:",radius)
    print("height is:",height)
    area = 3.14*(radius**2)*height
    return area
# default arguments
print(cylinder_volume())
# Positional argument
print(cylinder_volume(2,2))
# named arguments
print(cylinder_volume(radius=3,height=3))

# global vs local variables

# global and local variables have the same name. but not the same variable
# global variable is definded outside function 
value=2
# local variable is definded in function
def two_times(value):
    print("local value:",value)
    value=2*value
    print("local value:",value)

print("global value:",value)
two_times(value=value)
print("global value:",value)

# can defind global variable in function use global
def show_value(): 
    global value1
    global value2
    value2=2
    print("Print value1 in function:",value1)
    print("Print value1 in function:",value2)


# can't print value1 because the function defind value1 but can't set value
value1=1 # You must set value to value1
print("Print value1 outside function:",value1)
# can't print value2 outside function becasue value2 is local variable
# print("Print value1 outside function:",value2)
show_value()


