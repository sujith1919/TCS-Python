class Dog(object):
    def speak(self):
        print "bhou..bhou"
    def guard(self):
        print "I am guarding your home"

class Cat(object):
    def speak(self):
        print "meau..meau"
    def hunt(self):
        print "I am hunting mice"

class Doat(Cat,Dog):
    def hobby(self):
        print "programming in python"

    def speak(self):print "bhou..meau"
    def oldspeak(self):
        super(Doat,self).speak()
    
ginger=Doat()
ginger.speak()
ginger.guard()
ginger.hunt()
ginger.hobby()
ginger.oldspeak()

