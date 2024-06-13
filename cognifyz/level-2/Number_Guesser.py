import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    
    
    lower_bound = int(input("Enter the lower bound of the range: "))
    upper_bound = int(input("Enter the upper bound of the range: "))
    
    
    secret_number = random.randint(lower_bound, upper_bound)
    
    print(f"I have selected a number between {lower_bound} and {upper_bound}. Try to guess it!")
    
    while True:
        
        guess = int(input("Enter your guess: "))
        
       
        if guess < secret_number:
            print("Your guess is too low. Try again!")
        elif guess > secret_number:
            print("Your guess is too high. Try again!")
        else:
            print("Congratulations! You guessed the correct number!")
            break

number_guessing_game()
