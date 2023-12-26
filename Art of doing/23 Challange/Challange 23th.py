#Yes or No Issue Polling App
print("Welcome to the Yes or No Issue Polling App")
#introduction and ask suitabel input from users
issue = input("\nWhat is the yes or no issue you will be voting on today: ")
no_voters = int(input("What is the number of voters you will allow on the issue: "))
#ask user for the passord for admin to see the result of poll
password = input("Enter a password for polling results: ").lower()
#process
count_Yeses=0
count_NOes = 0
voters_database = {}
for i in range(no_voters):
        name=input("\nEnter your full name: ").lower()
        #check user already voted or not
        if name not in voters_database:
            print("Here is issue:", issue)
            choice = input("What do you think...yes or no: ").lower()
            if choice == 'yes' or choice == "no":
              voters_database[name]=choice
              count = i + 1
              print(f"Thank you {name}! Your vote of {choice} has been recorded.")
              #count both yes or no
              if choice == 'yes':
                 count_Yeses +=1
              else:
                 count_NOes +=1
            else:
               print("Enter valid choice! Only Yes or No ...")
        else:
            print("Sorry, it seems that someone with that name has already voted.")
#summary of poll
print(f"\nThe following {count} people voted:")
for i in voters_database.keys():
    print(i)
print(f"\nOn the follwing issue: {issue}")
if count_Yeses > count_NOes:
    print(f"Yes wins! {count_Yeses} votes to {count_NOes}")
elif count_NOes > count_Yeses:
    print(f"NO wins! {count_NOes} votes to {count_Yeses}")
else:
    print(f"It's tie.......")
#access voting reslut
admin_passwrod = input("\nTo see the voting result enter the admin password:").lower()
if admin_passwrod == password:
    for i,j in voters_database.items():
        print(f"Voter: {i} \t\t\t\t\t\t\t Vote: {j}")
    print("Thank you for using the Yes or No Issue Polling App.")
else:
    print("Admin password is wrong")
    print("Thank you for using our services.")