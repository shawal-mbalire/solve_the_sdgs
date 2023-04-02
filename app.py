#importing useful modules
import json
import os
import yaml
import openai 
import folium
import requests
import streamlit as st
import streamlit_authenticator as stauth
import pandas as pd

from streamlit_folium import st_folium
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

m = folium.Map(location=[0.34201915128408633, 32.59443256441762], zoom_start=16)
tooltip = "Liberty Bell"
folium.Marker(
    [39.949610, -75.150282], popup="Liberty Bell", tooltip=tooltip
).add_to(m)

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
    st.title("Patient Medications")
    st.write("Here you can view a list of your current medications, dosages, and instructions for use.")
    
    # Display list of current medications
    current_medications = ["Atenolol", "Azithromycin", "Melatonin"]
    selected_medication = st.selectbox("Select a medication", current_medications)
        
    # Set medication reminders
    st.write("Set a medication reminder:")
    dosage = st.number_input("Dosage (e.g. 1 tablet)")
    frequency = st.selectbox("Frequency", ["Daily", "Weekly", "Monthly"])
    start_date = st.date_input("Start date")
    end_date = st.date_input("End date")
    st.write(f"Reminder set for {dosage} of {selected_medication} {frequency.lower()} starting on {start_date} and ending on {end_date}.")
    

    # Get more information about the selected medication using OpenAI GPT API
    medication_info = chat(f"THi, can you tell me more about the medication {selected_medication}? I have been prescribed {dosage} tablets and I am concerned about possible side effects. I have a history of no disease, but I am not allergic to any medications. Can you provide more information about this medication and how it may impact my health?")
    st.write(f"**{selected_medication}**: {medication_info}")

    # Display map of nearby pharmacies
    st.write(" ## Nearby pharmacies:")
    # Add code to display a map of nearby pharmacies based on user location
    st_folium(m, width=1000, height=500, returned_objects=[])

    

    
    # Display upcoming appointments
    st.write(" ## Upcoming appointments:")
    # Add code to display a list of upcoming appointments with doctors
    st.write("You have no upcoming appointments.")

def reminders():
    #get all reminders
    st.write("# Reminders")
def patient_app():
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
def doctor_app():
    # Page title and header text
    st.write("<h1>Medication Management</h1>", unsafe_allow_html=True)
    st.write("<p>Keep track of your Patients' medications and appointments.</p>", unsafe_allow_html=True)

    # Navigation links
    nav_selection = st.sidebar.radio(label="Navigation", options=["Doctor dashboard", "Patient Profiles", "Appointments","Records"])

    if nav_selection == "Doctor dashboard":
        doctor_dashboard()
    elif nav_selection == "Patient Profiles":
        patient_profiles()
    elif nav_selection == "Appointments":
        appointment_scheduling()
    elif nav_selection == "Records":
        medical_records()
    
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


#patient functions
def load_health_map():
    """ TODO show a map with the nearest health facilities"""
    pass
def doctors_nearby():
    """ TODO show a list of doctors who can be consulted"""
    pass


#Doctor functions
def doctor_dashboard():
    st.title("Doctor Dashboard")
    st.write("Welcome to your dashboard! Here you can view your patient caseload, upcoming appointments, and any outstanding tasks or reminders.")
    
    st.write("Select a page to view:")
    page = st.selectbox("", ["Patient Profiles", "Appointment Scheduling", "Prescriptions", "Medical Records"])
    
    if page == "Patient Profiles":
        patient_profiles()
    elif page == "Appointment Scheduling":
        appointment_scheduling()
    elif page == "Prescriptions":
        prescriptions()
    elif page == "Medical Records":
        medical_records()
def patient_profiles():
    st.title("Patient Profiles")
    st.write("Here you can access detailed information about your patients, including medical history, test results, medication lists, and any other relevant health information.")

    # Load patient data from database
    patient_data = pd.read_csv("patient_data.csv") # Replace with appropriate data source
    
    # Display patient data in a table
    st.write("<h2>Patient Data</h2>", unsafe_allow_html=True)
    st.dataframe(patient_data)
# Define a function to create a new appointment
def create_appointment(name, date, time):
    appointment = pd.DataFrame({
        'Name': [name],
        'Date': [date],
        'Time': [time]
    })
    return appointment
# Define a function to display the appointment form
def appointment_form():
    name = st.text_input('Patient Name')
    date = st.date_input('Appointment Date')
    time = st.time_input('Appointment Time')
    if st.button('Schedule Appointment'):
        appointment = create_appointment(name, date, time)
        st.write('Appointment scheduled for:')
        st.write(appointment) 
def appointment_scheduling():
    st.title("Appointment Scheduling")
    st.write("Use this page to schedule appointments with your patients and manage your calendar.")
    appointment_form()
def prescriptions():
    st.title("Prescriptions")
    st.write("Here you can manage your patients' medication prescriptions, including renewals, dosage changes, and other medication-related tasks.")
    
    patients = pd.read_csv("patient_data.csv")
    
    # Select patient
    patient_name = st.selectbox("Select Patient", patients["Name"].unique())
    patient = patients.loc[patients["Name"] == patient_name].iloc[0]
    
    # Show patient info
    st.write(f"<h3>Patient Information</h3>",unsafe_allow_html=True)#Name,Age,Gender,Blood Type,Medical History,Medication List
    st.write(f"<b>Name:</b> {patient['Name']}<br>"
             f"<b>Age:</b> {patient['Age']}<br>"
             f"<b>Gender:</b> {patient['Gender']}<br>"
             f"<b>Address:</b> {patient['Blood Type']}<br>"
             f"<b>Phone:</b> {patient['Medical History']}<br>"
             f"<b>Email:</b> {patient['Medication List']}<br>", 
             unsafe_allow_html=True)
    
    # Show medication info
    st.write(f"<h3>Medication Information</h3>",unsafe_allow_html=True)
    medication_list = patient["Medication List"].split(", ")
    for medication in medication_list:
        st.write(f"<b>Medication:</b> {medication}<br>",
                 #f"<b>Dosage:</b> {patient[medication]}<br>"
                 #f"<b>Renewal Date:</b> {patient[medication+'_renewal']}<br>", 
                 unsafe_allow_html=True)
    
    # Renew medication
    st.write(f"<h3>Renew Medication</h3>",unsafe_allow_html=True)
    medication_to_renew = st.selectbox("Select Medication to Renew", medication_list)
    renewal_date = st.date_input("Select Renewal Date")
    if st.button("Renew"):
        #patients.loc[patients["name"] == patient_name, [medication_to_renew+"_renewal"]] = renewal_date
        patients.to_csv("patient_data.csv", index=False)
        st.success("Medication Renewed Successfully!")
def medical_records():
    # Page title and header text
    st.write("<h1>Medical Records</h1>", unsafe_allow_html=True)
    st.write("<p>Use this page to access and manage your patients' medical records, including test results, imaging scans, and other diagnostic information.</p>", unsafe_allow_html=True)

    # Load patient data
    patient_data = pd.read_csv("patient_data.csv")

    # Display patient selection dropdown
    selected_patient = st.selectbox("Select Patient", patient_data["Name"])

    # Filter patient data by selected patient
    selected_patient_data = patient_data[patient_data["Name"] == selected_patient]

    # Display patient information
    st.write(f"<h2>{selected_patient}</h2>", unsafe_allow_html=True)
    st.write("<h3>Medical History</h3>", unsafe_allow_html=True)
    try: st.write(selected_patient_data["Medical History"].iloc[0], unsafe_allow_html=True)
    except: st.write("No medical history available")
    try: st.write("<h3>Test Results</h3>", unsafe_allow_html=True)
    except: st.write("No test results available")
    try: st.write(selected_patient_data["Test Results"].iloc[0])
    except: st.write("No test results available")
    try: st.write("<h3>Imaging Scans</h3>", unsafe_allow_html=True)
    except: st.write("No test results available")
    try: st.write(selected_patient_data["Imaging Scans"].iloc[0], unsafe_allow_html=True)
    except: st.write("No test results available")

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
        doctor_app()
    else:
        st.write(f'Welcome *{name}*')
        patient_app()
elif st.session_state["authentication_status"] == False:
    st.error('Username/password is incorrect')
    try:
        if authenticator.register_user('Register user', preauthorization=False):
            st.success('User registered successfully')
            with open('config.yaml', 'w') as file:
                yaml.dump(config, file, default_flow_style=False)
    except Exception as e:
        st.error(e)
elif st.session_state["authentication_status"] == None:
    st.warning('Please enter your username and password')

