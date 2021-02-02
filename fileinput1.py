#how to use fileinput module

import fileinput
for line in fileinput.input():
    print(fileinput.filename() + " " + line)
	
	
#provides built-in filename() and filelineno()