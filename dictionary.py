
student_details={}
print(type(student_details))
student_details[96]=("raina",96,"f")
student_details[66]=("r",66,"f")
student_details[25]=("abc",256,"m")
#access value from dictionary
print(student_details[66])

#check whether key exists in dictionary
if 65 in student_details: #membership operator
	print(student_details[62])
else:
	print("Not Found")

for s in student_details:
	print(s) #prints all the keys

"""print(student_details.items())"""
items=student_details.items()
for s in items:
	print(str(s[0])+"-"+s[1][0])#print name and roll no
#print length 

print(len(student_details))
