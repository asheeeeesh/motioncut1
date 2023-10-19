import random
import string

def generate_password(length=12):
    # Define character sets for different types of characters
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = "!@#$%^&*()_+-=[]{}|;:,.<>?/\\"

    # Combine character sets
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Ensure that each password has at least one of each character type
    password = random.choice(lowercase_letters) + random.choice(uppercase_letters) + random.choice(digits) + random.choice(special_characters)

    # Generate the remaining characters for the password
    remaining_length = length - 4
    for _ in range(remaining_length):
        password += random.choice(all_characters)

    # Shuffle the characters to make the password random
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

def generate_passwords(num_passwords, length=12):
    passwords = []
    for _ in range(num_passwords):
        password = generate_password(length)
        passwords.append(password)
    return passwords

if __name__ == "__main__":
    num_passwords = int(input("Enter the number of passwords to generate: "))
    password_length = int(input("Enter the length of each password: "))

    passwords = generate_passwords(num_passwords, password_length)

    print("Generated Passwords:")
    for i, password in enumerate(passwords, start=1):
        print(f"Password {i}: {password}")
