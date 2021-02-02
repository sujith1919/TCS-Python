#In interactive mode, the last printed expression is assigned to the variable _.
#This means that when you are using Python as a desk calculator,
#it is somewhat easier to continue calculations, for example:

>>> tax = 12.5 / 100
>>> price = 100.50
>>> price * tax
12.5625
>>> price + _
113.0625
>>> round(_, 2)
113.06

#boolean operators  and , or , not

var1 = 10

#-------------------------------------------------------------------------------
# The "and" Operator will only return True if both comparisons return True.
#-------------------------------------------------------------------------------

print( var1 == 10 and var1 <= 5 )

#-------------------------------------------------------------------------------
# The "or" Operator will return True if any of the comparisons returns True.
#-------------------------------------------------------------------------------

print( var1 == 20 or var1 >= 5 )

#-------------------------------------------------------------------------------
# The "not" Operator simply negates or inverts the result of the comparison.
#-------------------------------------------------------------------------------

print( not var1 == 10 )

# True or False

is_prime=False  #correct
is_prime=false  #wrong 'first letter must be in capitals

healthy=True	#correct
healthy=true	#wrong 'first letter must be in capitals

