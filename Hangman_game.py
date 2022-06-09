import random
import Hangman_logo as hl
import Hangman_stages as hs
import Word_list as wl

print(hl.hangmanSymbol)

life = 6



stt = ' '
chosen_word = (random.choice(wl.word_list))
needed_word = list(chosen_word)

lis = ['_' for i in range(len(chosen_word))]
while life:
    print("                         ", stt.join(lis))
    print()
    user_letter_guess = input("Guess a letter: ").lower()
    map = 0
    for i in range(len(needed_word)):
        if needed_word[i] == user_letter_guess:
            lis[i] = user_letter_guess
            needed_word[i]= '_'
            map = 1
            break
    if map == 0:
        life -= 1
        print(hs.stages[life])
    st = ''
    if st.join(lis) == st.join(chosen_word):
        print(chosen_word)
        print("You Won!")
        exit()        

print("Game Over!")        