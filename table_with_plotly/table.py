from turtle import fillcolor
import streamlit as st
import pandas as pd
# import plotly.express as px
import plotly.graph_objects as go

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

interactive = st.container()

with interactive:
    # st.title("Title")
    st.header("Interactive Table")
    df = pd.read_csv("data.csv")
    df.columns = "y/h y+ U/Ub U+ u v w uv".split()
    # st.write(df)

    fig = go.Figure(data=go.Table(columnwidth = [2,1,1,1,1,1,1,1], header = dict(values = list(df.columns)), cells = dict(values = [df["y/h"], df["y+"], df["U/Ub"], df["U+"], df["u"], df["v"], df["w"], df["uv"]], fill_color = "#c3c4c7", align="left")   ))

    fig.update_layout(margin=dict(l=10, r=10), paper_bgcolor="red",)
    st.write(fig)

