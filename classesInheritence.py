# class Car:
#     speed=0
#     started=False
#     def start(self):
#         self.started=True
#         print('The car has started')
    
#     def Speed(self,val):
#         if self.started:
#             self.speed=val
#             print('vroooooooooooooooommm!  ')
#             print('Speed is now ',val)
#         else:
#             print('You need to start the car \'First\' ')
    
#     def stop(self):
#         self.speed=0
#         print('Breaking......................!')
#         print('************Stoped*****************')
#         print('the speed is now ',self.speed)

# obj=Car()
# obj.start()
# obj.Speed(40)
# obj.stop()


# class Vehicle:
#     def __init__(self,speed=0,started=False):
#         self.started=started
#         self.speed=speed

#     def start(self):
#         self.started=True
#         print('The car has started')
    
#     def Speed(self,val):
#         if self.started:
#             self.speed=val
#             print('vroooooooooooooooommm!  ')
#             print('Speed is now ',val)
#         else:
#             print('You need to start the car \'First\' ')
    
#     def stop(self):
#         self.speed=0
#         print('Breaking......................!')
#         print('************Stoped*****************')
#         print('the speed is now ',self.speed)


# class Car(Vehicle):
#     trunk_open=False
#     def open_trunk(self):
#         self.trunk_open=True
#     def close_trunk(self):
#         self.trunk_open=False


# class Motorcycle(Vehicle):
#     def __init__(self, centre_stand_out=False):
#         self.centre_stand_out=centre_stand_out
#         super().__init__()
    

#         #override the super method 
#     def start(self):
#         # super().start()
#         print('Sorry ran out of fuel !')


# motorcycle=Motorcycle()
# motorcycle.start()
# print(motorcycle.started)

# access modifiers in python



#public access modifiers
# class Ammar:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def returnage(self):
#         print('My age is :',self.age)

# ammar=Ammar('Ammar Tariq',23)

# print('My name is :',ammar.name)
# ammar.returnage()

#protected modifiers

# class Student:
#     _name=None
#     _roll=None
#     _branch=None
#     def __init__(self,name,roll,branch):
#         self._name=name
#         self._roll=roll
#         self._branch=branch
    
#     #accessing the protected data members
#     def _displayrollbranch(self):
#         print('Roll no :',self._roll)
#         print('Branch :',self._branch)
    
# class StudenDetails(Student):
#     def __init__(self, name, roll, branch):
#         super().__init__(name, roll, branch)
    
#     # public member function
#     def displayDetails(self):

#         #access the protected data member name
#         print('Name :',self._name)

#         # accessing the protected method of the base class 
#         self._displayrollbranch()

# studendetails=StudenDetails('Ammar Tariq',665,'CUI-ATD')
# studendetails.displayDetails()


#private access modifiers

# class Student:
#     __name=None
#     __age=None
#     __roll=None

#     def __init__(self,name,age,roll):
#         self.__name=name
#         self.__age=age
#         self.__roll=roll

#     def __displaydetails(self):
#         print('name :',self.__name)
#         print('name :',self.__age)
#         print('name :',self.__roll)

#     def accessprivateDetails(self):
#         self.__displaydetails()


# obj=Student('Ammar Tariq',23,'fa19-bse-065')
# obj.accessprivateDetails()

# # #name mangling
# print(obj._Student__name)


# copy constructor in python

# import copy

# class MyClass:
#     def __init__(self, param1, param2):
#         self.attribute1 = param1
#         self.attribute2 = param2

# # Creating an instance of MyClass
# obj1 = MyClass("value1", "value2")

# # Using the copy method from the copy module for a shallow copy
# obj2 = copy.copy(obj1)

# # Accessing attributes of the copied object
# print(obj2.attribute1)
# print(obj2.attribute2)


class City:
    def __init__(this):
        this.name='Ammar'
        this.price='*0903094093094304'
    
    def show(this):
        print(this.name)
        print(this.price)
    

c=City()
print(c.name)
c.show()

class MyClass:
    def __init__(self, value):
        self.value = value

    def print_value(self, prefix):
        print(f"{prefix}: {self.value}")

# Create an object
obj = MyClass(42)

# Call the method; you don't explicitly pass the instance
obj.print_value("The value is")
