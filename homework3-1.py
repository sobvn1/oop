class Human:
    name = ''
    age = 0
    growth = 0

    def __new__(self, name, age, growth):
        self.name = name
        self.age = age
        self.growth = growth
        return self

human1 = Human('Isken', 14, 171)
print(human1.name)
print(human1.age)
print(human1.growth)