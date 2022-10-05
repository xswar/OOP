class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def a(self):
        print('my name is ' + self.name)

    def age1(self,a):
        print(self.age+a)

p1 = Human(name='Abai',age=34)
print(p1.name,p1.age)
p1.a()
p1.age1(11)