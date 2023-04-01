#importing useful modules
import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import os
from dotenv import load_dotenv

#loading environment variables
load_dotenv(".env")
API_KEY = os.getenv("API_KEY")

with open("config.yaml") as ymlfile:
    config = yaml.load(ymlfile, Loader=SafeLoader)

#creating authentication object
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

#render login widget
name, authentication_status, username = authenticator.login('login', 'main')

#if authentication_status:
#    authenticator.logout('Logout', 'main')
#    st.write(f'Welcome *{name}*')
#    st.title('Some content')
#elif authentication_status == False:
#    st.error('Username/password is incorrect')
#elif authentication_status == None:
#    st.warning('Please enter your username and password')

if st.session_state["authentication_status"]:
    authenticator.logout('Logout', 'main')
    if username == 'jsmith':
        st.write(f'Welcome *{name}*')
        st.title('Application 1')
        authenticator.logout('Logout1', 'sidebar')
    elif username == 'rbriggs':
        st.write(f'Welcome *{name}*')
        st.title('Application 2')
        authenticator.logout('Logout1', 'sidebar')
elif st.session_state["authentication_status"] == False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] == None:
    st.warning('Please enter your username and password')

#loging in users using stauth


#Setup of the streamlit side bar

 
#setup of needed page settings


