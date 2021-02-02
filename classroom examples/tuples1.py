#tuples are read only lists

a = (4,6,7,3,4)
b = 4,3,1,2,8,4,0,7

print(type(a))
print(type(b))

print(len(b))
print(min(b))
print(max(b))
print(sum(b))

print(a[0])
print(a[-1])

print(a[2:5])
print(a[:5])
print(a[2:])

print(a[:])
print(a[::])
print(a[::1])
print(a[::-1])

print(b.index(4))
print(b.count(4))