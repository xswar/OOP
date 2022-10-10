from bekberdi_hw1 import Hero

class Air(Hero):
    strength = 1
    def __init__(self, name, nickname, hp, damage, fly=False):
        super().__init__(name, nickname, hp, damage)
        self.fly = fly

    def brand_phrase(self):
        self.fly = True
        print(f"fly in the {self.fly}_phrase")

    def __Gen_x(self):
        pass


class Terrestrial(Hero):
    strength = 2
    def __init__(self, name, nickname, hp, damage, fly=False):
        super().__init__(name, nickname, hp, damage)
        self.fly = fly

    def brand_phrase(self):
        self.fly = True
        print(f"fly in the {self.fly}_phrase")

    def __Gen_x(self):
        pass


class Space(Hero):
    strength = 3
    def __init__(self, name, nickname, hp, damage, fly=False):
        super().__init__(name, nickname, hp, damage)
        self.fly = fly

    def brand_phrase(self):
        self.fly = True
        print(f"fly in the {self.fly}_phrase")

    def __Gen_x(self):
        pass

bob1 = Air('ssg', 'kll', 30, 20)
print(bob1.name, bob1.nickname, bob1.hp, bob1.damage)
bob1.brand_phrase()

bob2 = Terrestrial('dds', 'jkk', 40, 10)
print(bob2.name, bob2.nickname, bob2.hp, bob2.damage)


bob3 = Space('rrs', 'bbs', 50, 60)
print(bob3.name, bob3.nickname, bob3.hp, bob3.damage)
