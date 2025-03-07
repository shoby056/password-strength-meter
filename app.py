import streamlit as st
import re

# Custom Dark Theme CSS with Block Background
st.markdown(
    """
    <style>
        /* Background Color */
        body {
            background-color: #0d1117;
        }
       
        
        /* Title */
        .main-title {
            font-size: 32px;
            font-weight: bold;
            color: #00c8ff;
            text-align: center;
        }
        /* Password Strength Box */
        .password-box {
            background: #1f2937;
            padding: 12px;
            border-radius: 10px;
            text-align: center;
            font-size: 20px;
            font-weight: bold;
            box-shadow: 0px 0px 10px rgba(255, 255, 255, 0.1);
        }
        /* Progress Bar Styling */
        .stProgress > div > div > div > div {
            border-radius: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Function to check password strength
def check_password_strength(password):
    strength = 0

    # Conditions for password strength
    if len(password) >= 8:
        strength += 1  # Length check
    if re.search(r"\d", password):
        strength += 1  # Contains numbers
    if re.search(r"[A-Z]", password):
        strength += 1  # Contains uppercase letter
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1  # Contains special characters

    return strength

# Streamlit UI with Block Background
# st.markdown("<div class='main-container'>", unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>🔐 Ultimate Password Strength Meter</h1>", unsafe_allow_html=True)

password = st.text_input("Enter your password:", type="password")

if password:
    strength = check_password_strength(password)

    # Strength Levels
    if strength == 0:
        remarks, color = "Very Weak 🔴", "red"
    elif strength == 1:
        remarks, color = "Weak 🟠", "orange"
    elif strength == 2:
        remarks, color = "Moderate 🟡", "yellow"
    elif strength == 3:
        remarks, color = "Strong 🟢", "green"
    else:
        remarks, color = "Very Strong 💪🔵", "cyan"

    # Display Strength
    st.markdown(f"<div class='password-box' style='color: {color};'>{remarks}</div>", unsafe_allow_html=True)

    # Animated Progress Bar
    st.progress(strength / 4)

    # Password Suggestions
    if strength < 2:
        st.warning("❌ Weak Password! Use uppercase, numbers, and special characters.")
    elif strength == 2:
        st.info("⚠️ Moderate Password. Try adding more special characters or uppercase letters.")
    else:
        st.success("✅ Strong Password!")

st.markdown("</div>", unsafe_allow_html=True)
