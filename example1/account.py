class Account:
	def __init__(self, name, number, balance):
		self.name = name
		self.number = number
		self.balance = balance
	def deposit(self, amount):
		if (amount < 0):
			print('amount cannot be negative')
		else:
			self.balance += amount
	def withdraw(self, amount):
		if (self.balance < amount):
			print('money is not enough');
		else:
			self.balance -= amount
	def __str__(self):
		return "Account('{name}', '{number}', {balance})".format(
			name = self.name, number = self.number, balance = self.balance)
