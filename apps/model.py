import streamlit as st
from PIL import Image

image = Image.open('images/corr.png')


def app():
    st.title('Data Cleansing')

    st.subheader('Handling Missing Value')

    st.write('* Kolom `Age` di inputasi dengan value _mean_')
    st.write(
        '* Kolom `DurationOfPitch`,`MonthlyIncome` di inputasi dengan value _median_')
    st.write('* Kolom `NumberOfFollowups` di inputasi dengan value _modus_')
    st.write('* Dilakukan _drop_ pada kolom `TypeOfContact`,`PreferredPropertyStar`,`NumberOfTrips`,`NumberOfChildrenVisiting`  ')

    st.write('\n\n')
    st.subheader('Handling Outliers')
    st.write('* Tidak dilakukan karena model non-linear (model yang robust)')

    st.write('\n\n')
    st.subheader('Handling Invalid Data Type')
    st.write('* 7 kolom diubah dari tipe data float menjadi integer')

    st.write('\n\n')
    st.subheader('Handling Invalid Value')
    st.write('Kesalahan penulisan _‘Fe Male’_ diubah menjadi _‘Female’_')

    st.write('\n\n')
    st.subheader('Feature Transformation')
    st.write('* Dilakukan :red[_standarisasi_] pada kolom `Age`')
    st.write(
        '* Dilakukan :red[_normalisasi_] pada kolom `DurationOfPitch` dan `MonthlyIncome`')

    st.write('\n\n')
    st.subheader('Feature Encoding ')
    st.write(
        '* Dilakukan :red[_One-hot encoding_] pada kolom `Occupation` dan `TypeOfContact`')
    st.write(
        '* Dilakukan :red[_Label encoding_] pada kolom `Gender`, `ProductPitched`, `MaritalStatus`, dan `Designation`')

    st.write('\n\n')
    st.subheader('Split Data')
    st.write(
        '* Dilakukan split data **70%** untuk _data train_ dan **30%** untuk _data test_')

    st.write('\n\n')
    st.subheader('Correlation Features')
    st.image(image,width=300)
    st.write('### **20 fitur --> 10 fitur & 1 target**')
    st.write(
        '* Untuk melihat apakah di antara fitur yang tersisa, terdapat fitur yang redundant atau tidak')
