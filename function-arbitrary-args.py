functions with arbitrary length args
def arbargs(command, *flags, **keywords):
    print "command: ",command
    for arg in flags:
        print arg
    print "-" * 40
    keys = sorted(keywords.keys())
    for kw in keys:
        print kw, ":", keywords[kw]
		
A dict can be used to send function keyword args like this
function(**dictname)
