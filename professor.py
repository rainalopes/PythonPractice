from college_user import CollegeUser 
class Professor(CollegeUser):
	def __init__(self,name,gender,subjects):
		super().__init__(name,gender)
		self.subjects=subjects

	def display_details(self)
		"""print("name:{0} \ngender:{1} \nsubjects:{2}".format(self.name,self.gender,self.marks))"""
		super().display_details()
		if len(self.subjects)==0:
			print("No subjects")
		else:
			for sub in self.subjects:
				print(sub) 
