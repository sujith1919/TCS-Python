import sys
if len(sys.argv)==3:
	print abs(int(sys.argv[1]) - int(sys.argv[2]))
else:
	print "Usage:\n\n\t" + sys.argv[0].split('\\')[-1] + " num1 num2"
	print "Usage:\n\n\t" + sys.argv[0] + " num1 num2"