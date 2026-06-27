import art
print(art.logo)
print("Welcome to the secret auction program!")
def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]  #Retrieving the values from Dictionary dict={Key:Value}
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


bids={}
continue_bidding=True
while continue_bidding:
    name = input("What is your name ?\t").capitalize()
    price = input("How much you want to bid ?\t $")
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
    if should_continue=="no":
        find_highest_bidder(bids)
        continue_biding=False
    elif should_continue=="yes":
        print("\n" * 100)
