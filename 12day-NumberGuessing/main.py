import random

def pick_magic_number():
  return int(random.randrange(1,100))
  
def play():
  print("Welcome to Number Guessing Game !")
  print("I'm thinking in a number between 1 and 100.")
  magic_number = pick_magic_number()
  #print(f"Psst, the correct answer is {magic_number}")
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    attemps = 10
  else:
    attemps = 5
  while attemps > 0:
    print(f"You have {attemps} attemps remaning to guess the number")
    guess = int(input("Make a guess: "))
    
    if guess == magic_number:
      attemps = -1
      print("You won !!")
    elif guess > magic_number:
      print("Too high")
    else:
      print("Too low")
    if attemps == 0:
      print("Run out number of attemps. You lose")
    attemps = attemps - 1

play()
