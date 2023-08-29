import streamlit as st

st.header('Contact me')

with st.form(key='contact_form'):
    email = st.text_input('Your email address')

    subject = st.text_input('Enter subject')

    details = st.text_area('Describe some details')

    submit = st.form_submit_button()

    if submit:
        st.success("Form submitted successfully!")



