#Abstraction:-hiding unnecessary information from user is called abstraction
#1.absrtact class  
'''class A():
    def method1(self):
        pass
obj1=A()
obj1.method1()'''

'''class A ():
    def method1(self):
        print("data")
obj1=A()
obj1.method1()'''


'''from abc import ABC ,abstractmethod
class A():
    def method1(self):
        print("python course")
obj1=A()
obj1.method1()'''

#output:-python course





'''from abc import ABC ,abstractmethod
class A(ABC):
    def method1(self):
        pass
    def method2(self):
        print("Python Full Stack")
    def method3(self):
        pass
class B(A):
    def method1(self):
        print("java full stack")
    def method3(self):
        print("data structures")

a=B()
a.method1()
a.method2()
a.method3()'''

#output:- java full stack
#              Python Full Stack
#              data structures







    

