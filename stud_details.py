#from studops import display as disp
#from studops import calculate as cal
from students import Student               
name = input("Enter student name:")
roll=int(input("Enter the roll number: "))
age=int(input("Enter the age: "))
gender=input("Enter the gender: ")
marks=float(input("Enter the marks: "))

s=Student(name,roll,age,gender,marks)#create an object of class student
s.name = name #attribute to the object using dot operator
s.roll= roll
s.age = age
s.gender = gender
s.marks =marks
print(s.name)
print(s.marks)
print(s.age)
s1=Student("raina",34,19,"f",88)
s1.display_details()
s1.calculate()
t=s1.get_name_roll()
print(t[0])
print(t[1])

print(s1.name)
print(s1.marks)

#disp(name,roll,age,gender,marks)
#cal(marks)


