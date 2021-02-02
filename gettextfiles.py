import os
for (dirname, subdir, files) in os.walk('c:\\'):
	for myfile in files:
		if (myfile.endswith('.txt')):
			print os.path.join(dirname,myfile)