#-------------------------------------------------------------------------------
# Define a new function that simply print's out "Game Over!"...
#-------------------------------------------------------------------------------

def printIt():
    print( "I am already good at Python!" )

# Now, lets call our new function...

printIt();



#simple function with single argument

def double1(num):
    print (num+num)
	
double1(5)

#function with single argument and a default value

def double1(num=2):
    print (num+num)
	
double1(5)
double1()

# function with multiple arguments

def sum(a=1,b=3):
    print (a+b)
	
sum()
sum(3,5)

# function with multiple arguments of different types
# can you make this function work.

def wish(name,age):
    print ("Hello, " + name + " you are " + age + " old")
	
#wish(India,65)

# function returning a value


# function returning multiple values

def average( numberList ):
    numCount = 0
    runningTotal = 0
    
    for n in numberList:
        numCount = numCount + 1
        runningTotal = runningTotal + n

    # Return the average and the number count
    return runningTotal / numCount, numCount


# Test the average() function...

myNumbers = [5.0, 7.0, 8.0, 2.0]

theAverage, numberCount = average( myNumbers )

print( "The average of the list is " + str( theAverage ) + "." )
print( "The list contained " + str( numberCount ) + " numbers." )


# what if you don't know the order of the arguments

wish(age=65,name="India")
#this is called calling a function by keyword arguments


