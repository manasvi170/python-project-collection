# Creating a Rock Paper Scissors game
import random
print("Welcome to the Rock Paper Scissor game.\n You will be playing against the computer!\n\n")
Rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

Paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

Scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images=[Rock ,Paper,Scissors]
# user playing
user_playing=int(input('Choose one Rock (0), Paper(1), Scissors(2):'))
if user_playing==0:
    print(Rock)
elif user_playing==1:
    print(Paper)
elif user_playing==2:
    print(Scissors)
if user_playing>=3 or user_playing<0:
    print("You typed an invalid number. You lose!")
    raise SystemExit

#computer playing
print("Computer Choose :")
game_components=[Rock,Paper,Scissors]
computer_choose=random.randint(0,2)

if computer_choose==0:
    print(Rock)
elif computer_choose==1:
    print(Paper)
else:
    print(Scissors)


# Rules
if user_playing==0 and computer_choose==2:
    print("You WON!")
elif computer_choose==2 and user_playing==0:
    print("You lose..")
elif user_playing==computer_choose:
    print("It`s a draw ")
elif user_playing>computer_choose:
    print("You WON!")
elif computer_choose>user_playing:
    print("You lose...")
