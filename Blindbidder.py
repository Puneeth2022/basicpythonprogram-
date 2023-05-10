def highest_bid(bids):
    highest_price=0
    higher = ""
    for bidder in bids:
        bid_price=bids[bidder]
        if bid_price>highest_price:
            highest_price=bid_price
            higher=bidder
    print(f"the winner is {higher} and the highest bid is {highest_price}")

print("wlecome to the bitting board")
bids={}
bidder_finished=False
while not bidder_finished:
    name=input("what is your name??\n")
    bid=int(input("what is your bid??\n"))
    bids[name]=bid
    print("is there a bidder")
    bidder_presence=(input("yes or no\n"))
    if bidder_presence=="no":
        bidder_finished=True
highest_bid(bids)


