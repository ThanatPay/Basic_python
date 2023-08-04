import math

# basic calculation
print(1+2) # 3
print(4-2) # 2
print(5*2) # 10
print(1/2) # 0.5
print(3//2) # 1
print(17%3) # 2
print(2**4) # 16
print(10+2*3) # 16
print((10+2)*3) #36

# Use python to find volume of cone
radius=10
height=3
volume=(1/3)*(math.pi)*(radius**2)*(height)
print('Volume :', volume) # Volume :  314.15926535897927
# to show volume till 2 decimal places
print('Volume :', round(volume,2)) # Volume :  314.16

# Number data types (int, float, complex numbers)
print(type(volume)) # float
foo=2.3e-3
print(foo) # 0.0023
print(type(1)) # int
print(0xA) # 10 (A is base 16)
print(type(0x12)) # int
c1=2+3j
print(type(c1)) # complex
c2=3-4j
print(c1+c2) # 5-j

# Internal representation of numbers
# (a) integers are stored in simple binary format
print(format(5,'b')) # 4 bytes (or 32 bits), visual of binary presentation
# (b) floats use IEEE754 standard : https://en.wikipedia.org/wiki/IEEE_754
print(5-4.7) # this prints 0.2999999999999998 and not 0.3. why? Due to IEEE 754 standard