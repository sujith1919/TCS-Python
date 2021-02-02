import os
size=0
count=0
for (dirname, subdir, files) in os.walk('c:\\'):
	for myfile in files:
		filename=os.path.join(dirname,myfile)
		if filename.endswith('.jpg'):
			size=size+os.stat(filename).st_size
			count=count+1
			print count,size/(1024*1024*1024.0),size/count

			
			
#if filename.endswith('.txt'):
#if os.stat(filename).st_size > 1024*1024
#if time.time()-os.stat(filename).st_ctime < 60 * 60 * 24 * 1