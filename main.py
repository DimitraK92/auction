from os import system
import signal
from art import logo

def handler(signum, frame):
    system("cls")
    exit(1)

signal.signal(signal.SIGINT, handler)

print(logo)
  
def start_auction():  
  bids = {}
  bidding_finished = False
  while not bidding_finished:
    name = input("What is your name?: ")
    price = float(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Y/N\n")
    if should_continue.upper() == "Y":
      system("cls")
    else: 
      bidding_finished = True
      find_highest_bidder(bids)

def find_highest_bidder(bidding_record):
  highest_bid = max(bidding_record.values())
  max_bidders = [key for key, val in bidding_record.items() if val == highest_bid]
  # In real life no-one would bid the same price. So the first one wins.
  winner = max_bidders[0]
  print(f"The winner is {winner} with a bid of ${highest_bid}")

start_auction() 