import streamlit as st
st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #0095f6; /* Instagram Blue */
        color: white;
        height: 3em;
        width: 100%;
        border-radius: 8px; /* Slightly rounded corners */
        border: none;
        font-size: 16px;
        font-weight: bold;
        transition: background-color 0.3s ease;
    }
    
    /* Change color when you hover over it */
    div.stButton > button:first-child:hover {
        background-color: #1877f2; /* Darker Blue on hover */
        color: white;
        border: none;
    }
    
    /* Fix for button click effect */
    div.stButton > button:first-child:active {
        background-color: #1877f2;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)
st.title("🎂 Age Calculator")
name = st.text_input("What is your name?")
if st.button("calculate"):
  st.write(f"button clicked! Hello{name}")
birth_year = st.number_input("What year were you born?",min_value=1900, max_value=2026,value=2000)
age = 2026 - birth_year
st.header(f"Hello {name}!")
st.subheader(f"You are {age} years old.")
st.write(f"📅 Months: {age * 12}")
st.write(f"🗓️ Weeks: {age * 52}")
st.write(f"☀️ Days: {age * 365}")
st. balloons()
