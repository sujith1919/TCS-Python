class Baby(object):
	babycount=0 # class variable
	def __init__(self,nickname):
		self.nickname=nickname
	def cry(self):
		print "I am crying......."
	def laugh(self):
		print "Ha ha ha"
	
baby1=Baby('Pinky')
baby2=Baby('Munna')

baby1.cry()
baby2.laugh()

print Baby.babycount