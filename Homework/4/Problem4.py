#!usr/bin/env python

#A
a = 5
b = a
print(id(a), id(b))

c = b
b = 3
print(a,b,c)
print(id(a),id(b),id(c))

b = a
b = 5
print(id(a),id(b))

#The IDs correspond to the numbers assigned to the variables since they are copied

#B
a = [5]
b = a
print(id(a), id(b))
 
b.append(1)
print(a,b)
print(id(a),id(b))

#The IDs are the same because there is one list that can be accessed from 2 different names instead of 2 copies

#C
a = [5]
b = list(a)
print(a,b)
print(id(a), id(b))
 
b = a[:]
print(a,b)
print(id(a), id(b))

#The IDs change as we are not referencing the original list, we are only creating new ones different ways

#D
a = (5,)
b = tuple(a)
print(id(a), id(b))
 
b = a[:]
print(id(a), id(b))

#Tuples are considered a basic data type so in this case we are simply creating copies that have the same ID