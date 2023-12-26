# MPH to MPS conversion app

print("welcome to the MPH to MPS conversion app")
#get user input
Value1 = float(input("\nWhats you speed in miles per hour:"))

#convert the MPH to MPS by dividing 2.237
Value2 = (Value1/2.237)
#round the vlaue to keep 2 no. after the dot
Original = round(Value2,2)

#display the result
print(f'Your speed in meter per second is {Original}')