arr = [10, 20,30, 40]
print(arr) # print list elements
arr.append(60)
print(arr) # print after append
arr1 = [1, 2,3,4,2,4,2,3,6,7,8,3,2,2]
# Verfiy that 2 is how many time is repeated
cnt = arr1.count(2)
print(f" {cnt} times given number is repeated")
#sort the array
arr1.sort()
print(arr1)
#
arr1.clear()
print("Array elements are cleared: ",arr1)
arr1.insert(0,10)
print("0th index filled: ", arr1)
arr1.insert(1,10)
print("1st index filled: ", arr1)
arr1.insert(5,20)
print("2nd index filled: ", arr1)
#check the Index method
index_ch =arr.index(20)
print("Index of element", index_ch)

list1 = [10, 20,3,1,5,6,20]
print("Shallow copy: list1 and list 2 are same address")
list2 = list1
print("list2 array are : \t", list2)
print(f"list1 address is : {id(list1)} and list2 address is : {id(list2)}" )
print("This is deep copy: compare address of List3 is different")
list3 = list1.copy()
print(f"list1 address is : {id(list1)} and list2 address is : {id(list2)} \n and list2 address is : {id(list3)}" )
list1.sort(reverse=True)
print("Descending order sort: ", list1)
list1.sort(reverse=False)
print("Ascending order sort: ", list1)
list1.pop()
print("Array after pop : ", list1)
list1.remove(5) # Remove first occurance of the value
print("Array after remove : ", list1)