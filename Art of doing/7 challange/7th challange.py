#introducing different list that contains different type of data type

print("\t\t\t\t\t Summary Table")

#first list that contain string type of data
List_s =['15','100','55','42']
print(f"\nThe variable List_s is a {type(List_s)}")
print(f"It contains the elemesnts: {List_s}")
#check data type of first element in the list
print(f"The element {List_s[0]} is a {type(List_s[0])}")


#second list that contain int type of data
List_i =[15,100,55,42]
print(f"\nThe variable List_i is a {type(List_i)} ")
print(f"It contains the elements: {List_i}")
#check data type of first element
print(f"The element {List_i[0]} is a {type(List_i[0])}")

#third list that contain float type of data
List_f =[15.0,100.0,55.0,42.0]
print(f"\nThe variable List_f is a {type(List_f)} ")
print(f"It contains the elements: {List_f}")
#check data type of first element
print(f"The element {List_f[0]} is a {type(List_f[0])}")

#fourth list that contain lists inside the list
List_l =[[1,2,3],[4,5,6],[7,8,9]]
print(f"\nThe variable List_l is a {type(List_l)} ")
print(f"It contains the elements: {List_l}")
#check data type of first element
print(f"The element {List_l[0]} is a {type(List_l[0])}")

print("\nNow sorting List_s and List_i")
#sort the List_s and List_i resp.
List_i.sort()
List_s.sort()
print(f"Sorted List_s: {List_s}")
print(f"Sorted List_i: {List_i}")

print("\nString are sorted alphabetically while integers are sorted numerically!")
