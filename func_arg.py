my_dict1 ={"name":"Aaru",
        "school": "2nd std"
        }
my_dict2 ={"name":"pooja",
        "school": "1st std"
        }
# ex 1: normal arguments
print("function for normal arguments: ")
def display(kid):
    print(f"Today is {kid} birthday")
display("Aamar")
kid1 = input("eneter the kid name : ")
display(kid1)

# ex 1: default arguments - default parameter is overwritten by passing parameter 
print("function for default arguments: ")
def display_def_arg(name, country ="India"):
    print(f"{name} is living in the {country}")
display_def_arg("Ram")
display_def_arg("kumar", "Germany")

#ex 2: arbitrary arguments -if you do no know how many arguments
print("function for arbitrary arguments: ")
def my_func_arb(*my_arg):
    print("entered args are: ", my_arg)

my_func_arb(10)
my_func_arb(10,20)
my_func_arb("apple")
my_func_arb("apple", "banana")

#ex 3: Keyword arguments - send arguments with the key-value syntax
print("function for keyword arguments: ")
def my_func_keyarg(length,breadth,height):
    print("area : ", length*breadth*height)

my_func_keyarg(length=10,breadth=2,height=4)
my_func_keyarg(breadth=2,height=4, length=10,)
my_func_keyarg(height=4, length=10,breadth=2)

#ex 4: Keyword arguments - If you do not know how many keyword arguments that will be passed into your function, 
# add two asterisk: ** before the parameter name in the function definition.
print("function for arbitrary keyword arguments: ")
def my_func_keywordArb(**my_arg):
    print("area : ", my_arg)

my_func_keywordArb(length=10,breadth=2,height=4)
my_func_keywordArb(breadth=2,height=4, length=10,)
my_func_keywordArb(height=4, length=10,breadth=2)
my_func_keywordArb(my_dict1 ={"name": "Aaru", "study":"2nd"})
my_func_keywordArb(my_dict1 ={"name": "Aaru", "study":"2nd"}, my_my_dict2={"name": "pooja", "study":"1st"})