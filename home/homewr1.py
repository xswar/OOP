class Hero:
    def __init__(self, name, nickname,hp,damage):
        self.name=name
        self.nickname=nickname
        self.hp=hp
        self.damage=damage

    def heal(self):
        self.hp += 100
    def two_damage(self):
        self.damage *= 2
    def greetings(self):
        print(f'my name is {self.name}'
    def brand_phrase(self):
        print('good will win')


hero1 = Hero('Azamat', 'Azelit', 100, 20)
hero2 = Hero('Beka', 'Belaz', 203, 50)
hero3 = Hero('Aidin','Smart', 313, 100)
hero4 = Hero('Andrey', 'Kind', 2031, 140)

hero1.heal()
hero2.two_damage()
hero3.brand_phrase()
hero4.greetings()
