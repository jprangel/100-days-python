import random
import time

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print(" !! Welcome to Rock Paper Scissors against the PC !!")
human_op = input("What do you wanna choose? type 1 for Rock, 2 for Paper or 3 for Scissors \n")
pc_op = random.randint(1,3)
human_op = int(human_op)
print("You choosed: ")
if human_op == 1:
  print(rock)
elif human_op == 2:
  print(paper)
elif human_op == 3:
  print(scissors)

print("The PC choosed...")
time.sleep(3)
if pc_op == 1:
  print(f"{rock}")
elif pc_op == 2:
  print(f"{paper}")
elif pc_op == 3:
  print(f"{scissors}")

if human_op == 1 and pc_op == 3:
  print("You won !!!")
elif human_op == 2 and pc_op == 1:
  print("You won !!!")
elif human_op == 3 and pc_op == 2:
  print("You won !!!")
elif human_op == pc_op:
  print("WE HAVE A DRAW, PLAY AGAIN")
else:
 print("You LOSE !!!")
