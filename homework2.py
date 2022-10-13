from homework1 import Hero
class Ground_hero(Hero):
    def __init__(self, name, nickname, fly):
         self.name = name
         self.nickname = nickname
         self.fly = fly
    def brand_phrase(self):
        fly = True
        print(f'Hooray, I can fly! {fly}')
    def __Gen_X(self):
        pass
class Air_hero(Hero):
    def __init__(self, name, nickname, fly):
             self.name = name
             self.nickname = nickname
             self.fly = fly
    def brand_phrase(self):
        fly = True
        print(f'Fly in the {fly}')
    def __Gen_X(self):
        pass
class space_hero(Hero):
    def __init__(self, name, nickname, fly):
              self.name = name
              self.nickname = nickname
              self.fly = fly
    def brand_phrase(self):
        fly = True
        print(f'Fly in the {fly}')
    def __Gen_X(self):
        pass
g_hero = Ground_hero('TAB', 'TABS', False)
g_hero.brand_phrase()
a_hero = Air_hero('SAPD', 'SAPD', False)
a_hero.brand_phrase()
s_hero = space_hero('PUP', 'PUP', False)
s_hero.brand_phrase()