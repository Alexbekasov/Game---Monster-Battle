# game_data.py
import random  # Modul' dlya raboty s sluchaynymi chislam

# Bazovyy klass dlya personazha (igroka i monstera)
class Character:
    def __init__(self, name, hp, attack):
        self.name = name  # Imya personazha
        self.hp = hp  # Zdorov'ye personazha
        self.attack = attack  # Sila ataki personazha

    # Funktsiya dlya proverki, zhiv li personazh
    def is_alive(self):
        return self.hp > 0  # Esli zdraviy (HP bol'she 0), to personazh zhiv

    # Funktsiya dlya polucheniya urovnya urozhayushchego urozhaya
    def take_damage(self, amount):
        self.hp -= amount  # Umen'shaem HP na količestvo urovnya

    # Funktsiya dlya togo, chtoby personazh nanel urod
    def deal_damage(self):
        return random.randint(1, self.attack)  # Sluchaynyy urok ot 1 do ataki

# Klass dlya igroka, nasleduyushchij ot Character
class Player(Character):
    def __init__(self, name):
        super().__init__(name, hp=100, attack=20)  # Inicializiruyem obekt iz klassa "Character", ukazyvaya nachalnye znacheniya HP i ataki
        self.level = 1  # Uroven' igroka
        self.experience = 0  # Opyat igroka

    # Funktsiya dlya lecheniya igroka
    def heal(self):
        self.hp = min(100, self.hp + 20)  # Lekarstvo, maksimalno do 100 HP

# Klass dlya monstera, nasleduyushchij ot Character
class Monster(Character):
    def __init__(self, level):
        name = random.choice(["Goblin", "Orc", "Dragon"])  # Sluchaynyy vybor imeni monstera
        hp = 20 + level * 10  # Urovnevaya zavisimost' HP
        attack = 5 + level * 3  # Urovnevaya zavisimost' ataki
        super().__init__(name, hp, attack)  # Inicializiruyem objekt iz klassa "Character", ukazyvaya zadan'ye HP i ataku
