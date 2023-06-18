import streamlit as st
from PIL import Image

image = Image.open('images/modeling.png')
image2 = Image.open('images/hyper.png')
image3 = Image.open('images/feature.png')
image4 = Image.open('images/target.png')


def app():
    st.title('Modeling')
    st.write('Penggunaan precision karena ingin menurunkan angka false positive (FP).False positive adalah kesalahan memprediksi jumlah _potential customer_.')
    st.image(image)

    st.title('Hyperparameter Tuning')
    st.image(image2)
    st.write(
        ':orange[**Random forest** sebagai best-fit model karena selisih nilai data test dan data train tidak lebih dari **0,1**.] ')

    st.title('Feature Importance')
    st.image(image3)
    st.write(
        'Dari hasil modeling random forest yang sudah dilakukan hyperparameter tuning berikut fitur teratas yang paling penting yaitu `Passport`, `ProductPitched`, dan `Age`.')

    st.title('Korelasi Fitur dan Target')
    st.image(image4)
    st.write('`Passport` 	: Korelasi positif ')
    st.write('`ProductPitched`	: Korelasi negatif')
    st.write('`Age`				: Korelasi negatif')
