#polymorhism:-
'''a=4;b=8
print(a+b)
print(a.__add__(b))
print(a.__sub__(2))
print(a.__mul__(8))
print(a.__pow__(2))
#print(a.__div__(4))
print(a.__eq__(4))
print(a.__le__(8))
print(a.__ge__(2))
a=[1,2,3,4,5];b=[6,7,8,9,10]
print(a.__add__(b))
print(a.__getitem__(3))
print(b.__getitem__(4))
a="python";b="course"
print(a.__add__(b))
print(a.__add__(" "+b))'''



#operator overloading:-

'''class A():
    def __init__(self,a):
        self.a=a
    def __add__(self,value):
        return self.a*value.b
class B():
    def __init__(self,b):
        self.b=b
X=A(6)
Y=B(4)
#print(x+y)
print(X+Y)'''

#output:-24


#method overloading

'''class new():
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print("the sum is",a+b+c)
        elif a!=None and b!=None:
            print("product is",a*b)
        else:
            print("program ends.......")
a=new()
#a.sum(2,4,6)
a.sum(4,5)'''

#output:-product is 20

#method overriding:-

'''class animal():
    def speak(self):
        print("anima can make sounds")
class dog():
    def speak(self):
        print("dog can barks")

a=animal()
b=dog()
a.speak()
b.speak()'''

#output:-anima can make sounds
#              dog can barks

'''class  car():
        def vehicle(self):
            print("thar")
class bike():
    def vehicle(self):
        print("vespa")

a=car()
b=bike()
a.vehicle()
b.vehicle()'''


#output:-thar
#              vespa




