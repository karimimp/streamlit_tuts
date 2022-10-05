import streamlit as st
from new_model import show_new_model
from load_model import show_load_model

st.header("Rotating Channel Dimensionless Numbers")
model_choice = st.sidebar.selectbox("New model or load model", ("New", "Load"))

if model_choice == "New":
    show_new_model()
else:
    show_load_model()

# model_choice = st.sidebar.selectbox("New model or load model", ("New", "Load"))

# if model_choice == "New":
#     st.subheader("Input variables")
#     h = st.number_input(label = "Channel half-width, h (mm)", min_value = 0.01, value = 10., step = 1., format='%.1f')
#     h = h/1e3

#     omega = st.number_input(label = "Rotational, ω (rpm)", min_value = 0.0, value = 1000., step = 1., format='%.1f')
#     omega = omega*np.pi/30

#     nu = st.number_input(label = "Kinematic viscosity, υ (cSt)", min_value = 1., value = 1000., format='%.1f')
#     nu = nu*1.0e-6

#     Ub = st.number_input(label = "Bulk velocity, Ub (m s⁻¹)", value = 0.1, format='%.3f')


#     if st.button("Calculate"):

#         Re_ = Re(nu,h,Ub)
#         Ro_ = Ro(omega,h,Ub)
#         Ek_ = Ek(nu,omega,h)

#         data = {"h": [h], "omega":[omega], "nu":[nu],"Ub":[Ub],"Re":[Re_],"Ro":Ro_, "Ek":[Ek_]}
#         results = pd.DataFrame(data)
#         results2 = convert_df(results)

#         st.download_button(label="Download data as CSV", data=results2, file_name="my_file.csv", mime='text/csv')


# else:
#     st.write("Upload model")

