
'''1.  duck typing
if any thing walk like a duck, swim or behve like a duck then its duck '''


# class Duck:
#     def walk(self):
#         print('Thapak Thapak Thapak Thapak')
    
# class Horse:
#     def walk(self):
#         print('Tagr tage tagr tager')

# class Cat:
#     def talk(self):
#         print('.................. sloe slow slow.........')
# def function(obj):
#     if hasattr(obj,'walk'):

#      obj.walk()

# d=Duck()
# function(d)

# h=Horse()
# function(h)
# c=Cat()
# function(c)

# function ovverloading in py 

# class myClass:
#     def sum(self,a=None,b=None,c=None):
#         if a!=None and b!=None and c!=None:
#             s=a+b+c
#             print('this is sum :',s)
#         elif a!=None and b!=None:
#             s=a+b
#             print('this is sum :',s)
#         else:
#             print('provide at least two numbers')
    
    
# ojb=myClass()
# ojb.sum()


# optr overiding

# class A:
#     def __init__(self,x):
#         self.x=x
    
#     def __add__(self,other):
#         return self.x + other.x
    
   
# class B:
#     def __init__(self,x):
#         self.x=x
    
    


# a=A(100)
# b=B(20)
# print(a+b)

