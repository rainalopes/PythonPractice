print("program starts")
for i in range(1,4):
	n1=input("Enter n:")
	try:
		n2=int(n1)#scope of n2 is in the entire module
	except ValueError:
		print("Please enter a proper value")
	else:
		print("Value taken is: {0}".format(n2))#no exception in corresponding try
		break

print("program ends")

