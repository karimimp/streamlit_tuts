import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

header = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()
st.markdown("""
    <style>
    .main {
        backgroud-color: #F5F5F5;
    }
    </style>
""")


@st.cache
def get_data():
    df = pd.read_parquet("data/yellow_tripdata_2022-01.parquet")
    return df

with header:
    st.title("Welcome to This App")
    st.text("This app looks into the transaction of taxis in NY")

with dataset:
    st.header("New York City Taxi Dataset")
    st.text("This dataset is publicly accessible")
    df = get_data()
    st.write(df.head(5))
    location_distribution = pd.DataFrame(df['PULocationID'].value_counts().head(25))
    st.subheader("Pick up location id")
    st.bar_chart(location_distribution)


with features:
    st.header("The Features")
    st.markdown("* first feature: this is feature 1")
    st.markdown("* 2nd feature: this is feature 2")
    st.markdown("This is **markdown** and a formula $$ \lambda = {{h \sqrt{\omega sin(a)} } \over {\nu}} $$")


with model_training:
    st.header("Training the model")
    st.text("The model is trained in this section.")
    # columns
    sel_col, disp_col = st.columns(2)
    max_depth = sel_col.slider('max depth of model?', 10, 100, step=10)
    n_estimators = sel_col.selectbox('how many trees?', options=[100,200,300], index=0)

    sel_col.text('List of different features:')
    sel_col.write(df.columns)
    input_feature = sel_col.text_input('which feature?', 'PULocationID')

    regr = RandomForestRegressor(max_depth = max_depth, n_estimators=n_estimators)
    x = df[[input_feature]]
    y = df[["trip_distance"]]

    regr.fit(x,y)
    prediction = regr.predict(y)

    disp_col.subheader('mean absolute error')
    disp_col.write(mean_absolute_error(y, prediction))

    disp_col.subheader('mean squared error')
    disp_col.write(mean_squared_error(y, prediction))

    disp_col.subheader('r score')
    disp_col.write(r2_score(y, prediction))

