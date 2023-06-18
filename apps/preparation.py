import streamlit as st
from PIL import Image

image = Image.open('images/problem.jpg')


def app():
    st.title('Problem Statement')

    st.image(image)

    st.write('\n \n **_Tahun lalu hanya 19% pelanggan yang membeli paket liburan._**')

    st.write(
        '**_Revenue perusahaan tidak mengalami peningkatan yang signifikan._**')

    st.subheader('Goal :')
    st.write('Untuk menaikkan conversion rate dan revenue perusahaan')

    st.subheader('Objective :')
    st.write(
        'Membuat model untuk memprediksi pelanggan yang akan membeli paket liburan terbaru')

    st.subheader('Business Metrics :')
    st.write('Total revenue dan conversion rate')
