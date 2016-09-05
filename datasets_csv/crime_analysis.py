# Crime arrest data analysis

# import modules
import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as	plt

# import the csv file
# all_data = pd.read_csv('urine_test_caught.csv')
# all_data = pd.read_csv('institution_case_caught.csv')
all_data = pd.read_csv('dda_1952_caught.csv')

all_data = all_data.dropna()
# print(all_data)
# print(all_data.columns)
# print(all_data.describe())

# urine test drug +
# print(all_data.set_index('Year').diff())
# pd.options.display.float_format = '{:.2f}%'.format
# print(all_data.set_index('Year').pct_change())

# arrested remanded in institutions
# print(all_data[all_data['Crime'] == 'Distributor'].describe())
# print(all_data[all_data['Crime'] == 'Distributor and Drug Addict'].describe())
# print(all_data[all_data['Crime'] == 'Drug Addict'].describe())

# drug crimes committed under DDA 1952
print(all_data[all_data['Dangerous Drug Act, 1952'] == 'Sec. 39B (Distributing)'].describe())
print(all_data[all_data['Dangerous Drug Act, 1952'] == 'Sec. 39A (Possession)'].describe())
print(all_data[all_data['Dangerous Drug Act, 1952'] == 'Other Sec.'].describe())
