import random

def generate_random_number(min, max):
    """Generates a random number between min and max.

    Args:
        min (int): The minimum value of the random number.
        max (int): The maximum value of the random number.

    Returns:
        int: A randomly generated number within the specified range.
    """
    return random.randint(min, max)

def user_guess():
    """Prompts the user to guess a number.

    Returns:
        int: The number guessed by the user.
    """
    
    ran_num = int(input('Enter your guess: '))
    return ran_num

def check_guess(guess, answer):
    """Checks if the user's guess matches the generated number.

    Args:
        guess (int): The user's guessed number.
        answer (int): The correct number.

    Returns:
        bool: True if the guess is correct, False otherwise.
        str: A message indicating whether the guess was too high, too low, or correct.
    """
    if guess == answer:
        print("Just right! Congratulations!")
        return True
        
    else:
        if guess < answer:
            print("Too low!")
            return False
        else : 
            print("Too high!")
            return False

def play_game(min_number, max_number):
    """Controls the flow of the game, utilizing other functions."""

    print("Guess the number between 1 and 100.")
    
    answer = generate_random_number(min_number,max_number)
    
    guess = user_guess()
    
    check_num = check_guess(guess, answer)
    tracker = 1

    while check_num == False:
        guess = user_guess()
        check_num = check_guess(guess, answer)
        tracker +=1
    
    print(f'You guessed the number in {tracker} tries.')

    
    

    



# main program
if __name__ == "__main__":
    play_game(min_number=1, max_number=100)


# EXPECTED OUTPUT:
# Guess the number between 1 and 100.
# Enter your guess: 50
# Too high!
# Enter your guess: 25
# Too low!
# Enter your guess: 37
# Too high!
# Enter your guess: 31
# Too high!
# Enter your guess: 28
# Just right! Congratulations!
# You guessed the number in 5 tries.