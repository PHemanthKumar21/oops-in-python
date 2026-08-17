#OOPS:
#Syntax
'''class classname():
#attributes
    name="hemanth"
    age="21"
    place="vja"
    def fname(method_name):
        print("statements......")
a=classname()
print(dir(a))
a.fname()'''

#Class declaration:
'''class details():
    name="hemanth"
    age="21"
    place="vja"
    def display(self):
            print(self.name,self.age,self.place)
a=details()
print(dir(a))
a.display()'''
#output:-hemanth 21 vja

#Object instantiation
'''class details():
    def fname(data,name,age,place):
        data.name=name
        data.age=age
        data.place=place
    def display(data):
        print(data.name,data.age,data.place)
a=details()
print(dir(a))
a.fname("hemanth","21","vja")
a.display()
b=details()
b.fname("shyam","21","vja")
b.display()'''

#output:-hemanth 21 vja
#              shyam 21 vja


#object initialization

'''class details():
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=details("hemanth","21","vja")
print(dir(a))
a.display()'''

#output:-hemanth 21 vja



#Run time

'''class details():
    def __init__(self):
        self.name=input("name")
        self.age=int(input("age"))
        self.place=input("place")
    def display(self):
        print(self.name,self.age,self.place)
a=details()
print(dir(a))
a.display()'''




'''class details():
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=details(input("name"),int(input("age")),input("place"))
print(dir(a))
a.display()''' 



#diff b/w _ and __
'''class employee():
    def __init__(self):
            self. name="hemanth"
            self._mailid="hemanth@gmail.com"
            self.__salary=10000
a=employee()
print(dir(a))
print(a.name)
print(a._mailid)
print(a.name_employee__salary)'''


'''class employee1():
    def __init__(self):
            self. name="hemanth"
            self._mailid="hemanth@gmail.com"
            self.__salary=10000
class employee2():
    def __init__(self):
            self. name="sai"
            self._mailid="sai@gmail.com"
            self.__salary=20000
a=employee1()
print(dir(a))
print(a.name)
print(a._mailid)
print(a._employee1__salary)'''



