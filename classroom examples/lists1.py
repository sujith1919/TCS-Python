#working with lists
#lists are like C arrays
#but a lot more flexible

a = [3,6,8,4,5,6,7,4.5,"hello","hi"]
b = [3,6,8,4,5,6,7]

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