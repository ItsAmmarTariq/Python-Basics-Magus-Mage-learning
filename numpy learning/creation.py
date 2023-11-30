import numpy as np

arr = np.array([[10, 20, 30, 40], [50, 60, 70, 80]])
print(arr[::-3])

# obtaining first two elements from both list
print(arr[0:3,0:3])

# as we can see that our first list is on 1st index we can acees it by 0th index

# all vlues
print(arr[0,:])

print(arr[1, ::-1])

# shape
print(np.shape(arr))  # shows two rows and 4 cloums
print(np.size(arr))
print(np.ndim(arr))
print(arr.dtype)