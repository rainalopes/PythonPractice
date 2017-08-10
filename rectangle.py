#this is a function to calculating area and perimeter
def area(l=4,b=2):
#default parameters
	return l*b
def perimeter(l,b):
	return 2*(l+b)
"""calling a function area
and perimeter"""
print(area())
print(area(2))
print(area(l=9,b=2))#passing keyword arguments
print(area(b=2,l=5))#using keyword arguments we can pass in any order
print(perimeter(b=2,l=4))
print(perimeter(l=2,b=4))#using keyword arguments we can pass in any order
"""length=2
breadth=5
a=area(length,breadth)
p=perimeter(length,breadth)
print("Area is "+ str(a))
print("Perimeter is "+ str(p)
)"""
length=int(input("Enter length:"))
breadth= int(input("Enter breadth:"))

print("length is" + str(length))
print("breadth is" + str(breadth))
