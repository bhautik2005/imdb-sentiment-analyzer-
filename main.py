#  Import Libraries

import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import load_model
import streamlit as st

 
# Load Word Index + Model
 
word_index = imdb.get_word_index()
reverse_word_index = {value: key for key, value in word_index.items()}

model = load_model('simple_Rnn_imdb2.h5')

 
#   Helper Functions
 

def preprocess_text(text):
    words = text.lower().split()
    encoded_review = [word_index.get(word, 2) + 3 for word in words]
    padded_review = sequence.pad_sequences([encoded_review], maxlen=500)
    return padded_review

def decode_review(encoded_review):
    return ' '.join([reverse_word_index.get(i - 3, '?') for i in encoded_review])


#UI of application

st.set_page_config(page_title="IMDB Sentiment Analyzer", page_icon="🎬")

st.title("🎬 IMDB Movie Review Sentiment Analyzer")
st.write("Enter a movie review and classify it as Positive or Negative")

# Example reviews
example_reviews = {
    "Positive Example": "This movie was absolutely fantastic, the acting was brilliant and the story was very engaging.",
    "Negative Example": "Worst movie ever. Completely boring and waste of time.",
}

selected_example = st.selectbox(
    "Try an example:",
    ["None"] + list(example_reviews.keys())
)

if selected_example != "None":
    user_input = st.text_area("Movie Review", example_reviews[selected_example])
else:
    user_input = st.text_area("Movie Review")

if st.button("🔍 Classify"):
    if user_input.strip() != "":
        with st.spinner("Analyzing..."):
            preprocessed_input = preprocess_text(user_input)
            prediction = model.predict(preprocessed_input)
            score = float(prediction[0][0])
            sentiment = "Positive 😊" if score > 0.5 else "Negative 😞"

        st.success(f"Sentiment: {sentiment}")
        st.progress(score)
        st.write(f"Confidence: {round(score * 100, 2)}%")

    else:
        st.warning("Please enter a review first.")
