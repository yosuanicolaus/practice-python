""" HANGMAN
When you run hangman.py, the output will look like this:

Hangman, by Al Sweigart al@inventwithpython.com

 +--+
 |  |
    |
    |
    |
    |
=====
The category is: Animals

Missed letters: No missed letters yet.

_ _ _ _ _
Guess a letter.
> e
--snip--
 +--+
 |  |
 O  |
/|  |
    |
    |
=====
The category is: Animals

Missed letters: A I S
O T T E _
Guess a letter.
> r
Yes! The secret word is: OTTER
You have won! """

import random
import string

HANGMAN_PICS = [r"""
 +--+
 |  |
    |
    |
    |
    |
=====""",
                r"""
 +--+
 |  |
 O  |
    |
    |
    |
=====""",
                r"""
 +--+
 |  |
 O  |
 |  |
    |
    |
=====""",
                r"""
 +--+
 |  |
 O  |
/|  |
    |
    |
=====""",
                r"""
 +--+
 |  |
 O  |
/|\ |
    |
    |
=====""",
                r"""
 +--+
 |  |
 O  |
/|\ |
/   |
    |
=====""",
                r"""
 +--+
 |  |
 O  |
/|\ |
/ \ |
    |
====="""]
HANGMAN_PICS.reverse()
CATEGORY = 'Animals'
WORDS = 'ANT BABOON BADGER BAT BEAR BEAVER CAMEL CAT CLAM COBRA COUGAR COYOTE CROW DEER DOG DONKEY DUCK EAGLE FERRET FOX FROG GOAT GOOSE HAWK LION LIZARD LLAMA MOLE MONKEY MOOSE MOUSE MULE NEWT OTTER OWL PANDA PARROT PIGEON PYTHON RABBIT RAM RAT RAVEN RHINO SALMON SEAL SHARK SHEEP SKUNK SLOTH SNAKE SPIDER STORK SWAN TIGER TOAD TROUT TURKEY TURTLE WEASEL WHALE WOLF WOMBAT ZEBRA'.split()


def main():
    print('Hangman, by Yosua Nicolaus, Mar 26 2022')

    life = 6
    guess_word = random.choice(WORDS)
    guess = ''
    iter_ans = [ch for ch in guess_word]
    iter_guess = ['_' for ch in guess_word]
    missed = []

    while iter_guess != iter_ans:
        # draw_hangman(life)
        print(HANGMAN_PICS[life])
        print('Category:', CATEGORY, '\n')

        print('Missed:', ' '.join(missed), '\n')

        print(' '.join(iter_guess))

        while True:
            guess = input('Enter Guess Letter: ').upper()
            if len(guess) != 1:
                print('guess should have 1 length!')
            elif guess not in string.ascii_uppercase:
                print('guess has to be a letter!')
            elif guess in missed:
                print('you guessed this letter before!')
            else:
                break

        for i, ch in enumerate(iter_ans):
            if guess == ch:
                iter_guess[i] = ch

        if guess not in iter_ans:
            missed.append(guess)
            life -= 1
        
        if life == 0:
            print('Oops! You lost. The answer was', guess_word)
            return

    print('Congratulation! You guessed it!')
    print('The answer was', guess_word)
    print('remaining life:', life)
        

main()
