#working with lists
#lists are like C arrays
#but a lot more flexible

b = [3,6,8,4,5,6,7]
c = [4,5,6]

print( b + c )

b.extend(c) # same as b + c

d= b + c

print( b * 3 )

print(b[2:5])
b[2:5] = "A"  #replace a slice
print(b)

