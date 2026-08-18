#Encapsulation
#combining multiple units into single unit is knowm it as encapsulation:
#1)publicdata
'''class A():
    publicdata=100
    def method1(self):
        print(self.publicdata)
class B(A):
    def method2(self):
        print(self.publicdata)
a=B()
a.method1()
a.method2()'''

#output:-  100
#                100


#2)Protecteddata
'''class A():
    _protecteddata=200
    def method1(self):
        print(self._protecteddata)
class B(A):
    def method2(self):
        print(self._protecteddata)

a=B()
a.method1()
a.method2()
print(a._protecteddata)'''

#output:-  200
#                200
#                200


#3)privatedata
class A():
    __privatedata="hemanth"
    def method1(self):
        print(self.__privatedata)
class B(A):
    def method2(self):
        print(self._A__privatedata)
    
a=B()
a.method1()
a.method2()



        

                


