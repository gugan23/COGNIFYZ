import re

def is_palindrome(s):
    cleaned_s = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned_s == cleaned_s[::-1]

def main():
    print("Palindrome Checker")
    print("------------------")
    print('')
    user_input = input("Enter a string to check if it is a palindrome: ")
    if is_palindrome(user_input):
        print(f'"{user_input}" is a palindrome.')
    else:
        print(f'"{user_input}" is not a palindrome.')

if __name__ == "__main__":
    main()
