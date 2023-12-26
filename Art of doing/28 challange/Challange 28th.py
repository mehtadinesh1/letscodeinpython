#Prime Number App
import time
print("Welcome to the Prime Number App")
#introduction
while True:
  print("\nEnter 1 to determine if a specific number is prime.")
  print("Enter 2 to determine all prime numbers within a set range.")
  choice = int(input("Enter your choice 1 or 2: "))
  if choice == 1:
    number = int(input("\nEnter a number to determine if it is prime or not: "))
    if number > 1:
         for i in range(2, number):
            if number % i == 0:
               print("\nIt is not prime no")
               break;
         else:
             print(f"{number},It is prime no.")
    else:
       print("it is not prime no.")

  elif choice == 2:
    lower_bound = int(input("\nEnter the lower bound of your range: "))
    upper_bound = int(input("Enter the upper bound of your range: "))
    prime_no_list = []
    #find prime numbers and store in list
    start = time.time()
    for num in range(lower_bound,upper_bound+1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    pass
                    break;
            else:
                prime_no_list.append(num)
        else:
            pass
    end = time.time()
    #display prime no.
    print(f"\nCalculation took a total of {round(end-start,4)} seconds")
    print(f"The following numbers between {lower_bound} and {upper_bound} are prime")
    input("Press enter to continue:")
    for num in prime_no_list:
        print(num)
  else:
    print("That is not valid option")


  #ask user for continue the program
  answer = input("Would you like to run the program again (y/n): ")
  if answer == 'n':
      print("\nThank you using our service.....")
      exit()

