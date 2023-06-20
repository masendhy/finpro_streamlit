import streamlit as st
from PIL import Image

image = Image.open('images/confusion.png')
image_3305 = Image.open('images/3305.png')
image_76 = Image.open('images/76.png')
image_26 = Image.open('images/26.png')
image_721 = Image.open('images/721.png')
image_rev = Image.open('images/revenue.png')
image_con = Image.open('images/convertion.png')


def app():
    st.title('Confusion Matrix')
    st.image(image, width=600)

    st.write('\n')
    st.write('\n')
    st.write('\n')

    with st.container():

        tab1, tab2, tab3, tab4 = st.columns(4)

        with tab1:
            st.image(
                image_3305, caption="True Negative : Diprediksi tidak mengambil paket liburan dan itu benar", width=125,)

        with tab2:
            st.image(
                image_76, caption="False Negative: Diprediksi tidak mengambil paket liburan dan itu salah", width=125,)

        with tab3:
            st.image(
                image_26, caption="False Positive : Diprediksi mengambil paket liburan dan itu salah", width=125,)

        with tab4:
            st.image(
                image_721, caption="True Positive : Diprediksi mengambil paket liburan dan itu benar", width=125,)

    st.title('Kenaikan Total Revenue')
    st.image(image_rev, width=600)
    st.write(
        ':orange[`Revenue = (TP * Profit per package) - ((TP + FP) * Cost per marketing)`]')

    st.title('Kenaikan Conversion Rate')
    st.image(image_con, width=600)
    st.write(
        ':orange[`Conversion Rate = (TP / (TP + FP)) x 100%`]')
