t1= (1,2,3,4, 2, 2)
print("tuple values are: ", t1)

#
cnt = t1.count(2)
print("count method :  ", cnt)
t2= (10,20,30,45, 32, 62,2,3,4,5,6)
Index_ch = t2.index(20)
print("first Index method :  ", Index_ch)
Index_ch = t2.index(62)
print("2nd Index method :  ", Index_ch)
t2 =t1
print(t2)
print(f"address of tuple1 {id(t1)} and address of tuple_2 {id(t2)}")