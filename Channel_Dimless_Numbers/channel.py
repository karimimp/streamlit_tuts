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

    c1,c2 = st.columns(2)

    c1.subheader("Re: "); c2.subheader(f"{Re_:.3f}")
    c1.subheader("Ro: "); c2.subheader(f"{Ro_:.3f}")
    c1.subheader("Ek: "); c2.subheader(f"{Ek_:.4f}")

    # st.balloons()

    # if st.button("Save"):
    results = {"h": h, "omega": omega, "nu": nu, "Re":Re_, "Ro": Ro_, "Ek":Ek_}
    df = pd.DataFrame(results, index=[0])

    st.write(df)
    # st.download_button(label="Download results as CSV", data=results, file_name="results.csv", mime='text/csv',)

        # with open("saved_data.pkl", 'wb') as file:  # write binary
        #     pickle.dump(results, file)


