class MyError(Exception):
    def __init__(self, value):
		self.value = value
    def __str__(self):
		return repr(self.value)

try:
    raise MyError('testing my custom exception')
except MyError as e:
    print 'My exception occurred, value:', e.value

	
	
