import streamlit as st

# counter = 0
# st.write(counter)

# if st.button("up"):
#     counter += 1
#     st.write(counter)

if "counter" not in st.session_state:
    st.session_state.counter = 0

# st.write(st.session_state.counter)

if st.button("up"):
    st.write(st.session_state.counter )
    st.session_state.counter += 1

if st.button("reset"):
    st.session_state.counter = 0