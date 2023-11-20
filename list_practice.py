# li=[1,2,3,4,5,6,7]

# for i in li:
#     print(i)

# print(li[2])


# def shift_zeros(arr):
#     for ind,val in enumerate(arr):
#         if val == 0:
#             for val2 in arr[ind+1:]:

#                 if val2 !=0:
#                     arr[ind],arr[val2]=arr[val2],arr[ind]
#                     break
    
#     return arr

# print(shift_zeros([1,0,2,3]))


# #other approach 

# def shift(arr):
#     for i in arr:
#         if i==0:
#             arr.remove(i)
#             arr.append(i)
#     return arr

# print(shift([0,3,0,6,2,1,0,5,3,0]))


my_list = [1, 2, 3, 4, 5]

# Get an iterator from the list using iter()
my_iterator = iter(my_list)

# Use the iterator to retrieve elements
print(next(my_iterator))  # Output: 1
print(next(my_iterator))  # Output: 2
print(next(my_iterator))  # Output: 1
print(next(my_iterator))  # Output: 1
print(next(my_iterator))  # Output: 1

# Continue calling next() to iterate over the remaining elements

num=[1,2,3,4,5,6,7]

squared=list(map(lambda x:x**2,num))

print(squared)

even=list(filter(lambda x:x%2==0,num))

print(even)


circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]
result=list(map(
    round,circle_areas,range(1,7)
))

# print(result)

my_strings=['a','b','c']
my_numbers=[1,2,3]

res=list(map(lambda x,y:(x,y),my_strings,my_numbers))
print(dict(res))


scores=[69,58,41,75,82,90,60,34,67,87,58,90]

# def is_Score(score):
#     return score>60

res_filter=list(filter(lambda x: x>60,scores))
print(res_filter)

#checkng the palindrome using the filter

dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")

# palidrome=list(filter(lambda word:word==word[::-1],dromes))
# print(palidrome)

from functools import reduce


sum_num=[2,3,5,6,3,1,43,7,8,645,54]

def custom_sum(first,second):
    return first+second
sum_of_numbers=(reduce(custom_sum,sum_num))

# print(sum_of_numbers)


# Use map to print the square of each numbers rounded
# to three decimal places
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]

def find_square(num):
    return round(num**2,3)

res3_digit=list(map(find_square,my_floats))
print(res3_digit)

# Use filter to print only the names that are less than 
# or equal to seven letters
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]

res_names=list(filter(lambda word:len(word)<=7,my_names))
print(res_names)


# Use reduce to print the product of these numbers
my_numbers = [4, 6, 9, 23, 5]


reduce_result = reduce(lambda num1, num2: num1 + num2, my_numbers, 0)
print(reduce_result)
