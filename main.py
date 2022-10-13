class Hero:
    def __init__(self, hp, damage, nickname, name):
        self.hp = hp
        self.damage = damage
        self.nickname = nickname
        self.name = name
    def heal(self):
        print(f'{self.hp + 100} hp baff')
    def two_damage(self):
        print(f'{self.damage + 50} damage baff')
    def greetings(self):
        print('my name is ' + self.nickname)
    def brand_phrase(self):
        print('my real name' + self.name)
hero_1 = Hero(500 , 200 , 'black pantera ', 'T`chala')
hero_2 = Hero(150, 600, 'Iron-man', 'Tony Stark')
hero_3 = Hero(300, 300, 'Captain America', 'Stive Rodgers')
hero_4 = Hero(150, 253, 'Ant man', 'Scott Lang')
hero_1.heal()
hero_1.two_damage()
hero_1.greetings()
hero_2.brand_phrase()
hero_2.heal()
hero_2.two_damage()
hero_2.greetings()
hero_2.brand_phrase()
hero_3.heal()
hero_3.two_damage()
hero_3.greetings()
hero_3.brand_phrase()
hero_4.heal()
hero_4.two_damage()
hero_4.greetings()
hero_4.brand_phrase()
