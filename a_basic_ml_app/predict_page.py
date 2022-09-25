import streamlit as st
import pickle
import numpy as np

def load_model():
    with open("saved_steps.pkl", 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()


regressor = data["model"]
le_country = data["le_country"]
le_education = data["le_education"]

def show_predict_page():
    st.title("Software Developer Salary Prediction")

    st.write("""### We need som info to predict the salary""")
    countries = ("United States",
                 "Canada",
                 "United Kingdom",
                 "Germany",
                 "Brazil",
                 "Australia",
                 "India",
                 "France",
                 "Poland",
                 "Netherlands",
                 "Mexico",
                 "Spain",
                 "Italy",
                 "Sweden",
                 "Russian Federation",
                 "Ukraine",
                 "Turkey",)
    education_level = ("Less than a Bachelors",
                 'Bachelor’s degree', 'Master’s degree', 'Post grad')

    country = st.selectbox("Country", countries)
    education = st.selectbox("Education", education_level)
    experience = st.slider("Year of Experience", 0, 50, 3)

    if st.button("Calculate Salary"):
        X = np.array([[country, education, experience]])
        X[:, 0] = le_country.transform(X[:,0])
        X[:, 1] = le_education.transform(X[:,1])
        X = X.astype(float)

        salary = regressor.predict(X)
        st.subheader(f"Estimated Salary = ${salary[0]:.2f}")





