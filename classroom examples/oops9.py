#multiple inheritance

class Dog(object):
    def speak(self):print("bhou..bhou")
    def likes(self):print("bones")

class Cat:
    def speak(self):print("meau..meau")
    def likes(self):print("milk")

class Doat(Cat,Dog):
    def hobby(self):print("python programming")

tommy = Doat()

tommy.speak()
tommy.likes()
tommy.hobby()

print(Doat.__mro__) #method resolution order
