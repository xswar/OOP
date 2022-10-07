from less2 import Password

class P2(Password):
    def __init__(self, login, password):
        super().__init__(login, password)

    def save(self):
        with open('users','a') as r:
            for i in r:
                if f'{self.passw,self.login}'+'\n'==i:
                    raise ValueError('такой уже есть')
        Password.save(self)

    def show(self):
        return self.passw,self.login

x=P2('admin','1234567')
x.save()