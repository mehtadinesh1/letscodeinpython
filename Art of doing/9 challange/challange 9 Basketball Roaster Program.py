#Basketball Roaster Program
print("Welcome to the Basketball Roster Program")
#get input as player name from user
add_player1=input("\nWho is your point guard: ").title()
add_player2=input("Who is your shooting guard: ").title()
add_player3=input("Who is your small forword: ").title()
add_player4=input("Who is your power forward: ").title()
add_player5=input("Who is your center: ").title()
player_list=[add_player1,add_player2,add_player3, add_player4,add_player5]

#display basketball roster
print("\n\t\t\tYour starting 5 for the upcoming basketball season")
print(f"\t\t\t\t\tPoint Guard:   \t\t{player_list[0]}")
print(f"\t\t\t\t\tShooting Guard:\t\t{player_list[1]}")
print(f"\t\t\t\t\tSmall Forward: \t\t{player_list[2]}")
print(f"\t\t\t\t\tPower Forward: \t\t{player_list[3]}")
print(f"\t\t\t\t\tCenter:        \t\t{player_list[4]}")

#remove one player and get another player name from user
injured_plaer=player_list.pop(2)
print(f"\nOh no, {injured_plaer} is injured.")
print(f"Your roaster only has {len(player_list)} players.")
replacement_player = input(f"Who will take {injured_plaer}'s spot: ").title()
#place the replacement player in exact poistion of injured player
player_list.insert(2,replacement_player)


#display updated basketball roster
print("\n\t\t\tYour starting 5 for the upcoming basketball season")
print(f"\t\t\t\t\tPoint Guard:   \t\t{player_list[0]}")
print(f"\t\t\t\t\tShooting Guard:\t\t{player_list[1]}")
print(f"\t\t\t\t\tSmall Forward: \t\t{player_list[2]}")
print(f"\t\t\t\t\tPower Forward: \t\t{player_list[3]}")
print(f"\t\t\t\t\tCenter:        \t\t{player_list[4]}")

print(f"\nGood luck {replacement_player} you will do great!")
print(f"Your roster now {len(player_list)} players.")


