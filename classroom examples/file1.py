#writing into a file
f=open("a.txt","w")
f.write("this is line number one\n")
f.write("this is line number two\n")
f.write("this is line number 3\n")
f.write("four\n")
f.write(str(5))
f.close()

#reading from a file all at once

f=open("a.txt","r")
text = f.read()
print(text)
f.close()

#reading from a file char by char
f=open("a.txt","r")
print(f.read(1))
print(f.read(2))
f.close()
#reading from a file line by line
f=open("a.txt","r")
print(f.readline())
print(f.readline())
f.close()