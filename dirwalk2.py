import os
totalsize=0
filecount=0
for (dirname, subdir, files) in os.walk('c:\\users\\'):
	for myfile in files:
		if myfile.endswith('.txt'):
			filename=os.path.join(dirname,myfile)
			print(filename)
			totalsize+=os.stat(filename).st_size
			filecount+=1
print(totalsize)
print(filecount)
print(totalsize/filecount)

			
#this program lists all your files recursively.		

#modify this program to list only txt files.


#find the size of all the txt files on your machine.
