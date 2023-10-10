# This code is for a blind auction program whereby participants don't get to know how much bid is made by
# other participants.
# As such, a device running the application is passed around and participants are asked to enter their first
# and the amount for their bid.
# Then the app asks the participant whether there are other bidders in the room.
# If the participant looks around and sees other bidders in the room, he answers 'yes', then the app will
# clear the screen (and the next participant gets to enter their details without seeing the name or bid amount
# any previous participant.
# The app compiles the data of all participants and their bid amount, and announces the winner with the highest bid.

from replit import clear
participants = [ ]
amounts = [ ]
print("Welcome to the Blind Auction Program")

other_bidders = True
while other_bidders == True:
    name = input("Please enter your first name: ")
    bid = int(input("How much is your bid?: $"))
    others = (input("Are there any other bidders? Enter 'yes' or 'no': ")).lower()
    participants.append(name)
    amounts.append(bid)

    if others == "no":
        other_bidders = False
        print("Thank you for your participation")
    else:
        clear()

max_bid = max(amounts)
index_of_winner = amounts.index(max_bid)
bid_winner = participants[index_of_winner]

print(f"The winner is {bid_winner} with a bid of {max_bid}")
