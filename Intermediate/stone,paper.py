from random import randint
t=["Rock","Paper","Scissors"]
computer=t[randint(0,2)]
player=False
while player==False:
  player=input("'Rock', 'Paper' , 'Scissors' ? Which do you Prefer?:")
  
  if player==computer:
    print("Tie!")
  elif player=="Rock":
    if computer=="Paper":
      print("You Lose!",computer,"Covers",player)
    else:
      print("You Win!",computer,"Smashes",computer)
  elif player=="Paper":
    if computer=="Scissors":
      print("You Lose!",computer,"Cut",player)
    else:
      print("You Win!",computer,"Covers",Computer)
  elif player=="Scissors":
    if computer=="Rock":
      print("You Lose.....",computer,"Smashes",player)
    else:
      print("You Win!",computer,"Cut",Computer)
  else:
    print("That's not a valid play.Check your spelling!")
  player=False
  computer=t[randint(0,2)]
