f = open("c:\\users\\tring\\desktop\\synechron2\\a.txt","r")
print(f.name)
print(f.mode)

for line in f:
    print(line.rstrip())

f.close()
