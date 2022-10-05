import streamlit as st
import numpy as np
import pandas as pd
from utilities import Re,Ro,Ek,convert_df
import json

def show_new_model():
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

        ## this is a working example of saving results as csv
        # data = {"h": [h], "omega":[omega], "nu":[nu],"Ub":[Ub],"Re":[Re_],"Ro":[Ro_], "Ek":[Ek_]}

        # temp = pd.DataFrame(data)
        # results = convert_df(temp)

        # st.download_button(label="Download data as CSV", data=results, file_name="results.csv", mime='text/csv')

        ## this is an example of saving as json file
        data = {"h": h, "omega":omega, "nu":nu,"Ub":Ub,"Re":Re_,"Ro":Ro_, "Ek":Ek_}
        json_string = json.dumps(data)
        # st.json(json_string, expanded=True)
        st.download_button(label="Download JSON",file_name="data.json",mime="application/json",data=json_string,
)

