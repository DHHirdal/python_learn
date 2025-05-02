import numpy as np

#Slicing in python means taking elements from one given index to another given index.
#We pass slice instead of index like this: [start:end].
#We can also define the step, like this: [start:end:step].
#If we don't pass start its considered 0
#If we don't pass end its considered length of array in that dimension
#If we don't pass step its considered 1

arr = np.array([1,8,5,6,3,1,4,7,9,10])
print(arr[0:4])
print(arr[2:5])
print(arr[2:20:2])
print(arr[1:20:3])
print(arr[4:])
print(arr[:4])

print(arr[-5:-1:1])