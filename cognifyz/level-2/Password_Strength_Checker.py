import re

print("Password Strength Checker")
print("-------------------------")
print('')

def password_strength_checker(password):
    criteria = {
        "length": len(password) >= 8,
        "uppercase": re.search(r'[A-Z]', password) is not None,
        "lowercase": re.search(r'[a-z]', password) is not None,
        "digit": re.search(r'\d', password) is not None,
        "special": re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None
    }
    strength_score = sum(criteria.values())
    
    if strength_score == 5:
        strength = "Very Strong"
    elif strength_score == 4:
        strength = "Strong"
    elif strength_score == 3:
        strength = "Medium"
    elif strength_score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"
        
    feedback = []
    if not criteria["length"]:
        feedback.append("Password must be at least 8 characters long.")
    if not criteria["uppercase"]:
        feedback.append("Password must contain at least one uppercase letter.")
    if not criteria["lowercase"]:
        feedback.append("Password must contain at least one lowercase letter.")
    if not criteria["digit"]:
        feedback.append("Password must contain at least one digit.")
    if not criteria["special"]:
        feedback.append("Password must contain at least one special character.")

    return strength, feedback

def main():
    password = input("Enter your password: ")
    strength, feedback = password_strength_checker(password)
    
    print(f"Password Strength: {strength}")
    print('')
    for message in feedback:
        print(f"Feedback: {message}")

if __name__ == "__main__":
    main()
