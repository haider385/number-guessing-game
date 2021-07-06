from random import randint


def initialize(highscore=None):
    num_guesses = 0
    current_guess = 0
    number = randint(1, 10)
    print("""\n\nHello!\nWelcome to the Number guessing game.
I'm thinking of a number between 1 and 10. Can you guess it?
    """)
    if not highscore:
        highscore = 0
    else:
        print("Your current high score is {} attempts".format(highscore))
    return current_guess, number, num_guesses, highscore


def game(current_guess, number, num_guesses, highscore):
    while current_guess != number:
        try:
            current_guess = int(input("Guess number {}: ".format(
                num_guesses + 1
                )))
        except:
            print("Please enter an integer!\n")
            continue
        else:
            if current_guess not in range(1, 11):
                print("Please guess a number between 1 and 10!\n")
                continue
            num_guesses += 1

        if current_guess > number:
            print("The number is lower than {}, try again!\n".format(
                current_guess))
        elif current_guess < number:
            print("The number is higher than {}, try again!\n".format(
                current_guess))
        else:
            print("""\nCongratulations! The number was {}.
It took you {} attempts to get it right.""".format(
                 number, num_guesses))
            if highscore:
                if num_guesses < highscore:
                    highscore = num_guesses
            else:
                highscore = num_guesses
    return highscore


def main():
    playing = True
    highscore = None
    while playing:
        current_guess, number, num_guesses, highscore = initialize(highscore)
        highscore = game(current_guess, number, num_guesses, highscore)
        try:
            decision = input(
                "Enter 'Y' if you would like to play again.\n").lower()
        except:
            playing = False

        if decision != 'y':
            print("Thank you for playing, Goodbye!")
            break

main()
