import streamlit as st
import pandas as pd
import numpy as np
import sklearn
import pickle


# Load necessary file
model = pickle.load(open('model.pkl', 'rb'))

 
with st.form('For Assurance Prediction'):
  st.markdown('## Enter the input')
  news_input = st.text_area(' ', ' ')
  tingkat_pelayanan = st.selectbox('Tingkat Pelayanan', options=['30 (Rawat Inap)', '40 (Rawat Jalan'])# categorical
  jumlah_peserta_aktif = st.number_input('Jumlah Peserta Aktif Periode Ini:', step=0.1, min_value=0.0, format='%.f')# float
  submitted = st.form.form_submit_button('Prediksi Asuransi')
  
  
  if submitted:
    st.info('Hasil Predikisi: ') #apa??
	st.info(model)
	