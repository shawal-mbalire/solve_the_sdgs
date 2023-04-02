"""import csv

# Define the data for the 10 dummy patients
dummy_patients = [
    {"Name": "John Doe", "Age": 35, "Gender": "Male", "Blood Type": "A+", "Medical History": "N/A", "Medication List": "Ibuprofen 400mg, Vitamin C 500mg"},
    {"Name": "Jane Smith", "Age": 45, "Gender": "Female", "Blood Type": "B+", "Medical History": "High blood pressure", "Medication List": "Lisinopril 10mg, Metoprolol 50mg"},
    {"Name": "David Kim", "Age": 28, "Gender": "Male", "Blood Type": "AB+", "Medical History": "N/A", "Medication List": "N/A"},
    {"Name": "Emily Chen", "Age": 22, "Gender": "Female", "Blood Type": "O-", "Medical History": "N/A", "Medication List": "N/A"},
    {"Name": "Michael Brown", "Age": 60, "Gender": "Male", "Blood Type": "A-", "Medical History": "Diabetes, High cholesterol", "Medication List": "Metformin 1000mg, Atorvastatin 40mg"},
    {"Name": "Samantha Lee", "Age": 32, "Gender": "Female", "Blood Type": "B-", "Medical History": "Asthma", "Medication List": "Albuterol inhaler, Fluticasone nasal spray"},
    {"Name": "William Davis", "Age": 47, "Gender": "Male", "Blood Type": "O+", "Medical History": "N/A", "Medication List": "N/A"},
    {"Name": "Amy Johnson", "Age": 55, "Gender": "Female", "Blood Type": "A+", "Medical History": "Depression", "Medication List": "Fluoxetine 20mg"},
    {"Name": "Richard Martinez", "Age": 42, "Gender": "Male", "Blood Type": "B+", "Medical History": "N/A", "Medication List": "N/A"},
    {"Name": "Lisa Garcia", "Age": 30, "Gender": "Female", "Blood Type": "AB-", "Medical History": "N/A", "Medication List": "N/A"},
]

# Open the CSV file in append mode and write the dummy patient data to it
with open("patient_data.csv", mode="a", newline="") as csv_file:
    fieldnames = ["Name", "Age", "Gender", "Blood Type", "Medical History", "Medication List"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    writer.writeheader()
    
    # Write the data for each dummy patient to the CSV file
    for patient in dummy_patients:
        writer.writerow(patient)
"""
import database as db
dummy_patients = [
    {"Name": "John Doe", "Age": 35, "Gender": "Male", "Blood Type": "A+", "Medical History": "N/A", "Medication List": "Ibuprofen 400mg, Vitamin C 500mg"},
    {"Name": "Jane Smith", "Age": 45, "Gender": "Female", "Blood Type": "B+", "Medical History": "High blood pressure", "Medication List": "Lisinopril 10mg, Metoprolol 50mg"},
    {"Name": "David Kim", "Age": 28, "Gender": "Male", "Blood Type": "AB+", "Medical History": "N/A", "Medication List": "N/A"},
    {"Name": "Emily Chen", "Age": 22, "Gender": "Female", "Blood Type": "O-", "Medical History": "N/A", "Medication List": "N/A"},
    {"Name": "Michael Brown", "Age": 60, "Gender": "Male", "Blood Type": "A-", "Medical History": "Diabetes, High cholesterol", "Medication List": "Metformin 1000mg, Atorvastatin 40mg"},
    {"Name": "Samantha Lee", "Age": 32, "Gender": "Female", "Blood Type": "B-", "Medical History": "Asthma", "Medication List": "Albuterol inhaler, Fluticasone nasal spray"},
    {"Name": "William Davis", "Age": 47, "Gender": "Male", "Blood Type": "O+", "Medical History": "N/A", "Medication List": "N/A"},
    {"Name": "Amy Johnson", "Age": 55, "Gender": "Female", "Blood Type": "A+", "Medical History": "Depression", "Medication List": "Fluoxetine 20mg"},
    {"Name": "Richard Martinez", "Age": 42, "Gender": "Male", "Blood Type": "B+", "Medical History": "N/A", "Medication List": "N/A"},
    {"Name": "Lisa Garcia", "Age": 30, "Gender": "Female", "Blood Type": "AB-", "Medical History": "N/A", "Medication List": "N/A"},
]

for user in dummy_patients:
    db.insert_user(user)