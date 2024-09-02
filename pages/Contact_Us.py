import streamlit as st
import pandas as pd
from send_email import send_mail


st.header('Contact us')

df = pd.read_csv(r'C:\Users\mrokas\PycharmProjects\WebdesignSoloproject\topics.csv')
topic=[]
for items,row in df.iterrows():
    topic.append(row['topic'])

with st.form(key="contact_form",clear_on_submit=True):
    user_email = st.text_input('Your email address:',key='entry_email')
    topic = st.selectbox('Choose a topic:',topic,key='topic')
    email_body = st.text_area('Your message here',key = 'email_body')
    button = st.form_submit_button('Send Email')
    if button:
        #print(user_email, topic, email_body)
        send_mail(topic, email_body, user_email)
        st.rerun()



#st.session_state