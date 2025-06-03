# Program to implement composition 02
class Animal:
    name = ""
    category = ""

    def __init__(self, name):
        self.name = name

    def set_category(self, category):
        self.category = category


class Turtle(Animal):
    category = "Reptile"


class Snake(Animal):
    category = "Reptile"

class Fish(Animal):
    category = "Aquatic"

class Zoo:
    def __init__(self):
        self.available_animals = {}

    def add_animal(self, animal):
        self.available_animals[animal.name] = animal.category

    def total_of_category(self, category):
        result = 0
        for animal in self.available_animals.values():
            if animal == category:
                result += 1
        return result


zoo = Zoo()

print(Turtle.category)
turtle = Turtle("Turtle")   # create an instance of the Turtle class
snake = Snake("Snake")      # create an instance of the Snake class
fish = Fish("Shark")

zoo.add_animal(turtle)
zoo.add_animal(snake)
zoo.add_animal(fish)

print(zoo.total_of_category("Reptile"))     # how many zoo animal types in the reptile category

print(isinstance(snake, Animal))
print(issubclass(Snake, Animal))

print(zoo.total_of_category("Aquatic")) 