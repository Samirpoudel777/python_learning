# class Student:
#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade

#     def display_details(self):
#         print(f"Name: {self.name}, Grade: {self.grade}")
# student1 = Student("Samir", "A")
# student1.display_details()

# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages

#     def display(self):
#         print(f"Title: {self.title}")
#         print(f"Author: {self.author}")
#         print(f"Pages: {self.pages}")

# book1 = Book("trader got rich", "samir poudel", 408)
# book2 = Book("rich mindset", "samir poudel", 777)

# book1.display()
# print("you will sucess with completeing your dream")
# book2.display()
# print("never feel dissapointed after reading such type of book")
# Base class
# class Person:
#     def __init__(self, name):
#         self.name = name


# class Teacher(Person):
#     def __init__(self, name, subject):
#         super().__init__(name)  # Inherit name from Person
#         self.subject = subject

#     def introduce(self):
#         print(f"Hello, my name is {self.name} and I teach {self.subject}.")

# t1 = Teacher("Mr.samir poudel", "trading")
# t1.introduce()

# class Cat:
#     def make_sound(self):
#         print("Meow!")
# class Dog:
#     def make_sound(self):
#         print("Woof!")
# def animal_sound(animal):
#     animal.make_sound()
# c = Cat()
# d = Dog()


# animal_sound(c)  
# animal_sound(d)  

import time

print("Printing after a delay...")
time.sleep(3)  # Delay for 3 seconds
print("Hello, world!")
