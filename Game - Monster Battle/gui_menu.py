import tkinter as tk
from tkinter import simpledialog, messagebox
from PIL import Image, ImageTk
from main import load_all_players, Player, main, SAVE_FILE
import os

# Peremennaya dlya khraneniya nakhodyashchegosya igroka
selected_player = None

# Funktsiya dlya nachala igry s ukazannym igrokom
def start_game_with(player_data):
    global selected_player
    # Razbivaem dannye igroka na imya i ego stats
    name, (hp, attack, level, xp) = player_data
    selected_player = Player(name)
    # Ukazivayem nachalnye kharakteristiki igroka
    selected_player.hp = hp
    selected_player.attack = attack
    selected_player.level = level
    selected_player.experience = xp
    root.quit()  # Zakryvaem okno tkinter posle vybora igroka
    root.destroy()  # Ubezhdayemsya, chto okno zavershilos
    main(selected_player)  # Prodolzhaem igru v konsoli s etim igrokom

# Funktsiya dlya sokhraneniya igrokov v fayl
def save_players(players):
    with open(SAVE_FILE, "w") as f:
        for name, stats in players.items():
            # Sokhranyaem informatsiyu o kazhdom igroke
            f.write(f"{name},{stats[0]},{stats[1]},{stats[2]},{stats[3]}\n")

# Osnovnoye okno GUI
def gui_menu():
    global root
    root = tk.Tk()  # Sozdanie glavnego okna
    root.title("Character Manager")  # Ustanavlivaem nazvanie okna
    root.geometry("400x400")  # Ustanavlivaem razmery okna

    # Zagruzhayem i otobrazhaem izobrazhenie geroja
    image_path = "hero.jpg"  
    img = Image.open(image_path)
    img = img.resize((300, 300))  # Menyaem razmer izobrazheniya
    img_tk = ImageTk.PhotoImage(img)

    # Otobrazhaem kartinku v okne Tkinter
    img_label = tk.Label(root, image=img_tk)
    img_label.image = img_tk  # Soderzhim ssylku na izobrazhenie, chtoby ono ne bylo udaleno
    img_label.pack(pady=10)  # Razmeshchayem kartinku v okne

    # Загружаем информацию о персонажах
    players = load_all_players()
    selected_name = tk.StringVar(value=None)

    # Funktsiya dlya obnavleniya spiska igrokov
    def refresh_list():
        listbox.delete(0, tk.END)  # Ochechayem spisok
        for name in players:
            # Dobavlyaem dannye o kazhdom igroke v spisok
            listbox.insert(tk.END, f"{name} (Lv {players[name][2]}, XP {players[name][3]}, HP {players[name][0]})")

    # Funktsiya, kotorya vypolnyaetsya pri vybore igroka iz spiska
    def on_select(event):
        if listbox.curselection():
            # Poluchayem index vybrannogo igroka
            index = listbox.curselection()[0]
            name = list(players.keys())[index]  # Naходим imya iz indeksa
            selected_name.set(name)  # Ustanavlivaem ego v tekstovuyu peremennuyu

    # Funktsiya dlya zagruzki igroka
    def load_character():
        name = selected_name.get()
        if name:
            # Esli igrok vybrany, nachinayem igru s etim igrokom
            start_game_with((name, players[name]))
        else:
            messagebox.showwarning("Select Character", "Please select a character to load.")  # Soobshchenie ob oshibke

    # Funktsiya dlya sozdaniya novogo igroka
    def create_character():
        name = simpledialog.askstring("New Character", "Enter your hero's name:")  # Zapros imeni novogo igroka
        if name:
            if name in players:
                messagebox.showerror("Name Exists", "A character with this name already exists.")  # Esli igrok s takim imenem uje est', soobshchaem ob etom
            else:
                # Sozdanie novogo igroka s nachal'nymi kharakteristikami
                players[name] = [100, 20, 1, 0]
                save_players(players)  # Sokhranyaem novogo igroka
                refresh_list()  # Obnovlyaem spisok

    # Funktsiya dlya udaleniya igroka
    def delete_character():
        name = selected_name.get()
        if name:
            # Zapros na podtverzhdenie udaleniya
            if messagebox.askyesno("Delete", f"Delete {name}?"):
                del players[name]  # Udalyayem igroka
                save_players(players)  # Sokhranyaem izmeneniya
                selected_name.set(None)  # Ochishchayem vybrannoe imya
                refresh_list()  # Obnovlyaem spisok

    # Funktsiya dlya pereklyucheniya imeni igroka
    def rename_character():
        old_name = selected_name.get()
        if old_name:
            # Zapros na novoe imya
            new_name = simpledialog.askstring("Rename Character", "Enter new name:")
            if new_name and new_name not in players:
                # Menyayem imya, esli ono odinakovo ne zanyato
                players[new_name] = players.pop(old_name)
                save_players(players)  # Sokhranyaem izmeneniya
                selected_name.set(None)  # Ochishchayem vybrannoe imya
                refresh_list()  # Obnovlyaem spisok
            else:
                messagebox.showerror("Invalid", "Name is taken or empty.")  # Soobshchenie ob oshibke

    # Nadpis' v okne
    tk.Label(root, text="Your Characters", font=("Helvetica", 14)).pack(pady=10)

    # Spisok dlya otobrazheniya igrokov
    listbox = tk.Listbox(root, height=10, width=40)
    listbox.pack()
    listbox.bind("<<ListboxSelect>>", on_select)  # Privyazka obrabotchika k klikam

    refresh_list()  # Perednem otobrazhenie spiska igrokov

    # Knopki dlya raboty s igrokami
    tk.Button(root, text="Load Game", command=load_character).pack(pady=5)
    tk.Button(root, text="New Character", command=create_character).pack(pady=5)
    tk.Button(root, text="Delete Character", command=delete_character).pack(pady=5)
    tk.Button(root, text="Rename Character", command=rename_character).pack(pady=5)
    tk.Button(root, text="Quit", command=root.quit).pack(pady=10)

    root.mainloop()  # Nachinayem rabotu okna GUI
