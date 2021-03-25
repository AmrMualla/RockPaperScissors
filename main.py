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

import random

Choice = input("Type rock, paper or scissors? \n")
Programchoices = [rock, paper, scissors]
Program = random.randint(0,2)
Programchoice = Programchoices[Program]

if(Choice == "rock" or Choice == "Rock"):
  print("You chose: " + rock)
  Choice = rock
elif(Choice == "paper" or Choice == "Paper"):
  print("You chose: " + paper)
  Choice = paper
else:
  print("You chose: " + scissors)
  Choice = scissors

print("The program chose: " + Programchoice)

if(Programchoice == rock and Choice == paper):
  print("Congratulations, you won!")
elif(Programchoice == paper and Choice == scissors):
  print("Congratulations, you won!")
elif(Programchoice == scissors and Choice == rock):
  print("Congratulations, you won!")
elif(Programchoice == rock and Choice == scissors):
  print("Tough luck, you lost. ;(")
elif(Programchoice == paper and Choice == rock):
  print("Tough luck, you lost. ;(")
elif(Programchoice == scissors and Choice == paper):
  print("Tough luck, you lost. ;(")
else:
  print("It was a tie! :|")