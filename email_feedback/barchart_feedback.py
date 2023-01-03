import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.title(f"\U0001f9d0 \t Feedback")
st.markdown("---")

if "mdf" not in st.session_state:
    st.session_state.mdf = pd.DataFrame(columns=['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7'])


idx = st.text_input(label="Name", placeholder="Optional")
q1 = st.slider(label="Q1: How friendly is the PyHSS web app?", min_value = 1, max_value = 5, step=1, key="q1")

q2 = st.slider(label="Q2: How likely are you to recommend the web app to a colleague? ", min_value=1, max_value=5, step=1, key="q2")

q3 = st.slider(label="Q3: On a scale of 1 to 5, how likely are you to use the web app again?", min_value = 1, max_value = 5, step=1, key="q3")

q4 = st.slider(label="Q4: How likely are you to use the web app in place of a different tool or service you currently use?", min_value = 1, max_value = 5, step=1, key="q4")

q5 = st.slider(label="Q5: How likely are you to use the web app while traveling or on the go?", min_value = 1, max_value = 5, step=1, key="q5")

q6 = st.slider(label="Q6: How likely are you to use the web app more or less frequently in the future?", min_value = 1, max_value = 5, step=1, key="q6")

q7 = st.slider(label="Q7: How likely are you to use the web app in conjunction with other tools or services?", min_value = 1, max_value = 5, step=1, key="q7")

run = st.button('Submit')

df_new = pd.DataFrame({'Q1': q1, 'Q2': q2, 'Q3': q3, 'Q4': q4, 'Q5': q5, 'Q6': q6, 'Q7': q7}, index=[idx])

if run:
    st.session_state.mdf = pd.concat([st.session_state.mdf, df_new], axis=0)
    # st.dataframe(st.session_state.mdf)
    # updated_df = st.dataframe(st.session_state.mdf)
    questions = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7']
    answers = [st.session_state.mdf['Q1'].mean(), st.session_state.mdf['Q2'].mean(), st.session_state.mdf['Q3'].mean(), st.session_state.mdf['Q4'].mean(), st.session_state.mdf['Q5'].mean(), st.session_state.mdf['Q6'].mean(), st.session_state.mdf['Q7'].mean()]
    # fig = go.Figure()
    fig = go.Figure(data=[go.Bar(x=questions, y=answers,
                hovertext=['How friendly', 'Recommend to colleague', 'Use it again', 'Replace other tools', 'While traveling', 'Future use', 'With other tools'])])
    # Customize aspect
    fig.update_traces(
        marker_color='rgba(107,118,250,255)',
        marker_line_color='rgba(57,70,253,255)',
        marker_line_width=2, opacity=0.5
        )
    fig.update_layout(
            title="Average score",
            font=dict(family="monospace",size=16,color="RebeccaPurple"),
            width=680,
            height=500
        )
    st.write(fig)

st.write(f"Total: {st.session_state.mdf.shape[0]}")