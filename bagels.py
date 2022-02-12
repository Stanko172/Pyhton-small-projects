#Bagels is a deductive logic game where you must guess a number based on clues

import random 

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    print('''
    I am thinking of a {}-digit number with no repeated digits.
    Try to guess what it is. Here are some clues:
    When I say:    That means:
    Pico         One digit is correct but in the wrong position.
    Fermi        One digit is correct and in the right position.
        Bagels       No digit is correct.

    For example, if the secret number was 248 and your guess was 843, the
    clues would be Fermi Pico.'''.format(NUM_DIGITS))


    while True:
        secret_number = get_secret_number()
        print('I have thought up a number.')
        print(' You have {} guesses to get it.'.format(MAX_GUESSES))

        guesses_number = 1
        while guesses_number <= 10:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print("Guess #{}".format(guesses_number))
                guess = str(input("> ")) 
            
            #Check if guess is correct
            if(guess == secret_number):
                print("Yohoo! You got it right :D")
                break
            
            #If not show clues
            clues = get_clues(guess, secret_number)
            print(clues)

            guesses_number += 1

            #Check if user ran out of guesses
            if(guesses_number > MAX_GUESSES):
                print("You run out of guesses")
                print("The correct number was {}".format(secret_number))
        
        #Ask if user want's to play again
        print("Do you want to play again?(yes/no)")
        if not input('> ').lower().startswith('y'): break 

    print("Thanks for playing :)")


def get_secret_number():
    number_list = list('1234567890')
    random.shuffle(number_list)
    secret_number = "".join([number_list[i] for i in range(NUM_DIGITS)])
    return secret_number

def get_clues(guess, secret_number):
    #Loop through guess digits
    #Check if digits with the same index are equal both in guess and secret number
    #If not check if the digit is present if other indices
    clues = []
    for i in range(len(guess)):
        if guess[i] == secret_number[i]:
            clues.append('Fermi')
        elif guess[i] in secret_number:
            clues.append('Pico')
    #If clues array is empty than it's a bagel
    if(len(clues) == 0): clues.append('Bagel')
    else:
        #Sort clues alphabetically
        clues.sort()

    return ' '.join(clues)

if __name__ == "__main__":
    main()