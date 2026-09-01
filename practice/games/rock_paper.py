import random

my_list = ["rock", "paper", "scissor"]
print("rock👊")
print("paper📝")
print("scissor✂")

while True:
    computer = my_list[random.randint(0,2)]
    user = input("Enter Your Choice = ")

    if(user=="rock" and computer=="scissor") or (user=="paper" and computer=="rock") or (user=="scissor" and computer=="paper"):
          print("You Win🤴")

    elif(computer=="rock" and user=="scissor") or (computer=="paper" and user=="rock") or (computer=="scissor" and user=="paper"):
              print("You Lost😕")

    elif(computer=="rock" and user=="rock") or (computer=="paper" and user=="paper") or (computer=="scissor" and user=="scissor"):
                  print("Tie....😂")

    else:
            print("You Enter Invalid Strings...🙄")
            break