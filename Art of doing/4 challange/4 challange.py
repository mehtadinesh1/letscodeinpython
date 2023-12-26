#Welcome to the Ringh Triangle Solver app
print("Welcome to the Right Triangle solver app")

#get first and second leg vlaue from user
first_leg = float(input("What is the first leg of the Triangle:"))
second_leg = float(input("What is the second leg of the Triangle:"))

#formula of get the value of hypotenuse

hypotenuse = ((first_leg**2) + (second_leg**2))**(1/2)
#formula of calculate the area
area = (first_leg*second_leg)/2

#display the result
print(f"For a triangle with legs of {first_leg} and {second_leg} the hypotenuse is {hypotenuse}.")
print(f"For a triangle with legs of {first_leg} and {second_leg}) the area is {area}.")



