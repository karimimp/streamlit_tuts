import streamlit as st
import pandas as pd
import plotly.express as px

df =  pd.read_csv("data2.csv")
df.columns = "norm U".split()
st.write(df.head(7))

fig = px.line(df, x="norm", y="U", title="DNS data", markers=True)

st.write(fig)