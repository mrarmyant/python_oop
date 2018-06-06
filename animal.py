class Animal:
    def __init__(self,name,health):
        self.name=name
        self.health=health

    def walk(self):
        self.health-=1
        return self

    def run(self):
        self.health-=5
        return self

    def displayHealth(self):
        print(self.health)
        return self

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, 150)

    def pet(self):
        self.health+=5
        return self

class Dragon(Animal):
    def __init__(self, name):
        super().__init__(name,170)

    def displayHealth(self):
        super().displayHealth()
        print ("I am a Dragon")


    def fly(self):
        self.health-=10

gracie= Dog("Gracie")
carroll=Dragon("Carroll")

muppet=Animal("Muppet",50)
muppet.walk()
muppet.walk()
muppet.walk()
muppet.run()
muppet.run()
muppet.displayHealth()

gracie.walk()
gracie.walk()
gracie.walk()
gracie.pet()
gracie.displayHealth()

carroll.displayHealth()
gracie.displayHealth()