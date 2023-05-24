# import random module
import random

def number_guesser():
    
    # initialize variables; total_guesses and games_played are initialized outside of the loop so that they can are not reset to 0 each time the user plays again
    total_guesses = 0
    games_played = 0

    while True:
        # generate random number between 1 and 1000
        random_number = random.randint(1, 1000)
        print("I'm thinking of a number between 1 and 1000. Can you guess what it is?")

        # initialize variables; attempts is initialized inside the loop so that it is reset to 0 each time the user plays again
        attempts = 0
                      
        # loop until user guesses correct number
        while True:
            user_input = input("Enter your guess (1-1000) or 'q' to quit: ")

            # check if user wants to quit
            if user_input.lower() == 'q':
                print("Thanks for playing!")
                # check if user played any games, if so, print games_played and average guesses per game
                if games_played > 0:
                    average_guesses = total_guesses / games_played
                    print("Games played:", games_played)
                    print("Average guesses per game:", average_guesses)
                return

            # validates if the input is a number that falls in the range of 1-1000, if not, prompt user to enter a valid number, adds 1 to attempts
            try:
                # int function converts user input to integer
                user_guess = int(user_input)
                if user_guess < 1 or user_guess > 1000:
                    # built-in exception class that is raised when a function receives an argument of the correct type but an inappropriate value
                    raise ValueError
            # if the user_input does not convert to an integer, or if the user_input is not between 1-1000, print error message, continue loop
            except ValueError:
                print("Invalid input. Please enter a valid guess between 1 and 1000.")
                continue
            attempts += 1

            # check if user guess is correct, sets adds attempts to total_guesses, adds 1 to games_played, breaks loop
            if user_guess == random_number:
                print("You guessed correctly!")
                print("It took you", attempts, "attempt(s) to guess the number.")
                total_guesses += attempts
                games_played += 1
                break
            # if user guess is too high or too low, prompts user to guess again
            elif user_guess > random_number:
                print("Your guess is too high. Try again.")
            # if user guess is too low, prompts user to guess again
            else:
                print("Your guess is too low. Try again.")

        # prompt user to play again, if yes, continue loop
        play_again = input("Would you like to play again? (y/n): ")
        if play_again.lower() == "y":
            continue
        # if no, check if user played any games, if so, print games_played and average guesses per game, break loop
        else:
            if games_played > 0:
                average_guesses = total_guesses / games_played
                print("Games played:", games_played)
                print("Average guesses per game:", average_guesses)
            break

# call function
number_guesser()