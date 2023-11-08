### okkk 

a=6
print(type(a))

# class 'int'
b=7.000
print(type(b))

print(type(a+b))

# this is also a float because of bigger float clss

print(type(True))

print(type('hello'))

# age=int(input('Enter your age'))
# if age>=18:
#     print(f"you can vote")
# else:
#     print(f"you cannot vote")

length= 4.5

print(f"area of sqaure of {length*length}")


_st='hello world'

for i in _st:
    print(i)


#####  complex data types  #########


# real=5
# imgnry=7

# z=complex(real,imgnry)

# print(f"the real part is {z.real}  and the imagnery part is {z.imag}")



z=6+3j

print(f"the real part is {z.real}  and the imagnery part is {z.imag}")

fl=5.8

s=''
lis=[1,2,3,4]

for i in lis:
    s+=str(i)

inte=int(''.join(s)) 

print(type(inte))


