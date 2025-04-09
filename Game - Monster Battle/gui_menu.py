import tkinter as tk
from tkinter import simpledialog, messagebox
from PIL import Image, ImageTk
from main import load_all_players, Player, main, SAVE_FILE
import os

selected_player = None

def start_game_with(player_data):
    global selected_player
    name, (hp, attack, level, xp) = player_data
    selected_player = Player(name)
    selected_player.hp = hp
    selected_player.attack = attack
    selected_player.level = level
    selected_player.experience = xp
    root.quit()  # Close the tkinter window after the player selection
    root.destroy()  # Ensure the window is fully closed
    main(selected_player)  # Continue the game in the console

def save_players(players):
    with open(SAVE_FILE, "w") as f:
        for name, stats in players.items():
            f.write(f"{name},{stats[0]},{stats[1]},{stats[2]},{stats[3]}\n")

def gui_menu():
    global root
    root = tk.Tk()
    root.title("Character Manager")
    root.geometry("400x400")

    # Load an image (change to your actual image file)
    image_path = "your_image.jpg"  # Replace with your image path
    img = Image.open(image_path)
    img = img.resize((100, 100))  # Resize image if necessary
    img_tk = ImageTk.PhotoImage(img)

    # Add image to Tkinter window
    img_label = tk.Label(root, image=img_tk)
    img_label.image = img_tk  # Keep a reference to avoid garbage collection
    img_label.pack(pady=10)

    players = load_all_players()
    selected_name = tk.StringVar(value=None)

    def refresh_list():
        listbox.delete(0, tk.END)
        for name in players:
            listbox.insert(tk.END, f"{name} (Lv {players[name][2]}, XP {players[name][3]}, HP {players[name][0]})")

    def on_select(event):
        if listbox.curselection():
            index = listbox.curselection()[0]
            name = list(players.keys())[index]
            selected_name.set(name)

    def load_character():
        name = selected_name.get()
        if name:
            start_game_with((name, players[name]))
        else:
            messagebox.showwarning("Select Character", "Please select a character to load.")

    def create_character():
        name = simpledialog.askstring("New Character", "Enter your hero's name:")
        if name:
            if name in players:
                messagebox.showerror("Name Exists", "A character with this name already exists.")
            else:
                players[name] = [100, 20, 1, 0]
                save_players(players)
                refresh_list()

    def delete_character():
        name = selected_name.get()
        if name:
            if messagebox.askyesno("Delete", f"Delete {name}?"):
                del players[name]
                save_players(players)
                selected_name.set(None)
                refresh_list()

    def rename_character():
        old_name = selected_name.get()
        if old_name:
            new_name = simpledialog.askstring("Rename Character", "Enter new name:")
            if new_name and new_name not in players:
                players[new_name] = players.pop(old_name)
                save_players(players)
                selected_name.set(None)
                refresh_list()
            else:
                messagebox.showerror("Invalid", "Name is taken or empty.")

    tk.Label(root, text="Your Characters", font=("Helvetica", 14)).pack(pady=10)

    listbox = tk.Listbox(root, height=10, width=40)
    listbox.pack()
    listbox.bind("<<ListboxSelect>>", on_select)

    refresh_list()

    tk.Button(root, text="Load Game", command=load_character).pack(pady=5)
    tk.Button(root, text="New Character", command=create_character).pack(pady=5)
    tk.Button(root, text="Delete Character", command=delete_character).pack(pady=5)
    tk.Button(root, text="Rename Character", command=rename_character).pack(pady=5)
    tk.Button(root, text="Quit", command=root.quit).pack(pady=10)

    root.mainloop()
