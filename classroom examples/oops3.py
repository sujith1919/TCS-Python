class Dog:
    def __init__(self,color,breed): #constructor
        self.color=color
        self.breed=breed
    def speak(self):
        print("bhou..bhou")
    def guard(self):
        print("I am guarding your home")
    def __del__(self): #destructor
        print("bye")

tommy = Dog("brown","pug")
tommy.speak()
tommy.guard()
print(tommy.color)

del tommy




