import numpy as np

A0 = np.array(10)
print(type(A0))
print("0-D array element: ", A0)
A1= np.array([1,2,3])
print("1-D array element: ", A1)
A2= np.array([[1,2,3], [4,3,5],[1,2,3]])
print("2-D array element: \n", A2)
A3= np.array([[[1,2,3],[4,4,4],[5,5,5]],[[1,2,3],[4,5,6],[6,6,6]], [[2,2,2],[3,3,3],[4,4,4]]])
print("3-D array element: \n", A3)

print("Check the dimension of Array:")
print(f"Array A0 is {A0.ndim} dimesion and size is {A0.nbytes}")
print(f"Array A1 is {A1.ndim} dimesion and size is {A1.nbytes}")
print(f"Array A2 is {A2.ndim} dimesion and size is {A2.nbytes}")
print(f"Array A3 is {A3.ndim} dimesion and size is {A3.nbytes}")

arr = np.array([1,2,3,4], ndmin=5)
print("user provided dimesion: ", arr)
