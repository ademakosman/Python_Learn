import random
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

#Write your code below this line 👇

user_selection = int(input(print(" What do you choose? 0 For rock, 1 for Paper, 2 for Scissors")))
selection = [rock,paper,scissors]
if user_selection == 0:
  print(rock)
  selection_a=0
elif user_selection == 1:
  print(paper)
  selection_a=1
else:
  print(scissors) 
  selection_a=2 

computer_selection = random.randint(0,2) 
if computer_selection == user_selection:
  print(selection[selection_a])
  print(" NO ONE WIN, DRAW")
elif computer_selection == 1 and user_selection == 0:
  print(paper)
  print(" COMPUTER WIN")
elif computer_selection == 1 and user_selection == 2:
  print(paper)
  print(" YOU WIN")
elif computer_selection == 0 and user_selection == 1:
  print(rock)
  print(" YOU WIN")
elif computer_selection == 0 and user_selection == 2:
  print(rock)
  print(" COMPUTER WIN")
elif computer_selection == 2 and user_selection == 0:
  print(rock)
  print(" YOU WIN")
elif computer_selection == 2 and user_selection == 1:
  print(rock)
  print(" COMPUTER WIN")

