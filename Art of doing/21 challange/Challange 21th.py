#Thesaurus App
import random
print("Welcome to the Thesaurus!")
#introduction
print("\nChoose a word from the thesaurus and I will give you a synonym.")
#describe worlds of thesaurus app and their respective synonym
word_dict = {"hot":['spicy','boiling','sharp'], 'cold':['chilly','cool','icy'], 'happy':['merry','joyfull','lucky'], 'sad':['unhappy','regretful','sorrowful']}
#feth the keys  form dictionary
word_list = word_dict.keys()
for i in word_list:
    print("-",i)
#choose word
pick_word=input("\nWhat word would you like a aynonym for:").lower()
#show one synonym of respective word
if pick_word in word_list:
    #fetch values from respective key 
    list=word_dict.get(pick_word)
    print(f"A synonym for {pick_word} is {random.choice(list)}.")
else:
    print("Choose only in available words.")
#ask user to see whole Thesaurus
user_request = input("\nWould you like to see the whole thesaursu (yes/no):").lower()
#display the whole thesaurus
if user_request == "yes":
    for i in word_list:
        print(f"\n{i} synonyms are")
        list= word_dict.get(i)
        for i in list:
            print("-",i)
#display thank you message
else:
    print("\nI hope you enjoyed the program. Thank you!")

'''if pick_word == "hot":
    hot_list = word_dict.get("hot")
    print(f"A synonym for {pick_word} is {random.choice(hot_list)}")
elif pick_word == "cold":
    cold_list = word_dict.get("cold")
    print(f"A eynonym for {pick_word} is {random.choice(cold_list)}")
elif pick_word == "happy":
    happy_'''

