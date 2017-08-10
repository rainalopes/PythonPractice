"""file=open("/home/dbit/Desktop/f4.cpp")
for line in file:
	print(line)
file.close()"""
#copy["/home/dbit/pictures/2.2.png","/home/dbit/Desktop"]

file=open("/home/dbit/Desktop/f4.cpp","wt")

name=input("Enter name")
rollno=input("Enter roll no")

file.write(name+"|"+str(rollno))

file.close()
