#importing useful modules
import streamlit as st
import json
from streamlit_lottie import st_lottie
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import os
from dotenv import load_dotenv
import requests

#page settings
st.set_page_config(
    page_title="Streamlit Authentication",
    page_icon=":lock:",
    layout="wide",
    initial_sidebar_state="expanded",
)

#hidding st watermark hamburger menu and header
st.markdown(
    """
    <style>
    .reportview-container .main footer, .reportview-container .main header {
        display: none;
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True,
)

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

#Setup of the streamlit side bar

 
#setup of needed page settings


def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottiefile("cubicmaths.json")  # replace link to local lottie file
#lottie_hello = load_lottieurl("https://lottiefiles.com/140746-cubicmaths")

st_lottie(
    lottie_coding,
    speed=1,
    reverse=False, 
    loop=True,
    quality="low", # medium ; high
    #renderer="svg", # canvas
    height=None,
    width=None,
    key=None,    
)  
