from cProfile import label
import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
# pretty plot
plt.rcParams.update({'font.size': 10, 'font.family': 'monospace'})
plt.rcParams['axes.linewidth'] = 1.5
plt.rcParams['lines.linewidth'] = 2
plt.rcParams['lines.markersize'] = 8
plt.rcParams["image.cmap"] = "Set1"
line_styles = ['-', '--', ':', '-.']
marks = ['o', "s", "v", "X",  "H", "^", "p", "*", "8", "<", "p", "P", ">"]
all_colors = ["black", "red", "blue","green", "cyan", "magenta",  "navy", "darkviolet",  "seagreen", "saddlebrown", "teal", "crimson", "olive"]

def Ae(N, alfa, rpm):
    return N*np.sin(alfa)*rpm*np.pi/30


Ae_form = st.form(key="Variable")

alfa = Ae_form.slider("Cone Angle", min_value=30, max_value=45, step=1)
N = Ae_form.slider("Number of discs", min_value=20, max_value=150, step=1)
c1, c2 = Ae_form.columns(2)
min_rpm = c1.number_input("Minimum rpm", value=4000., format='%.0f')
max_rpm = c2.number_input("Maximum rpm", value=10000., format='%.0f')
rpms = np.linspace(min_rpm, max_rpm, num=10)

plot_choice = st.radio("Plotly or Matplotlib?", ('plotly', 'matplotlib'))
if Ae_form.form_submit_button("Explore"):
    results = []
    for rpm in rpms:
           results.append(Ae(N, alfa, rpm))

    df = pd.DataFrame({'rpm': rpms, 'Ae': results})

    if plot_choice == 'matplotlib':
        fig, ax = plt.subplots(dpi=150, tight_layout=True)
        ax.plot(df['rpm'], df['Ae'], color=all_colors[0], label='Ae')
        ax.grid(color='b', alpha=0.3, linestyle='dashed', linewidth=0.5, which="both")
        ax.set_xlabel('RPM')
        ax.set_ylabel('Ae')
        ax.legend(frameon=False, loc='best')
        st.pyplot(fig)
    else:
        fig = px.line(df, x='rpm', y="Ae", markers=True)
        fig.update_layout(width=800)
        st.write(fig)
