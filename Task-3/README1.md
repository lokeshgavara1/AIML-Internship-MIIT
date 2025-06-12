# Random Password Generator

## Overview
This Python project generates secure, random passwords based on user-specified criteria, such as password length and the inclusion of uppercase letters, lowercase letters, digits, and special characters. The script ensures that at least one character from each selected type is included, making the passwords robust and suitable for various use cases.

## Features
- **Customizable Passwords**: Specify password length (minimum 4 characters) and choose to include:
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Digits (0-9)
  - Special characters (!@#$%^&* etc.)
- **Input Validation**: Ensures valid input and at least one character type is selected.
- **Secure Generation**: Uses Python's `random` module with shuffling to create unpredictable passwords.
- **Command-Line Interface**: Simple and interactive user input for generating passwords.

## Requirements
- Python 3.6+
- No external libraries required (uses standard Python libraries: `random`, `string`)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/random-password-generator.git
   cd random-password-generator
   ```
2. Ensure Python 3.6+ is installed:
   ```bash
   python --version
   ```

## Usage
1. Run the script:
   ```bash
   python password_generator.py
   ```
2. Follow the prompts to specify:
   - Password length (e.g., 12)
   - Whether to include uppercase letters, lowercase letters, digits, and special characters (y/n)
3. The script will output a generated password or an error message if inputs are invalid.

### Example
```bash
Random Password Generator
-----------------------
Enter password length (minimum 4): 12
Include uppercase letters? (y/n): y
Include lowercase letters? (y/n): y
Include digits? (y/n): y
Include special characters? (y/n): y

Generated Password: K7@aL9#pQz2m
```

## Notes
- The password generator ensures at least one character from each selected type is included for security.
- If you encounter errors, check that the password length is at least 4 and at least one character type is selected.
- This project uses Python's standard library, making it lightweight and portable.
