#Vote Registration App
print("Welcome to the Voter REgistration App")
#user intro
name=input("\nPleasse enter your name:")
age=int(input("Please enter your age:"))
#create list of parties
party_list=['Repulicam','Democratic','Independent','Green']

#check the age of the user valid or not for vote
if age >= 18:
    print(f"\nCongratulation {name}! You are old enough to register to vote.")
    #list of political parites to join
    print("\nHere is a list of political parties to join")
    for i in party_list:
        print("-",i)
    join_party=input("\nWhat party would you like to join:").title()
    #summray
    if join_party in party_list:
        print(f"\nCongratulation {name}! You have joinded the {join_party} party!")
        #show selected party background
        if join_party in ('Repulican','Democratic'):
          print("That is a major party!")
        else:
          print("That is a minor party!")
    else:
        print("\nThat is no given party!")
#below 18 not eligible for vote
else:
    print("You are not old enough to register to vote.")
