import streamlit as st
import time

#session state
if "photo" not in st.session_state:
    st.session_state["photo"] = "not done"

col1, col2, col3 = st.columns([1,2,1])
col1.markdown("# Welcome!")
col1.markdown("Info about the app")

def change_photo_state():
    st.session_state["photo"] = "done"


# upload photo
uploaded_photos = col2.file_uploader("Upload a photo", on_change=change_photo_state)
# camera input
camera_photo = col2.camera_input("Take a photo!", on_change=change_photo_state)

if st.session_state["photo"] == "done":
    progress_bar = col2.progress(0)
    for perc in range(100):
        time.sleep(0.05)
        progress_bar.progress(perc+1)

    col2.success("Photo uploaded successfully")

    col3.metric(label="Temperature", value="15 °C", delta="3 °C")

    with st.expander("Read more"):
        st.write("Hello, here are more details about this topic")
        if uploaded_photos is None:
            st.image(camera_photo)
        else:
            st.image(uploaded_photos)

