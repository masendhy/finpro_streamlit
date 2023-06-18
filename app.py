import streamlit as st
from multiapp import MultiApp
# import your app modules here
from apps import about, preparation, eda, evaluation, model, recommendation,modeval
from PIL import Image

app = MultiApp()
image = Image.open('images/pandas.png')

st.image(image)


st.markdown("""
#  Final Project Data Science Rakamin Bootcamp Batch 32
""")

# Add all your application here
app.add_app("About", about.app)
app.add_app("Bussines Understanding", preparation.app)
app.add_app("Exploratory Data Analysis", eda.app)
app.add_app("Data Pre-Processing", model.app)
app.add_app("Modeling & Evaluation", modeval.app)
app.add_app("Bussines Simulation", evaluation.app)
app.add_app("Bussines Recommendation", recommendation.app)
# The main app
app.run()
