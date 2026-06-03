print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?\n"))
total_bill=bill
tip = float(input("What percentage tip would you like to give? 10 12 15 \n"))
tip =tip/100
print(f"You are paying to the server %{tip} tip" )
amount_paid_to_server=total_bill*tip
print(f"You paid to server ${amount_paid_to_server}!")
final_Amount=total_bill+amount_paid_to_server
print("Your price that was left paid after including the tip :",final_Amount)
people = int(input("How many people to split the bill? "))
print(f"Your Amount to be paid by {people} people after splitting the bill:",round(final_Amount / people,2))



