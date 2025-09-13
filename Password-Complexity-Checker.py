import re

def check_password_strength(password):
    # Initialize strength score
    strength_score = 0

    # Check password length
    if len(password) >= 8:
        strength_score += 1
    else:
        print("Password should be at least 8 characters long.")

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        strength_score += 1
    else:
        print("Password should contain at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        strength_score += 1
    else:
        print("Password should contain at least one lowercase letter.")

    # Check for numbers
    if re.search(r'[0-9]', password):
        strength_score += 1
    else:
        print("Password should contain at least one number.")

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength_score += 1
    else:
        print("Password should contain at least one special character.")

    # Evaluate strength
    if strength_score == 5:
        print("Password is strong.")
    elif strength_score == 4:
        print("Password is medium strength.")
    else:
        print("Password is weak.")

# Test the function
password = input("Enter your password to check strength: ")
check_password_strength(password)
