class Animal:
    def __init__(self, name):
        self.name = name
      
    def move(self):
        print("An animal moves in some way.")

class Fish(Animal):
    def move(self):
        print(f"{self.name} swimming")

class Bird(Animal):
    def move(self):
        print(f"{self.name} flying")

animals = [
    Fish("Shark"),
    Bird("Eagle"),
    Animal("Generic Creature")
]

print("Let's see how the animals move:\n")
for creature in animals:
    creature.move()
