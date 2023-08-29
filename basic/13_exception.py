# run command in try
# if runtime error, run command in except
# else, run command in else
# and run command in finally

# if you don't know type of error
# use Exception
try:
    x=int(input("Enter number1: "))
    y=int(input("Enter number2: "))
    z = x/y
except Exception as e:
    print(e)
else:
    print("Division is: ", z)
finally:
    print('Finish')

# if you know type of error
# use type of error
try:
    x=int(input("Enter number1: "))
    y=int(input("Enter number2: "))
    z = x/y
except ZeroDivisionError as e:
    print('Division by zero exception')
    z = None
except ValueError as e:
    print('Type error exception')
    z = None
else:
    print("Division is: ", z)
finally:
    print('Finish')

# can defind type of error
while True:
    try:
        x = int(input())
        y = int(input())
        if x == 0 and y == 0:
            print('Finish')
            break
        if x < 0 and y < 0:
            raise Exception("cannot use Negative value")
        print("Division is: ",x/y)
    except Exception as e:
        print(e)
    finally:
        print('work...')