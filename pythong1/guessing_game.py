import random

def number_guessing_game():
    number_to_guess = random.randint(1, 10)
    attempts = 0
    max_attempts = 3
    print("I'm thinking of a number between 1 and 10.")
    print(f"You have {max_attempts} attempts to guess the number.")

    while attempts < max_attempts:
        guess = int(input("Take a guess: "))
        attempts += 1
        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempt(s).")
            break

        if attempts == max_attempts:
            print(f"Game over! The correct number was {number_to_guess}.")
            break

if __name__ == "__main__":
    number_guessing_game()
