import streamlit as st
import random

st.set_page_config(page_title="Magic 8 Ball 🎱", layout="centered")

st.title("🎱 Ask the Magic 8 Ball!")
question = st.text_input("What’s your question?")

answers=['It is certain.', 
             'It is decidedly so.', 
             'Without a doubt.',
             'Yes definitely.', 
             'You may rely on it.', 
             'As I see it, yes.',
             'Most likely.',
             'Outlook good.', 
             'Yes.', 
             'Signs point to yes.',
             'Reply hazy, try again.', 
             'Ask again later.', 
             'Better not tell you now.',
             'Cannot predict now.', 
             'Concentrate and ask again.',
             "Don't count on it.", 
             'My reply is no.', 
             'My sources say no.', 
             'Outlook not so good.',
             'Very doubtful.']

if st.button("Shake!"):
    if question:
        response = random.choice(answers)
        st.write(f"🧿 *{response}*")
    else:
        st.warning("Please enter a question first.")