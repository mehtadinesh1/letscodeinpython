#Welcome to the Code Breaker App
from collections import Counter
print("Welcome to the Code Breakers App")

phrase_1 ='''To Sherlock Holmes she is always the woman. I have seldom heard him mention her under any
other name.
In his eyes she eclipses and predominates the whole of her sex. It was not that he felt any
emotion akin to love for Irene Adler.
All emotions, and that one particularly, were abhorrent to his cold, precise but admirably
balanced mind.
He was, I take it, the most perfect reasoning and observing machine that the world has seen,
but as a lover he would have placed himself in a false position.
He never spoke of the softer passions, save with a gibe and a sneer.
They were admirable things for the observer excellent for drawing the veil from men's motives
and actions.
But for the trained reasoner to admit such intrusions into his own delicate and finely adjusted
temperament was to introduce
a distracting factor which might throw a doubt upon all his mental results.
Grit in a sensitive instrument, or a crack in one of his own highpower lenses,
would not be more disturbing than a strong emotion in a nature such as his.
And yet there was but one woman to him, and that woman was the late Irene Adler, of dubious
and questionable memory.
I had seen little of Holmes lately. My marriage had drifted us away from each other.
My own complete happiness, and the homecentred interests which rise up around the man who
first finds himself master of his own establishment,
were sufficient to absorb all my attention, while Holmes, who loathed every form of society with
his whole Bohemian soul,
remained in our lodgings in Baker Street, buried among his old books, and alternating from
week to week between cocaine and ambition,
the drowsiness of the drug, and the fierce energy of his own keen nature.
He was still, as ever, deeply attracted by the study of crime, and occupied his immense faculties and extraordinary powers of observation in following out
those clues,
and clearing up those mysteries which had been abandoned as hopeless by the official police.
From time to time I heard some vague account of his doings: of his summons to Odessa in the
case of the Trepoff murder,
of his clearing up of the singular tragedy of the Atkinson brothers at Trincomalee,
and finally of the mission which he had accomplished so delicately and successfully for the
reigning family of Holland.
Beyond these signs of his activity, however, which I merely shared with all the readers of the
daily press, I knew little of my former friend and companion
'''
phrase_1 = phrase_1.lower()
updated_phrase_1 = ''.join(e for e in phrase_1 if e.isalpha())
#count letter occurence in phrase 1
letter_counter_phrase1 = Counter(updated_phrase_1)
#show frequency analysis chart of phrase 1
print("\nHere is the frequency analysis from key phrase 1:")
print(f"\nLetter\t\t\t\ttOccurence\t\t\t\tPercentage")
for key,value in sorted(letter_counter_phrase1.items()):
    percentage = value/len(phrase_1)*100
    percentage=round(percentage,2)
    print(f"{key}\t\t\t\t\t\t{value}\t\t\t\t\t\t{percentage}%")
#sort the letters ordered from highest occurence to lowest:
ordered_letter_phrase1 = []
print("\nLetters ordered from highest occurrence to lowest:")
for key,vlaues in  sorted(letter_counter_phrase1.items(),key=lambda x:x[1],reverse=True):
    ordered_letter_phrase1.append(key)
    print(key,end='')

phrase_2 = '''Quite so! You have not observed. And yet you have seen.
That is just my point. Now, I know that there are seventeen steps, because I have both seen
and observed.
By the way, since you are interested in these little problems,
and since you are good enough to chronicle one or two of my trifling experiences, you may be
interested in this.
He threw over a sheet of thick, pink tinted notepaper which had been lying open upon the table.
It came by the last post, said he. Read it aloud.
The note was undated, and without either signature or address.
There will call upon you tonight, at a quarter to eight o'clock,
it said, "a gentleman who desires to consult you upon a matter of the very deepest moment.
Your recent services to one of the royal houses of Europe have shown that you are one who
may safely be trusted
with matters which are of an importance which can hardly be exaggerated.
This account of you we have from all quarters received.
Be in your chamber then at that hour, and do not take it amiss if your visitor wear a mask.
This is indeed a mystery, I remarked. What do you imagine that it means?
I have no data yet. It is a capital mistake to theorise before one has data.
Insensibly one begins to twist facts to suit theories, instead of theories to suit facts.
But the note itself. What do you deduce from it?
I carefully examined the writing, and the paper upon which it was written.
The man who wrote it was presumably well to do, I remarked, endeavouring to imitate my
companion's processes.
Such paper could not be bought under half a crown a packet.
It is peculiarly strong and stiff
'''
phrase_2 = phrase_2.lower()
updated_phrase_2 = ''.join(e for e in phrase_2 if e.isalpha())
#count letter occurence in phrase 1
letter_counter_phrase2 = Counter(updated_phrase_2)
#show frequency analysis chart of phrase 1
print("\nHere is the frequency analysis from key phrase 1:")
print(f"\nLetter\t\t\t\ttOccurence\t\t\t\tPercentage")
for key,value in sorted(letter_counter_phrase2.items()):
    percentage = value/len(phrase_2)*100
    percentage=round(percentage,2)
    print(f"{key}\t\t\t\t\t\t{value}\t\t\t\t\t\t{percentage}%")
#sort the letters ordered from highest occurence to lowest:
ordered_letter_phrase2 = []
print("\nLetters ordered from highest occurrence to lowest:")
for key,vlaues in  sorted(letter_counter_phrase2.items(),key=lambda x:x[1],reverse=True):
    ordered_letter_phrase2.append(key)
    print(key,end='')

#ask user for encode and decode
choice = input("\nWould you like to encode or decode a message:").lower()
phrase = input("What is the phrase:").lower()
#remove all non_alph char
updated_phrase = ''.join(e for e in phrase if e.isalpha())
#show converted message
if choice == 'encode':
    print("\nThe encoded message is:")
    for letter in updated_phrase:
        #fetch letter by using both phrases ordered list
        fetch_index = ordered_letter_phrase2.index(letter)
        fetch_letter = ordered_letter_phrase1[fetch_index]
        print(''.join(fetch_letter),end="")

elif choice == 'decode':
    print("The decoded message is:",)
    for letter in updated_phrase:
        fetch_index = ordered_letter_phrase1.index(letter)
        fetch_letter = ordered_letter_phrase2[fetch_index]
        print(''.join(fetch_letter),end='')
else:
    print("\nEnter valid option only!")
