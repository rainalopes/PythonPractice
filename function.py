
#Argument packing
def add(*nos):
	sum=0
	for n in nos:
		sum+=n
	return sum
print(add())
print(add(3,4))
print(add(1,5,7,8,4))

#Argument unpacking

def two_adder(a,b):
	return a+b

l=[3,4]
print(two_adder(l[0],l[1]))
print(two_adder(*l))


def perimeter(**stats):
	print(type(stats))
	for s in stats:
		print(s)
	return 2*(stats["length"]+stats["breadth"])
#keyword argument packing
"""print(perimeter(4,5))"""#does not work

"""print(perimeter(l=3,b=4))"""#does not work
print(perimeter(length=6,breadth=3))

#Keyword argument unpacking
def area(length,breadth):
	return length*breadth

s={"length":8,"breadth":5}
print(area(s["length"],s["breadth"]))
print(area(**s)) #argument unpacking
