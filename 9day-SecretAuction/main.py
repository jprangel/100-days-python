from art import logo
import os

other_bidder = True
bid_dict = {}

print(logo)
print("Welcome to the secret audiction program")
while other_bidder:
  name = input("What is your name?: ")
  bid = int(input("What is your bid? $ "))
  bid_dict[name] = bid
  other_bidder = input("Are there other bidders? Type 'yes' or 'no'.\n")
  if other_bidder == "yes":
    os.system('clear')
  else:
    other_bidder = False
    max_bid_name = max(bid_dict, key=bid_dict.get)
    max_bid_bid = bid_dict[max_bid_name]
    print(f"The winner is {max_bid_name} with a bid of {max_bid_bid}.")
    print("Goodbye !")
