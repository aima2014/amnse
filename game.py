import random
lower_bound = 1
upper_bound = 10
max_attempts=  12
secret_number = random.randint(lower_bound, upper_bound)







def get_guess():
    while True:
        guess = int(input("Enter your guess between 1 to 10:"))
        if lower_bound <= guess <= upper_bound:
            return guess
        else:
            print("Invalid input. Please enter a valid integer.")




def check_guess(guess, secret_number):
    if guess == secret_number:
        return "correct"
    elif guess < secret_number:
        return "too low"
    else:
        return "too high"
    

    
def play_game():
    attempts = 0
    won = False

    while attempts <  max_attempts:
        attempts += 1
        guess = get_guess()
        result = check_guess(guess, secret_number)
        if result == "correct":
            print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
            won = True
            break
        else:
            print(f"{result}. Try again.")
            if not won:
                print(f"Sorry, you  have used all  attempts. The secret number was {secret_number}.")

if __name__ == "__main__":
    print("Welcome to the Number Guessing Game!")
    play_game()


