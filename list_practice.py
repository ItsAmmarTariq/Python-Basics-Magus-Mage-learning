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



import numpy as np
