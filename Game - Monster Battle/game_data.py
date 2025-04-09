# game_data.py
import random

class Character:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, amount):
        self.hp -= amount

    def deal_damage(self):
        return random.randint(1, self.attack)

class Player(Character):
    def __init__(self, name):
        super().__init__(name, hp=100, attack=20)
        self.level = 1
        self.experience = 0

    def heal(self):
        self.hp = min(100, self.hp + 20)

class Monster(Character):
    def __init__(self, level):
        name = random.choice(["Goblin", "Orc", "Dragon"])
        hp = 20 + level * 10
        attack = 5 + level * 3
        super().__init__(name, hp, attack)
