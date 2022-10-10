class Car:
    year = 1883

    def drive(self):
        self.__motor()
        self.__motor2()
        print('поехала')

    def __motor(self):
        print('включение двигателя')

    def __motor2(self):
        print('давать заряд')

    def _stop(self):
        print('экстренное выключение')


c = Car()
c.drive()
c._stop()
c._Car__motor()


class BMW(Car):
    year = 1929

    def __init__(self, model, color, age):
        self.model = model
        self.color = color
        self.age = age

    def drive(self):
        print(self.model + ' drive')


bmw = BMW('x5', 'black', 2015)
bmw.drive()
