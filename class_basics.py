# class_basics.py
# Simple example of defining a class and using objects

class Student:
    def __init__(self, name, branch):
        self.name = name
        self.branch = branch

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Branch: {self.branch}")

# Create object
student1 = Student("Subesh", "CSE")
student2 = Student("Aarav", "ECE")

# Call method
student1.display_info()
print("---")
student2.display_info()
