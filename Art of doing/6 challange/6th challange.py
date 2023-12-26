#Welcome to the Grade Sorter App

print("Welcome to the Grade Sorter App")

First_g = int(input("What is your first grade (0-100):\t"))
Second_g = int(input("What is your first grade (0-100):\t"))
Third_g = int(input("What is your first grade (0-100:\t"))
Fourth_g = int(input("What is your first grade (0-100:\t"))

#create list and put all grades in that list
Grade_List = [First_g,Second_g,Third_g,Fourth_g]

print("Your grades are:",Grade_List)
#sort the grade list and then revrse the list to see grades higher to lower
Grade_List.sort()
Grade_List.reverse()
#display sorted grade list in descending
print("Your grades from highest to lowest are:",Grade_List)
print("\nThe lowest two grades will now be dropped.")
#remove last two lowest grade by pop funtion
print(f"Removed grade: {Grade_List.pop()}")
print(f"Removed grade: {Grade_List.pop()}")

# show remainging list
print("Your remaining grades are:",Grade_List)
#display highest grades in list
print(f"Nice work! Your highest grade is a {Grade_List[0]}")

