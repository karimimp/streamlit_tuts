from turtle import width
import plotly.express as px
import streamlit as st
import pandas as pd

df = px.data.gapminder()

st.write(df.head(5))

year_options = df['year'].unique().tolist()
year = st.selectbox("Which year?", year_options, 0)
# df = df[df['year'] == year]

fig = px.scatter(df, x='gdpPercap', y="lifeExp", size="pop", color='continent', log_x=True, size_max=55, range_x=[100, 1e5], range_y=[25,90], animation_frame="year", animation_group="country")

fig.update_layout(width=800)
st.write(fig)

covid = pd.read_csv("data.csv")
covid.columns = ["Country", "Code", "Date", "Confirmed", "Days since confirmed"]
covid["Date"] = pd.to_datetime(covid["Date"]).dt.strftime('%Y-%m-%d')
country_option = covid["Country"].unique().tolist()

st.write(covid.head(5))
date_option = covid['Date'].unique().tolist()
date = st.selectbox("Which date?", date_option, 100)
country = st.multiselect("Which country?", country_option, ['Brazil'])

covid = covid[covid["Country"].isin(country)]
# covid = covid[covid["Date"] == date]

fig2 = px.bar(covid, x="Country", y="Confirmed", color="Country", range_y=[0,35000], animation_frame="Date", animation_group="Country")
fig2.update_layout(width=800)
st.write(fig2)
