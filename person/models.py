class Person:
    def __init__(self, name, last, age):
        self.name = name
        self.last = last
        self.age = age

    def full(self):
        return f'{self.name} {self.last} {self.age}'

