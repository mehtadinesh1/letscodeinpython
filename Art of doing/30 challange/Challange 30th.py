# Power-Ball simulator
import random

print("------------------Power-Ball Simulator----------------")
# introduction and ask users for input
white_balls = int(input("\nHow many white-balls to draw from for the 5 winning numbers (Normally 69): "))
if white_balls < 5:
    white_balls = 5
red_balls = int(input("How many red balls is to draw from for the Power-Ball (Normally 26): "))
if red_balls < 1:
    red_balls = 1
# calculate the odd of winning this lottery
odds = 1
for i in range(5):
    odds *= white_balls - i
odds *= red_balls / 120
print(f"You have a 1 in {odds} chance of winning this lottery.")

# generate winning ticket
winning_ticket = []
while len(winning_ticket) < 5:
    number = random.randint(1, white_balls)
    if number not in winning_ticket:
        winning_ticket.append(number)
winning_ticket.sort()
number = random.randint(1, red_balls)
winning_ticket.append(number)

# ask user for purchase the tickets
purchase_ticket = int(input("Purchase tickets in what intervals: "))

# process of Power-Ball simulator
print("\n-----------------Welcome to the Power-Ball--------------")
print("\nTonight's winning numbes are: ", end='')
for number in winning_ticket:
    print(number, end=' ')

input("\nPress 'Enter' to begin purchasing tickets!!! ")
count_tickets = 0
ticket_database = []
while True:
    # generate lottery ticket
    lottery_ticket = []
    while len(lottery_ticket) < 5:
        num = random.randint(1, white_balls)
        if num not in lottery_ticket:
            lottery_ticket.append(num)
    lottery_ticket.sort()
    num = random.randint(1, red_balls)
    lottery_ticket.append(num)
    # check for duplicate lottery in ticket database
    if lottery_ticket not in ticket_database:
        ticket_database.append(lottery_ticket)
        print(lottery_ticket)
        count_tickets += 1
        if lottery_ticket == winning_ticket:
            print("Winning ticket number: ", end='')
            for number in lottery_ticket:
                print(number, end=' ')
            print(f"\nPurchase a total of {count_tickets} tickets")
            break;
    else:
        print("Losing ticket generated")

    if count_tickets == purchase_ticket:
        print(f"\nYou purchaseed {count_tickets} so far:")
        # ask for continue the game
        permission = input("\nKeep puchasing ticket (y/n): ").lower()
        if permission == 'y':
            pass
        else:
            # diplay game over
            print(f"\nYou bought {count_tickets} tickets and still lost!")
            print("Better luch next time!")
            break;
