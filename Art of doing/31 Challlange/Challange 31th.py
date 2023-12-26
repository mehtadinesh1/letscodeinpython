#Python Dice App
import random
print("Welcome to the Python Dice App")
#create fuction for dice reslut and return sum of all results
def dice_results(x,y):
    result = []
    for _ in range(x):
     number = random.randint(1,y)
     print(number)
     result.append(number)
    return sum(result)

def roll_again():
    choice = input("Would you like to roll again (y/n): ").lower()
    if choice == "y":
        roll = True
    else:
        roll = False
    return roll
rolling = True
while rolling:
  #ask user for inputs
  sides = int(input("\nHow many sides would you like on your dice: "))
  no_dices = int(input("How many dice would you like to roll: "))
  print(f"\nYou rolled {no_dices} {sides} sided dice.")
  #display the reults and value
  print("\n-----Result are as followed------")
  value = dice_results(no_dices,sides)
  print(f"\nThe total value of your roll is {value}")
  #ask to run program again
  rolling = roll_again()

print("\nThank you far using the Python Dice App.")


