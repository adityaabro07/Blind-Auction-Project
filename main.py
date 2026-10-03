#Blind Auction Project
def highest_bidder(bidding_dictionary):
    winner=""
    highest_bid=0
    for bidder in bidding_dictionary:
        bid_amount=bidding_dictionary[bidder]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner=bidder

    print((f"The winner is {winner} with a bid of ${highest_bid}"))
auction_table={}
continue_bidding=True
while continue_bidding:
    name1 = input("Enter your name")
    bid1 = int(input("Enter your bid"))
    auction_table[name1]=bid1
    should_continue=input("Do you want to continue?(y/n)".lower())
    if should_continue=="n":
        continue_bidding=False
        highest_bidder(auction_table)
    elif should_continue=="y":
        print("\n"*20)