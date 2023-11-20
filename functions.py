# from functools import reduce

# def func():
#     print('hello there im a function')

# func()




# add_one=(lambda a:a+1)

# print(add_one(2))

# full_name =lambda first_name,last_name:f"Full name : {first_name.title()} {last_name.title()}"
# print(full_name('Ammar','Tariq'))


# #map functions


# a=list(map(lambda x:x.capitalize(),['a','b','c','d']))
# print(a)

# print([x.capitalize() for x in ['a','b','c']])


# def even(x):
#     return x%2==0

# print(list(filter(even,range(20))))


# #reduce 


# numbers =[1,2,3,4,5,6,7,8]

# product_of_list=reduce((lambda x,y:x*y),numbers)

# print(product_of_list)



# def add(x,y):
#     return x+y

# res=add(2,5)
# print('the addition is ' ,res)


# # *********calculator*************

# optr=input('Enter any operator')

# match optr:
#     case '+':
#         num1=float(input('enter first number'))
#         num2=float(input('enter 2nd number'))
#         res=num1+num2
#         print('the result is ',res)
#     case '-':
#         num1=float(input('enter first number'))
#         num2=float(input('enter 2nd number'))
#         res=num1-num2
#         print('the result is ',res)
#     case '*':
#         num1=float(input('enter first number'))
#         num2=float(input('enter 2nd number'))
#         res=num1*num2
#         print('the result is ',res)
#     case '/':
#         num1=float(input('enter first number'))
#         num2=float(input('enter 2nd number'))
#         res=num1/num2
#         print('the result is ',res)
#     case _:
#         print('you did a mistake chose only \"+,-,*,/\" ')


# def reverse_str(x):
#     x=x[::-1]
#     print('the reverse of input is',x)

# reverse_str('123')



# def shiftZeroatend(arr):
#     for ind,val in enumerate(arr):
#         if val==0:
#             for val2 in arr[ind+1:]:
#                 if val2 !=0:
#                     arr[ind],arr[val2]=arr[val2],arr[ind]
#                     break
            
#     return arr
# print(shiftZeroatend([1,0,2,3]))


# def outer(nam):
#     # inner func
#     def inner():
#         print('hello :',nam)
    
#     inner()

# outer('Ammar')
#ok ok ok

# def greet():

#     name='Muhammad SAW'
#     return lambda : 'Salam Beloved Last Prophet of Allah ' + name

# messege=greet()
# #even we can access the variable

# print(messege())
# print(messege.name)


# def outer():
#     x=1
#     def inner():
#         nonlocal x
#         x+=2
#         return x 
#     return inner


# a=outer()
# print(a())
# print(a())
# print(a())


# sizes=list(map(int,input().split()))
# print(sizes)

# customer=int(input())
# customers_request=[tuple(map(int,input().split())) for _ in range(customer)]
# print(customers_request)
    
# n = int(input())
# arr = map(int, input().split())
# my_list=list(arr)
# unique_score=list(set(my_list))
# maxx=max(unique_score)
# unique_score.remove(maxx)
# print(max(unique_score))


#decorator 

def outerfunc(func):
    def inner(number):
        print('argument for ',func.__name__,"is",number)
        return func(number)
    return inner


@outerfunc
def add_one(x):
    return x+1

print(add_one(1))