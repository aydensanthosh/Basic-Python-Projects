import turtle
import time
import random
WIDTH,HEIGHT=500,500
COLORS=['red','green','navy','blue','brown','black','orange','yellow','purple','magenta']


def get_number_of_racers():
    racer=0
    while True:
        racer=input("Enter the numbers of turtles you want to race(2-10): ")
        if racer.isdigit():
            racer=int(racer)
            if 2<=racer<=10:
                break
            else:
                print("Try again (between 2-10)!\n")
        else:
            print("Invalid: Enter a number.\n")
    return racer
def init_turtle_screen(racers):
    screen=turtle.Screen()
    screen.bgcolor("light green")
    screen.setup(WIDTH,HEIGHT)
    screen.title("Turtle Racing!!!")

def create_turtles(colors):
    turtles=[]
    spacingx=WIDTH//(len(colors)+1)
    for i,colors in enumerate(colors):
        racer=turtle.Turtle()
        racer.color(colors)
        racer.shape('turtle')
        racer.speed(3)
        racer.left(90)
        racer.penup()
        #Set position 
        racer.setpos(-WIDTH//2 + (i+1)*spacingx,-HEIGHT//2+20)
        racer.pendown()
        racer.speed(2)
        turtles.append(racer)
        
    return turtles
def race_turtle(colors):
    players=create_turtles(colors)
    check=True
    while check:
        for racer in players:
            racer.forward(random.randrange(5,20))
            
            x,y =racer.pos()
            if y>=HEIGHT//2-20 :
                check=False
                return(players.index(racer))



if __name__=='__main__':
    racers=get_number_of_racers()
    init_turtle_screen(racers)
    random.shuffle(COLORS)
    colors=COLORS[:racers]
    winner_idx=race_turtle(colors)
    time.sleep(2)
    print(f"\n\nThe winner is turtle # {winner_idx+1} with color {colors[winner_idx]}")






