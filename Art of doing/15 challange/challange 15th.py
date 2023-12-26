#Average calculator App
import math
print("Welcome to the Average Calculator App")
#get user name and enter no. of grades wanna calculate
name=input("\nWhat is your name:").title()
total_grades= int(input("How many grades would you like to enter: "))
grade_list=[]
for i in range(total_grades):
    grade=int(input("Enter grade:"))
    grade_list.append(grade)
#sort the grade list from hight to low
grade_list.sort(reverse=True)
print("\nGrade Highest to lowest:")
for i in grade_list:
    print(f"\t\t\t{i}")
#summary
print(f"{name}'s Grade Summary:")
print(f"\n\t\t\tTotal no. of grades {len(grade_list)}")
print(f"\t\t\tHighest Grade: {max(grade_list)}")
print(f"\t\t\tLowest Grade: {min(grade_list)}")
list_sum =sum(grade_list)
avg=float(list_sum/len(grade_list))
print(f"\t\t\tAverage: {round(avg,2)}")
#find next assignment grade to achive desire avg
des_avg=float(input("\nWhat is you desired average:"))
next_assignment_grade = float(des_avg*(len(grade_list)+1)-list_sum)
print(f"\nGood luck {name}")
print(f"You will need to get a {round(next_assignment_grade,2)} your next assignment to earn a {des_avg} average.")

#change one grade vlaue and check difference
des_grade_list=grade_list.copy()
print("\nLets see what your average could have been if you did better/worse on an assignment.")
ch_grade= int(input("What grade would you like to change: "))
des_grade_list.remove(ch_grade)
new_grade=int(input(f"What grade would you like to change {ch_grade} to: "))
des_grade_list.append(new_grade)
des_grade_list.sort(reverse=True)
print(f"\nNew Grades Highest to lowest:")
for i in des_grade_list:
    print(i)
#summary
print(f"\n{name}'s New Grade Summary:")
print(f"\t\t\tTotal Number of Grades: {len(des_grade_list)}")
print(f"\t\t\tHighest Grade: {max(des_grade_list)}")
print(f"\t\t\tLowest Grade: {min(des_grade_list)}")
list2_sum = sum(des_grade_list)
new_avg=float(list2_sum/len(des_grade_list))
print(f"Average: {round(new_avg)}")

#average difference
print(f"\nYour new average would be {new_avg} compared to your real average of {avg}!")
print(f"That is a change of {round(new_avg-avg,2)} points!")

#conclusion
print(f"\nToo bad your original grades are still!")
print(f"{grade_list}")
print("You should go ask for extra credit!")


