'''rock paper sissor game
   Arthor: k0mmo
   Python3
   Date created 11/17/19
'''

import random
import sys
import os
import time


# Clears screen feature
def clear():

    # for windows
    if os.name == 'nt':
        os.system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        os.system('clear')

# Intro text to game and gets users choice
def main():
    while True:
        clear()
        def rules():
            # Displays The rules of the game
            print("\n   Welcome to Rock Paper Sissors")
            print("====================================")
            print("| The Rules are simple you select  |")
            print("|   either Rock Paper or Sissor    |")
            print("|   if your choice beats the PC    |")
            print("|           You Win!               |")
            print("====================================\n")
            print("        Please pick one\n")
            print("       Rock Paper Sissor\n")
            print("    Please enter quit to exit\n")
            checks()

        def checks(): # check system to see who won
            # Player Check
            user_input = input("           >> ")
            print("====================================\n")
            print("    You have picked: " + user_input.lower())
            # Oppoent Check
            O_choices = ["rock", "paper", "sissor"]
            Oppoent_selection = random.choice(O_choices)
            print("\n   Your oppoent has pick: " + Oppoent_selection)

            def Results_win(): # Displays who won
                # Win statement
                clear()
                print("\n      You have picked: " + user_input.lower())
                print("\n   Your oppoent has pick: " + Oppoent_selection)
                print("\n====================================")
                print("             You win!")
                print("====================================\n")
                rules()
                time.sleep(5)

            # Lose Statement
            def Results_lose():
                clear()
                print("\n    You have picked: " + user_input.lower())
                print("\n   Your oppoent has pick: " + Oppoent_selection)
                print("\n====================================")
                print("             You Lose!")
                print("====================================\n")
                rules()
                time.sleep(5)

            # Tie Statement
            def Results_tie():
                clear()
                print("\n    You have picked: " + user_input.lower())
                print("\n   Your oppoent has pick: " + Oppoent_selection)
                print("\n====================================")
                print("             It's a Tie!")
                print("====================================\n")
                rules()
                time.sleep(5)

            # check system to see who won
            if user_input not in ["rock", "paper", "sissor", "quit"]:
                clear()
                print("\n====================================")
                print(" Invalid choice please pick again.")
                print("====================================\n")
                rules()
            elif user_input == "rock":
                if Oppoent_selection == "sissor":
                    Results_win()
                elif Oppoent_selection == "paper":
                    Results_lose()
                elif user_input == "rock" and Oppoent_selection == "rock":
                    Results_tie()
            elif user_input == "paper":
                if Oppoent_selection == "rock":
                    Results_win()
                elif Oppoent_selection == "sissor":
                    Results_lose()
                elif user_input == "paper" and Oppoent_selection == "paper":
                    Results_tie()
            elif user_input == "sissor":
                if Oppoent_selection == "paper":
                    Results_win()
                elif Oppoent_selection == "rock":
                    Results_lose()
                elif user_input == "sissor" and Oppoent_selection == "sissor":
                    Results_tie()
            elif user_input == "quit": # invalid statment if user picks outside the choices
                clear()
                print("\n====================================")
                print("    Thanks for playing, Good Bye.")
                print("====================================\n")
                sys.exit()
        rules() # starts loop

main()
