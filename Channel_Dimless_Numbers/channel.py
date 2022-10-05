import streamlit as st
from new_model import show_new_model
from load_model import show_load_model
from explore_model import show_explore_model

st.header("Rotating Channel Dimensionless Numbers")

model_choice = st.sidebar.selectbox("Modeling choice", ("New", "Explore","Load"))

if model_choice == "New":
    show_new_model()
elif model_choice == "Explore":
    show_explore_model()
else:
    show_load_model()
