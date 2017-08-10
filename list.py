cars=["mercedes","bmw","audi"]
print(type(cars))
#ordered collection
print(cars[0])
print(cars[2])
#modify a element
cars[0]="scorpio"
print(cars[0])
#number of elements
print(len(cars))
print(cars[len(cars)-1])
cars.append("nano")#add element at the end of the list
print(cars)

cars.extend(["i20","i50","i28"])#lists of cars at the end of the list
print(cars)
#inserting element at a specific position in the list
cars.insert(1,"swift")
print(cars)
#removing from end from the list
print(cars.pop())
print(cars)

#removing from specific index position
print(cars.pop(2))
print(cars)
#print all elements of the list
for car in cars:
	print(car)
cars.sort()#Sort elements in ascending order
print(cars)
"""cars.reverse()
print(cars)"""
cars.sort(reverse=True)
print(cars)
nos=[1,2,3,4,5,6]
#NEW LIST WITH SQUARES
squares=[]
"""for i in range(0,len(nos)):
	squares.append(nos[i]**2)
print(squares)"""
"""for no in nos:
	squares.append(no**2)
print(squares)"""

n2=[n**2 for n in nos]
print(n2)


n3=[n**2 for n in nos if n%2==0]
print(n3)

n4=[n**3 for n in nos if n%2==0 and n>4]
print(n4)

