import os,time
age=2*24*60*60
for (dirname, subdir, files) in os.walk('c:\\'):
	for myfile in files:
		filename=os.path.join(dirname,myfile)
		fileage=time.time() - os.stat(filename).st_ctime 
		if fileage < age:
				print(filename)