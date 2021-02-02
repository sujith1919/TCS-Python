class B(object):
    def method(self,arg):
        print 'this is parent method'+arg
        
class C(B):
    def method(self,arg):
        print 'this is child method'+arg+arg
    def met(self, arg):
        super(C, self).method(arg)
        
ob=B()
ob.method('hello')

oc=C()
oc.method('hello')
oc.met('hello')