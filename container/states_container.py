import streamlit as st

main_container = st.container()

if "counter" not in st.session_state:
    st.session_state.counter = 0

# st.write(st.session_state.counter)

if st.button("up"):
    main_container.write(st.session_state.counter )
    st.session_state.counter += 1

if st.button("reset"):
    st.session_state.counter = 0