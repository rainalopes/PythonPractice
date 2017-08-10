def display(n,r,a,g,m):
	print("Name of student is "+n)
	print("Roll number of the student is "+str(r) )
	print("Age of student is: "+str(a))
	print("Gender of the student is: "+g)
	print("Marks scored: "+str(m))

def calculate(m):
	if m<=100 and m>=70:
		print("A")
	elif m<70 and m>=60:
		print("B")
	elif m<60 and m>=50:
		print("C")
	elif m<50 and m>=40:
		print("D")
	elif m<40 and m>=0:
		print("FAIL")
	else:
		print("Invalid")

