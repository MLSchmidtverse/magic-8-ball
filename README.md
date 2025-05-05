# 🎱 Magic 8 Ball – Your Personal Python Oracle

This little app is a playful take on the classic Magic 8 Ball – built with Python and Streamlit. Ask any yes/no question, shake the ball, and get your answer from the wisdom of the code gods.

## 🔍 Why This Project?

After running into some deployment issues with a more complex Streamlit project (thanks, `nltk.download()` 🙄), I decided to give myself a fresh start. During a daily Python refresher, I built a simple Magic 8 Ball script and thought:

> "What if I used this as a low-pressure way to re-approach Streamlit – and have some fun with it?"

And here we are. This project is a reminder that:

- Small things can have impact
- Your inner child deserves to code sometimes
- Streamlit makes UI ridiculously easy

## 🧠 Tech Stack

- **Python** – the logic behind the magic
- **Streamlit** – for the web interface
- **random.choice()** – instead of mapping to `randint`, I just use a list of answers

## 🚀 Try it out

👉 [Click here to try the app live](https://your-app-url.streamlit.app)  

Or run it locally:

```bash
git clone https://github.com/yourusername/magic-8-ball
cd magic-8-ball
pip install -r requirements.txt
streamlit run app.py