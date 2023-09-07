# class

# __init__: run command when call class
# __del__: clear RAM when class is stopped
class Player:
    def __init__(self):
        print("Default construtor")
    def detail(self,name,height,weight):
        self.name=name
        self.height=height
        self.weight=weight
    def showData(self):
        print("name:",self.name)
        print("height:",self.height)
        print("weight:",self.weight)
    def __del__(self):
        print("Call destructor")

# call class Player in p variable 
# run command in __init__
p=1
p=Player()
# class.function: run function in class
p.detail("Steven", 183.5, 80.0)
p.showData()
# call class Player again in p variable
# previous class Player is stopped
# run command in __del__
p=Player()
p.detail("Steven", 183.5, 80.0)
p.showData()

# public attribute: can update and call outside class
# private attribute: can update and call outside class if call class._attribute 
# protect attribute: cannot update and cannot call outside class
class Player:
    def __init__(self,name,height,weight):
        self.name=name # public attribute
        self._height=height # privat attribute
        self.__weight=weight # protect attribute
    def showData(self):
        print("name:",self.name)
        print("height:",self._height)
        print("weight:",self.__weight)

p=Player('Steven',183.5,80.0)
p.name="Gerrard"
p.height=185.0
p.weight=81.0
p.showData() # name change, weight dont change, weight dont change
p._height=185.0
p.__weight=81.0
p.showData() # weight change, weight dont change

# __str__: when call class return value type string (Normally, not return value)
class Player:
    def __init__(self,name,height,weight):
        self.name=name
        self.height=height
        self.weight=weight
    def __str__(self):
        # print(vars(self)) # get variable to dictionary
        return "name:{} height:{} weight:{}".format(self.name,self.height,self.weight)

print(Player('Steven',183.5,80.0))

# __repr__: when call class return value (traditional type)
# self.__class__.__name__ -> return name of class
class Player:
    def __init__(self,name,height,weight):
        self.name=name
        self.height=height
        self.weight=weight
    def __repr__(self):
        return "{}{}".format(self.__class__.__name__,repr((self.name,self.height,self.weight)))

print(Player('Steven',183.5,80.0))
# if you have both __str__ and __repr__ -> run __str__

# __eq__: compare value in class
class Member:
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def __repr__(self):
        return "{}{}".format(self.__class__.__name__,repr((self.name,self.score)))
    def __eq__(self, other):
        return self.score == other.score

m1=Member('Steven',80)
print(m1)
m2=Member('Jordan',75)
print(m2)
m3=Member('Steven',80)
print(m3)
print(id(m1),id(m2),id(m3)) # not same instance
print(m1==m2)
print(m1==m3) # if you don't have __eq__ it's not equal (not same instance)

# operation loading
class Member:
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def __repr__(self):
        return "{}{}".format(self.__class__.__name__,repr((self.name,self.score)))
    def __add__(self, other):
        return self.score + other.score # method can be anythong
    def __sub__(self, other):
        return self.score - other.score # method can be anythong
    
m1=Member('Steven',80)
print(m1)
m2=Member('Jordan',75)
print(m2)
# using + when you call method __add__ 
print(m1+m2)
# using - when you call method __sub__ 
print(m1-m2)

# class method
# class can set instance method like __init__ when using @classmethod
# class can run function without run instance method when using @staticmethod
class Player:
    def __init__(self,name,height,weight):
        self.name=name
        self.height=height
        self.weight=weight
    @classmethod
    def of(cls,player_string,sep='-'):
        s=player_string.split(sep)
        return cls(s[0],s[1],s[2])
    @staticmethod
    def gram_oz(g):
        return g*0.035274
    def __str__(self):
        return "{}-{}-{}".format(self.name,self.height,self.weight)
    
print(Player('Steven',183.5,80.0))
print(Player.of('Steven-183.5-80.0'))
print(Player.gram_oz(20))