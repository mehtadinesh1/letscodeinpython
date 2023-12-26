#Favorite Teacher Program
print("Welcome to the Favorite Teachers Program")
#get favorite teachers list from user
fav1_teacher = input("\n Who is your frist favorite teacher: ").title()
fav2_teacher = input("Who is your second favorite teacher: ").title()
fav3_teacher = input("Who is your third favorite teacher: ").title()
fav4_teacher = input("Who is your fourth favorite teacher: ").title()
teacher_list=[fav1_teacher,fav2_teacher,fav3_teacher,fav4_teacher]

#display teacher list and sort in alpha. and reverse alph. the list
print(f"\nYour favorite teachers ranked are:\t {teacher_list}")
print(f"Your favorite teachers alphabetically are:\t {sorted(teacher_list)}")
print(f"Your favorite teachers in reverse alphabetically order are:\t {sorted(teacher_list,reverse=True)}")

#display teacher name according ranking
print(f"\nYour top two teachers are: {teacher_list[0]} and {teacher_list[1]}")
print(f"Your next two favorite teachers are: {teacher_list[2]} and {teacher_list[3]}")
print(f"your last favorite teacher is: {teacher_list[-1]}")
print(f"You have a total of {len(teacher_list)} favorite teachers.")
#change first rank teacher name and add new teacher name at first rank
add_new_teacher=input(f"\nOops, {teacher_list[0]} is no longer your first favorite teacher. Who is your new Favorite teacher: ")
teacher_list.insert(0,add_new_teacher)

#display teacher list and sort in alpha. and reverse alph. the list
print(f"\nYour favorite teachers ranked are:\t {teacher_list}")
print(f"Your favorite teachers alphabetically are:\t {sorted(teacher_list)}")
print(f"Your favorite teachers in reverse alphabetically order are:\t {sorted(teacher_list,reverse=True)}")
#display teacher name according ranking
print(f"\nYour top two teachers are: {teacher_list[0]} and {teacher_list[1]}")
print(f"Your next two favorite teachers are: {teacher_list[2]} and {teacher_list[3]}")
print(f"your last favorite teacher is: {teacher_list[-1]}")
print(f"You have a total of {len(teacher_list)} favorite teachers.")

#alter the list by remove the teacher
remove_teacher =input(f"\nYou've decided you no longer like a teacher. Which teacher would you like to remove from the list: ").title()
teacher_list.remove(remove_teacher)

#display teacher list and sort in alpha. and reverse alph. the list
print(f"\nYour favorite teachers ranked are:\t {teacher_list}")
print(f"Your favorite teachers alphabetically are:\t {sorted(teacher_list)}")
print(f"Your favorite teachers in reverse alphabetically order are:\t {sorted(teacher_list,reverse=True)}")

#display teacher name according ranking
print(f"\nYour top two teachers are: {teacher_list[0]} and {teacher_list[1]}")
print(f"Your next two favorite teachers are: {teacher_list[2]} and {teacher_list[3]}")
print(f"your last favorite teacher is: {teacher_list[-1]}")
print(f"You have a total of {len(teacher_list)} favorite teachers.")