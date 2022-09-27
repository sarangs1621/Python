import random
secretnum = random.randint(1,100)
guessNum=int(input("guess a number between 1 and 100 inclusivly:"))
while guessNum != secretnum:
   if guessNum<secretnum:
      print("your guess is too low")
   else:
      print("your guess is too high")
   guessNum=int(input("guess number between 1 and 100 inclusivly:"))
print("congradulation!!!! you guessed the number correctly")
