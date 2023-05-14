from random import randint

def check_answer(guess, answer):
    if answer>guess:
        print("Too low")
    elif answer<guess:
        print("Too high")
    else:
        print("right answer!!\nyou have won the game\n")    


print("Welcome To Number Guessing Game !")
print("I am Thinking of number between 1 to 100")
answer=randint(1,100)
print("you want to play hard or easy game")
type=input().lower()

if type=="easy":
    for i in range(0,10):
        print(f"You have {10-i} attempts ")
        guess=int(input("make a guess\n"))
        check_answer(guess, answer)
elif type=="hard":
    for i in range(0,5):
        print(f"You have {5-i} attempts ")
        guess=int(input("make a guess\n"))
        check_answer(guess, answer)

