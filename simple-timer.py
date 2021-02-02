#this is a simple timer implementation

import time

def measure_time(function):
	start_time=time.time()
	function()
	end_time=time.time()
	print end_time-start_time
	
def loop():
	for x in range(1000):
		print x*x
		
measure_time(loop)
