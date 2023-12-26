#Guess My Word App
import random
print("Welcome to the Guess My Word App ")
#intoduction
#create dictionaries that contian different types of categories
categories = {'Sports' :['football','vollyball','cricket','tenis','rugby','soccer'],
              'Fruits':['manggo','apple','lichy','strawberry','banana','gauva'],
              'Animals':['bear','lion','tiger','snake','monkey','deer','hind','horse']}
#fetch all categories in list
categories_list = list(categories.keys())
while True:
  #fetch random categories and form that categories fetch random word
  random_category = random.choice(categories_list)
  random_word = random.choice(categories.get(random_category))
  print(f"\nGuess a {len(random_word)} letter word from the following category: {random_category}")
  dash_pattern = []
  for i in range(len(random_word)):
      print('_',end="")
      dash_pattern.append('_')
  #guessing process
  guess = 0
  while True:
      guess_word = input("\nEnter your guess:").lower()
      if guess_word == random_word:
          guess += 1
          print(f"\nCorrect! You guessed the word in {guess} guesses.")
          break;
      else:
          guess += 1
          print("That is not correct. Let us reveal a letter to help you!")
          while True:
              random_letter_index = random.randint(0,len(random_word)-1)
              if dash_pattern[random_letter_index] == '_':
                  dash_pattern[random_letter_index] = random_word[random_letter_index]
                  for i in dash_pattern:
                      print(i, end='')
                  break;

          '''dash_pattern_list = list(dash_pattern)
          #fetch random letter
          random_word_letter = random.choice(random_word)
          #fetch index value
          random_word_letter_index = random_word.index(random_word_letter)
          if random_word_letter not in dash_pattern_list or dash_pattern[random_word_letter_index].isalpha():
              #replace dash in dash_pattern with ranodom letter
              dash_pattern_list[random_word_letter_index]=random_word_letter
              #reconstruct the string dash_pattern again
              dash_pattern = ''.join(dash_pattern_list)
              print(dash_pattern)'''

  #ask for play again
  interest = input("Would you like to play again (y/n): ").lower()
  if interest == "n":
      print("Thank you for using our service.....")
      exit()



