import streamlit as st
from PIL import Image


st.set_page_config(
    page_title="Final Project ",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",

)


image = Image.open('images/banner.png')
image_sendhy = Image.open('images/sendhy.png')
image_vio = Image.open('images/vio.png')
image_jannisah = Image.open('images/jannisah.png')
image_edgar = Image.open('images/edgar.png')
image_nanda = Image.open('images/nanda.png')
image_faris = Image.open('images/faris.png')
image_teguh = Image.open('images/teguh.png')
image_jodhi = Image.open('images/jodhi.png')


def app():
    st.write('\n \n')
    st.image(image,width=300)

    st.title('About Dataset')

    st.write('### Holiday Package Prediction')
    st.write('"Trips & Travel.Com" company wants to enable and establish a viable business model to expand the customer base. One of the ways to expand the customer base is to introduce a new offering of packages. ')

    st.markdown(
        '[dataset link](https://www.kaggle.com/datasets/susant4learning/holiday-package-purchase-prediction)')

    st.write('\n \n')
    st.title('Our Team')

    with st.container():

        tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.columns(8)

        with tab1:
            st.image(image_edgar, width=75, caption='Edgar')

        with tab2:
            st.image(image_teguh, width=75, caption='Teguh')

        with tab3:
            st.image(image_jannisah, width=75, caption='Jannisah')

        with tab4:
            st.image(image_sendhy, width=75, caption='Sendhy')

        with tab5:
            st.image(image_vio, width=75, caption='Vionella')

        with tab6:
            st.image(image_faris, width=75, caption='Faris')

        with tab7:
            st.image(image_jodhi, width=75, caption='Jodhi')

        with tab8:
            st.image(image_nanda, width=75, caption='Nanda')
