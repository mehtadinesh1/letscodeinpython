#Loan Calculator App
print("Welcome to the Loan Calculator App")
def display_information(info_dict,mon):
    print(f"----Loan information after {mon} months------")
    for item,value in info_dict.items():
        print(f"{item} : {value}")

def loan_calculation(info_dict,mon):
    interest_payment = ((interest_rate / 100) / 12) * info_dict["Principal"]
    if info_dict["Principal"] < 250 :
        last_payment = info_dict["Principal"]
        info_dict["Money Paid"] += last_payment
        info_dict['Principal'] = 0
    else:
        info_dict["Principal"] = info_dict.get("Principal") + interest_payment - monthly_payment
        info_dict['Money Paid'] += monthly_payment
    mon +=1
    return info_dict,mon
def summary(info_dic,mon):
    print(f"\nCongratulation! You paid off your loan in {mon} month!")
    print(f"Your initial loan was ${amount} at a rate of {interest_rate}%.")
    print(f"Your monthly payment was ${monthly_payment}.")
    print(f"You spent ${info_dic['Money Paid']} in total.")
    print(f"You spent ${info_dic['Money Paid']-amount} on interest!")

information = {}
month = 0
amount = float(input("\nEnter the loan amount: "))
interest_rate = float(input("Enter the interest rate: "))
monthly_payment = float(input("Enter the desired monthly payment amount: "))
information["Principal"] = amount
information["Rate"] = interest_rate/100
information["Monthly Payment"] = monthly_payment
information["Money Paid"] = 0
display_information(information,month)
input("Press 'Enter' to begin paying off your loan")
while True:
    information, month = loan_calculation(information,month)
    display_information(information,month)
    if information["Principal"] > amount:
        print("\nYou will never pay off your loan!!!!")
        print("You cannot get ahead of the interest! :-(")
        break;
    if information["Principal"] <= 0:
        summary(information,month)
        break;
    else:
        pass


