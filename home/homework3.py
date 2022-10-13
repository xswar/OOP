class Add:
    def __init__(self,val):
        self.val=val
    def __add__(self, other):
        return self.val + other.val
class Sub:
    def __init__(self,val):
        self.val=val
    def __sub__(self, other):
        return self.val - other.val
class Mul:
    def __init__(self,val):
        self.val=val
    def __mul__(self, other):
        return self.val * other.val
class Truediv:
    def __init__(self,val):
        self.val=val
    def __truediv__(self, other):
        return self.val / other.val

class Calculator(Add,Sub,Mul,Truediv):
    def __init__(self,val):
        Add.__init__(self,val)
        Sub.__init__(self,val)
        Mul.__init__(self,val)
        Truediv.__init__(self,val)

num1 = Calculator(5)
num2 = Calculator(2)

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)


