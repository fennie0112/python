import random

random_num = int(random.random()*101)
total_life = 10

while True:
    num =int(input("Guess the number(1-100) = "))

    if(num<1 or num>100):
        print("You cross the limit...!!💢💢")
        break

    total_life -= 1
    if(num==random_num):
        print("You won the game...🥳")
        print("congratulations✨✨🎊🎊🎉🎉")
        break

    elif(total_life==0):
        print("Game over You Lost the Game..🤦‍♀️🤦‍♀️")
        break

    elif(num>random_num):
        print("Try to Guess Lower Value😊")

    elif(num<random_num):
            print("Try to Guess Higher Value😀")

