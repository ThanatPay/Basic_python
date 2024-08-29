class Player: # super class
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def __str__(self):
        return "{} {}".format(self.fname,self.lname)

class PlayerNumber(Player): #subclass
    def __init__(self,num,fname,lname):
        super().__init__(fname,lname)
        self.num=num
    def __str__(self):
        return "{} {}".format(self.num,super().__str__())

class PlayerNational(PlayerNumber): # subclass
    def __init__(self,num,fname,lname,nation):
        super().__init__(num,fname,lname)
        self.nation=nation
    def __str__(self):
        return "{} {}".format(super().__str__(),self.nation)

p1=Player('Steven','Gerrard')
print(p1)
p2=PlayerNumber('08','Steven','Gerrard')
print(p2)
p3=PlayerNational('08','Steven','Gerrard','England')
print(p3)

# abstract base method class
# subclass must implement method below @abstractmethod
# can't call super class if you have @abstractmethod

from abc import ABC, abstractmethod 

class Member(ABC):
    def __init__(self,id,fname,lname):
        self.id=id
        self.fname=fname
        self.lname=lname
    def __str__(self):
        return "{} {} {}".format(self.id,self.fname,self.lname)
    
    @abstractmethod
    def discount(self):
        pass

    def full_name(self):
        return "{} {}".format(self.fname,self.lname)


class Gold(Member):
    def discount(self):
        return 0.10

g=Gold('1234','Peter','Parker')
print(g)
print(g.discount())
print(g.full_name()) # can call method in super class

# subclass can inherit method from multi super class
class Name:
    def fname(self, fname):
        print("First name:",fname)
    def lname(self, lname):
        print("Last name:",lname)

class National:
    def number(self,nation_num):
        print('National number:',nation_num)
    def national_name(self,nation_country):
        print('National country:',nation_country)

class Club:
    def number(self,club_num):
        print('Club number:',club_num)
    def club_name(self,club_name):
        print('Club name:',club_name)

class Player(Name,National,Club):
    pass

p=Player()
p.fname("Steven")
p.lname("Gerrard")
# if you have function same name (number in National and Club)
p.number(8)
# in this code run in National because in subclass Player -> National subclass written before Club

# if you want to run in Club
class Player(Name,Club,National):
    pass

p=Player()
p.number(8)
