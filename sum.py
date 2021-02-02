import sys
print "My name=",sys.argv[0]
print "First arg",sys.argv[1]
print "Second arg",sys.argv[2]

if (len(sys.argv)>3):
	sum=0
	for i in sys.argv[1:]:
		sum=sum+int(i)
	print sum
else:
	print "Please give atleast two parameters only"


