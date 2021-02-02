"""
1. Write a function which will generate
 a random integer between 1 and 5000
2. Call the function 1000 times and save
 the results into a list.
3. Print how many times each number has repeated
"""

import random

def r1():
	return random.randint(1,5000)
	
l=[]

for x in range(1000):
	l.append(r1())
	
print len(l)

u=[]

for x in l:
	if x not in u:
		u.append(x)
		
print len(u)

for x in u:
	print "{} repeated {} times".format(x,l.count(x))
	
