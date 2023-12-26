#Guess My Number App
import random
print("Welcome to the Guess My Number App")
#Introductio
name=input("\nHello! What is you name:")
print(f"Well {name}, I am thinking of a number between 1 and 20")
#choose random no between 1-20
number=random.randint(1,20)
#guess the no. five times
for i in range(5):
    guess=int(input("\nTake a guess:"))
    if guess < number:
        print("Your guess is too low.")
    elif guess > number:
        print("Your guess is too high.")
    else:
        #game is done, recap loosing and winning
        if guess == number:
            print(f"\nGood Job, {name}! You guess my number in {i + 1} guesses!")
            break;
        else:
            print(f"\nGame over! The number I was thinking of was {number}")

