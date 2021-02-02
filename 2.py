#let's play with numbers

>>> 2+2
4
>>> # This is a comment
... 2+2
4
>>> 2+2  # and a comment on the same line as code
4
>>> (50-5*6)/4
5
>>> # Integer division returns the floor:
... 7/3
2
>>> 7/-3
-3

#The equal sign ('=') is used to assign a value to a variable.
#Afterwards, no result is displayed before the next interactive prompt:


>>> width = 20
>>> height = 5*9
>>> width * height
900

#A value can be assigned to several variables simultaneously:


>>> x = y = z = 0  # Zero x, y and z
>>> x
0
>>> y
0
>>> z
0

#Variables must be “defined” (assigned a value) before they can be used, or an error will occur:

>>> # try to access an undefined variable
... n
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'n' is not defined


#Floating point support
>>> 3 * 3.75 / 1.5
7.5
>>> 7.0 / 2
3.5

#Complex number support

>>> 1j * 1J
(-1+0j)
>>> 1j * complex(0,1)
(-1+0j)
>>> 3+1j*3
(3+3j)
>>> (3+1j)*3
(9+3j)
>>> (1+2j)/(1+1j)
(1.5+0.5j)


>>> a=1.5+0.5j
>>> a.real
1.5
>>> a.imag
0.5

# operator reference
print( 5 + 5 )    # Addition

print( 5 - 2 )    # Subtraction

print( 5 * 5 )    # Multiplication

print( 13 / 4 )   # Float Division

print( 13 // 4 )   # Floor Division

print( 2 ** 2 )   # Exponentiation

print( abs(-2.5) ) # Absolute Value

#Comparison operators

var1 = 10

#-------------------------------------------------------------------------------
# The "less than" operator (<) will return True if var1 is less than 10.
#-------------------------------------------------------------------------------

print( "var1 < 10 = ", var1 < 10 )

#-------------------------------------------------------------------------------
# The "less than or equal to" operator (<=) will return True if var1 is less
# than or equal to 10.
#-------------------------------------------------------------------------------

print( "var1 <= 10 = ", var1 <= 10 )

#-------------------------------------------------------------------------------
# The "greater than" operator (>) will return True if var1 is greater than 10.
#-------------------------------------------------------------------------------

print( "var1 > 10 = ", var1 > 10 )

#-------------------------------------------------------------------------------
# The "greater than or equal to" operator (>=) will return True if var1 is
# greater than or equal to 10.
#-------------------------------------------------------------------------------

print( "var1 >= 10 = ", var1 >= 10 )

#-------------------------------------------------------------------------------
# The "is equal to" operator (==) will return True if var1 is equal to 10.
#-------------------------------------------------------------------------------

print( "var1 == 10 = ", var1 == 10 )

#-------------------------------------------------------------------------------
# The "is not equal to" operator (!=) will return True if var1 is not equal to
# 10.
#-------------------------------------------------------------------------------

print( "var1 != 10 =", var1 != 10 )


