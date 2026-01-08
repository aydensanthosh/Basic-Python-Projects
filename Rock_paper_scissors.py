import random
options=["rock","paper","scissor"]
user_wins=0
bot_wins=0

print("Welcome to Rock Paper and Scissors!\nwhere one must lose and the winner take it all.\n\n")
while True:
    user_choice=input("Choose your weapon(Rock/Paper/Scissor) or Q if you forfeit: ").lower()
    if user_choice!="q":
        if user_choice in options:
            rand_number=random.randint(0,2)
            computer_choice=options[rand_number]
            if user_choice=="rock" and computer_choice=="scissor":
                user_wins+=1
                print(f"Computer choose {computer_choice.title()}")
                print("Victory is yours!")
            elif user_choice=="paper" and computer_choice=="rock":
                user_wins+=1
                print(f"Computer choose {computer_choice.title()}")
                print("Victory is yours!")
            elif user_choice=="scissor" and computer_choice=="paper":
                user_wins+=1
                print(f"Computer choose {computer_choice.title()}")
                print("Victory is yours!")
            elif user_choice==computer_choice:
                print("You are at par with the bot!\nIt is a draw.")
            else:
                bot_wins+=1
                print(f"Computer choose {computer_choice.title()}")
                print("You have been defeated!")
        else:
            print("Not a weapon you lose!")
            break
    else:
        break

print(f"Times User won:{user_wins}")
print(f"Time Bot won:{bot_wins}")
print("You have fought bravely!\nGoodBye!")