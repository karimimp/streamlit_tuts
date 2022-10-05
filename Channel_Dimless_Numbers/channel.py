import numpy as np
import streamlit as st
import pickle
import pandas as pd

st.header("Rotating Channel Dimensionless Numbers")

def Ro(omega,h,u):
    return (2*omega*h/u)

def Re(nu,h,u):
    return (u*h/nu)

def Ek(nu,omega,h):
    return (nu/(omega*h**2))

def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

model_choice = st.sidebar.selectbox("New model or load model", ("New", "Load"))

if model_choice == "New":
    st.subheader("Input variables")
    h = st.number_input(label = "Channel half-width, h (mm)", min_value = 0.01, value = 10., step = 1., format='%.1f')
    h = h/1e3

    omega = st.number_input(label = "Rotational, ω (rpm)", min_value = 0.0, value = 1000., step = 1., format='%.1f')
    omega = omega*np.pi/30

    nu = st.number_input(label = "Kinematic viscosity, υ (cSt)", min_value = 1., value = 1000., format='%.1f')
    nu = nu*1.0e-6

    Ub = st.number_input(label = "Bulk velocity, Ub (m s⁻¹)", value = 0.1, format='%.3f')


    if st.button("Calculate"):

        Re_ = Re(nu,h,Ub)
        Ro_ = Ro(omega,h,Ub)
        Ek_ = Ek(nu,omega,h)

        data = {"h": [h], "omega":[omega], "nu":[nu],"Ub":[Ub],"Re":[Re_],"Ro":Ro_, "Ek":[Ek_]}
        results = pd.DataFrame(data)
        results2 = convert_df(results)

        st.download_button(label="Download data as CSV", data=results2, file_name="my_file.csv", mime='text/csv')

        # results_choice = st.selectbox("Show results on the screen or save as a CSV file?", ("Screen", "CSV"))

        # results_choice = st.selectbox("Show results on the screen or save as a CSV file?", ("Screen", "CSV"))

        # if results_choice == "CSV" and st.button("CSV"):
        #     # if st.button("Save"):
        #         # file_name = st.text_input(label="file_name.csv", value="results.csv")

        #     open("results.csv", 'w').write(results.to_csv())
        #     st.write("File saved successfully.")
        # else:
        #     c1,c2 = st.columns(2)

        #     c1.subheader("Re: "); c2.subheader(f"{Re_:.3f}")
        #     c1.subheader("Ro: "); c2.subheader(f"{Ro_:.3f}")
        #     c1.subheader("Ek: "); c2.subheader(f"{Ek_:.4f}")

else:
    st.write("Upload model")

