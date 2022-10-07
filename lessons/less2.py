

# супер Класс
class Human:
    # атрибуты класса
    head = 1
    foots = 2
    body = 1
    hands = 2

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def medot(self):
        print('ходить')

    def seve(self):
        print('его нет')


# дочерний класс
class Hero(Human):
    def __init__(self, name, age, superAbitity):
        super().__init__(name, age)
        self.super = superAbitity

    def medot(self, p):
        print('есть способности и что-то ещё')

    def __medot(self):
        print(self.age*2)


class WoterHero(Hero):
    t = 'дыхание под водой'

    def __init__(self, name, age, superAbitity):
        super().__init__(name, age, superAbitity)


class FireHero(Hero):
    fire = 'fire rezist'

    def __init__(self, name, age, superAbitity, nickname):
        super().__init__(name, age, superAbitity)
        self.nick = nickname


human = Human('beka', 50)
# human.medot('вот это')

hero = Hero('beka', 23, 'Жаловаться')
# print(hero.name, hero.super)
# hero.medot()
woter = WoterHero('Нурсултан', 12, 'общаться с рыбами')
# print(f'меня зовут {woter.name} и я умею {woter.super} а еще есть способность {woter.t} ')
woter.medot('1')


# fire = FireHero('Адиль', 19, 'fire ball', 'Феникс')
# print(f'приветсвую моё прозвище {fire.nick}')


class Password:

    def __init__(self, login, password):
        self.login = login
        self.passw = password
        self.__lenPass()

    def __lenPass(self):
        if len(self.passw)<5:
            raise ValueError('слишком короткий пароль')

    def save(self):
        with open('users','a') as r:
            r.write(f'{self.passw,self.login}'+'\n')

d=Password('lenn','123456876')
d.save()