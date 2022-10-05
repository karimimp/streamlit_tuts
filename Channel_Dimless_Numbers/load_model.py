import streamlit as st
from utilities import Re,Ro,Ek,convert_df
import pandas as pd
import numpy as np
import json


def show_load_model():
    st.subheader("Load You json File")
    user_file = st.file_uploader("json file", type=["json"])
    if user_file is not None:

        # st.write(user_file)
        json_file = json.load(user_file)
        # st.write(json_file)
        df = pd.json_normalize(json_file, meta=['h','omega','nu','Ub'])

        h = df["h"]/1.0e3
        omega = df["omega"]*np.pi/30
        nu = df["nu"]*1.0e-6
        Ub = df["Ub"]

        Re_ = Re(nu,h,Ub)
        Ro_ = Ro(omega,h,Ub)
        Ek_ = Ek(nu,omega,h)

        c1,c2 = st.columns(2)

        c1.markdown(r"# Re:")
        c2.metric(label=" ", value=f"{Re_[0]:.3f}")

        c1.markdown(r"# Ro:")
        c2.metric(label="", value=f"{Ro_[0]:.3f}")

        c1.markdown(r"# Ek:")
        c2.metric(label="", value=f"{Ek_[0]:.3f}")
