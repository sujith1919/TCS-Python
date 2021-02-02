f = open("c:\\users\\tring\\desktop\\synechron2\\a.txt","r")
print(f.name)
print(f.mode)

for lineno,line in enumerate(f):
    print(lineno + 1,line.rstrip())

f.close()
