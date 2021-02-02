#lambda functions

add = lambda a,b:a+b

print(type(add))
print(add(4,5))

square = lambda n:n*n
cube = lambda x:x**3

a=["kulu","manali","leh","ooty","araku"]

print(sorted(a))
print(sorted(a,key=lambda x:x.count('a')))
print(sorted(a,key=lambda x:x.upper()))
print(sorted(a,key=lambda x:len(x)))
