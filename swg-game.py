# snake water gun game
import random

# choice2 = input("enter your choice:")
# print(choice2)
print("--------------------------  snake,water and gun game in python ---------------------------------")
print("\nLet's start the game! ")
name = input("Enter your name: ")
human_p = 0
com_p = 0
same = 0
i=0
while(i<10):
    lst = ["s", "w", "g"]
    choice1 = random.choice(lst)
    # print(choice1)
    choice2 = input("\nPress s for Snake, w for Water or g for Gun: ")
    choice2 = choice2.lower()
    if(choice1 == "s"):
        if(choice2 == "w"):
            print("Computer win")
            com_p = com_p + 1
        elif(choice2 == "g"):
            print(name,"won")
            human_p = human_p + 1
        elif(choice1 == choice2):
            print("same as")
            same = same +1
        else:
            print("try again! You enter wrong input")
    elif(choice1 == "w"):
        if (choice2 == "g"):
            print("Computer win")
            com_p = com_p + 1
        elif (choice2 == "s"):
            print(name," won")
            human_p = human_p + 1
        elif (choice1 == choice2):
            print("same as")
            same = same + 1
        else:
            print("\nTry again! You enter wrong input ")
    elif (choice1 == "g"):
        if (choice2 == "w"):
            print(name,"win")
            human_p = human_p + 1
        elif (choice2 == "s"):
            print("Computer won")
            com_p = com_p + 1
        elif (choice1 == choice2):
            print("same as")
            same = same + 1
        else:
            print("Try again! You enter wrong input ")
    print(f"\nComputer's score is: {com_p}")
    print(f"\n{name} score is: {human_p}")
    i = i+1

print("\nGame over")
print(com_p)
print(human_p)
if(com_p > human_p):
    print("Computer won and you lost! ")
elif (human_p > com_p):
    print(f"{name} won and computer lost! ")
else:
    print("It's a tie! ")