#With the while loop we can execute a set of statements as long as a condition is true
i=1
while i<6:
    print(i)
    i=i+1

print("while with break")
i=1
while i<10:
    if (i==5):break
    print(i)
    i+=1

print("while with contiue")
i=1
while i<10:
    i=i+1
    if (i==5):
        continue
    print(i)

# With the else statement we can run a block of code once when the condition no longer is true:

j=1
while j<5:
    j=j+1
    print(j)
else:
    print(" else is executing outside the while loop")

print("while loop for list" )

list1 = ["ab", "ba", "ca", "da"]
i = 0
while i <len(list1):
    print(list1[i])
    i=i+1

print("while loop for Dict" )

my_dict = {"l1":"ab", 
        "l2":"ba", 
        "l3":"ca", 
        "l4":"da"}
key_list = list(my_dict.keys())
i=0
while i< len(key_list):
    key = key_list[i]
    value = my_dict[key]
    print(f"Key: {key}, Value: {value}")
    i=i+1

print("while loop for Set" )

my_set = {"ab", "ba", "ca", "da"}
while my_set:
    x=my_set.pop()
    print(x)