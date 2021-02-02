def outfun(self):
	print 'hello, iam out of the class'
	
class TestObject(object):
	def f1(self):
		print "I am inside the class"
	f2=outfun
	
i=TestObject()
i.f1()
i.f2()