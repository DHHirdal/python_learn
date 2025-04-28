d1 = {'Name': 'Hero', 'age':26, 'Hobby': 'cricket'}
print(type(d1))
print(d1)
print("value of dictionary: ",d1['Name'])
print("value of dictionary: ",d1['age'])
print("value of dictionary: ",d1['Hobby'])
d1['Hobby']= 'running'
print(d1)
x= d1.get('Name')
print("get the dictionary value: ", x)
y=d1.keys()
print(y)
z=d1.items()
print(z)

#------------------------------------------------------
#    Change or Add items to the dictionary
#------------------------------------------------------
car = {"name": "tata",
       "Model": "Tata nano",
       "price": '1.5L'}
print("original dictionary: ",car)
car.update({"Model": "Tata punch", "price":"8L"})
print("dict after update", car)
car ["type"] = "Petrol"
print(car)

#------------------------------------------------------
#    loop dictionary
#------------------------------------------------------

for i in car:
    print("loop to car dictionary: ",i)

print("For loop to keys")
for i in car.keys():
    print("keys of dict: ",i)

print("For loop to values")
for i in car.values():
    print("values of dict: ", i)

print("For loop to key & values")
for x,y in car.items():
    print("values of dict: ", x,y)

#------------------------------------------------------
#    Copy a dictionary
#-----------------------------------------------------
car1 = car.copy()
print("copy the dict car1 : ", car1)
car2 = dict(car)
print("copy the dict car2 : ", car1)

#-----------------------------------------------------------
#             end of file 
#-----------------------------------------------------------