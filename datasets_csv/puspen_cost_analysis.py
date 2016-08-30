# Data analysis for Compulsory Rehab Cost

# import modules
import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as	plt

# import the csv file
# all_data = pd.read_csv('puspen_cost.csv')
# all_data = pd.read_csv('mmt_cost.csv')
all_data = pd.read_csv('nsp_cost.csv')

all_data = all_data.dropna()
#print(all_data)
print(all_data.columns)
print(all_data.describe())

# puspen cost
# print(all_data['Number of Residents'])
# print(all_data['Cost Estimate (RM)'])

# Difference between the years for Cost Estimate and Number of Residents
print(all_data.set_index('Year').diff())
pd.options.display.float_format = '{:.2f}%'.format
print(all_data.set_index('Year').pct_change())
