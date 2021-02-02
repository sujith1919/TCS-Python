#Performance
from timeit import Timer

def factr(n):
	"""this is a recursive way of finding factorial"""
	if n==0:
		return 1
	else:
		return n*factr(n-1)

def factn(n):
	"""this is a numerical way of finding factorial"""
	fact=1
	for i in range(2,n+1):
		fact*=i
	return fact
	
print factr(3)
print factn(3)

print Timer(lambda:factr(10)).timeit()
print Timer(lambda:factn(10)).timeit()
print Timer('x**y','x=23;y=50').timeit()
print Timer('x**y','x=2;y=5').timeit()

