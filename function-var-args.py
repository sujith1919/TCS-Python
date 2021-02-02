#Handling variable number of arguments
def sumall(*num):
	print type(num)
	sum=0
	for i in num:
		sum=sum+i
	print "No. of arguments= ",len(num),"Sum of args= ",sum

sumall()
sumall(1)
sumall(1,2)
sumall(1,2,3)
sumall(1,2,3,4,5,6,7,8,9,10)
