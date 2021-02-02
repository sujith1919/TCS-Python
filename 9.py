numbers = [100, 25, 125, 50, 150, 75, 175]

for x in numbers:
    print x 
    if x == 50:
        print "Found It!" 
		break


		




		
		
		
		
		
#for and continue		
		


numbers = [100, 25, 125, 50, 150, 75, 175]

for x in numbers:
    # Skip all triple digit numbers
    if x >= 100:
        continue
    print( x )