##    ________________________TASK-3__________________________ 


import random
import string

def generate_password(length):
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_chars = string.punctuation

    all_chars = uppercase_letters + lowercase_letters + digits + special_chars

    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def main():
    try:
        desired_len = int(input("Enter the desired password length- "))
        if desired_len <= 0:
            print("Please enter a positive integer for the password length.")
            return

        generated_password = generate_password(desired_len)
        print(f"Generated password: {generated_password}")
    except ValueError:
        print("Invalid input. Please enter a valid positive integer.")

if __name__ == "__main__":
    main()


