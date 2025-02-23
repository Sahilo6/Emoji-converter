import streamlit as st

emojis = {
    "love": "❤️",
    "pizza": "🍕",
    "cat": "🐱",
    "dog": "🐶",
    "happy": "😊",
    "sad": "😢",
    "fire": "🔥",
    "sun": "☀️",
    "bath": "🛁",
    "coffee": "☕",
    "car": "🚗",
    "rain": "🌧️"
}

st.title("Emoji Converter")

user_input = st.text_input("Enter a sentence:")

if st.button("Convert"):
    if user_input.strip():
        words = user_input.split()
        result = [emojis.get(word.lower(), word) for word in words]
        st.write(" ".join(result))
    else:
        st.warning("Enter some text.")
