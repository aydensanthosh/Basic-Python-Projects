import random
def roll():
    roll_a_die=random.randint(1,6)
    return roll_a_die
max_points=50

while True:
    players=input("Enter the number of players(2-4): ")
    if players.isdigit():
        players=int(players)
        if 2<=players<=4:
            break
        else:
            print("Enter a number between 2-4!")
    else:
        print("Invald, Try Again")
points=[0 for i in range(players)]

while max(points)<max_points:
    for i in range(players):
            print(f"\nPlayer #{i+1}.")
            print(f"Your Total score in {points[i]}\n")
            current_score=0
            while True:
                choice=input("Do you want to play?(y)[q=quitting game]: ").lower()
                if choice=="y":
                    value=roll()
                    if value==1:
                        current_score=0
                        print("You rolled a 1, Your turn is over.")
                        current_score =0
                        break
                    else:
                        current_score+=value
                        print(f"You rolled a {value}.\nYour new score is {current_score}.")
                else:
                    points[i]+=current_score
                    print(f"Your total score is {points[i]}")
                    break
winner=max(points)
winner_idx=points.index(winner)
print(f"\n\n\nThe winner is Player #{winner_idx+1} with {points[winner_idx]} points")
