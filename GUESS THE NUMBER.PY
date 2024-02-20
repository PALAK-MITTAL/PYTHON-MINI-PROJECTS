import random

target=random.randint(1,100)

while True:
  userchoice=input("enter the value you guess or QUIT for exiting from game:")
  if(userchoice=="QUIT"):
    break
  userchoice=int(userchoice)
  if(userchoice==target):
    print("CONGRATS! you guess the correct number.")
    break
  elif(userchoice<target):
    print("guess again, your guess was small")
  else:
      print("guess again, your guess was big")

print("---------------GAME OVER----------------------")
