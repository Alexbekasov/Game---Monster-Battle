# main.py
from game_data import Player, Monster
import random
import os

player = None
SAVE_FILE = "savefile.txt"

def save_game(player):
    lines = []
    found = False
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            lines = f.readlines()
    with open(SAVE_FILE, "w") as f:
        for line in lines:
            if line.startswith(player.name + ","):
                f.write(f"{player.name},{player.hp},{player.attack},{player.level},{player.experience}\n")
                found = True
            else:
                f.write(line)
        if not found:
            f.write(f"{player.name},{player.hp},{player.attack},{player.level},{player.experience}\n")

def load_all_players():
    players = {}
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            for line in f:
                data = line.strip().split(",")
                if len(data) == 5:
                    name = data[0]
                    players[name] = [int(i) for i in data[1:]]
    return players

def choose_character():
    global player
    while True:
        print("\n--- Character Menu ---")
        print("1. Load existing character")
        print("2. Start new character")
        print("3. Delete a character")
        print("4. Rename a character")
        print("5. Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            players = load_all_players()
            if not players:
                print("No saved characters found.")
                continue
            print("Saved characters:")
            for name in players:
                print(f"- {name}")
            name = input("Enter character name to load: ")
            if name in players:
                hp, attack, level, xp = players[name]
                player = Player(name)
                player.hp = hp
                player.attack = attack
                player.level = level
                player.experience = xp
                return
            else:
                print("Character not found.")
        elif choice == "2":
            name = input("Enter your hero's name: ")
            players = load_all_players()
            if name in players:
                print("A character with that name already exists.")
                continue
            player = Player(name)
            return
        elif choice == "3":
            players = load_all_players()
            if not players:
                print("No characters to delete.")
                continue
            print("Saved characters:")
            for name in players:
                print(f"- {name}")
            name = input("Enter character name to delete: ")
            if name in players:
                with open(SAVE_FILE, "r") as f:
                    lines = f.readlines()
                with open(SAVE_FILE, "w") as f:
                    for line in lines:
                        if not line.startswith(name + ","):
                            f.write(line)
                print(f"{name} has been deleted.")
            else:
                print("Character not found.")
        elif choice == "4":
            players = load_all_players()
            if not players:
                print("No characters to rename.")
                continue
            print("Saved characters:")
            for name in players:
                print(f"- {name}")
            old_name = input("Enter current character name: ")
            if old_name not in players:
                print("Character not found.")
                continue
            new_name = input("Enter new character name: ")
            if new_name in players:
                print("A character with that name already exists.")
                continue
            # Rename in save file
            with open(SAVE_FILE, "r") as f:
                lines = f.readlines()
            with open(SAVE_FILE, "w") as f:
                for line in lines:
                    if line.startswith(old_name + ","):
                        updated_line = new_name + line[len(old_name):]
                        f.write(updated_line)
                    else:
                        f.write(line)
            print(f"{old_name} has been renamed to {new_name}.")
        elif choice == "5":
            print("Goodbye!")
            exit()
        else:
            print("Invalid option.")


def battle(monster):
    global player
    while player.is_alive() and monster.is_alive():
        print(f"\n{player.name} HP: {player.hp} | {monster.name} HP: {monster.hp}")
        action = input("Choose action - [A]ttack, [H]eal, [R]un: ").lower()
        if action == "a":
            dmg = player.deal_damage()
            monster.take_damage(dmg)
            print(f"You hit {monster.name} for {dmg} damage!")
        elif action == "h":
            player.heal()
            print("You healed 20 HP!")
        elif action == "r":
            print("You ran away!")
            return
        else:
            print("Invalid choice.")
            continue

        if monster.is_alive():
            dmg = monster.deal_damage()
            player.take_damage(dmg)
            print(f"{monster.name} hits you for {dmg}!")

    if player.is_alive():
        print(f"You defeated {monster.name}!")
        player.experience += 10
        if player.experience >= 30:
            player.level += 1
            player.experience = 0
            print("You leveled up!")
    else:
        print("You died! Game Over.")
        exit()

def main():
    choose_character()
    print(f"\nWelcome, {player.name} the Hero!")

    while True:
        print("\n--- New Encounter ---")
        monster = Monster(player.level)
        print(f"A wild {monster.name} appears!")

        battle(monster)
        save_game(player)

        again = input("Fight another? (y/n): ").lower()
        if again != "y":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
