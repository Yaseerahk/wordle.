import random

print("Welcome to the wordle game")
print("How to play:")
print("You have 5 chances to guess the 5 letter word.Y represents the correct letter in the incorrect place,G represents Correct letter in the correct place. _represent an empty space and the incorrect letter and place ")

with open("5 letter word dictionary.txt", 'r') as dictionary:
    
    dictionary = dictionary.read().split('\n') 
word = random.choice(dictionary)
dif_letters = list(set(word))

count_letters = {}
for i in dif_letters:
    count_letters[i] = word.count(i)

tries = 0

while True:
    
    if tries == 5:
        print(f"You did not guess the word!\nThe word was {word}")
        break
    
    user_inp = input(">>").lower()

    if user_inp == "q":
        break

    if not len(user_inp) == 5:
        print("Your input must be 5 letters long")
        continue

    if not user_inp in dictionary:
        print("Your word is not in the dictionary")
        continue

    if user_inp == word:
        print(f"You guessed the word in {tries} tries")
        break

    
    letter = 0
    letter_dict = {}
    letters_checked = []
    return_answer = "  "
    for i in word:
       
        counter = 0
        cont = False
        for g in letters_checked:
            if g == user_inp[letter]:
                counter += 1
               
                if counter >= count_letters[i]:
                    cont = True

        if cont:
            return_answer += "_"
            letters_checked.append(user_inp[letter])
            letter += 1
            continue


        answer_given = False
        do_not_add = False
     
        if user_inp[letter] in word:
            answer_given = True
         
            if user_inp[letter] == i:
                return_answer += "G"
            else:
                if not user_inp[word.index(user_inp[letter])] == word[word.index(user_inp[letter])]:
                    return_answer += "Y"
                else:
                    answer_given = False
                    do_not_add = True

 
        if not answer_given:
            return_answer += "-"

        if not do_not_add:
           letters_checked.append(user_inp[letter])

        letter += 1

    print(return_answer)

    tries += 1