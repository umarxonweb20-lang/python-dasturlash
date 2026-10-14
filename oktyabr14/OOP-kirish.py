#OOP - object Oriented programaning (Objectga yonaltirilgan Dasturlash )

#snake case 
# def python_ programming()
# pass

# camel case 
# class PythonProgramming:
#   pass
# 

class Animal:
    def __init__(self, name: str):
        self.name = name

    def bark(self):
        print("VoooooV voooov")

animal = Animal("Dog")
animal2 = Animal("Cat")

# animal.bark()


class Car:
    def __init__(self, name: str, color: str, year: int):
        self.name = name
        self.color = color
        self.year = year
        self.age = 2027 - year

    def say_name(self):
        print("My name is", self.name)

    def say_age(self):
        print("I'm", self.age, "year old")

    def honk(self):
        print("Biiiiiiiiiibiiiiiiiib")


car1 = Car("Cabalt", "white", 2020)
car2 = Car("Malibu-2", "block", 2025)

car1.honk()
car2.say_age()

        