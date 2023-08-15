# for loop

# range() function
print(range(6)) # range(0,6)
print(range(1,6)) # range(1,6)
print(list(range(1,6))) # [1,2,3,4,5]
for i in range(1,6):
    print(i)
# 1
# 2
# 3
# 4
# 5

# sum all value using simple sum
values = [1000,1500,2000,2500]
sum_value = values[0] + values[1] + values[2] + values[3]
print(sum_value) # 7000

# sum all value using for loop
sum_value = 0
for value in values:
    sum_value = sum_value + value
print(sum_value) # 7000

# print index number, value and then sum value
# using range
sum_value = 0
for i in range(len(values)):
    print(f"index {i}, value: {values[i]}")
    sum_value += values[i]
# index 0, value: 1000
# index 1, value: 1500
# index 2, value: 2000
# index 3, value: 2500
print(f"The sum of value is {sum_value}")
# The sum of value is 7000

# using enumerate
sum_value = 0
for index, value in enumerate(values):
    print(f"index {index}, value: {value}")
    sum_value += value
# index 0, value: 1000
# index 1, value: 1500
# index 2, value: 2000
# index 3, value: 2500
print(f"The sum of value is {sum_value}")
# The sum of value is 7000

# break (out of loop)
for value in values:
    if value==2000:
        break
    print(value)
# 1000
# 1500

# continue (go to next step of loop)
for value in values:
    if value==2000:
        continue
    print(value)
# 1000
# 1500
# 2500

# while loop
num=0
while num<=5:
    print(num)
    num=num+1
# 0
# 1
# 2
# 3
# 4
# 5