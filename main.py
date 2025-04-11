def bonfire_art():
    return """
       )  (
      (   ) )
       ) ( (
     _______)_
  .-'---------|  
 ( C|/\\/\\/\\/\\/|  
  '-./\\/\\/\\/\\/|  
    '_________'
     '-------'
    ~ BONFIRE ~
    """

def fog_gate_art():
    return """
    |||||||||||||||||||||
    |||  FOG GATE    ||||
    |||||||||||||||||||||
    """

def you_died_art():
    return """
 __     ______  _    _   _      ____   _____ ______ 
 \ \   / / __ \| |  | | | |    / __ \ / ____|  ____|
  \ \_/ / |  | | |  | | | |   | |  | | (___ | |__   
   \   /| |  | | |  | | | |   | |  | |\___ \|  __|  
    | | | |__| | |__| | | |___| |__| |____) | |____ 
    |_|  \____/ \____/  |______\____/|_____/|______|
    """

def start_game():
    print("\n🔥 DARK SOULS II: CURSE OF THE HOLLOW 🔥")
    print("You are the Bearer of the Curse. A forgotten soul wandering toward Drangleic...")
    print("You stand at the edge of the fog gate, heart heavy with dread.")
    print(fog_gate_art())
    print("\nDo you:")
    print("1. Enter the fog gate.")
    print("2. Turn back toward the cursed forest.")
    choice = input("> ")

    if choice == "1":
        fog_gate()
    elif choice == "2":
        forest_path()
    else:
        dead("You hesitate too long. Shadows descend, and your soul is lost.")

def fog_gate():
    print("\nYou walk through the fog gate and find yourself in Majula, a cliffside village bathed in fading sunlight.")
    print(bonfire_art())
    print("An Emerald Herald stands silently near the bonfire.")
    print("Do you:")
    print("1. Speak to her.")
    print("2. Ignore her and explore the well.")
    choice = input("> ")

    if choice == "1":
        herald_path()
    elif choice == "2":
        well_path()
    else:
        dead("You wander aimlessly and fall into a pit of despair.")

def forest_path():
    print("\nYou head back into the cursed forest. The air is thick with decay.")
    print("A hollow knight blocks your path.")
    print("Do you:")
    print("1. Fight the hollow.")
    print("2. Flee deeper into the woods.")
    choice = input("> ")

    if choice == "1":
        fight_knight()
    elif choice == "2":
        lost_in_forest()
    else:
        dead("You freeze in fear. The hollow strikes you down.")

def herald_path():
    print("\nThe Emerald Herald speaks in a soft, otherworldly voice.")
    print("'Bearer of the Curse... seek souls, larger and more powerful... lest this land swallow you whole.'")
    print("Do you:")
    print("1. Accept her guidance.")
    print("2. Mock her cryptic words.")
    choice = input("> ")

    if choice == "1":
        win("You begin your journey with purpose. The path ahead is long, but you are no longer alone.")
    elif choice == "2":
        dead("She fades. The bonfire dies. Hope withers.")
    else:
        dead("You say nothing. The silence devours you.")

def well_path():
    print("\nYou look down into the dry well and see something glimmering.")
    print("Do you:")
    print("1. Climb down.")
    print("2. Throw a rock in to test the depth.")
    choice = input("> ")

    if choice == "1":
        dead("The rope snaps. You fall into darkness. Your soul is scattered.")
    elif choice == "2":
        win("You hear the clink of metal. A hidden passage is revealed behind the well.")
    else:
        dead("You wait too long. Something drags you in.")

def fight_knight():
    print("\nYou draw your blade. The hollow knight attacks with wild fury.")
    print("Do you:")
    print("1. Parry and counter.")
    print("2. Dodge and strike from behind.")
    choice = input("> ")

    if choice == "1":
        dead("Your parry is too slow. The knight's blade finds your heart.")
    elif choice == "2":
        win("Your dodge is swift. The knight falls. You absorb his soul.")
    else:
        dead("You hesitate and are impaled.")

def lost_in_forest():
    print("\nThe woods twist and shift. Trees whisper curses.")
    print("You find a crumbling shrine and a talking cat named Shalquoir.")
    print("Do you:")
    print("1. Talk to the cat.")
    print("2. Destroy the shrine.")
    choice = input("> ")

    if choice == "1":
        win("Shalquoir offers wisdom and safe passage. You survive, for now.")
    elif choice == "2":
        dead("The forest awakens. Vines coil around you. You are lost forever.")
    else:
        dead("Confused, you fall into madness.")

def win(message):
    print("\n🌟 YOU PERSIST 🌟\n")
    print(message)
    play_again()

def dead(message):
    print(you_died_art())
    print(message)
    play_again()

def play_again():
    print("\nTry again, Young Hollow? (y/n)")
    if input("> ").lower() == "y":
        start_game()
    else:
        print("All will fade...")

# Start the game
start_game()
