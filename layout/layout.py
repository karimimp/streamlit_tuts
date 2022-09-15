import streamlit as st

def clean_text(txt):
    text = txt.replace("”", "'").replace("“","'").replace("-\n", "").replace("\n", " ").strip()
    return text

st.title(" Intro to Layout & Image ")

st.sidebar.image("logo.png", width=100)
st.sidebar.header("Options")
txt = st.sidebar.text_area("Paste text here")
btn1 = st.sidebar.button("Clean Text")

if btn1:
    col1, col2 = st.columns(2, gap="small")

    col1_expander = col1.expander("Expand original")
    with col1_expander:
        col1_expander.header("Original")
        col1_expander.write(txt)


    col2_expander = col2.expander("Cleaned Text")
    with col2_expander:
        col2_expander.header("Cleaned")
        clean = clean_text(txt)
        col2_expander.write(clean)



