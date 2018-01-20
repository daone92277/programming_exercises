class Animal():
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1
        return self
  
    def run(self):
        self.health += 5
        return self

    def display_health(self):
        print "the", self.name + "'s" " health is",  self.health
        return self

animal_1 = Animal("zebra", 50)
animal_1.walk()
animal_1.walk()
animal_1.walk()
animal_1.run()
animal_1.run()
animal_1.display_health()
animal_2 = Animal("lion", 100) 

class Dog(Animal):
         
    def pet_the_dog(self):
        self.health += 5
        return self



D = Dog("chihuahua", 150)

D.walk()
D.walk()
D.walk()
D.run()
D.run()
D.pet_the_dog()
D.display_health()

class Dragon(Animal):
         
    def fly(self):
        self.health -= 10
        return self

    def dragon_health(self):
        self.display_health()
        print "I am a Dragon"
        return self



dragon = Dragon("dragon", 2000)
dragon.fly()
dragon.dragon_health()

class Hippo(Animal):
         
    def_confirm(self):
        


dragon = Dragon("dragon", 2000)
dragon.fly()
dragon.dragon_health()



    
      

