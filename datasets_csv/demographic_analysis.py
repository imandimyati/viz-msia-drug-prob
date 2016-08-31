# Demographic data analysis

# import modules
import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as	plt

# import the csv file
# all_data = pd.read_csv('drug_addicts_gender.csv')
# all_data = pd.read_csv('drug_addicts_age.csv')
# all_data = pd.read_csv('drug_addicts_ethnic.csv')
# all_data = pd.read_csv('drug_addicts_education.csv')
# all_data = pd.read_csv('drug_addicts_occupation.csv')
# all_data = pd.read_csv('drug_addicts_reasons.csv')

all_data = all_data.dropna()
# print(all_data)
# print(all_data.columns)
# print(all_data.describe())

# gender
# print(all_data[all_data['Gender'] == 'Male'].describe())
# print(all_data[all_data['Gender'] == 'Female'].describe())
# print(all_data.set_index('Gender').diff())

# age
# print(all_data[all_data['Age'] == 'Under 13'].describe())
# print(all_data[all_data['Age'] == '13-15'].describe())
# print(all_data[all_data['Age'] == '16-19'].describe())
# print(all_data[all_data['Age'] == '20-24'].describe())
# print(all_data[all_data['Age'] == '25-29'].describe())
# print(all_data[all_data['Age'] == '30-34'].describe())
# print(all_data[all_data['Age'] == '35-39'].describe())
# print(all_data[all_data['Age'] == '40 and Over'].describe())
# print(all_data[all_data['Age'] == 'No Information'].describe())

# ethnic
# print(all_data[all_data['Ethnicity'] == 'Malay'].describe())
# print(all_data[all_data['Ethnicity'] == 'Bumiputera Sabah'].describe())
# print(all_data[all_data['Ethnicity'] == 'Bumiputera Sarawak'].describe())
# print(all_data[all_data['Ethnicity'] == 'Chinese'].describe())
# print(all_data[all_data['Ethnicity'] == 'Indian'].describe())
# print(all_data[all_data['Ethnicity'] == 'Others'].describe())

# education
# print(all_data[all_data['Education Qualifications'] == 'No Education'].describe())
# print(all_data[all_data['Education Qualifications'] == 'Primary School'].describe())
# print(all_data[all_data['Education Qualifications'] == 'LCE/SRP/PMR'].describe())
# print(all_data[all_data['Education Qualifications'] == 'MCE/SPM/SPMV'].describe())
# print(all_data[all_data['Education Qualifications'] == 'HSC/STP/STPM'].describe())
# print(all_data[all_data['Education Qualifications'] == 'Diploma'].describe())
# print(all_data[all_data['Education Qualifications'] == 'Degree/Master/PHD'].describe())
# print(all_data[all_data['Education Qualifications'] == 'Other Qualifications'].describe())

# occupation
# print(all_data[all_data['Occupation'] == 'Labour'].describe())
# print(all_data[all_data['Occupation'] == 'Unemployed'].describe())
# print(all_data[all_data['Occupation'] == 'Agriculture'].describe())
# print(all_data[all_data['Occupation'] == 'Services'].describe())
# print(all_data[all_data['Occupation'] == 'Sales'].describe())
# print(all_data[all_data['Occupation'] == 'Transportation'].describe())
# print(all_data[all_data['Occupation'] == 'Technical'].describe())
# print(all_data[all_data['Occupation'] == 'Construction'].describe())
# print(all_data[all_data['Occupation'] == 'Manufacturing'].describe())
# print(all_data[all_data['Occupation'] == 'Management'].describe())
# print(all_data[all_data['Occupation'] == 'Student'].describe())
# print(all_data[all_data['Occupation'] == 'Clerical'].describe())
# print(all_data[all_data['Occupation'] == 'Entertainment'].describe())
# print(all_data[all_data['Occupation'] == 'Part Time'].describe())

# reasons
# print(all_data[all_data['Reasons'] == 'For Fun'].describe())
# print(all_data[all_data['Reasons'] == 'Friends Influence'].describe())
# print(all_data[all_data['Reasons'] == 'Curiousity'].describe())
# print(all_data[all_data['Reasons'] == 'Stimulation'].describe())
# print(all_data[all_data['Reasons'] == 'Pain Killer'].describe())
# print(all_data[all_data['Reasons'] == 'Accidental'].describe())
# print(all_data[all_data['Reasons'] == 'Depression'].describe())
# print(all_data[all_data['Reasons'] == 'Other Reasons'].describe())
# print(all_data[all_data['Reasons'] == 'No Information'].describe())
