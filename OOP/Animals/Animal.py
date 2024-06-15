class Animal:
    def __init__(self, name, race, color, arms, legs):
        self.name = name
        self.race = race
        self.color = color
        self.arms = arms
        self.legs = legs

    def __str__(self):
        return f"Name: {self.name}\nRace: {self.race}\nColor: {self.color}\nArms: {self.arms}\nLegs: {self.legs}"

    def move(self):
        print("Moving")

    def play(self):
        print("Playing")


# Inherits from Animal class
class Dog(Animal):
    # Specific behavior
    def bark(self):
        print("Woof!")


# Creating an instance
my_dog = Dog("Pedo", "Jack Russel", "white/black", 0, 4)

# Inherited attribute and behavior
print(my_dog)
print("------------------")
my_dog.move()

# Specific behavior
my_dog.bark()
