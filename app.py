#importing useful modules
import json
import os
import yaml
import openai 
import requests
import streamlit as st
import streamlit_authenticator as stauth

from streamlit_lottie import st_lottie
from yaml.loader      import SafeLoader
from dotenv           import load_dotenv

#page settings
st.set_page_config(
    page_title           ="MedicMan",
    page_icon            =':pill:',
    layout               ="wide",
    initial_sidebar_state="expanded",
)
#hidding st watermark hamburger menu and header
st.markdown(
    """
    <style>
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
#set the api key
openai.api_key = API_KEY
chat_model     = "gpt-3.5-turbo"

#lets define useful functions
def chat(prompt):
    output = openai.ChatCompletion.create(
        model=chat_model,
        messages = [{"role":"user","content":prompt}],#roles are user system assistant
    )
    return output["choices"][0]["message"]["content"]#return the message
def home():
    # Display information about the application
    st.write("<h2>About</h2>", unsafe_allow_html=True)
    st.write("<p>Medication Management is a simple application that helps you manage your medications. You can add medications to your list, view information about them, and set reminders for when to take them.</p>", unsafe_allow_html=True)
    # Get list of medications from Redis database

    # Display list of medications

    st.write("<h2>Features</h2>", unsafe_allow_html=True)
    st.write("<ul><li>Add medications to your list</li><li>View information about medications, including potential side effects</li><li>Set reminders for when to take medications</li></ul>", unsafe_allow_html=True)

    # Display medication reminder scheduler
def medication_entry():
    # Medication entry form
    st.write("<h2>Add Medication</h2>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:med_name = st.text_input('Medication Name',key='form_med_name')
    with col2:dosage   = st.text_input('Dosage')
    with col3:schedule = st.selectbox('Schedule', ['Once a day', 'Twice a day', 'Three times a day'])

    if st.button('Add Medication'):
        add_medication(med_name, dosage, schedule)
        st.success(f"Added {med_name} to medication list")
        st.write("<h2>Medication Information Lookup</h2>", unsafe_allow_html=True)
def get_medication():
    med_lookup = st.text_input('Medication Name',key='med_lookup')
    if med_lookup:
        info = lookup_medication_info(med_lookup)
        st.write(f"<b>Medication:</b> {med_lookup}<br><b>Potential Side Effects:</b> {info}", unsafe_allow_html=True)
def medications():
    #det all medications
    st.write("# Medications")
def reminders():
    #get all reminders
    st.write("# Reminders")
def app():
    # Page title and header text
    st.write("<h1>Medication Management</h1>", unsafe_allow_html=True)
    st.write("<p>Keep track of your medications and set reminders for when to take them</p>", unsafe_allow_html=True)

    # Navigation links
    nav_selection = st.sidebar.radio(label="Navigation", options=["Home", "Medications", "Reminders"])

    if nav_selection == "Home":
        home()
    elif nav_selection == "Medications":
        medications()
    elif nav_selection == "Reminders":
        reminders()
    
    lottie_coding = load_lottiefile("cubicmaths.json")  # replace link to local lottie file
    #lottie_hello = load_lottieurl("https://lottiefiles.com/140746-cubicmaths")
    st_lottie(
        lottie_coding,
        speed=1,
        reverse=False, 
        loop=True,
        quality="low", # medium ; high
        #renderer="svg", # canvas
        height=500,
        width=None,
        key=None,    
    )  
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
def load_health_map():
    """ TODO show a map with the nearest health facilities"""
    pass
def doctors_nearby():
    """ TODO show a list of doctors who can be consulted"""
    pass
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
    authenticator.logout('Logout', 'sidebar')
    if username == 'jsmith':
        st.write(f'Welcome *{name}*')
        app()
    else:
        st.write(f'Welcome *{name}*')
        app()
elif st.session_state["authentication_status"] == False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] == None:
    st.warning('Please enter your username and password')

