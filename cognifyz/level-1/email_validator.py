import re

def validate_email(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.fullmatch(regex, email):
        return True
    return False


email = input("Enter an email address: ")

if validate_email(email):
    print("Valid Email")
else:
    print("Invalid Email")
