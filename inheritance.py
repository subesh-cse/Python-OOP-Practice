# inheritance.py
# Demonstrating inheritance and method overriding

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

# Child class inheriting from Animal
class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks.")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows.")

# Using super() to extend functionality
class Parrot(Animal):
    def __init__(self, name, can_talk=False):
        super().__init__(name)
        self.can_talk = can_talk

    def speak(self):
        if self.can_talk:
            print(f"{self.name} says: 'Hello!'")
        else:
            super().speak()

# Creating objects
dog = Dog("Bruno")
cat = Cat("Kitty")
parrot1 = Parrot("Mithu", True)
parrot2 = Parrot("Birdy")

# Calling speak
dog.speak()
cat.speak()
parrot1.speak()
parrot2.speak()
