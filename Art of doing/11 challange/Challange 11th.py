#Binary/Hexadecimal Converter App
print("Welcome to the Binary/Hexadecimal Converter App")
#get user input as int number
max_value=int(input("\nCompute binar and hexadecimal values up to the following decimal number: "))

#get slicing index form the user
print("\nUsing slices, we will now show a portion of each list.")
first_number=int(input("What decimal number would you like to start at: "))
last_number=int(input("What decimal number would you like to start at: "))
#dispaly the result of individual number
print(f"\nDecimal values from {first_number} to {last_number}:")
for i in range(first_number,last_number+1):
    print(i,"\n")

print(f"\nBinary vlaues from {first_number} to {last_number}:")
for i in range(first_number,last_number+1):
    print(bin(i),"\n")

print(f"Hexadecimal vlaues form {first_number} to {last_number}:")
for i in range(first_number,last_number+1):
    print(hex(i),"\n")
#show full list
input(f"\nPress Enter to see all values form 1 to {max_value}.")
print("Decmial---Binary---Hexadecimal")
print("--------------------------------")
for i in range(1,max_value+1):
    print(i,"----",bin(i),"----",hex(i),"\n")


