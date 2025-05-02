import numpy as np


#0-D array are scalar value
N=np.array(42)
print("Scalar array is: ", N)

print("Numpy 1-D array: ")
A= range(1,20,2)
print(type(A))
n= np.array(A)
print("Print array with step size 2: ", n)
print("Sum of elements :", n.sum())
print("Average of elements :", n.mean())
print("min of elements :", n.min())
print("Max of elements :", n.max())
print("Std of elements :", n.std())
print("variance of elements :", n.var())