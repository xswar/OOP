class Human:
    def __new__(cls,name,age,growth):
        instance = super().__new__(cls)
        instance.name=name
        instance.name=age
        instance.growth=growth
        return instance

human1 = Human('Antoxa',23,180)
