import streamlit as st
import pandas as pd
import numpy as np
import sklearn
import pickle

st.set_page_config(page_title='Aplikasi Regresi Asuransi', layout='wide')

# Load necessary file
model = pickle.load(open('model.pkl', 'rb'))
#scl  = pickle.load(open('scl.pkl', 'rb'))

# Title
st.write('# Deskripsi App')
st.write('Ini adalah deployment web app dari model regresi untuk prediksi asuransi.')
 
with st.form('Prediksi Asuransi'):
  st.markdown('## Masukkan Input')
  tingkat_pelayanan = st.selectbox('Tingkat Pelayanan', options=['30 (Rawat Inap)', '40 (Rawat Jalan'])# categorical
  jumlah_peserta_aktif = st.number_input('Jumlah Peserta Aktif Periode Ini:', step=0.1, min_value=0.0, format='%.f')# float
  submitted = st.form_submit_button('Lakukan Prediksi')
  
  if submitted:
    # input_data = pd.DataFrame({'x1': [tingkat_pelayanan], 'x2':[jumlah_peserta_aktif]})
    input_data = np.asarray([tingkat_pelayanan, jumlah_peserta_aktif])
    scaled_input_data = input_data #scl.transform(input_data)
    st.info('Hasil Prediksi: {}'.format(model.predict(scaled_input_data))) #apa??
	
    if st.checkbox('Lihat Model'):
      st.write('Coefficient: {}'.format(model.coef_))
      st.write('Intercept: {}'.format(model.intercept_))
	