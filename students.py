class Student:
	def __init__(self,name,rollno,age,gender,marks):
		self.name=name
		self.rollno=rollno
		self.age=age
		self.gender=gender
		self.marks=marks

	def display_details(self):
		print("Name is: "+self.name)
		print("Roll number is"+str(self.rollno))
		print("Age is: "+str(self.age))
		print("Gender is: "+self.gender)
		print("Marks is: "+str(self.marks))

	def calculate(self):
		marks=self.marks
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

	def get_name_roll(self):
		t=(self.name,self.rollno)
		return t;

