"""import patterns
import mathops"""#one way
from patterns import fibo
from mathops import evenodd as eo
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
