import random


DOG_NAMES = [
    "Bob",
    "Bobby"
]


class Dog:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name not in DOG_NAMES:
            raise ValueError(f"{name} is not a valid dog name")
        self._name = name

    @staticmethod
    def random_dog():
        return Dog(random.choice(DOG_NAMES))


pug = Dog("Bob")
print(pug.name)
pug.name = "Bobby"
print(pug.name)
Dog.random_dog()