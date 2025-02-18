

# Instagram Brute-Forcer & Password List Generator by Taha185

**Description**:  
This repository contains two powerful Python scripts designed for educational purposes only:

1. **Instagram Brute-Forcer**:  
   A simple Instagram login brute-forcer that attempts to login to Instagram accounts by using a list of possible passwords. It automates the process of trying multiple passwords on an Instagram account and checks if any of them successfully authenticate the user. This script is for testing your own Instagram accounts or for educational use in security research only.

2. **Password List Generator**:  
   A customizable password list generator that helps create a list of random passwords with user-defined length, complexity, and number of passwords. The generator can include letters (lowercase and uppercase), digits, and special symbols. This tool is useful for creating wordlists for use with penetration testing or brute-forcing login attempts.

⚠️ **Disclaimer**:  
Both tools are for **educational purposes** only. **Do not use these scripts for unauthorized access or malicious activities**. Brute-forcing Instagram accounts without permission is illegal and unethical. The author takes no responsibility for any misuse of these scripts.

---

### **Features**:

#### **Instagram Brute-Forcer**:
- **Automated Login Attempts**:  
  The script attempts to brute-force the login of an Instagram account by trying each password in a provided password list.
  
- **Colorful Output**:  
  The brute-forcing script uses colored output to clearly display the success or failure of each password attempt.
  
- **Login Feedback**:  
  The script will show a success message if the correct password is found, or continue to the next password if the attempt fails.
  
- **Disclaimer Reminder**:  
  A disclaimer is shown to remind users that unauthorized brute-forcing is illegal.

#### **Password List Generator**:
- **Customizable Parameters**:  
  Create a password list with user-defined parameters such as password length, number of passwords to generate, and whether to include special symbols.

- **Randomized Passwords**:  
  The generator can create passwords from a pool of lowercase and uppercase letters, digits, and special characters.
  
- **Output to File**:  
  The generated passwords are saved to a text file, which can be used in brute-forcing scripts or for secure password storage.

---

### **How to Use**:

#### **Instagram Brute-Forcer**:
1. **Input**:  
   - Enter the Instagram username.
   - Provide the path to the password list file (e.g., `C:\path\to\wordlist.txt`).
   
2. **Execution**:  
   - The script will start attempting each password from the wordlist.
   - It will show success if the correct password is found or failure if not.

#### **Password List Generator**:
1. **Input**:  
   - Specify the desired password length.
   - Define how many passwords you want to generate.
   - Decide if you want to include special characters.
   
2. **Execution**:  
   - The script will generate a random list of passwords.
   - The passwords are saved to a file (`generated_passwords.txt`).

---

### **Important Notes**:
- **Ethical Considerations**:  
  Both tools should be used only on systems where you have explicit permission. Brute-forcing an Instagram account without permission is illegal, and this tool should not be used for unauthorized access. Always respect privacy and security guidelines.

- **Rate-Limiting and Account Lockouts**:  
  Instagram has strong protections in place to prevent brute-forcing. The script may not work if Instagram blocks the account after multiple failed login attempts, or the account may be flagged for suspicious activity.

- **Security**:  
  Always ensure your own accounts are protected with strong, unique passwords and enable **two-factor authentication (2FA)** to prevent unauthorized access.

---

### **Disclaimer**:

**The creator of this repository (Taha185) is not responsible for any misuse of the tools provided**. These scripts are intended strictly for educational use, research purposes, or testing on accounts that you own or have explicit permission to test. Unauthorized access to any system is illegal and can result in severe legal consequences.
