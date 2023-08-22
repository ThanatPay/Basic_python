import math

def sphere(r=1):
    return (4/3)*math.pi*(r**3)


def cylinder(r=1,h=1):
    return math.pi*(r**2)*h

def cone(r=1,h=1):
    return (1/3)*math.pi*(r**2)*h