import streamlit as st
import pandas as pd

st.title("Session States and Call Back Functions")

if 'number_of_rows' not in st.session_state or 'type' not in st.session_state:
    st.session_state['number_of_rows'] = 5 # create the variable
    st.session_state['type'] = 'normalized'

df = pd.read_csv("data.csv")
df.columns = "y/h y+ U/Ub U+ u v w uv".split()


increment = st.button('Show more columns')
if increment:
    st.session_state.number_of_rows += 1

decrement = st.button("Show fewer columns")
if decrement:
    st.session_state.number_of_rows -= 1

st.table(df.head(st.session_state['number_of_rows']))

st.write(st.session_state) # every time you click, it runs from top to bottom

types = {'normalized': ['y/h', 'U/Ub'], 'plus': ['y+', 'U+'], 'prime': ['u', 'v', 'w', 'uv']}

# using call back function
def handle_click(new_type):
    st.session_state.type = new_type

def handle_without_button():
    if st.session_state.type:
        st.session_state.type=st.session_state.new_kind

column = st.selectbox('Select a column:', types[st.session_state['type']])
## no call back
# st.session_state['type'] = st.radio("What kind of results?", ['normalized', 'plus', 'prime'])

## with call back
# type_of_analysis = st.radio("What kind of results?", ['normalized', 'plus', 'prime'])
# change = st.button('Change', on_click=handle_click, args=[type_of_analysis])
# without button
type_of_analysis = st.radio("What kind of results?", ['normalized', 'plus', 'prime'], on_change=handle_without_button, key='new_kind')


if st.session_state['type'] == 'normalized':
    st.table(df[types['normalized']])
elif st.session_state['type'] == 'plus':
    st.table(df[types['plus']])
else:
    st.table(df[types['prime']])
