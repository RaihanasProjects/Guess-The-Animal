import streamlit as st

st.set_page_config(
    page_title="Guess the Animal",
    page_icon="🐾",
    layout="centered"
)

st.title("🐾 Guess the Animal AI Game")

st.write("I am thinking of an animal... Ask me yes/no questions!")

# Input box
question = st.text_input("Ask your question:")

# Button
if st.button("Ask"):
    if question:
        st.write(f"You asked: {question}")
        st.write("AI answer: (we will connect this soon)")
    else:
        st.warning("Please enter a question first!")

# Guess section
st.subheader("Make a guess")

guess = st.text_input("What animal do you think it is?")

if st.button("Submit Guess"):
    if guess:
        st.write(f"You guessed: {guess}")
        st.write("Result: (we will check this later)")
    else:
        st.warning("Enter a guess first!")
