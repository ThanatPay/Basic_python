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


# class Player:
#     def __init__(self):
#         print("Player Information")
#     def detail(self,name,height,weight):
#         self.name=name
#         self.height=height
#         self.weight=weight
#     def showData(self):
#         print("name:",self.name)
#         print("height:",self.height)
#         print("weight:",self.weight)