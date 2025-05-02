import numpy as np

#Joining NumPy Arrays - concatenate() function
#Joining Arrays Using Stack Functions - stack() method along with the axis
#Stacking Along Rows - NumPy provides a helper function: hstack() to stack along rows.
#Stacking Along Columns -NumPy provides a helper function: vstack()  to stack along columns.
#Stacking Along Height (depth) -NumPy provides a helper function: dstack() to stack along height, which is the same as depth.

arr1 = np.array([[1,2,8], [2,7,3]])
arr2 = np.array([[11,22,39], [52,77,32]])
arr3 = np.array([[1,2,3], [2,7,8]])

new_arr = np.concatenate((arr1, arr2),axis=1)
print(new_arr)
new_arr = np.concatenate((arr1, arr2),axis=0)
print(new_arr)

print()
new_arr = np.hstack((arr1, arr2))
print("hstack",new_arr)
new_arr = np.vstack((arr1, arr2))
print("vstack", new_arr)
new_arr = np.dstack((arr1, arr2))
print("Deep stack: ", new_arr)