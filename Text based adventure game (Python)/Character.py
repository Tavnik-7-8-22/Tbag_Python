import random


class BaseCharacter:
    def __init__(self, name='unknown', **kwargs):
        self.name = name
        self.health = 0
        self.strength = 0
        self.speed = 0
        self.xp = 0
        self.is_alive = True
        self.MAX_HEALTH = 0
        self.heritage = ""
        self.inventory = []
        self.possessive_nickname = self.name + '\'s'
        self.other_nickname = self.name
        self.attributes = {"name": name, "health": 0, "strength": 0, "speed": 0, "xp": 0, "is_alive": True,
                           "MAX_HEALTH": 0, "heritage": '', "inventory": [], "possessive_nickname": self.name + 's',
                           "other_nickname": self.name}

    def change__init__(self, var, val):
        setattr(self, var, val)
        print(self.name)

    def set_dead(self):
        self.is_alive = False

    def show_health(self):
        print("{} current health is {}".format(self.possessive_nickname, self.health))
        return "{} current health is {}".format(self.possessive_nickname, self.health)

    def show_xp(self):
        print("{} current XP level is {}".format(self.possessive_nickname, self.xp))
        return "{} current XP level is {}".format(self.possessive_nickname, self.xp)

    def show_attributes(self):
        print("{} current health is {}, strength is {}, speed is {}.".format(self.possessive_nickname, self.health,
                                                                             self.strength, self.speed))
        return "{} current health is {}, strength is {}, speed is {}.".format(self.possessive_nickname, self.health,
                                                                              self.strength, self.speed)

    def hit_chance(self):
        return int((self.speed/12*60) + (self.strength/12*20) + (self.health/12+20))

    def dodge_chance(self):
        return int((self.speed/12*60) + (self.strength/12*20) + (self.health/12+20))

    def attack(self, victim):  # STILL NEED TO ADD PRINT STATEMENTS
        crit_hit = random.randint(6, 8)
        strong_hit = random.randint(4, 6)
        even_hit = random.randint(3, 5)
        weak_hit = random.randint(2, 4)
        if self.hit_chance() > victim.dodge_chance():
            if random.randint(0, 100) >= 51:
                victim.health -= crit_hit
            elif victim.strength < self.strength:
                victim.health -= strong_hit
            elif victim.strength == self.strength:
                victim.health -= even_hit
            elif victim.strength > self.strength:
                victim.health -= weak_hit
        else:
            victim.health -= weak_hit
        victim.show_health()
        if victim.health <= 0:
            self.xp += victim.xp
            victim.XP = 0
            victim.set_dead()

    def feed_food(self):
        self.health += random.randint(0, 3)
        if self.health > self.MAX_HEALTH:
            self.health = self.MAX_HEALTH
        print('{} ate food.'.format(self.other_nickname))
        self.show_health()
        assert self.health > 0, "Error: health less than 0 despite feeding."

    def feed_nut_food(self):
        self.health += random.randint(3, 6)
        if self.health > self.MAX_HEALTH:
            self.health = self.MAX_HEALTH
        print('{} ate nutritious food.'.format(self.other_nickname))
        self.show_health()
        assert self.health > 0, "Error: health less than 0 despite feeding."


class User(BaseCharacter):
    def __init__(self, name='unknown'):
        super().__init__()
        self.is_alive = True
        self.possessive_nickname = 'Your'
        self.other_nickname = 'You'
