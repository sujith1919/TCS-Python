import subprocess
# Simple command
print(subprocess.call(['ls', '-l'], shell=True))

#on windows

print(subprocess.call(['dir'], shell=True))

#checking the output

output = subprocess.check_output(['dir'],shell=True)
print 'Have %d bytes in output' % len(output)
print output


#hide output
subprocess.call(["ping", "www.google.com"],stdout=subprocess.PIPE, stderr=subprocess.PIPE)

#windows

import subprocess
subprocess.call("dir",shell=True)

#hide output
success=subprocess.call("ping www.google.com",stdout=subprocess.PIPE, stderr=subprocess.PIPE)

print(success)



#capturing the output of a command

output = subprocess.check_output(['dir', '/w'],shell=True)
print(output)




