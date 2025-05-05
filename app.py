import streamlit as st
from PIL import Image
import random

st.set_page_config(page_title="Magic 8 Ball 🎱", layout="centered")

image = Image.open("magic8ball.png")
st.image(image, width=150)

st.title("🎱 Welcome to the Magic 8 Ball Oracle")
st.markdown("Ask your question, focus your thoughts... and click **Shake!** to know your fate.")

question = st.text_input("Your question:")

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
        st.write(f"### 🧿 *{response}*")
    else:
        st.warning("Please enter a question first.")