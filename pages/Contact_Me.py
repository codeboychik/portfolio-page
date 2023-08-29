import re
import streamlit as st
from send_email import send_email

st.header('Contact me')

with st.form(key='contact_form'):
    st.info('All fields are mandatory.')
    email = st.text_input('Your email address')
    subject = st.text_input('Enter subject').strip()
    details = st.text_area('Describe some details').strip()
    submit = st.form_submit_button()

    if submit:
        if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email) is not None\
                and len(details) > 0 and len(subject) > 0:
            send_email(receiver=email, subject=subject, details=details)
            st.success("Form submitted successfully!")
        else:
            st.error('An error occured.')



