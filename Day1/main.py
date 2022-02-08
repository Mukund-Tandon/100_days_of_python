import random
import art
import word_list

lives=6
print(art.logo)
chosen_word= random.choice(word_list.word_list)
display=[]
for letter in chosen_word:
    display.append("_")
remaining_letters= len(chosen_word)
while remaining_letters >0:
    guess=input("Guess a letter: ")
    if guess in display:
        print("already chosen this letter")
    for i in range(len(chosen_word)):
        if chosen_word[i]==guess:
            display[i]=guess
    print(display)
    remaining_letters= display.count("_")
    
    if guess not in chosen_word:
        lives-=1
        if lives==0:
            print(art.stages[lives])
            print("You loose")
            break
    if "_" not in display:
        print("You win")
    
    print(art.stages[lives])




