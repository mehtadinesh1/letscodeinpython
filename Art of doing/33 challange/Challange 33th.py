 #Python First National Bank
print("Welcome to the Python First National Bank.")

def current_information():
    for item,value in account_information.items():
        print(f"{item}: {value}")

def deposit():
    account_information[acount_type] += money
    print(f"\n{money} deposited in your {acount_type} account")

def withdraw():
    if account_information[acount_type] - money > 0:
        account_information[acount_type] -= money
        print(f"\n{money} withdraw from your {acount_type}")
    else:
        print(f"\nBy withdrawing {money} from your {acount_type} account goes in negative.")

def program_again():
    choice = input("Would you like to make another transacion (y/n); ")
    if choice == "y":
        return True
    else:
        return False

account_information = {}
choice = True
name = input("\nHello, what is your name: ").title()
saving_account = int(input("How much money would you like to set up your savings account with: "))
checking_account = int(input("How much money would you like to st up your checking account with: "))
account_information["Name"] = name
account_information["Savings"] = saving_account
account_information["Checking"] = checking_account
while choice:
  current_information()
  acount_type = input("\nwhat account woild you like to access (Savings or Checking): ").title()
  transaction_type = input("What type of transaction would you like to make (Deposit or Withdraw); ").title()
  money = int(input("How much money: "))
  if acount_type == "Savings" or acount_type == "Checking":
    if transaction_type == 'Deposit':
      deposit()
    else:
      withdraw()
  else:
      print("Sorry for inconvenience but this service is not available.")
  choice = program_again()

print("\nThank you. Have a great day!")