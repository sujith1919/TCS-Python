"""
Create a dict with all the squares of odd numbers
between 1 and 100
key = number value = square of that number
"""
#declare the dict
squares = {}
#get all the odd numbers
for x in range(1,100,2):
	#add numbers and squares to the dictionary
	squares[x]=x*x

#print the dict
print(squares)
