import streamlit as st
import numpy as np
import pandas as pd

def Ae(N, alfa, rpm):
    return N*np.sin(alfa)*rpm*np.pi/30


Ae_form = st.form(key="Variables")

selected_variables = Ae_form.multiselect("Select the variables to explore", ["Number of discs", "Cone angle", "Bowl speed"])
data = {}
c1, c2 = Ae_form.columns(2)
for var in selected_variables:

    c1.number_input(label = var+" minimum", format='%.0f')
    c2.number_input(label = var+" maximum", format='%.0f')

# data = {"Number of discs": 1, "Cone angle":1, "Bowl speed":1}
# df = pd.DataFrame.from_dict(data, orient='index')


# c1.write("column1")

# c2.write("column2")

# min_val = 1
# max_val = 100

# st.write(np.linspace(min_val, max_val, num=10))

Ae_form.form_submit_button("Explore")

