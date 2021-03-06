import streamlit as st
import pandas as pd
import numpy as np
import sklearn
import pickle

st.set_page_config(page_title='Aplikasi Regresi Unit Cost', layout='wide')

# Load necessary file
model = pickle.load(open('model_baru.pkl', 'rb'))
scl  = pickle.load(open('std_scl_new.pkl', 'rb'))


# Title
st.write('# Deskripsi App')
st.write('Ini adalah deployment web app dari model regresi untuk prediksi unit cost pada sebuah daerah akibat penambahan rumah sakit.')
 
with st.form('Prediksi Asuransi'):
  st.markdown('## Masukkan Input')
  tingkat_pelayanan = st.selectbox('Tingkat Pelayanan', options=['30 (Rawat Jalan)', '40 (Rawat Inap)'])# categorical
  tingkat_pelayanan_ = 40
  if tingkat_pelayanan=='30 (Rawat Jalan)':
    tingkat_pelayanan_ = 30
  
  jumlah_peserta_aktif = st.number_input('Jumlah Peserta Aktif Periode Ini:', step=0.1, min_value=0.0, format='%.f')# float
  submitted = st.form_submit_button('Lakukan Prediksi')
  
  if submitted:
    input_data = pd.DataFrame({'x1': [tingkat_pelayanan_], 'x2':[jumlah_peserta_aktif]})
    scaled_input_data = scl.transform(input_data)
    st.info('Hasil Prediksi Unit Cost: {}'.format(model.predict(scaled_input_data)[0])) #apa??

	
if st.checkbox('Lihat Model'):
  st.write('Y = {} * x1 + {} * x2 + {}'.format(model.coef_[0], model.coef_[1], model.intercept_))
  st.write('Jumlah Fitur: {}'.format(model.n_features_in_))
  st.write('Coefficient: {}'.format(model.coef_))
  st.write('Intercept: {}'.format(model.intercept_))
  