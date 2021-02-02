name   = input("Enter your name : ")
height = int(input("Enter your height : "))
weight = int(input("Enter your weight : "))

print(name, height, weight)

#bmi = weight in kgs /height in mts squared

bmi = weight / ((height/100) ** 2)

print(round(bmi))

print("Your BMI is %f" % bmi)
print("Your BMI is %d" % bmi)
print("Your BMI is %s" % bmi)

"""
print("Your name is ",name,"Your Height is",height)

print("Your name is {}, your height is {} your weight is {} kgs".format(name,height,weight))
"""

print("Your name is {1}, your height is {2} your weight is {0} kgs".format(weight,name,height))
print("Your name is {1}, your height is {2} your weight is {0:.2f} kgs".format(weight,name,height))
