import random
random_choice=random.randint(0,2)
game_tool =["rock","paper","scissors"]
user_choice=int(input("Enter your choice?\n0:rock\n1:paper\n2:scissor\n"))
print(game_tool[random_choice])
if random_choice== user_choice:
    print("it is a draw !!")
elif user_choice==0 and random_choice==2:
    print("you win!")
elif user_choice==2 and random_choice==0:
    print("you los!!")
elif user_choice==1 and random_choice==0:
    print("you win!")
elif user_choice==0 and random_choice==1:
    print("you los!!")
elif user_choice==0 and random_choice==2:
    print("you win!")
elif user_choice==2 and random_choice==0:
    print("you los!!")
elif user_choice==2 and random_choice==1:
    print("you win!")
elif user_choice==1 and random_choice==2:
    print("you los!!")
else :
    print ("invalid choive!!!")