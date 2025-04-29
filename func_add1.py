#Example-1

def addition(x,y):
    return(x+y)

print("sum is : ",addition(2, 3))

def calculator(math_type, x, y):
    match math_type:
        case 1: print(f"addition of {x} and {y} is : ", x+y)
        case 2: print(f"Substraction of {x} and {y} is : ", x-y)
        case 3: print(f"muliplication of {x} and {y} is : ", x*y)
        case 4: 
            if y==0:
                print("wrong number: division by zero not possible, enter other than zero")
            else:
                print(f"division of {x} and {y} is : ", x/y)
        case 5: print(f"floor division of {x} and {y} is : ", x//y)
        case 6: print(f"modulus of {x} and {y} is : ", x%y)
        case _:
            print("outside the our operation")

math_type = int(input("enter the calculation type 1 to 7: "))
x = int(input("enter the 1st number: "))
y = int(input("enter the 2nd number: "))
calculator(math_type,x,y)