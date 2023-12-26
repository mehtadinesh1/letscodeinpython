#Fibonacci Calculator App.
#get user desire no.
number=int(input("How many fabonacci number you want: "))
#compute fibonacci series
fib=[1,1]
for i in range(number-2):
    new_fib = fib[i]+ fib[i+1]
    fib.append(new_fib)
#display fabonacci series
print(f"\nThe first {number} numbers of the Fibonacci sequence are:")
for i in fib:
    print(i)
#compute golden raio
ratio=[]
for i in range(number-1):
    new_ratio=fib[i+1]/fib[i]
    ratio.append(new_ratio)
#display ration
print("\nThe corresponding Golden Ratio values are:")
for i in ratio:
    print(i)
print(f"\nThe ratio of consecutive Fibonacci terms approaches Phi: 1.618...")
