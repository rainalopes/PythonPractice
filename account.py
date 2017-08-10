class InsufficientBalError(Exception):
	def __init__(self,msg):
		super().__init__(msg)

class Account:
	def __init__(self,acc_no,balance,min_bal):
		self.acc_no=acc_no
		self.balance=balance
		self.min_bal=min_bal

	def withdraw(self,amt):
		if self.balance-amt<self.min_bal:
			raise InsufficientBalError("Insufficient Balance its currently {0}".format(self.balance))
					
		self.balance=self.balance-amt
		return self.balance

