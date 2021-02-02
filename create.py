import sys
f=open(sys.argv[1],'w')
while True:
	text=raw_input()
	if (text == 'STOP!'):
		break
	f.write(text + '\n')
f.close()