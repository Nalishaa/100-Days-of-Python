from art import logo
print(logo)

# TODO-4: Compare bids in dictionary
def highest_bid(ppl_in_dictionary):
    max_bidder=""
    max_bid=0
    for key in dictionary:
        if dictionary[key] > max_bid:
            max_bid = dictionary[key]
            max_bidder=key
    print(f"The winner is {max_bidder} with a bid of ${max_bid}")

more="yes"
dictionary={}
while more == "yes":
    # TODO-1: Ask the user for input
    name=input("What is your name?: ")
    bid=int(input("What is your bid?: $"))

    # TODO-2: Save data into dictionary {name: price}
    dictionary[name]=bid

    # TODO-3: Whether if new bids need to be added
    more=input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    if more == "yes":
        print("\n" * 20)
    else:
        highest_bid(dictionary)

