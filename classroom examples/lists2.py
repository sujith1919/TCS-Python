#working with lists
#lists are like C arrays
#but a lot more flexible

b = [3,6,8,4,5,6,7]

#append to a list
print(b)
b.append(9)
print(b)

#insert into a list
print(b)
b.insert(1,200)
print(b)

#remove from a list
print(b)
b.remove(200)
print(b)

#pop from a list
print(b)
c = b.pop()
print(c)
print(b)
c = b.pop(2)
print(c)

# reverse a list

print(b)
b.reverse()
print(b)

# sort 
print(b)
b.sort()
print(b)

# sort descending
print(b)
b.sort(reverse = True)
print(b)

print(b.index(3)) #find where 3 is in the list
print(b.count(3)) #find how many times 3 is in the list



