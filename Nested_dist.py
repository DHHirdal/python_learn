car = {
    "company1" : {"Name": "Tata",
              "type": "petrol",
              "model": "SUV"},
    "company2" : {"Name": "Maruti",
              "type": "Diesel",
              "model": "Hachbak"}
}

print("original dict: ", car)
print("subdictionary -1",car["company1"])
print("subdictionary -2",car["company2"])
print("subdictionary -1 and its members : ",car["company1"]["Name"], 
      car["company1"]["type"], car["company1"]["model"])
print("subdictionary -2 and its members: ",car["company2"]["Name"], 
      car["company2"]["type"], car["company2"]["model"])

#-----------------------------------------------------------------
#                 Loop through the nested dictionary             
#----------------------------------------------------------------#

for i in car:
    print("loop members are: ", i)

print("Nested loop print: method-1")
for i in car:
    for j in car[i].values():
        print("dict member is: ", j)
print("Nested loop print: method-2")
for x,obj in car.items():
    print(x)
    for y in obj:
        print(y+ ':', obj[y])