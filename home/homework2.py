from homewr1 import Hero

class Airhero(Hero):
    fly = False
    def __init__(self,name,nickname,hp,damage):
        super().__init__(name,nickname,hp,damage)
    def brand_phrase(self):
        print('fly in the True_phrase')
        fly = True
    def __Gen_x(self):
        pass

class Earthhero(Hero):
    fly = False
    def __init__(self,name,nickname,hp,damage):
        super().__init__(name,nickname,hp,damage)
    def brand_phrase(self):
        print('fly in the True_phrase')
        fly = True
    def __Gen_x(self):
        pass

class Cosmohero(Hero):
    fly = False
    def __init__(self,name,nickname,hp,damage):
        super().__init__(name,nickname,hp,damage)
    def brand_phrase(self):
        print('fly in the True_phrase')
        fly = True
    def __Gen_x(self):
        pass

air_hero = Airhero('Frenk','franchesko',2031,543)
earth_hero = Earthhero('Alex','earthquake',2000,600)
cosmo_hero = Cosmohero('Antonio','cosmostar',3123,700)

air_hero.brand_phrase()
