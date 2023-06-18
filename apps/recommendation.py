import streamlit as st
from PIL import Image


image = Image.open('images/thanks.jpeg')


def app():
    st.title('Penargetan Customer')
    st.write(
        'Mendorong customer untuk :orange[***memperoleh paspor***] dengan melakukan penawaran khusus.')

    st.title('Penargetan Customer')
    st.write(
        'Perusahaan dapat menentukan harga paket terbaru :orange[***menyesuaikan range harga paket kelas bawah hingga menengah (Basic, Standard, dan Deluxe***] sehingga dapat menarik perhatian pelanggan.')

    st.title('Paket Liburan Terkini')
    st.write(
        'Menawarkan :orange[***tujuan dan destinasi wisata terkini***] yang diminati oleh kalangan usia muda (± 20-35 tahun), baik dari segi penginapan dan kegiatan-kegiatan yang termasuk di dalamnya.')

    st.write("# ***Thank You...***")
    st.image(image)
