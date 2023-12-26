#Quadratic Solver App
print("Welcome to the Quadratic Solver App.")
#define the format and rule of Quadratic Equation
print("\nA quadratic equation is of the form ax^2 + bx + c = 0")
print("Your solutions can be real or complex numbers.")
print("A complex number has two parts: a + bj")
print("Where a is the real portion and bj is the imaginary portion.")

#ask user how many equation you wanna solve
equation_no = int(input("\n How many equation would you like to solve today: "))

#equation solving process
for i in range(1,equation_no+1):
    print(f"\nSolving equation #{i}")
    print("---------------------------------------------")
    #ask for respective coefficient values form the user
    a=float(input("\nPlease enter your value of a (cofficient of x^2): "))
    b=float(input("Please enter your value of b (cofficient of x): "))
    c=float(input("Please enter your value of c (coefficient): "))
    discrimination= b**2 - 4*a*c
    x1= -b/2*a + (discrimination**(1/2))/2*a
    x2= -b/2*a - (discrimination**(1/2))/2*a
    print(f"\nThe solutions to {a}x^2 + {b}x + {c} are:")
    #display resp. solution
    print(f"\nx1 = ({x1})")
    print(f"x2 = ({complex(x2)}")
    print("\n")

print("\nThank you for using the Quadratic Solver App. Goodbye.")
