from random import randint

from game1 import *

count = 0
number0 = 1
number1 = 10
no_of_guesses = 5

def number_game_menu():
    print("\n===========================================")
    print("|                  Welcome                |")
    print("|            To the number game           |")
    print("|         s. Start                        |")
    print("|         q. Exit                         |")
    print("===========================================")

def number_game(rand_number):
    number_game_menu()
    user_choice = str(input(""))
    if user_choice == 's':
        counter = 0
        print(f"The number you are looking for is a number between {number0} and {number1}\nYou have {no_of_guesses} times to make a guess\n")
        while True:
            counter += 1
            if counter == no_of_guesses:
                choice = input("Sorry, you're out of guesses...\nDo you want to try again? y/n ")
                if choice == "y":
                    rand_number = randint(0, 10)
                    print("Let's go!")
                    counter = 0
                else:
                    break
            try:
                user_guess = int(input(f"What is your {counter} guess?\n "))
                if user_guess < rand_number:
                    print("You are gessing to low, make another guess!\n ")
                elif user_guess > rand_number:
                    print("Your guess is to high, go again!\n ")
                else:
                    print("\nYou guessed the correct number, congratulations!!! Please try again if you like! \n Do you want to go again? (y/n) ")
                    if input("Make your choice ") == "y":
                        rand_number = randint(0, 10)
                        print("Go again")  
                        counter = 0
                    else:
                        break
            except ValueError:
                print("Try an integer instead!\n")
    else:
        print("Leaving the game")
    print("Thanks for playing, you'll be redirected to the start menu.")