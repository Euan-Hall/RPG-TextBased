#Main Processes of the Game

import os

def start():
    print("WIP")

def gameHelp():
    print("""
Welcome to the help menu for PyPg
----------------------------
""")


def menu():
    print("""Welcome to a Python, text-based RPG Game - PyPG
-----------------------------------------------
1. Start			Make sure your choice is 
2. Help				the number. I.e. 1 for start.	
3. Exit				Game Created by Euan Hall""")

    try:
        choice = int(input("Choice:"))
    except TypeError:
        choice = 0
        
    while startDone == False:
        if choice == 1: # Start Game
            startDone == True
            os.cls()
            start()
            
        elif choice == 2: # Chose Help menu.
            os.cls()
            gameHelp()
            
        elif choice == 3: # Exit the game.
            exit()

        else: # Continue the loop if statement not met.
            continue
        

menu()
