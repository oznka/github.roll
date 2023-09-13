import random

game_list = ["rock", "paper", "scissors"]

user_wins = 0
cpu_wins = 0

cpu_choice = random.choice(game_list)

while True:
    user_choice = input("Type Rock, paper, scissors or Q to quit: ").lower()
    if user_choice == "q":
        break
    if user_choice not in game_list:
        print("Select a valid option!")
        continue

    print("Computer picked", cpu_choice, ".")

    if user_choice == "rock" and cpu_choice == "scissors":
        print("You won!")
        print( )
        user_wins += 1

    elif user_choice == "paper" and cpu_choice == "rock":
        print("You won!")
        print( )
        user_wins += 1

    elif user_choice == "scisssors" and cpu_choice == "paper":
        print("You won!")
        print( )
        user_wins += 1

    elif user_choice == cpu_choice:
        print("Draw!")
        print( )

    else:
        print("You lost!")
        print( )
        cpu_wins += 1


print("You won", user_wins, "times.")
print("CPU won", cpu_wins, "times.")
print("Goodbye!")
