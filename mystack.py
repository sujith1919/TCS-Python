#program for stack
	
version="1.0"
class Stack(object):
	"""this is an oops implementation of stack data structure"""
		
	def __init__(self):
		self.stack=[] # the array where all the items are stored
		print "New Stack created"
	
	def push(self,item):
		self.stack.append(item)
		print "pushed :",item
	def pop(self):
		item=self.stack.pop()
		print "popped :",item
		
# end class definition