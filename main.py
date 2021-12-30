import random
import string
from words import words
from visual import handman_visual as hv

#We will select a correct word
def correct_word():
    word = random.choice(words)
    while ' ' in word or '-' in word:
        word = random.choice(words)

    return word.upper()

#Let's start the game
def hangman():
    word = correct_word()
    seted_word = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    game = True
    live = 6

    while game:
        choice_letter = input('Guess a letter: ').upper()

        used_letters.add(choice_letter)

        # hide_letters = [letter if letter in used_letters else '-' for letter in word]
        hide_letters = []

        for letter in word:
            if letter in used_letters:
                hide_letters.append(letter)
            else:
                hide_letters.append('-')

        # We the used letters and the letter that you already discove
        print('Letter already used\n ' + ','.join(used_letters))
        print('How your guesses are doing: ' + ''.join(hide_letters))

        # We check if the game is done
        if '-' not in hide_letters:
            print("We have a winner!!")

            restart = input('\nWould you like play again:\nY for yes\nN for now\n').upper()

            if restart == 'Y':
                live = 6
                word = correct_word()
                used_letters = set()
            else:
                game = False

        else:
            if choice_letter not in word:
                live = live - 1
                print(f'Opportunity left: {live}')

                if live == 0:
                    print(hv[live])
                    print("\nOhhhh!! You lost!!\nDon't cry please")
                    print('The word that you DIDN\'T guess was', word)

                    restart = input('\nWould you like play again:\nY for yes\nN for now\n').upper()

                    if restart == 'Y':
                        live = 6
                        word = correct_word()
                        used_letters = set()
                    else:
                        game = False

                else:
                    pass
        print(hv[live])


hangman()