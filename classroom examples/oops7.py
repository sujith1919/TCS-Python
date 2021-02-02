class Dog:
    def __init__(self,color,breed):
        self.color=color
        self.breed=breed
    def __str__(self):
        return "I am a {} color {}".format(self.color,self.breed)

tommy=Dog("brown","pug")

print(tommy)
