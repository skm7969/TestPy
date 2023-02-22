#Ex1

# Create a class & object
#
# class new:
#     def newfunc(self):
#         pass
#     def display(self,name):
#         print(name)
#
#
#
# new1=new()
# new2=new()
#
# new2.newfunc()
# new2.display("Pubg")
#
# new1.display("Abbas")


#Ex 2

# class vicks():
#     def inhaler(self):
#         print("This is a instance method")
#     @staticmethod
#     def roll(self,num):
#         print(num)


#Creating class variables & access them with in a class methord
#
# class bottle():
#     a,b,c=20,'Vivan',40
#
#     def plastic(self):
#         print(self.a,self.c)
#
#     def glass(self):
#         print(self.b)
#
# mybot=bottle()
# mybot.glass()
# mybot.plastic()
#
# #combining global,local & class variable
#
# i,j,l=20,60,80
#
# class tv():
#     z,o,p=1,3,5
#     def lg(self,c,v,m):
#         print(c+v+m)
#         print(self.p+self.z+self.o)
#         print(i+j+l)
#
# carton=tv()
# carton.lg(44,55,66)


#One class multiple objects
# class mulobj:
#     def skm(self,name):
#         print("DIsplay method")
#         print(name)
#
# ob1=mulobj
# ob1.skm("Aksaaa","Rusho")
#
# ob2=mulobj
# ob2.skm("Rashi","auro")

#method -- Can give any name || Return the values || method can take arguement/parameter  || We have to use an object to invoke the method

# #constructor -- Name is fixed ,ie, def _init_(self):
#                 Constructor wont return any value
#                 Constructor takes arguements & parameters
#                 Constructor will be called at the time of object creation itself

# class const:
#     def __init__(self):
#         print("This is a constructor")
#     def methd1(self):
#         print("This is method")
#     def met2(self,x,y):
#         return (x+y)
#
#
# mc=const()
# mc.methd1()
# print(mc.met2(40,20))

#ex Parameterised constructor
#
# class pconst:
#     blues='asis'
#     def __init__(self,blues):
#         print(blues)
#
#         print(self.blues)

# var1=pconst("Valid") #passing param to const

#Ex9

class employee:
    def __init__(self, eid, ename, sal):
            self.eid=eid
            self.ename=ename
            self.sal=sal
    def __str__(self):
        return (self.ename,self.eid,self.eid)


    def display(self):
        print(self.eid)
        print(self.ename)
        print(self.sal)

ob44=employee(1,'om',90000)
print(ob44)


# ob2=employee(2,'skm',200)
# ob2.display()
#
# ob3=employee(23,'xyz',400)
# ob3.display()
#
# ob76=employee(62,'papu',92)
# ob76.display()