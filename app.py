import streamlit as st
import pandas as pd
import numpy as np
import sklearn
import pickle


# Load necessary file
model = pickle.load(open('model.pkl', 'rb'))

news_categories = ['sport', 'business', 'politics', 'tech', 'entertainment']
news_categories_imgs = ['sport.png', 'business.png', 'politics.jpg', 'tech.jpg', 'entertainment.jpg']


# Function to clean text
def clean_text(text, stp_word):
  text = text.strip()
  text = text.lower()
  text = text.translate(str.maketrans('','',string.punctuation))
  text = ' '.join([word for word in text.split() if word not in stp_word])
  return text

 
with st.form('For Assurance Prediction'):
  st.markdown('## Enter the input')
  news_input = st.text_area(' ', ' ')
  
  submitted = st.form.form_submit_button('Category Prediction')
  
  if submitted:
    news_input = clean_text(news_input, stp_word)
#	news_input_to_seq = tokenizer.texts_to_sequences(news_input)
#	pad_news_input_to_seq = pad_sequences(seq, padding='post', maxlen=120)
#	news_pred = model.predict(pad_news_input_to_seq)
#	idx = np.argmax(pred)-1
#	pred_lbl = news_categories[idx]
#	image = Image.open(dir+news_categories_imgs[idx])
#	st.markdown('### Prediction:')
#	st.image(image, caption=pred_lbl)
	
	