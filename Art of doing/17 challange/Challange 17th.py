#Coin Toss App
import random
print("Welcome to the Coin Toss App")
#intro and ask user how many time you want flip the coin
print("\nI will flip a coin a set numberof times.")
flip_times=int(input("How many times would you lke me to flip the coin:"))
result=['Head','Tail']
result_list=[]
for i in range(flip_times):
    res=random.choice(result)
    result_list.append(res)
#ask user want result list or not
permission = input("Would you like ot see the result of each flip (y/n):").lower()
if permission == "y":
    for i in result_list:
        print(i)
else:
    print("You skip to the summary directly")

#Summary
print(f"\nResult of flipping A coin {flip_times} times is:")
print(f"\nSide\t\t\tCount\t\t\tPercentage")
no_heads=result_list.count('Head')
no_tails=result_list.count('Tail')
head_per=(no_heads/flip_times)*100
tail_per=(no_tails/flip_times)*100
print(f"\nHeads\t\t\t{no_heads}\t\t\t{round(head_per,2)}")
print(f"\nTails\t\t\t{no_tails}\t\t\t{round(tail_per,2)}")


'''
#second way of do it

#initialize two variable
head=0
tail=0
for i in range (no_of_times_flips)
   coin=random.randint(0,1)
   if coin== 1
     head +=1
     if permission == 'y'
       print(head)
   else:
     tail +=1
     if permission == 'y'
      print(tail)
   if head == tail
      print(f"{i+1} flipping we have same no of head and tails
   '''