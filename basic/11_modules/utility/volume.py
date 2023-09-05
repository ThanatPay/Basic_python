import math

def sphere(r=1):
    return (4/3)*math.pi*(r**3)


def cylinder(r=1,h=1):
    return math.pi*(r**2)*h

def cone(r=1,h=1):
    return (1/3)*math.pi*(r**2)*h

# spacial variable -> __name__
# when you import in another file 
# code bolow if __name__ == '__main__' is't running
if __name__ == '__main__':
    print('Sphere volume :', round(sphere(1),4))
    print('Cylinder volume :',round(cylinder(1,1),4))
    print('Cone volume :',round(cone(1,1),4))