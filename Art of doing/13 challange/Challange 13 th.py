#Welcome to the Factorial Calculator App
import math
print("Welcome to the Factorial Calculator App")

#get user input as desire no. of which you want factorial
number=int(input("\nWhat number would you like to compute the factorial of? "))
#dispay the process to get foctorial
print(f"{number}! = ",end="")
for i in range(1,number+1):
    print(f"{i}",end="")
    if i == number:
        break;
    print(end="*")

#calculate foctorial through math library
fact = math.factorial(number)
print(f"\nHere is the result from the math library:")
print(f"The factorial of {number} is {fact}!")
#calculate through own algorithm
factorial = 1 # 1 is always minimum factorial
for i in range(1,number+1):
    factorial = factorial * i
print(f"\nHere is the result from my own algorithm:")
print(f"The factorial of {number} is {factorial}!")

#conclusion
print(f"\nIt is shown twice that {number}! = {fact} (with exitement)")



