#Database Admin Program
print("Welcome to the Database Admin Program")
#database contian user name and password
database = {'admin':'admin',
            'dinesh':'hello123',
            'nishant':'qwerty123',
            'sheetal':'abcd123'}
#get user's names from database and store as list
user_list = list(database.keys())

#ask user name
name = input("\nEnter your username: ").lower()
#check user name exist in database
if name in user_list:
    password = input("Enter you password: ")
    #if user is admin
    if name == 'admin' and password == database.get(name):
        print(f"\nHello {name}! You are logged in!")
        print("\nHere is th current user database:")
        for i,j in database.items():
            print(f"Username: {i} \t\t\t\t\t\t Password: {j}")
    #normal user
    elif password == database.get(name):
        print(f"\nHello {name}! You are logged in!")
        #ask permission to change password
        permission = input("Would you like to change your password: ").lower()
        if permission == "yes":
          new_password = input("What would you like your new password tto be: ")
          #conditions for enter new password
          if len(new_password) < 8:
              print(f"{new_password} not the minimum eigth character.")
              print(f"\n {name} your old password is {database.get(name)}")
          else:
              database[name]=new_password
              print(f"\n{name} your new password is {new_password}")
        else:
            print("\n Thank you for coming here!")
    else:
        print("\nYou enter wrong password.")
#in case user entry not in database
else:
    print("User not found!")


