

import random
import time

def displayIntro():
    print("beep")
    time.sleep(3)
    print("bop")
    for i in range(3):
        print("processing...")
        time.sleep(3)
    print("initializing homoromantic proticals")
    time.sleep(4)
    print("huge gay detected...")
    time.sleep(5)
    print("initalizing redemption arc")
    time.sleep(5)
    print()
    print("     #########################")
    print("     |                       |")
    print("     |   Welcome to catrabot |")
    print("     |         Beep bop      |")
    print("     #########################")
    print()
    print()




    print("Still a work in progress")

    print("I will likely forget about this project")
    print()

def hi():
    print("This is catbot...")
    time.sleep(3)

def choosePath():
    Feeling = ""
    while Feeling != "Adora" and Feeling != "2": # input validation
        Feeling = input("What do you want? Enter 'Adora': ")

    return Feeling

def checkPath(chosenPath):
    print("processing input")
    time.sleep(2)
    print("Kinda cringe tbh")
    time.sleep(2)
    print("Catra bot to gay for math")
    print()
    time.sleep(2)


    if chosenPath == str('Adora'):
        print("gay")
        time.sleep(2)
        print("gAy?")
        time.sleep(2)
        print("GAY!!! <3")
        time.sleep(3)
        print("GAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAY :)")
        time.sleep(2)
        print("Gay")
        time.sleep(3)
        print(">:3")
        x = int(input("please enter a number: "))
        for i in range(x):
            print("Gay")
            
    else: 
        print("Invalid input go away")
    

playAgain = "yes"
while playAgain == "yes" or playAgain == "y":
    displayIntro()
    choice = choosePath()
    checkPath(choice) # choice is equal to "1" or "2"
    playAgain = input("Do you want to play again? DM me to get me to stop being lazy and add more features (yes or y to continue playing): ")