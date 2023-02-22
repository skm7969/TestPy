# #ex1
# class Parent:
#     def met1(self):
#         print("Method 1 from parent class")
#
# class Child1(Parent):
#     def met2(self):
#         print("Met 2 from child class")
#
# obj1=Child1()
# obj1.met2()
# obj1.met1()
#
# #Ex2
# class P2:
#     x=90
#     y=50
#     def m3(self):
#         print(self.y+self.x)
#
# class P3(P2):
#     a,c=20,40
#     def m2(self):
#         print(self.c-self.a)
# ob1=P3()
# ob1.m3()
# ob1.m2()


# Multilevel Inheritance
#
# class P1:
#     d,o=90,89
#     def pm(self):
#         print(self.d+self.o)
#
# class P2(P1):
#     c,k=34,67
#     def pm2(self):
#         print(self.c*self.k)
#
# class P3(P2):
#     z,j=66,69
#     def pm3(self):
#         print(self.j%self.z)
#
# poj1=P3()
# poj1.pm()
# poj1.pm2()
# poj1.pm3()

# hierarchy Inheritance
#
# class P1:
#     d,o=90,89
#     def pm(self):
#         print(self.d+self.o)
#
# class P2(P1):
#     c,k=34,67
#     def pm2(self):
#         print(self.c*self.k)
#
# class P3(P1):
#     z,j=66,69
#     def pm3(self):
#         print(self.j%self.z)
#
# poj1=P3()
# poj1.pm()
# poj1.pm2()
# poj1.pm3()

# #Overriding
# class D:
#     def m3(self):
#         print("M3 from class D")
# class H(D):
#     def m3(self):
#         print("M3 from class H")
#         super().m3()
# Obj44=H()
# Obj44.m3()
#
# #Overriding variables Strings
#
# class ALOO:
#     g='Pela'
# class PYAJ(ALOO):
#     g='nalu'
# obj77=PYAJ()
# print(obj77.g)

# Overriding Methods & Polymorphism
#
# class PM:
#     def f1(self,name=None):
#         if name is not None:
#             print("Hello"+name)
#         else:
#             print("No hello")
# ob232=PM()
# ob232.f1('scotter')
# ob232.f1('repo')

# Overloading Ex 2

class Nine:
    def fuve(self, a=0, b=0, c=0):
        print(a + b + c)


ob1 = Nine()
ob1.fuve()
ob1.fuve(90,10)
ob1.fuve(7, 89, 40)
