import random
import time
Operators=["+","-","*","/"]
Min=3
Max=12
TOTAL_PROBLEMS=10
wrong=0
def generate_prob():
    left =random.randint(Min,Max)
    right=random.randint(Min,Max)
    Operator=random.choice(Operators)
    Exp=str(left)+Operator+str(right)

    answer=eval(Exp)

    return Exp, answer
consent=input("Are u ready to begin with the Math Quiz(**There will be a timer measuring your time!)[Press Enter to start]:")
start_time=time.time()
print("-"*50)
for i in range(TOTAL_PROBLEMS):
    exp,answer=generate_prob()
    while True:
        
        guess=input(f"Problem #{i+1}: {exp}=")
        guess=float(guess)
        
        if round(guess,2)==round(answer,2):
            break
        else:
            wrong+=1
end_time=time.time()
durtion=end_time-start_time
print("-"*50)
print("Nice Job!")
print(f"Wrong answers:{wrong}\nAccuracy={round((10/(10+wrong))*100,2)}")
print(f"Time taken = {round(durtion,2)}s")