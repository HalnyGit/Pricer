baseMap = {'ACT365':1}


class Depo(object):
	"""

	"""
	def __init__(self, tradeDate = 0, startDate = 0, endDate = 0, nominal = 0.0, rate = 0.0):
		self.tradeDate = tradeDate
		self.startDate = startDate
		self.endDate = endDate
		self.nominal = nominal
		self.rate = rate
	def calcInterest(self):
		days = float(self.endDate - self.startDate)
		interest = round((self.nominal * self.rate / 100 * days / 365), 2)
		proceeds = self.nominal + interest
		return proceeds, interest
	
	
dp = Depo(0, 2, 367, 100.0, 50.0)
print dp.calcInterest()	
