#example-1
def display():
    print("I am in the function")
#example-2
a=10
b=15

def addition():
    return (a+b)
print(f"addition {a} and {b} is :",addition())

#example-3
def arr_addition():
    arr =[]
    sum=0
    n=int(input("enter the number of elements: "))
    for i in range(n):
        x=int(input("enter element: "))
        print(f"entered {i}th element: ", x)
        arr.append(x)
    for i in arr:
        sum+=i
    print("array sum is: ", sum)

arr_addition()
display()
# In this function definition - 
# example 1: no argments and no return value
# example 2: No arguments and with return value 
# example 3 : addition of array using user inputs.