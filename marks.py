marks=float(input("Enter marks:"))

if marks<=100 and marks>=70:
	print("A")
elif marks<70 and marks>=60:
	print("B")
elif marks<60 and marks>=50:
	print("C")
elif marks<50 and marks>=40:
	print("D")
elif marks<40 and marks>=0:
	print("FAIL")
else:
	print("Invalid")

