# Data analysis for AADK Spending

# import modules
import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as	plt

# import the csv file
all_data = pd.read_csv('aadk_cost.csv')
# all_data = pd.read_csv('seizure_value.csv')

all_data = all_data.dropna()
#print(all_data)
print(all_data.columns)
# print(all_data.describe())

# aadk spending
print(all_data['Cost (RM)'])
print(all_data['Total Cost (RM)'])
print(all_data[all_data['Purpose'] == 'Development'].describe())
print(all_data[all_data['Purpose'] == 'Operation'].describe())

# seizure value
# print(all_data[all_data['Year'] == 2013].describe())
# print(all_data[all_data['Year'] == 2014].describe())
# print(all_data[all_data['Type of Drug'] == 'Heroin'].describe())
# print(all_data[all_data['Type of Drug'] == 'Marijuana'].describe())
