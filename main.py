import random as r
import tarun as t

## Rock, Paper, Scissors
gestures = ["Rock", "Paper", "Scissors"]
yourscore = 0
computerscore = 0

rounds = int(input("How many rounds you want to play?\n"))
for round in range(rounds):
  print(f"\n\nRound: {round+1}\nScore:\nYou: {yourscore} | Computer: {computerscore}")
  user_hand = int(input("What do you chose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
  computer_hand = r.randint(0,2)

  if user_hand > 2 or user_hand < 0:
    print("Invalid draw, you lose")
    computerscore += 1
  else:
    print("You chose:", t.gestures[user_hand], "\nComputer chose:", t.gestures[computer_hand])
    if user_hand == computer_hand:
      print("Draw Again")
    elif user_hand == 0:
      if computer_hand == 1:
        print("You lose")
      else:
        print("You win")
    elif user_hand == 1:
      if computer_hand == 0:
        print("You win")
      else:
        print("You lose")
    elif user_hand == 2:
      if computer_hand == 0:
        print("You lose")
      else:
        print("You win")


    if user_hand == computer_hand:
      print("Draw Again")
    elif (user_hand == 0 and computer_hand == 2) or (user_hand == 1 and computer_hand == 0) or (user_hand ==2 and computer_hand == 1):
      print("You win")
    else:
      print("You lose")

    if user_hand == computer_hand:
      print("Draw Again")
    elif (user_hand == 0 and computer_hand == 2):
      print("You win")
      yourscore += 1
    elif (computer_hand == 0 and user_hand == 2):
      print("You lose")
      computerscore += 1
    elif (user_hand > computer_hand):
      print("You win")
      yourscore += 1
    else:
      print("You lose")
      computerscore += 1
    
print(f"\nScore:\nYou: {yourscore} | Computer: {computerscore}")
if yourscore > computerscore:
  print("You are the RPS champion!")
elif yourscore == computerscore:
  print("It's a perfect match of equals!")
else:
  print("Practice your draws and better luck next time.")
