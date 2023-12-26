print("Welcome to the letter counter app")
#get user input
name = input("\nWhat's your name = ")
print("\nI will count number of times that a specific letter occur in a message")

message = input("\nPlease enter a message:")
letter = input("\nWhich letter would you like to count the ouccorence of:")

#Standardize to lower case
message=message.lower()
letter=letter.lower()

#Get the count and display the result
count = message.count(letter)
print(f"\n{name}, your message has {count} {letter}'s in it.")

