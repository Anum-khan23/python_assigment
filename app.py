import random
import streamlit as st

# Define character sets
upperChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowerChars = "abcdefghijklmnopqrstuvwxyz"
numChars = "0123456789"
symChars = "`~!@#:;,./|$%^&*)(_-=+"

# Streamlit UI
st.title("🔐 Secure Password Generator")
st.write("Generate a strong, random password based on your preferences.")

# User Input
passwordLength = st.slider("🔢 Select Password Length", min_value=6, max_value=100, value=12)
include_upper = st.checkbox("🔠 Include Uppercase Letters")
include_lower = st.checkbox("🔡 Include Lowercase Letters")
include_numbers = st.checkbox("🔢 Include Numbers")
include_symbols = st.checkbox("🔣 Include Symbols")

# Function to generate password
def generatePassword():
    passwordChars = ""
    if include_upper:
        passwordChars += upperChars
    if include_lower:
        passwordChars += lowerChars
    if include_numbers:
        passwordChars += numChars
    if include_symbols:
        passwordChars += symChars

    # Ensure at least one character type is selected
    if not passwordChars:
        st.error("⚠️ Please select at least one character type!")
        return ""
    
    return "".join(random.choice(passwordChars) for _ in range(passwordLength))

# Generate Password Button
if st.button("🔄 Generate Password"):
    password = generatePassword()
    if password:
        st.success("✅ Your Secure Password:")
        st.text(password)
        
        # Simple Strength Assessment
        if len(password) >= 12:
            st.write("🔒 Strength: Strong")
        elif len(password) >= 8:
            st.write("🔒 Strength: Medium")
        else:
            st.write("🔒 Strength: Weak")
        
        # Copy Button (Simulated)
        st.button("📋 Copy Password", on_click=lambda: st.toast("Password copied!"))
