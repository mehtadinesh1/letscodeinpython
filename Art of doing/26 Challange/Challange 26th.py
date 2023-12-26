#Factor Generator App
print("Welcome to the FActor Generator App")
#ask user for number
number = int(input("Enter a number to determine all factors of that number: "))
#process
while True:
    print(f"\nFactors of {number} are:")
    #create list that store factors so we can display summary
    factor_list = []
    #display factors
    for i in range(1,number+1):
        if number % i == 0:
            print(i)
            factor_list.append(i)
    print("\nIn summary:")
    for i in range(len(factor_list)//2):
        print(f"{factor_list[i]} * {factor_list[-1-i]} = {factor_list[i]*factor_list[-1-i]}")

    #ask user for continuation
    choice = input("\nRun again (y/n): ").lower()
    if choice == 'n':
        print("Thank you for using the program. Have a great day.")
        exit()
