import streamlit as st
from tensorflow.keras.models import load_model
import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

## loading the tensorflow model for prediction 

model=load_model('rnn_model.h5')

with open ('tokenizer.pkl','rb') as file:
    tokenizer=pickle.load(file)

st.title("Twitter Tweets Sentiment Analysis")

tweet=st.text_area("Enter the Tweet:")

if st.button('Predict Sentiment') and tweet.strip():
    sequences=tokenizer.texts_to_sequences([tweet])
    padded_sequence=pad_sequences(sequences,padding='pre',maxlen=99)

    prediction=model.predict(padded_sequence)
    predicted_class=np.argmax(prediction,axis=1)[0]

    sentiment_map={0:'Negative',1:'Neutral',2:'Positive'}

    st.write('Sentiment:',sentiment_map[predicted_class])