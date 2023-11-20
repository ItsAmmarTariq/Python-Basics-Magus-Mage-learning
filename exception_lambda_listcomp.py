
#  #question 1

# a=input('Enter any number ')

# try:
    
#     print('the converted number in integer is ',int(float(a)))
#     print('the converted number in float is ',float(a))

# except Exception as e:
#     print('Error', e)

# #question 2

# num1=float(input("Enter the first number"))
# num2 =float(input("Enter the first number"))

# optr=input("Enter the operater")

# if optr=='+':
#     print("sum is : ",num1+num2) 

# elif optr=='-':
#     print("sum is : ",num1-num2) 
# elif optr=='*':
#     print("sum is : ",num1*num2) 
# elif optr=='/':
#     print("sum is : ",num1/num2) 

# else:
#     print("you entered wrong input")


# # question 3

# for num in range(1, 101):
#     if num % 3 == 0 and num % 5 == 0:
#         print("FizzBuzz")
#     elif num % 3 == 0:
#         print("Fizz")
#     elif num % 5 == 0:
#         print("Buzz")
#     else:
#         print(num)

# #question 4

# st=input('Enter a string  ')
# print("reverse of  ",st +"is",st[::-1])


# #question 5

# def outer ():
#     count=0
#     def inner():
#         nonlocal count
#         count+=1
#         return count
#     return inner 

    
         
# a=outer()

# print(a())
# print(a())
# print(a())
# print(a())
# print(a())
# print(a())
# print(a())
# print(a())

# #question 6

# data =[
#     {'name': 'Ali', 'age':23},
#     {'name': 'Bob', 'age':13},
#     {'name': 'Zain', 'age':31},
#     {'name': 'Zunni', 'age':45},
#     {'name': 'Barbie', 'age':16},
# ]

# sorted_data= sorted(data,key=lambda x:x['age'])


# for data in sorted_data:
#     print(data)

# #question 7


# squares = [x**2 for x in range(1, 11)]


# print(squares)
# #question 8

# phone_book={
#     'Ammar Tariq': '343434343434',
#     'Ali Zain' : '6456453423432',
#     'Habib Tahir' : '1123345345345',
#     'Zain Abbasi' :'222887871',
#     }

# nam=input('Enter a name to search in phone book  : ')
# phone_number=phone_book.get(nam,None)

# if phone_number is None:
#     for full_name in phone_book.keys():
#        if nam.lower() in full_name.lower():
#           phone_number=phone_book[full_name]
#           break

# if phone_number is None:
#    print(" no name found in book")

# else :
#    print('phone number is ',phone_number)



# #question 9

# a=input('enter a string  ')

# try:
#     print("converting a string to integer ", int(a))
# except Exception as e:
#     print(e)

# # #question 10
# sum=0
# for i in range(1,21):
#     if i%2==0:
        
#         sum+=i

# print(sum)



# n=6

# if n%2==0 and range(2,5):
#     print("True")
    

# s=input('enter a string :')

# l=list(s)
# l.reverse()
# p=''.join(l)
# print(p)


#

# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         print('ok')
        
#     except ValueError:
#         break
#         print("Oops!  That was no valid number.  Try again...")


# try:
#     raise NameError('HiThere')
# except NameError:
#     print('An exception flew by!')
#     raise

try:
    raise TypeError('bad type')
except Exception as e:
    e.add_note('Add some information')
    e.add_note('Add some more information')
    raise
try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')