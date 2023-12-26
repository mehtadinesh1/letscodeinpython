#Even Odd Number Sorter App
print("Welcome to the Even Odd Number Sorter App")
while True:
  #ask user for enter string of number
  string_numbers = (input("Enter in a string of number separated by a comma(,) : "))
  string_numbers = string_numbers.replace(' ','')
  list_numb = string_numbers.split(',')
  #process
  #check no are odd or even and display them
  print("\n......Result Summary.....")
  even_list = []
  odd_list = []
  for i in list_numb:
     number = int(i)
     if number%2 == 0:
        print(f"{i} is even!")
        even_list.append(number)
     else:
        print(f"{i} is odd!")
        odd_list.append(number)
  #display even no.
  print(f"\nThe following {len(even_list)} number are even: ")
  for number in even_list:
     print(number)

  #display odd no.
  print(f"\nThe following {len(odd_list)} number are odd: ")
  for number in odd_list:
      print(number)

  #ask user for continoue the program of not
  choice = input("\nWould you like to run the program again: ").lower()
  if choice == 'n':
      print("\nThank you using our services!")
      exit()