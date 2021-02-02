#This program adds two numbers given on the command line.
#At the OS command prompt call this program as follows
#args.py 3 4
#It should return 7
import sys
print "You have entered ",len(sys.argv)-1," arguments"
print sys.argv[0]
sum=0
for x in sys.argv[1:]:
	sum=sum+int(x)
print sum

#run it as below on windows

#c:\python27\python args.py 3 4