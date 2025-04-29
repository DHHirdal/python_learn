def division(x,y):
    try:
        z=x/y
        print(f"division of {x},{y} value is :",z)
    except ZeroDivisionError:
        print("denominator of zero is not possible, try with non-zero")
    finally:
        print("end of the program")
    
division(1,2)
division(1,0)
division(0,5)

my_list =[2,3,4,5,6]
flag=0
def search_elemet(loc):
    try:
        for i in my_list:
            if (loc == i):
                flag =1
                break
            else:
                flag=0
        if (flag==1):
            print("found")
        else:
            print("Not found")
    except TypeError:
        print("TypeError: check the argument list")


search_elemet(2)
search_elemet(10)
search_elemet(2,3)