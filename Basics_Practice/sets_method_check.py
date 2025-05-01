set1 ={1,2,3,4,5,2,3,8}
print(type(set1))
print("Original set",set1)
set1.add(9)
print("new set after add", set1)
set1.add("apple")
print("new set after add", set1)
set1.add("zoo")
print("new set after add", set1)
set1.discard("zoo")
print("new set after discard", set1)
set1.clear()
print("new set after Clear", set1)
#Note: empty Set creation is not possible
set2 ={1,}
set2.add("apple")
print(set2)
s3 = set2.copy()
print("new set after copy: ", s3)

my_set ={"apple", "banana", "cat", "office", "class", "run"}
print("dispaly the set:  ",my_set)
for i in (my_set):
    print("my set element is : ", i)
my_set.pop()
print("new set after pop",my_set)
my_set.remove("cat")
print("new set after Remove",my_set)
