import time
import os

starttime=time.time()

for x in range(1000):
	x**x

endtime=time.time()

print(endtime-starttime)

time.sleep(1) #sleeps for 1 second

ts = os.path.getctime("10.py")
print(ts)
print(time.ctime(ts))
