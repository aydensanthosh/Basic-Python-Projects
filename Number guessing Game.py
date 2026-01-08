import random
tries=0
max=input("Enter the maximum Value: ")
if max.isdigit():
    max=int(max)
    rand_number=random.randint(0,max)
    while True:
        guess=input(f"Guess the number between 0 and {max}: ")
        if guess.isdigit():
            guess=int(guess)
            if guess==rand_number:
                print("Congrats you win!")
                break
            elif guess<rand_number:
                tries+=1
                print("You a little lower than the answer.")
            elif guess>rand_number:
                tries+=1
                print("You are a little higher than the answer.")
        else:
            print("Please enter a number")
else:
    print("Enter a number this time!")

print(f"It took you {tries} tries.")
