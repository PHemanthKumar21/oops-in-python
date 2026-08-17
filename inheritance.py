# inheritance
#1)single inheritance
'''class RBI():  #parent class
    cash = 100000
    def available_cash(cls):
        print("available cash is",cls.cash)
        print("available cash is",RBI.cash)
class SBI(RBI):#child -1
        pass
class HDFC(RBI):#child-2
        cash=50000
        def new_cash(cls):
            print("new cash is",cls.cash+cls.cash)
            print("new cash is",cls.cash+RBI.cash)
a=HDFC()
a.available_cash()
a.new_cash()'''

#output:-available cash is 50000
#              available cash is 100000
#              new cash is 100000
#              new cash is 150000


#MULTIPLE INHERITANCE:-
'''class father(): #PARENT CLASS -1 
    height=5.10
    def father_height(cls):
        print("father height is",cls.height)
class mother(): #PARENT CLASS -2
    weight=60
    def mother_weight(cls):
        print("mother weight is",cls.weight)
class kid(father,mother):
    def dob(cls):
        print("just born....")
a=father()
b=mother()
c=kid()
a.father_height()
b.mother_weight()
c.dob()'''

#output:-father height is 5.1
#              mother weight is 60
#              just born....


'''class father(): #PARENT CLASS -1 
    def height(cls):
        print("height is 6 ft")
class mother(): #PARENT CLASS -2
    def weight(cls):
        print("weight is 70")
class kid(father,mother):
    def dob(cls):
        print("just born....")
a=father()
b=mother()
c=kid()
a.height()
b.weight()
c.dob()'''


#3)MULTI-LEVEL INHERITANCE:-
'''class grandparent():
    def land(self):
        print("1 acre")
class parent(grandparent):
    def house(self):
        print("100 sqrt")
class child(parent):
    def bike(self):
        print("pulsar")
a=grandparent()
b=parent()
c=child()
a.land()
b.house()
c.bike()'''

#output:-1 acre
#              100 sqrt
#               pulsar


#4)hierarchical inheritance-where one parent class is inheritant by multiple chain classes.

'''class employee():  # PARENT CLASS
    def company(self):
        print("tcs")
class trainer(employee):  #CHILD CLASS -1
    def teaching(self):
        print("python")
class developer(employee):  #CHILD CLASS-2
    def developing(self):
        print("code")
a=trainer()
a.company()
a.teaching()
b=developer()
b.developing()
b.company()'''

'''output:-tcs
                python
                code
                tcs'''


#5)hybrid inheritance  is means combining one or more  than one type of inheritance mutli-level and hierarchical.
'''class person():
    def details(self):
        print("hemanth")

class trainer(person):
    def teaching(self):
        print("teaching python")
class student(person):
    def learning(self):
        print("learning python full stack")
class program_manager(trainer,student):
    def manage(self):
        print("assign classes ")
a=program_manager()
a.details()
a.teaching()
a.learning()
a.manage()'''


'''output:-hemanth
                teaching python
                learning python full stack
                assign classes'''

    





        
