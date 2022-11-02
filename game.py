import random

# Put your code here

def guessing_game():
    """A number-guessing game."""

    tries = 1
    game_over = False

    print('Welcome to the game')
    player_name = input("What is your name? ")
    print(f'{player_name}, you are thinking of a number within a range')
    print('Try to guess the number.')

    starting_range = int(input('What would you like the starting number to be? '))
    ending_range = int(input('What would you like the ending number to be? '))

    guess = random.randint(starting_range, ending_range+1)

    while not game_over:

        player_guess = int(input('Your guess? '))

        if player_guess < starting_range or player_guess > ending_range:
            print('Your guess is out of range! Try again.')
        elif player_guess == guess:
            print(f'Well done, {player_name}! You found the number in {tries} tries!')
            end_game = input("Would you like to play again? Type Y or N. ")
            if end_game == 'Y':
                guessing_game()
            else:
                game_over = True
                print("Game Over. ")
        elif player_guess < guess:
            tries += 1
            print('Your guess is too low, try again.')
        elif player_guess > guess:
            tries += 1
            print('Your guess is too high, try again.')
    
    
guessing_game() 
