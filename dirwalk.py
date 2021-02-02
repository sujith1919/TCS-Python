import os
for (dirname, subdir, files) in os.walk('c:\\'):
	for myfile in files:
		filename=os.path.join(dirname,myfile)
		if filename.endswith(".txt"):
			print(filename)
			
