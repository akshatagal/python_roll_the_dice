import random

while True:
    Choice = input("Do u wanna roll the dice (y/n) : ").lower()
    if Choice in ('y','yes'):
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print("The Dice Outcomes are : ",f'({die1},{die2})')
        print("Done!!")
        print(" ")
    elif Choice in ('n','no'):
        print("Okay Thanks for Playing !")
        
        break
    else:
        print("Invalid Choice")
        break
