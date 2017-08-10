"""import patterns
import mathops"""#one way
from com.example.custom.patterns import fibo #prefix module name with package
from com.example.custom.math import evenodd as eo #prefix module name with package
while True:
	print("Enter 1 to determine even or odd")
	print("Enter 2 to display fibonacci series")
	print("Enter 3 to exit")
	choice=int(input("Enter choice"))
	if choice==1:
		eo()		
	elif choice==2:
		fibo()
	else:break	
