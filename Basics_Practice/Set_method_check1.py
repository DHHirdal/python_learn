s1 ={"Apple","banana", "Cat"}
s2={"fruit", "animal", "john", "Apple"}
s1.update(s2)
un_s4 = s1|s2 
# this is union operator 
# Note: Both union() and update() will exclude any duplicate items.
print("Set after update:", s1) # union check the dulicate Items
print("Set after union: ", un_s4) # update check the dulicate Items

my_s1 = {1, 2,3,4 ,5 ,6}
my_s2 ={10,2,3,40,50,60}
my_s3 = {'ab', 'ba', 'ca', 'da'}
my_s4 = my_s1|my_s2|my_s3
print("after multiple union sets: ", my_s4)