ages=[10,11,12,13,14,11,12,10,12,10,13,14]
unique_ages=set(ages)
print(unique_ages)#unique
print(type(unique_ages))#set

fruits={"banana","apple","mango","grape","mango","apple","banana"}#unordered collection
print(fruits) #cannot access using index
for f in fruits:
	print(f)

#mathematical set
a={1,2,3}
b={2,3,4,5,6}

print(a-b)
print(a&b)
print(a^b)
print(a|b)

#empty set
e={}
print(type(e))#creates a dictionary

e1=set()
print(type(e1))
e1.add(1)
e1.add(1)
e1.add(6)
e1.add(2)
e1.add(3)
e1.add(3)
print(e1)
