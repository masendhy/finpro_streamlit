import streamlit as st
from PIL import Image

image = Image.open('images/boxplot.png')
image_age = Image.open('images/age.png')
image_product = Image.open('images/product.png')
image_passport = Image.open('images/passport.png')


def app():
    st.title('EXPLORATORY DATA ANALYSIS')

    st.write('**Jumlah Baris :** 4888 baris')
    st.write('**Jumlah Kolom :** 19 kolom')
    st.write('**Missing Value :** 8 kolom')
    st.write('**Duplicated Data :** None')
    st.write('**Target :** Kolom `ProdTaken`')
    st.write('**Kesalahan Value :** Kolom `Gender` _Fe Male_')
    st.write(
        '**Kemiripan Value :** Kolom `MaritalStatus` value _Divorced_, _Single_, dan _Unmarried_')
    st.write('**Tipe Data Kurang Sesuai :** 7 kolom dengan tipe data float, diubah menjadi tipe data integer')

    st.write('\n\n')
    st.subheader('Dataset Analysis')
    st.image(image, width=300)
    st.write('***Terdapat 2 kolom yang memiliki outliers***')

    st.write('\n\n')
    st.subheader('Bisnis Insight : _Penargetan Pelanggan_')
    st.image(image_passport, width=300)
    st.write(
        '***Mendorong pelanggan untuk :orange[memperoleh paspor] dengan melakukan penawaran khusus.***')

    st.write('\n\n')
    st.subheader('Bisnis Insight : _Penentuan Harga Paket Terbaru_')
    st.image(image_product, width=300)
    st.write(
        '***Perusahaan dapat menyesuaikan harga paket terbaru :orange[menyesuaikan range harga paket kelas bawah hingga menengah (Basic, Standard, dan Deluxe)], sehingga dapat menarik perhatian pelanggan.***')

    st.write('\n\n')
    st.subheader('Bisnis Insight : _Keterlibatan Digital_')
    st.image(image_age, width=300)
    st.write(
        '***Membangun kehadiran yang kuat di platform digital, seperti media sosial atau aplikasi mobile. Sesuaikan :orange[konten dengan minat pelanggan yang lebih muda], seperti gunakan bahasa, gambar, dan gaya komunikasi yang sesuai dengan target audiens.***')
