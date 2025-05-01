#loop the iteration
print("Program _1: for Loop iteration check")
for i in range(5):
    print(i)

print("Program _2: Factorial of a number")
# for loop for finding the factorial number
n = int(input ("Enter a number: "))
fact =1
temp =n
for i in range(n):
    fact = fact *n
    n=n-1
print(f"Factorial of {temp} is {fact}")

print("Program _3: find a key Element from array ")
n = int(input ("Enter a numbersize of array"))
arr = []
temp =n
for i in range (n):
    ele =int(input("Enter array elements: "))
    arr.append(i+1)
print(arr)
key =int(input("enter the key Element for search : " ))
flag =0
for i in arr:
    if (i == key):
        flag =1
        break
    else:
        flag=0
if (flag == 1):
    print("found")
else:
    print("not found")