import pandas as pd
from faker import Faker
from tqdm import tqdm
import random

random.seed(42)
Faker.seed(42)

fake = Faker()

num_hospitals = 5
num_patients = 100000

hospital_data = {
    "hospital_id": list(range(1, num_hospitals + 1)),
    "hospital_name": [fake.company() for _ in range(num_hospitals)]
}
hospitals_df = pd.DataFrame(hospital_data)

patients = []
for i in tqdm(range(1,num_patients+1)):
    hospital_id = random.randint(1,num_hospitals)
    name = fake.name()
    dob = fake.date_of_birth(minimum_age=1,maximum_age=99)
    admit = fake.date_time_between(start_date='-2y',end_date='-1d')
    discharge = fake.date_time_between(start_date=admit,end_date='now')
    patients.append([i,hospital_id,name,dob,admit,discharge])

patients_df = pd.DataFrame(patients,columns=["patient_id", "hospital_id", "patient_name", "dob", "admission_datetime",
"discharge_datetime"])

diagnoses_list = ["Flu", "Diabetes", "Hypertension", "Asthma", "Covid-19", "Migraine"]
diagnoses = []
for pid in tqdm(patients_df['patient_id']):
    for _ in range(2):
        diagnoses.append([fake.uuid4(),pid,random.choice(diagnoses_list)])

diagnoses_df = pd.DataFrame(diagnoses,columns=['diagnosis_id', 'patient_id', 'diagnosis_name'])

medicines = ["Paracetamol", "Ibuprofen", "Aspirin", "Amoxicillin", "Metformin", "Atorvastatin"]
treatments = []
for pid in tqdm(patients_df['patient_id']):
    for _ in range(5):
        treatments.append([
            fake.uuid4(),
            pid,
            random.choice(medicines),
            fake.time(),
            random.randint(1,30)
        ])

treatments_df = pd.DataFrame(treatments,columns=['treatment_id', 'patient_id', 'medicine_name', 'dose_time', 'duration'])  

billing = []
for pid in tqdm(patients_df['patient_id']):
    billing.append([
        fake.uuid4(),
        pid,
        round(random.uniform(1000,5000),2),
        random.choice(["cash","credit"])
    ])

billing_df = pd.DataFrame(billing,columns=['bill_id', 'patient_id', 'bill_amount', 'payment_mode'])

hospitals_df.to_csv("hospitals.csv", index=False)
patients_df.to_csv("patients.csv", index=False)
diagnoses_df.to_csv("diagnoses.csv", index=False)
treatments_df.to_csv("treatments.csv", index=False)
billing_df.to_csv("billing.csv", index=False)