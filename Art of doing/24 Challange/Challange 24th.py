#Welcome to the Frequency Analysis App
print("Welcome to the frequency Analysis App")
#create dictionary that contain letter, occurence and percentage in future
frequency_db = {}
#use for loop to ask user to enter as many time the phrases and get the resp. analysis
for l in range(2):
    # ask user for phrase
    phrase = input("\nEnter a word or phrase to count the occurrence of each letter: ").lower()
    #remove non-alphabetic character form phrase
    update_phrase= ''.join(i for i in phrase if i.isalpha())
    for i in update_phrase:
        if i not in frequency_db:
            #add letter and corressponding to its no_appearence and percentage in dictionary
            no_of_occurence = update_phrase.count(i)
            percentage_of_letter = no_of_occurence/len(update_phrase) * 100
            frequency_db[i] = [no_of_occurence,round(percentage_of_letter,2)]
    #display frequency analysis chart
    print(f"\nHere is the frequency analysis from key phrase {l+1}")
    print("\nLetter\t\t\t\tOccurrence\t\t\t\tPercentage")
    for key,value in sorted(frequency_db.items()):
        print(f"{key}\t\t\t\t\t\t{value[0]}\t\t\t\t\t\t{value[1]}%")

    #sort the letters ordered from highest occurence to lowest:
    print("\nLetters ordered from highest occurrence to lowest:")
    for key,vlaues in  sorted(frequency_db.items(),key=lambda x:x[1],reverse=True):
        print(key,end='')
    print("\n")


