import numpy as np

arr = np.array(["apple","ball", "cat"])
print(arr)
print(arr.shape)
arr1 = np.array([[1,2,3,4],[22,23,24,25],[41,44,45,46]])
print(arr1.shape)

arr3 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
new_arr = arr3.reshape(3,4)
print(new_arr)
arr_2d_to_1d = arr1.reshape(-1)
print(arr_2d_to_1d)

for i in arr:
    print("array element is: ", i)

#Iterate on each scalar element of the 2-D array:
for i in arr1:
    for j in i:
        print("array element is :", j)

#Iterate on each scalar element of the 2-D array:
for x in np.nditer(arr1):
    print("array element is :", x)