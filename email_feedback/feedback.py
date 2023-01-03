import streamlit as st
import smtplib
import email

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


st.title(f"\U0001f9d0 \t Feedback")

with st.form("feedback", clear_on_submit=True):
    name = st.text_input("Name", placeholder='Enter your name')
    email = st.text_input("Email", placeholder='Enter your email')
    message = st.text_area("Feedback", placeholder='Enter your feedback')

    submit = st.form_submit_button("Submit")

    if submit:
        extra_info = """
        Sender email address: {}\n
        Sender name: {}\n
        """.format(email, name)

        message += extra_info
        # Create the email message
        msg = MIMEMultipart()
        msg['Subject'] = 'Example Email'
        msg['From'] = 'sender@example.com'
        msg['To'] = 'receiver@example.com'

        # Add the message body
        body = MIMEText(message)
        msg.attach(body)
        # this part does not work yet!
        # Connect to the email server and send the email
        server = smtplib.SMTP('smtp.gmail.com', 587)
        # server.connect("smtp.mail.yahoo.com", 465)
        server.login("karimimp@gmail.com", "password")
        server.send_message(msg)
        server.quit()

