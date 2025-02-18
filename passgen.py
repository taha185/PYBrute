import random
import string
import os
import time

# Banner
def display_banner():
    banner = """
     ______     ______     ______   ______     ______     ______
    /\  ___\   /\  __ \   /\  ___\ /\  __ \   /\  ___\   /\  __ \\
    \ \  __\   \ \  __ \  \ \  __\ \ \  __ \  \ \  __\   \ \ \/\ \\
     \ \_____\  \ \_\ \_\  \ \_____\ \ \_\ \_\  \ \_____\  \ \_____\\
      \/_____/   \/_/\/_/   \/_____/  \/_/\/_/   \/_____/   \/_____/ 
   
                 Made by Taha185
    """
    print(banner)
    disclaimer = """
    Disclaimer:
    This script is for educational purposes only. Unauthorized access to computer systems is illegal.
    Do not use this script for malicious activities. The author is not responsible for any misuse of this script.
    """
    print(disclaimer)
    time.sleep(2)  # Delay for effect

# Function to generate a password list
def generate_password_list(length, num_passwords, include_symbols=True):
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    if include_symbols:
        characters += string.punctuation

    password_list = []
    
    for _ in range(num_passwords):
        password = ''.join(random.choice(characters) for _ in range(length))
        password_list.append(password)
    
    return password_list

# Main function
def main():
    display_banner()  # Display banner and disclaimer

    # Input from the user
    try:
        length = int(input("Enter password length: "))
        num_passwords = int(input("Enter number of passwords to generate: "))
        include_symbols = input("Include symbols? (yes/no): ").lower() == "yes"

        # Generate password list
        print("\nGenerating password list...")
        password_list = generate_password_list(length, num_passwords, include_symbols)

        # Save to a file
        file_name = "generated_passwords.txt"
        with open(file_name, 'w') as file:
            for password in password_list:
                file.write(password + "\n")

        print(f"\nPassword list generated successfully! Saved to {file_name}")
    
    except ValueError:
        print("Invalid input! Please enter valid numbers for password length and number of passwords.")

if __name__ == "__main__":
    main()
