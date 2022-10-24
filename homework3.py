class Calculator:
    def __init__(self, num):
        self.num = num


class Sum(Calculator):
    def __add__(self, other):
        return self.num + other


class Sub(Calculator):
    def __sub__(self, other):
        return self.num - other


class Mul(Calculator):
    def __mul__(self, other):
        return self.num * other


class Div(Calculator):
    def __truediv__(self, other):
        return self.num / other


class inherit(Sum, Sub, Mul, Div):
    ...


result1 = inherit(3) + 8
result2 = inherit(4) - 1
result3 = inherit(5) * 5
result4 = inherit(50) / 2
print(result1)
print(result2)
print(result3)
print(result4)