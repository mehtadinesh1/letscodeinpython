#Welcome to a game of Rock,Paper, Scissors
import random
print("Welcome to a game of Rock, Paper, Scissors")
#ask user for game round
game_round=int(input("\nHow many rounds would you like to play:"))
#create game option list and intial points
game_list=['Rock','Paper','Scissors']
player_point = 0
computer_point = 0
#game process
for i in range(game_round):
    print(f"Round {i+1}")
    print(f"Player: {player_point}\t\t\t\t Computer: {computer_point}")
    player_pick=input("Time to pick...rock,paper,scissors:").title()
    computer_pick=random.choice(game_list)
    print(f"\t\t\t\tComputer: {computer_pick}")
    print(f"\t\t\t\tPlayer: {player_pick}")
    #check all possibilites in game
    if player_pick in game_list:
        if player_pick == computer_pick:
            print("\t\t\t\tIt is tie, how boring!")
            player_point += 1
            computer_point += 1
            print("\t\t\t\tThis round was tie.")
        elif player_pick == "Rock" and computer_pick == "Paper":
            print("\t\t\t\tPaper covers rock!")
            computer_point +=1
            print(f"\t\t\t\tComputer win round {i+1}")
        elif computer_pick == "Rock" and player_pick == "Paper":
            print("\t\t\t\tPaper covers rock!")
            player_point +=1
            print(f"\t\t\t\tYou win round {i + 1}")
        elif player_pick == "Paper" and computer_pick == "Scissors":
            print("\t\t\t\tScissor cut paper!")
            computer_point +=1
            print(f"\t\t\t\tComputer win round {i + 1}")
        elif computer_pick == "Paper" and player_pick == "Scissors":
            print("\t\t\t\tScissor cut paper!")
            player_pick +=1
            print(f"\t\t\t\tYou win round {i + 1}")
        elif player_pick == "Scissors" and computer_pick == "Rock":
            print("\t\t\t\tRock stop scissors!")
            computer_point +=1
            print(f"\t\t\t\tComputer win round {i + 1}")
        else: #for computer_pick="Scissors" and player_pick="Rock"
            print("\t\t\t\tRock stop scissors!")
            player_point += 1
            print(f"\t\t\t\tYou win round {i + 1}")
    else:
        print("\t\t\t\tThat is not a valid game option!")
        print("\t\t\t\tComputer gets the point")
        computer_point +=1
#summary of the game
print("\nFinal Game Result")
print(f"\t\t\t\tRounds Played: {game_round}")
print(f"\t\t\t\tPlayer Score: {player_point}")
print(f"\t\t\t\tComputer Score: {computer_point}")
if player_point < computer_point:
    print("\t\t\t\tWinner: Computer :-(")
elif player_point > computer_point:
    print("\t\t\t\tWinner: You :-)")
else:
    print("\t\t\t\tGame tie between you and computer!")