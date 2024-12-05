import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import random
from datetime import datetime, timedelta

#Fungsi menghitung estimasi biaya pengiriman
def hitung_estimasi_biaya(asal,tujuan,berat,layanan):
    tarif_per_kg = {
        "Ekonomi" : 5000,
        "Reguler" : 8000,
        "Ekspress" :12000
    }
    jarak_kota = {
        ("Jakarta", "Bandung"): 150,
        ("Bandung", "Surabaya"): 800,
        ("Surabaya", "Tangerang") : 650,
    }

#Fungsi menghitung estimasi biaya
def hitung_estimasi_biaya(asal,tujuan,berat,layanan):
  tarif_per_kg = {
      "Ekonomi" : 5000,
      "Reguler" : 10000,
      "Ekspress" : 15000
      }
  jarak_kota = {
       ("Jakarta","Bandung"):150,a
       ("Bandung", "Surabaya"):800,
       ("Surabaya", "Tangerang"):650,
      } 

  jarak = jarak_kota.get((asal,tujuan), jarak_kota.get((tujuan,asal),500))
  tarif = tarif_per_kg[layanan]
  biaya = tarif * berat + (jarak * 10)
  return biaya

# Custom CSS
st.markdown(
    """
    <style>
    body {
        background-color: #f0f2f6;
        color: #333333;
    }
    .stButton>button {
        background-color: #ff6600;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px 20px;
    }
    .stButton>button:hover {
        background-color: #ff4500;
    }
    .css-1y4p8pa {
        background-color: #ff6600;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar
st.sidebar.title("Tentang Aplikasi")
st.sidebar.info(
    """
    **Aplikasi Pengiriman Paket Antar Pulau Jawa**  
    Menghitung estimasi biaya pengiriman berdasarkan:  
    - Kota asal dan tujuan  
    - Berat paket  
    - Jenis layanan (Ekonomi, Reguler, Express)  
    """
)

# Judul aplikasi dengan ikon
st.markdown("<h1 style='text-align: center; color: #333333;'>📦 Aplikasi Pengiriman Paket</h1>", unsafe_allow_html=True)

# Form input data pengiriman
st.markdown("<h3 style='color: #444444;'>Masukkan Informasi Pengiriman</h3>", unsafe_allow_html=True)

#Judul dan form input
st.title("Pengiriman Paket Ekspedisi Antar Pulau Jawa")
st.header("Masukan Informasi Pengiriman :")

asal = st.selectbox("Kota Asal",["Jakarta","Bandung","Surabaya","Tangerang"])
tujuan = st.selectbox("Kota Tujuan",["Jakarta","Bandung","Surabaya","Tangerang"])

berat = st.number_input("Berat Paket (KG)",min_value =0.1,step =0.1)

layanan = st.radio("Jenis Layanan",["Ekonomi","Reguler","Express"])

if st.button ("Hitung Estimasi Biaya"):
   if asal == tujuan:
      st.warning("Kota Asal dan Tujuan Tidak Boleh Sama!")
   else:
      estimasi_biaya = hitung_estimasi_biaya(asal,tujuan,berat,layanan)
      st.success(f"Estimasi Biaya Pengiriman : Rp{estimasi_biaya:,}")

      

#Footer
st.markdown("----------")      
st.markdown("Dibuat oleh Raden and Adriel")
