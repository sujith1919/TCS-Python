#unit testing with unittest module
def average(values): 
	"""Computes the arithmetic mean of a list of numbers. """ 
	return sum(values) / len(values) 

import unittest 
class TestAverage(unittest.TestCase): 
	def test_average1(self): 
		self.assertEqual(average([20, 30, 70]), 40.0)
		self.assertEqual(round(average([1, 5, 7]), 1), 4.0)
		self.assertRaises(ZeroDivisionError, average, [])
		self.assertRaises(TypeError, average, 20, 30, 70) 
	
	def test_average2(self): 
		self.assertEqual(average([20, 30, 70]), 40)
		self.assertEqual(round(average([1, 5, 7]), 1), 4)
		self.assertRaises(ZeroDivisionError, average, [])
		self.assertRaises(TypeError, average, 20, 30, 70) 

# This invokes all tests
unittest.main()
