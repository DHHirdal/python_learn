import numpy as np

A= range(1,4,1)
print(type(A))
np_arr= np.array(A)
print("Print array with step size 2: ", np_arr)
print("square root of :", np.sqrt(np_arr))
print("cube root of elements :",np.cbrt(np_arr))
print("Sin value of elements :", np.sin(np_arr))
print("log of elements :", np.log(np_arr))
print("log base10 of elements :", np.log10(np_arr))
print("log base2 of elements :", np.log2(np_arr))