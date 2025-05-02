import numpy as np

M1 = np.array([[1,2,3], [4,5,6], [3,4,6]])
M2 = np.array([[1,2,3], [4,5,6], [3,4,6]])

print("1st Matrix",M1)
print("2nd Matrix",M2)

print("addition of matrix : ",M1+M2)
# this is not a Matrix multiplication, it multiply element-to-element
print("multiplication of matrix : ",M1*M2) 
# this is a actual Matrix multiplication, it will check size of matrix and do the calculation
print("dot product of matrix : ",np.dot(M1,M2)) 
print("transpose of matrix : ",np.transpose(M1)) 
print("inverse of matrix : ",np.invert(M1)) 