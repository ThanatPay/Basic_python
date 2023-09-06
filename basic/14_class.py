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
        self.name=name # public attribute
        self.height=height # privat attribute
        self.weight=weight # protect attribute
    def __str__(self):
        # print(vars(self)) # get variable to dictionary
        return "name:{} height:{} weight:{}".format(self.name,self.height,self.weight)

print(Player('Steven',183.5,80.0))

# __repr__: when call class return value (traditional type)
# self.__class__.__name__ -> return name of class
class Player:
    def __init__(self,name,height,weight):
        self.name=name # public attribute
        self.height=height # privat attribute
        self.weight=weight # protect attribute
    def __repr__(self):
        return "{}{}".format(self.__class__.__name__,repr((self.name,self.height,self.weight)))

print(Player('Steven',183.5,80.0))
# if you have both __str__ and __repr__ -> run __str__