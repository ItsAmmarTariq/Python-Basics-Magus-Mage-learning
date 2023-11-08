from functools import reduce

def func():
    print('hello there im a function')

func()




add_one=(lambda a:a+1)

print(add_one(2))

full_name =lambda first_name,last_name:f"Full name : {first_name.title()} {last_name.title()}"
print(full_name('Ammar','Tariq'))


#map functions


a=list(map(lambda x:x.capitalize(),['a','b','c','d']))
print(a)

print([x.capitalize() for x in ['a','b','c']])


def even(x):
    return x%2==0

print(list(filter(even,range(20))))


#reduce 


numbers =[1,2,3,4,5,6,7,8]

product_of_list=reduce((lambda x,y:x*y),numbers)

print(product_of_list)



def add(x,y):
    return x+y

res=add(2,5)
print('the addition is ' ,res)


# *********calculator*************

optr=input('Enter any operator')

match optr:
    case '+':
        num1=float(input('enter first number'))
        num2=float(input('enter 2nd number'))
        res=num1+num2
        print('the result is ',res)
    case '-':
        num1=float(input('enter first number'))
        num2=float(input('enter 2nd number'))
        res=num1-num2
        print('the result is ',res)
    case '*':
        num1=float(input('enter first number'))
        num2=float(input('enter 2nd number'))
        res=num1*num2
        print('the result is ',res)
    case '/':
        num1=float(input('enter first number'))
        num2=float(input('enter 2nd number'))
        res=num1/num2
        print('the result is ',res)
    case _:
        print('you did a mistake chose only \"+,-,*,/\" ')


def reverse_str(x):
    x=x[::-1]
    print('the reverse of input is',x)

reverse_str('123')



def shiftZeroatend(arr):
    for ind,val in enumerate(arr):
        if val==0:
            for val2 in arr[ind+1:]:
                if val2 !=0:
                    arr[ind],arr[val2]=arr[val2],arr[ind]
                    break
            
    return arr
print(shiftZeroatend([1,0,2,3]))

