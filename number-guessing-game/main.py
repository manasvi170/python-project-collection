import art
import random
print(art.logo)
print("Welcome to the number guessing game")
print("I am thinking of a number between 1 and 100")
difficulty = input("\nChoose you difficulty 'easy' or 'hard' :")
num=random.randint(1,100)

def rules(lives,num):
    print(f"You have {lives} attempts remaining to guess the number")
    user_guess = int(input("Your Guess :"))
    if user_guess == num:
        print(f"Wohooo ,You did it!The number was {num}")
        print(art.winner)
        raise SystemExit
    if num > user_guess:
        print("Too low")
    else:
        print("Too High")

if difficulty == "easy":
    lives=10
else:
    lives=5

for lives in range(lives,0,-1):
    rules(lives,num)

print(f"\nYou lost the game!\nBetter luck next time . The number was {num}")
print(art.loser)






