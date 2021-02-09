# snake water gun game
import random

# choice2 = input("enter your choice:")
# print(choice2)
print("--------------------------  snake,water and gun game in python ---------------------------------")
print("Let's start the game")
name = input("Enter your name:")
human_p = 0
com_p = 0
same = 0
i=0
while(i<10):
    lst = ["snake", "water", "gun"]
    choice1 = random.choice(lst)
    # print(choice1)
    choice2 = input("enter your choice:")
    if(choice1 == "snake"):
        if(choice2 == "water"):
            print("computer win")
            com_p = com_p + 1
        elif(choice2 == "gun"):
            print(name,"win")
            human_p = human_p + 1
        elif(choice1 == choice2):
            print("same as")
            same = same +1
        else:
            print("try again! You enter wrong input")
    elif(choice1 == "water"):
        if (choice2 == "gun"):
            print("computer win")
            com_p = com_p + 1
        elif (choice2 == "snake"):
            print(name," win")
            human_p = human_p + 1
        elif (choice1 == choice2):
            print("same as")
            same = same + 1
        else:
            print("try again! You enter wrong input")
    elif (choice1 == "gun"):
        if (choice2 == "water"):
            print(name,"win")
            human_p = human_p + 1
        elif (choice2 == "snake"):
            print("computer win")
            com_p = com_p + 1
        elif (choice1 == choice2):
            print("same as")
            same = same + 1
        else:
            print("try again! You enter wrong input")
    print(f"computer score is:",com_p)
    print(f"{name} score is:",human_p)
    i = i+1

print("Game over")
print(com_p)
print(human_p)
if(com_p > human_p):
    print("computer is win and human lose")
elif (human_p > com_p):
    print(name,"is win and computer lose")
else:
    print("match is tie")
