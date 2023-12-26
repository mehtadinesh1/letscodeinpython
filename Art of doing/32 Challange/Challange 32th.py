#The Python Calculator App
print("Welcome to the Python Calculator App")
#addition
def addition(x,y):
    s = x + y
    print(f"The sum of {x} and {y} is {s}")
    return f'{x} + {y} = {s}'
def substraction(x,y):
    s = x - y
    print(f"The difference of {x} and {y} is {s}")
    return f'{x} - {y} = {s}'
def multiplication(x,y):
    s = x * y
    print(f"The product of {x} and {y} is {s}")
    return f'{x} * {y} = {s}'
def division(x,y):
    if y == 0:
        print("Divisioin Error")
        return "Div Error"
    else:
        s = x / y
        return f'{x} / {y} = {s}'
        print(f"The quotient of {x} and {y} is {s}")
#operation_input function
def operation_input():
    operation_list = ['Addition','Substraction','Multiplication','Division']
    operation = input("Enter an operation (Addition,Substraction,Multiplication,Division): ").title()
    if operation in operation_list:
        return operation
#main calculation fuction
def calculation(x,y):
    operation = operation_input()
    result = 0
    if operation == 'Addition':
        result = addition(x,y)
    elif operation == 'Substraction':
        result = substraction(x,y)
    elif operation == 'Multiplication':
        result = multiplication(x,y)
    elif operation:
        print("Invalid operation option")
        result = 'Opp Error'
    return result
#ask for run again
def calculation_again():
    user_choice = input("Would you like to run the program agian (y/n): ").lower()
    if user_choice == "y":
        return True
    else:
        return False
#display summary function
def calulation_summary():
    print("\nCalulation Summary:")
    for operations in summary_list:
        print(operations)

#start calculation operations
summary_list = []
choice = True
while choice:
    print("Enter two numbers and an operation and the desired operation will be performed. ")
    number1 = float(input("\nEnter a number:"))
    number2 = float(input("\nEnter a number:"))
    expression_result = calculation(number1,number2)
    summary_list.append(expression_result)
    choice = calculation_again()
#display summary of all calculations
calulation_summary()
print("\nThank you for using The Python Calculator App.")
