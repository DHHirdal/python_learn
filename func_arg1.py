
#function parameter is list,tuple, set and dictionary
my_list = [2,3,4,5]
my_tuple = (2,3,4,5)
my_set ={"john", "46", "cricketer"}
my_dict ={"name":"john","age": "46", "hobby":"cricketer"}
def my_func(my_arg):
    for i in my_arg:
        print(i)
print("list elements: ")
my_func(my_list)
print("tuple elements: ")
my_func(my_tuple)
print("set elements: ")
my_func(my_set)

# function parameter is dictinary
def my_func_dict(my_arg):
    loc_dict = dict(my_arg)
    for i in loc_dict.items():
        print(i)
print("Dictionary elements: ")
my_func_dict(my_dict)

def my_func_dict1(my_arg):
    for keys in my_arg:
        print(f"Dictinary key-value are: {keys} : { my_arg[keys]}")
print("Dictionary elements: ")
my_func_dict1(my_dict)