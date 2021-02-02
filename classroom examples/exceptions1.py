class MyError(Exception):
    def __init__(self, value):
        self.value = value
e = MyError('testing my custom exception')

raise e
	
	
