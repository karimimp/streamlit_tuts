from turtle import width
import streamlit as st
import numpy as np
from utilities import Ro, Ek
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

def show_explore_model():

    independent_variable = st.selectbox("Independent variable", ["channel height","rotation speed"])

    if independent_variable == "channel height":
        c1, c2 = st.columns(2)
        h_min = c1.number_input(label='Min height', value=1., format='%.0f')
        h_max = c2.number_input(label='Max height', value=100., format='%.0f')
        h_range = np.linspace(h_min/1e3, h_max/1e3, num=10)

        rpm = st.slider("RPM", min_value=0, max_value=20000, step=1)
        omega = rpm*np.pi/30

        u = st.slider("Bulk velocity, Ub (m s⁻¹)", min_value=0.001, max_value=10.)
        u = [0.5*u, u, 1.5*u]

        nu = st.number_input(label = "Kinematic viscosity, υ (cSt)", min_value = 1., value = 1000., format='%.1f')
        nu = nu*1.0e-6
        nu = [0.5*nu, nu, 1.5*nu]

        Ro_u0 = []; Ro_u1 = []; Ro_u2 = []
        Ek_nu0 = []; Ek_nu1 = []; Ek_nu2 = []
        for i in range(len(h_range)):
            Ro_u0.append(Ro(omega, h_range[i], u[0]))
            Ro_u1.append(Ro(omega, h_range[i], u[1]))
            Ro_u2.append(Ro(omega, h_range[i], u[2]))
            Ek_nu0.append(Ek(nu[0],omega, h_range[i]))
            Ek_nu1.append(Ek(nu[1],omega, h_range[i]))
            Ek_nu2.append(Ek(nu[2],omega, h_range[i]))

        df = pd.DataFrame({'h': h_range, 'Ro_u0': Ro_u0, 'Ro_u1': Ro_u1, 'Ro_u2': Ro_u2, 'Ek_nu0': Ek_nu0, 'Ek_nu1': Ek_nu1,'Ek_nu2': Ek_nu2})

        fig0 = go.Figure()
        names_fig0 = [f"Ub = {u[0]:.2f}", f"Ub = {u[1]:.2f}", f"Ub = {u[2]:.2f}"]
        fig0.add_trace(go.Scatter(x=df['h']*1e3, y=df['Ro_u0'], name=names_fig0[0]) )
        fig0.add_trace(go.Scatter(x=df['h']*1e3, y=df['Ro_u1'], name=names_fig0[1]))
        fig0.add_trace(go.Scatter(x=df['h']*1e3, y=df['Ro_u2'], name=names_fig0[2]))
        fig0.update_layout(
            title="Rossby number",
            xaxis_title="Channel Height, [mm]",
            yaxis_title="Ro, [-]",
            # legend_title="Legend Title",
            font=dict(family="monospace",size=16,color="RebeccaPurple"),
            width=800,
            height=500
        )
        st.write(fig0)

        fig1 = go.Figure()
        names_fig1 = [f"nu = {nu[0]/1e-6:.1f}", f"nu = {nu[1]/1e-6:.1f}", f"nu = {nu[2]/1e-6:.1f}"]
        fig1.add_trace(go.Scatter(x=df['h']*1e3, y=df['Ek_nu0'], name=names_fig1[0]) )
        fig1.add_trace(go.Scatter(x=df['h']*1e3, y=df['Ek_nu1'], name=names_fig1[1]))
        fig1.add_trace(go.Scatter(x=df['h']*1e3, y=df['Ek_nu2'], name=names_fig1[2]))
        fig1.update_layout(
            title="Ekman Number",
            xaxis_title="Channel Height, [mm]",
            yaxis_title="Ek, [-]",
            # legend_title="Legend Title",
            font=dict(family="monospace",size=16,color="RebeccaPurple"),
            width=800,
            height=500
        )
        st.write(fig1)

    else:
        c1, c2 = st.columns(2)
        rpm_min = c1.number_input(label='Min rpm', value=1., format='%.0f')
        rpm_max = c2.number_input(label='Max rpm', value=1000., format='%.0f')
        omega_range = np.linspace(rpm_min*np.pi/30, rpm_max*np.pi/30, num=10)

        h = st.slider("Channel height, h (mm)", min_value=0.01, max_value=1000.0)
        h = h/1.0e3

        u = st.slider("Bulk velocity, Ub (m s⁻¹)", min_value=0.001, max_value=10.)
        u = [0.5*u, u, 1.5*u]

        nu = st.number_input(label = "Kinematic viscosity, υ (cSt)", min_value = 1., value = 1000., format='%.1f')
        nu = nu*1.0e-6
        nu = [0.5*nu, nu, 1.5*nu]

        Ro_u0 = []; Ro_u1 = []; Ro_u2 = []
        Ek_nu0 = []; Ek_nu1 = []; Ek_nu2 = []
        for i in range(len(omega_range)):
            Ro_u0.append(Ro(omega_range[i], h, u[0]))
            Ro_u1.append(Ro(omega_range[i], h, u[1]))
            Ro_u2.append(Ro(omega_range[i], h, u[2]))
            Ek_nu0.append(Ek(nu[0],omega_range[i], h))
            Ek_nu1.append(Ek(nu[1],omega_range[i], h))
            Ek_nu2.append(Ek(nu[2],omega_range[i], h))

        df = pd.DataFrame({'rpm': omega_range, 'Ro_u0': Ro_u0, 'Ro_u1': Ro_u1, 'Ro_u2': Ro_u2, 'Ek_nu0': Ek_nu0, 'Ek_nu1': Ek_nu1,'Ek_nu2': Ek_nu2})

        fig0 = go.Figure()
        names_fig0 = [f"Ub = {u[0]:.2f}", f"Ub = {u[1]:.2f}", f"Ub = {u[2]:.2f}"]
        fig0.add_trace(go.Scatter(x=df['rpm']*30/np.pi, y=df['Ro_u0'], name=names_fig0[0]) )
        fig0.add_trace(go.Scatter(x=df['rpm']*30/np.pi, y=df['Ro_u1'], name=names_fig0[1]))
        fig0.add_trace(go.Scatter(x=df['rpm']*30/np.pi, y=df['Ro_u2'], name=names_fig0[2]))
        fig0.update_layout(
            title="Rossby number",
            xaxis_title="Rotational Speed, [rpm]",
            yaxis_title="Ro, [-]",
            # legend_title="Legend Title",
            font=dict(family="monospace",size=16,color="RebeccaPurple"),
            width=800,
            height=500
        )
        st.write(fig0)

        fig1 = go.Figure()
        names_fig1 = [f"nu = {nu[0]/1e-6:.1f}", f"nu = {nu[1]/1e-6:.1f}", f"nu = {nu[2]/1e-6:.1f}"]
        fig1.add_trace(go.Scatter(x=df['rpm']*30/np.pi, y=df['Ek_nu0'], name=names_fig1[0]) )
        fig1.add_trace(go.Scatter(x=df['rpm']*30/np.pi, y=df['Ek_nu1'], name=names_fig1[1]))
        fig1.add_trace(go.Scatter(x=df['rpm']*30/np.pi, y=df['Ek_nu2'], name=names_fig1[2]))
        fig1.update_layout(
            title="Ekman Number",
            xaxis_title="Rotational Speed, [rpm]",
            yaxis_title="Ek, [-]",
            # legend_title="Legend Title",
            font=dict(family="monospace",size=16,color="RebeccaPurple"),
            width=800,
            height=500
        )
        st.write(fig1)
