import random
from game_data import data
from art import logo,vs

def format_data(account):
    """Taking the account data and displaying it in a printable format"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name} , a {account_descr} , from {account_country} "

def check_answer(user_guess,a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess=="a"
    else:
        return user_guess=="b"

print(logo)
print("Welcome to the Higher Lower game !")
score=0
game_should_continue=True
account_b=random.choice(data)
while game_should_continue:
    account_a=account_b
    account_b=random.choice(data)
    if account_a==account_b:
        person_two=random.choice(data)

    print(f"Compare Person A :{format_data(account_a)}")
    print(vs)
    print(f"Against Person B :{format_data(account_b)}")
    guess=input("Who has more followers? Type 'A' or 'B': " ).lower()
    print("\n" * 20)
    print(logo)

    a_follower_count=account_a["follower_count"]  #Stores follower Count of account_a
    b_follower_count=account_b["follower_count"]  #Stores follower Count of account_b

    is_correct=check_answer(guess, a_follower_count , b_follower_count)

    """Checking if the user guessed is correct"""
    if is_correct:
        score+=1
        print(f"\nYou got it right! Correct score is {score}\n")
    else:
        print(f"\nSorry...that`s wrong! Final score: {score}")
        game_should_continue=False
