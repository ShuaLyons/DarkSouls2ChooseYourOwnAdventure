import tkinter as tk
from tkinter import messagebox

class DarkSoulsGame:
    def __init__(self, root):
        self.root = root
        root.title("Dark Souls II: Curse of the Hollow")
        self.text = tk.Text(root, height=20, width=75, bg="black", fg="white", font=("Courier", 10))
        self.text.pack(pady=10)
        self.button_frame = tk.Frame(root, bg="black")
        self.button_frame.pack()
        self.choices = []
        self.start_game()

    def display(self, content, options):
        self.text.delete(1.0, tk.END)
        self.text.insert(tk.END, content)
        for btn in self.choices:
            btn.destroy()
        self.choices = []
        for text, command in options:
            btn = tk.Button(self.button_frame, text=text, command=command, width=40)
            btn.pack(pady=2)
            self.choices.append(btn)

    def start_game(self):
        self.display(
            "\n🔥 DARK SOULS II: CURSE OF THE HOLLOW 🔥\n\n"
            "You are the Bearer of the Curse. A forgotten soul wandering toward Drangleic...\n"
            "You stand at the edge of the fog gate, heart heavy with dread.\n\n"
            + self.fog_gate_art() + "\n\n"
            "Do you:\n",
            [("Enter the fog gate", self.fog_gate),
             ("Turn back toward the cursed forest", self.forest_path)]
        )

    def fog_gate(self):
        self.display(
            "\nYou walk through the fog gate and find yourself in Majula, a cliffside village bathed in fading sunlight.\n"
            + self.bonfire_art() +
            "\nAn Emerald Herald stands silently near the bonfire.\n\nDo you:\n",
            [("Speak to her", self.herald_path),
             ("Ignore her and explore the well", self.well_path)]
        )

    def forest_path(self):
        self.display(
            "\nYou head back into the cursed forest. The air is thick with decay.\n"
            "A hollow knight blocks your path.\n\nDo you:\n",
            [("Fight the hollow", self.fight_knight),
             ("Flee deeper into the woods", self.lost_in_forest)]
        )

    def herald_path(self):
        self.display(
            "\nThe Emerald Herald speaks in a soft, otherworldly voice.\n"
            "'Bearer of the Curse... seek souls, larger and more powerful... lest this land swallow you whole.'\n\nDo you:\n",
            [("Accept her guidance", lambda: self.win("You begin your journey with purpose. The path ahead is long, but you are no longer alone.")),
             ("Mock her cryptic words", lambda: self.dead("She fades. The bonfire dies. Hope withers."))]
        )

    def well_path(self):
        self.display(
            "\nYou look down into the dry well and see something glimmering.\n\nDo you:\n",
            [("Climb down", lambda: self.dead("The rope snaps. You fall into darkness. Your soul is scattered.")),
             ("Throw a rock in to test the depth", lambda: self.win("You hear the clink of metal. A hidden passage is revealed behind the well."))]
        )

    def fight_knight(self):
        self.display(
            "\nYou draw your blade. The hollow knight attacks with wild fury.\n\nDo you:\n",
            [("Parry and counter", lambda: self.dead("Your parry is too slow. The knight's blade finds your heart.")),
             ("Dodge and strike from behind", lambda: self.win("Your dodge is swift. The knight falls. You absorb his soul."))]
        )

    def lost_in_forest(self):
        self.display(
            "\nThe woods twist and shift. Trees whisper curses.\n"
            "You find a crumbling shrine and a talking cat named Shalquoir.\n\nDo you:\n",
            [("Talk to the cat", lambda: self.win("Shalquoir offers wisdom and safe passage. You survive, for now.")),
             ("Destroy the shrine", lambda: self.dead("The forest awakens. Vines coil around you. You are lost forever."))]
        )

    def win(self, message):
        self.display(
            "\n🌟 YOU PERSIST 🌟\n\n" + message,
            [("Play Again", self.start_game),
             ("Quit", self.root.quit)]
        )

    def dead(self, message):
        self.display(
            self.you_died_art() + "\n" + message,
            [("Play Again", self.start_game),
             ("Quit", self.root.quit)]
        )

    def bonfire_art(self):
        return r"""
       )  (
      (   ) )
       ) ( (
     _______)_
  .-'---------|  
 ( C|/\/\/\/\/|  
  '-./\/\/\/\/|  
    '_________'
     '-------'
    ~ BONFIRE ~
        """

    def fog_gate_art(self):
        return r"""
    |||||||||||||||||||||
    |||  FOG GATE    ||||
    |||||||||||||||||||||
        """

    def you_died_art(self):
        return r"""
 __     ______  _    _   _      ____   _____ ______ 
 \ \   / / __ \| |  | | | |    / __ \ / ____|  ____|
  \ \_/ / |  | | |  | | | |   | |  | | (___ | |__   
   \   /| |  | | |  | | | |   | |  | |\___ \|  __|  
    | | | |__| | |__| | | |___| |__| |____) | |____ 
    |_|  \____/ \____/  |______\____/|_____/|______|
        """

# Start the GUI
root = tk.Tk()
app = DarkSoulsGame(root)
root.mainloop()
