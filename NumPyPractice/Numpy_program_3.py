import numpy as np

A1 = range (2, 5,1)
A2 = range (6, 9,1)
np_A1 = np.array(A1)
np_A2 = np.array(A2)
print("1st Array : ", np_A1)
print("2nd Array : ", np_A2)
print("Addition: ", np_A1+np_A2)
print("Subtraction: ", np_A1-np_A2)
print("Multiplication: ", np_A1*np_A2)
print("integer division: ", np_A1/np_A2)
print("floor division: ", np_A1//np_A2)
print("Modulus", np_A1%np_A2)