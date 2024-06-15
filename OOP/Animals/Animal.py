class Animal:
    def __init__(self, name, race, age, color, arms, legs):
        self.name = name
        self.race = race
        self.age = age
        self.color = color
        self.arms = arms
        self.legs = legs

    def __str__(self):
        return f"Name: {self.name}\nRace: {self.race}\nAge: {self.age}\nColor: {self.color}\nArms: {self.arms}\nLegs: {self.legs}"

    def move(self):
        print("Moving")

    def play(self):
        print("Playing")

    # Generic sound method for any animal
    def sound(self):
        print("Making a sound")


# Child class Dog
# Inherits from Animal class
class Dog(Animal):

    def __init__(self, name, race, age, color, arms, legs, bark_volume, crazy_level):
        super().__init__(name, race, age, color, arms, legs)
        self.bark_volume = bark_volume
        self.crazy_level = crazy_level

    # Overridden sound method for Dog
    def sound(self):
        # Call the sound method from Animal
        super().sound()
        # Additional functionality for Dog
        print("Woof!")

# Child class Cat
class Cat(Animal):
    def __init__(self, name, race, age, color, arms, legs, sweetness, crazy_level):
        super().__init__(name, race, age, color, arms, legs)
        self.sweetness = sweetness
        self.crazy_level = crazy_level

    # Overridden sound method for Cat
    def sound(self):
        # Call the sound method from Animal
        super().sound()
        # Additional functionality for Dog
        print("Meow!")




# Creating an instance
my_dog = Dog("Pedo", "Jack Russel", 0, "white/black", 0, 4, 7, 8)

# Inherited attribute and behavior
print(my_dog)
my_dog.move()
my_dog.sound()



# Creating instances
my_dog2 = Dog("Barney", "Labrador Retriever", 2, "grey/brown", 0, 4, 6, 5)
my_cat = Cat("Cosmo", "European short hair", 1, "white", 0, 4, 10, 12)
my_cat2 = Cat("Tyskie", "European short hair", 1, "orange", 0, 4, 10, 11)


animals = [my_dog, my_cat, my_dog2, my_cat2]

#iterate over animal list and let them do their sounds
for animal in animals:
    print(str(animal), "\n ----- \n",  animal.name)
    animal.sound()
