# main.py
from game_data import Player, Monster  # Importiruem klassy Player i Monster
import random
import os

player = None  # Peremennaya dlya hraneniya igroka
SAVE_FILE = "savefile.txt"  # Imya fayla dlya sokhraneniya igrokov

# Osnovnaya funktsiya dlya nachala igry
def main(loaded_player=None):
    global player
    if loaded_player:
        player = loaded_player  # Esli igrok zagruzhен, ustanavlivaem ego
    else:
        choose_character()  # Esli net zagruzhennogo igroka, vybirayem igroka

    print(f"\nWelcome, {player.name} the Hero!")  # Privetstvie igroka

    while True:
        print("\n--- New Encounter ---")  # Nachalo novogo srazheniya
        monster = Monster(player.level)  # Sozdanie novogo monstera v zavisimosti ot urovnya igroka
        print(f"A wild {monster.name} appears!")  # Soobshchenie o pojavlenii monstera

        battle(monster)  # Nachalo srazheniya s monsterom
        save_game(player)  # Sokhranyaem sostoyanie igry

        again = input("Fight another? (y/n): ").lower()  # Spravka o tom, hotim li my prodolzhit' srazheniya
        if again != "y":
            print("Thanks for playing!")  # Esli net, zakanchivaem igru
            break

# Funktsiya dlya sokhraneniya sostoyaniya igry v fayl
def save_game(player):
    lines = []  # Spisok dlya chiteniya stroki iz fayla
    found = False  # Flahovaya peremennaya, chtoby ubeditsya, chto igrok nakhodytsya v fayle
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:  # Otkryvaem fayl na chtenie
            lines = f.readlines()  # Chitayem vse stroki
    with open(SAVE_FILE, "w") as f:  # Otkryvaem fayl na zapis'
        for line in lines:
            if line.startswith(player.name + ","):  # Iskhem strokoy, nachinayushchiesya s imeni igroka
                f.write(f"{player.name},{player.hp},{player.attack},{player.level},{player.experience}\n")  # Zapis' dannykh igroka
                found = True  # Naidena stroka dlya igroka
            else:
                f.write(line)  # Zapis' ostal'nykh strok
        if not found:
            f.write(f"{player.name},{player.hp},{player.attack},{player.level},{player.experience}\n")  # Esli igrok ne nakhoditsya v fayle, dobavlyaem ego

# Funktsiya dlya zagruzki vsekh igrokov iz fayla
def load_all_players():
    players = {}  # Sozdanie slovarya dlya igrokov
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:  # Otkryvaem fayl dlya chteniya
            for line in f:
                data = line.strip().split(",")  # Razbivayem dannye na chasti
                if len(data) == 5:  # Esli dannye polnye
                    name = data[0]
                    players[name] = [int(i) for i in data[1:]]  # Zapis' dannykh igroka v slovar'
    return players

# Funktsiya dlya vybora igroka
def choose_character():
    global player
    while True:
        print("\n--- Character Menu ---")
        print("1. Load existing character")  # Zagruzit' sushchestvuyushchego igroka
        print("2. Start new character")  # Nachat' novogo igroka
        print("3. Delete a character")  # Udalit' igroka
        print("4. Rename a character")  # Pereklyuchit' imya igroka
        print("5. Quit")  # Vykhod iz igry
        choice = input("Choose an option: ")  # Vvod pol'zovatelya

        if choice == "1":
            players = load_all_players()  # Zagruzhayem vsekh igrokov
            if not players:
                print("No saved characters found.")  # Esli igroki ne nakhoditsya
                continue
            print("Saved characters:")
            for name in players:
                print(f"- {name}")
            name = input("Enter character name to load: ")  # Vvod imeni igroka
            if name in players:
                hp, attack, level, xp = players[name]
                player = Player(name)
                player.hp = hp
                player.attack = attack
                player.level = level
                player.experience = xp
                return  # Uspeshno zagruzhen igrok
            else:
                print("Character not found.")
        elif choice == "2":
            name = input("Enter your hero's name: ")  # Vvod imeni dlya novogo igroka
            players = load_all_players()
            if name in players:
                print("A character with that name already exists.")  # Esli imya uje est'
                continue
            player = Player(name)
            return  # Sozdali novogo igroka
        elif choice == "3":
            players = load_all_players()  # Zagruzhayem igrokov dlya udaleniya
            if not players:
                print("No characters to delete.")  # Esli net igrokov dlya udaleniya
                continue
            print("Saved characters:")
            for name in players:
                print(f"- {name}")
            name = input("Enter character name to delete: ")  # Vvod imeni igroka dlya udaleniya
            if name in players:
                with open(SAVE_FILE, "r") as f:
                    lines = f.readlines()  # Chitayem vse stroki iz fayla
                with open(SAVE_FILE, "w") as f:
                    for line in lines:
                        if not line.startswith(name + ","):  # Iskhem igroka dlya udaleniya
                            f.write(line)  # Ne zapisivayem ego v fayl
                print(f"{name} has been deleted.")
            else:
                print("Character not found.")
        elif choice == "4":
            players = load_all_players()  # Zagruzhayem igrokov dlya pereklyucheniya imeni
            if not players:
                print("No characters to rename.")  # Esli net igrokov dlya pereklyucheniya imeni
                continue
            print("Saved characters:")
            for name in players:
                print(f"- {name}")
            old_name = input("Enter current character name: ")  # Vvod togo, kogo khotim pereklyuchit'
            if old_name not in players:
                print("Character not found.")
                continue
            new_name = input("Enter new character name: ")  # Vvod novogo imeni
            if new_name in players:
                print("A character with that name already exists.")
                continue
            # Pereklyucheniye imeni v fayle
            with open(SAVE_FILE, "r") as f:
                lines = f.readlines()
            with open(SAVE_FILE, "w") as f:
                for line in lines:
                    if line.startswith(old_name + ","):
                        updated_line = new_name + line[len(old_name):]
                        f.write(updated_line)  # Zapis' novogo imeni
                    else:
                        f.write(line)
            print(f"{old_name} has been renamed to {new_name}.")
        elif choice == "5":
            print("Goodbye!")  # Vyhod iz igry
            exit()
        else:
            print("Invalid option.")  # Nekompetentny vybor

# Funktsiya dlya srazheniya s monsterom
def battle(monster):
    global player
    while player.is_alive() and monster.is_alive():
        print(f"\n{player.name} HP: {player.hp} | {monster.name} HP: {monster.hp}")
        action = input("Choose action - [A]ttack, [H]eal, [R]un: ").lower()  # Vybor deystviya
        if action == "a":
            dmg = player.deal_damage()  # Ataka igroka
            monster.take_damage(dmg)  # Uron monsteru
            print(f"You hit {monster.name} for {dmg} damage!")  # Soobshchenie ob atake
        elif action == "h":
            player.heal()  # Lekarstvo
            print("You healed 20 HP!")  # Soobshchenie ob lechenii
        elif action == "r":
            print("You ran away!")  # Soobshchenie o tome, chto igrok ubezhalsya
            return
        else:
            print("Invalid choice.")  # Oshibka v vibrannom deystvii
            continue

        if monster.is_alive():
            dmg = monster.deal_damage()  # Ataka monstera
            player.take_damage(dmg)  # Uron igroku
            print(f"{monster.name} hits you for {dmg}!")

    if player.is_alive():
        print(f"You defeated {monster.name}!")  # Pobeda nad monsterom
        player.experience += 10  # Opolnenie opyta
        if player.experience >= 30:
            player.level += 1  # Uroven' povyshaetsya
            player.experience = 0
            print("You leveled up!")  # Pozdravlenie s povysheniem urovnya
    else:
        print("You died! Game Over.")  # Smert' igroka
        exit()

if __name__ == "__main__":
    # Nachalo GUI pered igroy
    from gui_menu import gui_menu
    gui_menu()  # Zapuskaem okno GUI
