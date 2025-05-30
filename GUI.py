import streamlit as st
import random
import string

def generate_password(length, use_upper, use_char, use_digits):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_upper else ''
    char = string.punctuation if use_char else ''
    digits = string.digits if use_digits else ''
    
    all_chars = lower + upper + char + digits

    if not all_chars:
        return "Please select at least one character type."

    required_chars = []
    if use_upper:
        required_chars.append(random.choice(upper))
    if use_char:
        required_chars.append(random.choice(char))
    if use_digits:
        required_chars.append(random.choice(digits))

    if length < len(required_chars):
        return f"Password length must be at least {len(required_chars)}."

    rem_len = length - len(required_chars)
    password = required_chars + [random.choice(all_chars) for _ in range(rem_len)]
    random.shuffle(password)

    return ''.join(password)

def check_strength(password):
    score = 0
    if any(c.islower() for c in password): score += 1
    if any(c.isupper() for c in password): score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(c in string.punctuation for c in password): score += 1
    if len(password) >= 12: score += 1

    strength_levels = {
        1: "Very Weak 😢",
        2: "Weak 😕",
        3: "Moderate 🙂",
        4: "Strong 💪",
        5: "Very Strong 🔥"
    }

    return strength_levels.get(score, "N/A")

# Streamlit UI
st.set_page_config(page_title="PassGen", page_icon="🔐")
st.title("🔐 PassGen - Password Generator")

length = st.slider("🔢 Select password length", 4, 50, 12)
use_upper = st.checkbox("Include Uppercase Letters (A-Z)")
use_char = st.checkbox("Include Special Characters (!@#...)")
use_digits = st.checkbox("Include Digits (0-9)")

if st.button("🔄 Generate Password"):
    password = generate_password(length, use_upper, use_char, use_digits)
    
    if "Please select" in password or "must be at least" in password:
        st.error(password)
    else:
        strength = check_strength(password)
        st.success("🎉 Your password is ready!")

        # Display password with copy button
        st.code(password, language="")

        # Strength display
        st.markdown(f"# **Strength:** `{strength}`")
