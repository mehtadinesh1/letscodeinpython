#Welcome to the Multiplication/Exponent Table App

print("Wellcome to the Multiplication/Exponent Table App")

#get user input
name = input("Hello, What's your name:")
Number = float(input("What number would you like to work with:"))
message = name + " Math is cool"
print(f"\nMultiplication Table for {Number}")
#use for loop to print multiplication table
for i in range(1,10):
    print(f"{i} * {Number} = {i*Number}\n")


print(f"\nExponent Table for {Number}")
#use for loop to print exponent table
for j in range(1,10):
    print(f"{j} ** {Number} = {j**Number}\n")


print(f"\n",message)
print(f"\t\t",message.lower())
print(f"\t\t\t",message.upper())
print("\t\t\t\t",message.title())
