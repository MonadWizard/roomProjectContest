import time

global gold
global apples
gold = 0
apples = 0



def start():
    print("Hello and welcome....!")
    name = input("What's your name : ")
    print("Welcome, ",name," !")
    print("The objective of yhis game is to collect apples.")
    print("After collecting apple you sell them.")
    choice = input("Doyou want to play Y/N ?")
    if choice == "Y":
        begin()
    if choice == "N":
        print("Okay, bye.....")




def begin():
    global apples
    global gold
    print("Let's get started...!")

    if gold > 99:
        print("You've Won the game..!")
        play = input("Do you want to play again ?")
        if play == "Y":
            begin()
        if play == "N":
            print("Congraze again")


    pick = input("Do you want to pick an apple Y/N ?")
    if pick == "Y":
        time.sleep(1)
        print("You pick an apple.")
        apples=apples+1
        print("You currently have ,", apples, " apples")
        begin()

    if pick == "N":
        sell = input("Do you want to sell your apples Y/N ?")
        if sell == "Y":

            print("You currently have, ",apples," apples")
            print("You've sold your apples.")
            gold = apples * 10
            apples = 0
            print("your gold is now :",gold)
            begin()

start()










