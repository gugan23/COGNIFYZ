import random

def guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False

    print("Guessing Game")
    print("-------------")
    print('')
    print("I have generated a number between 1 and 100. Try to guess it!")

    while not guessed:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            if user_guess < number_to_guess:
                print("Too low ⚠️")
            elif user_guess > number_to_guess:
                print("Too high ⚠️")
            else:
                guessed = True
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    guessing_game()
