#using doctest to write test cases
import doctest
def average(values): 
	"""Computes the arithmetic mean of a list of numbers. 
	>>> print average([20, 30, 70]) 
	40
	>>> print average([1,2,3,4,5,6,7,8,9,10])
	5
	>>> print average([20,21,22]) 
	21
	""" 
	return sum(values) / len(values) 
import doctest 
# automatically validate the embedded tests

doctest.testmod()
