import fileinfo
f=fileinfo.FileInfo("marks.csv")
f.getfilesize()
f.getlinecount()
f.getcreationtime()
f.firstline()
f.lastline()
f.nthline(3)
f.getage()
f.search("7")
f.close()
