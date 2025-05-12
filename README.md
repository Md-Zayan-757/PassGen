# 🔐 PassGen - Password Generator

PassGen is a simple and interactive password generator web app built with Streamlit. It allows you to create strong, customizable passwords with options to include uppercase letters, special characters, and digits. The app also evaluates the strength of the generated password to help you choose a secure one.

---

## Features

- Select password length (4 to 50 characters)
- Option to include:
  - Uppercase letters (A-Z)
  - Special characters (e.g., !@#...)
  - Digits (0-9)
- Password strength evaluation with visual feedback
- Easy-to-use interface with a copyable password display

---

## Installation

1. Make sure you have Python 3.7+ installed.

2. Install Streamlit if you haven't already:

```
pip install streamlit
```

3. Save the password generator script (e.g., `passgen.py`).

---

## Usage

Run the Streamlit app with the following command:

```
streamlit run passgen.py
```

This will open the web interface in your default browser.

---

## How It Works

- **Password Generation:**  
  The app generates a password based on your selected options:
  - Lowercase letters are always included.
  - Uppercase letters, digits, and special characters are included based on your selections.
  - Ensures at least one character from each selected category is present.
  - Password length must be at least equal to the number of selected character types.

- **Strength Check:**  
  Password strength is assessed on:
  - Presence of lowercase, uppercase, digits, special characters
  - Password length (12 or more characters)
  
  Strength levels range from "Very Weak 😢" to "Very Strong 🔥".

---

## Code Overview

- `generate_password(length, use_upper, use_char, use_digits)`  
  Generates a password with the specified criteria.

- `check_strength(password)`  
  Returns a strength label based on password complexity.

- Streamlit UI components for user input and displaying results.

---

## Contributing

Feel free to fork the repository and submit pull requests. Suggestions and improvements are welcome!

---

## License

This project is open source and available under the License.

---
Enjoy generating strong passwords with PassGen! 🔐

---
