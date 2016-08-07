# Data analysis for Drug Addicts by Gender

# import modules
import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as	plt

# import the csv file
all_data = pd.read_csv('drug_addicts_gender.csv')
all_data = all_data.dropna()
#print(all_data)

print(all_data.columns)
print(all_data.describe())
print(all_data['Total'])
print(all_data[all_data['Year'] == 'Male']).describe())

# # BMI of 30 or higher is considered obese (Higher number of countries with obese female)
# obese_female = all_data[all_data['Avg Female BMI'] > 30]
# print("number of countries with obese female throughout 1980 until 2007:", len(obese_female))
#
# obese_male = all_data[all_data['Avg Male BMI'] > 30]
# print("number of countries with obese male throughout 1980 until 2007:", len(obese_male))
#
# # Recent years have higher number countries with obese people
# print("Year: %d" % len(obese_female[obese_female['Year'] == 2007]))
# print("Year: %d" % len(obese_male[obese_male['Year'] == 2007]))
#
# # BMI of 18.5 below is considered obese (No countries with male underweight, )
# under_female = all_data[all_data['Avg Female BMI'] < 18.5]
# print("countries with underweight female throughout 1980 until 2007:", under_female)
#
# under_male = all_data[all_data['Avg Male BMI'] < 18.5]
# print("number of countries with underweight male throughout 1980 until 2007:", len(under_male))
#
# # Food supply (normal range is 1500-3000 kilocalories per day)
# low_supply = all_data[all_data['Kilocalories Per Day'] < 1500]
# print("countries with low food supply throughout 1980 until 2007:", low_supply)
#
# high_supply = all_data[all_data['Kilocalories Per Day'] > 3000]
# print("number of countries with high food supply throughout 1980 until 2007:", len(high_supply))
#
# higher_supply = all_data[all_data['Kilocalories Per Day'] > 3500] # almost 500g
# print("number of countries with high food supply throughout 1980 until 2007:", len(higher_supply))
#
# # obese female boxplot
# female_bmi = obese_female['Avg Female BMI']
# fig	= plt.figure()
# ax	= fig.add_axes([0.1, 0.1, 0.8, 0.8])
# ax.boxplot([female_bmi])
# ax.set_xlabel('')
# ax.set_ylabel('Avg Female BMI\n(kg/sqm)')
# ax.set_title('Number of countries with obese female from 1980-2007')
# ax.set_xticks([1])
# ax.set_xticklabels([''])
# #plt.show()
#
# # obese male boxplot
# male_bmi = obese_male['Avg Male BMI']
# fig	= plt.figure()
# ax	= fig.add_axes([0.1, 0.1, 0.8, 0.8])
# ax.boxplot([male_bmi])
# ax.set_xlabel('')
# ax.set_ylabel('Avg Male BMI\n(kg/sqm)')
# ax.set_title('Number of countries with obese male from 1980-2007')
# ax.set_xticks([1])
# ax.set_xticklabels([''])
# #plt.show()
#
# # comparison female and male, in terms of number of countries with obesity throughout the years
# fig	= plt.figure()
# ax = fig.add_axes([0.1,	0.1, 0.8, 0.8])
# counts = [obese_male,	obese_female]
# labels = ['Male', 'Female']
# colors = ['yellowgreen', 'gold']
# explode = [0, 0.1]
# ax.pie( counts, labels=labels, explode=explode, colors=colors)
# ax.set_title('Gender Comparison')
# plt.show()
#
# # Get descriptive statistics (to check avg/mean)
# # the 00's
# year_2007 = all_data[all_data['Year'] == 2007]['Kilocalories Per Day']
# # year_2006 = all_data[all_data['Year'] == 2006]['Kilocalories Per Day']
# # year_2005 = all_data[all_data['Year'] == 2005]['Kilocalories Per Day']
# # year_2004 = all_data[all_data['Year'] == 2004]['Kilocalories Per Day']
# # year_2003 = all_data[all_data['Year'] == 2005]['Kilocalories Per Day']
# # year_2002 = all_data[all_data['Year'] == 2002]['Kilocalories Per Day']
# # year_2001 = all_data[all_data['Year'] == 2001]['Kilocalories Per Day']
# # year_2000 = all_data[all_data['Year'] == 2000]['Kilocalories Per Day']
#
# # the 90's
# # year_1999 = all_data[all_data['Year'] == 1999]['Kilocalories Per Day']
# # year_1998 = all_data[all_data['Year'] == 1998]['Kilocalories Per Day']
# # year_1997 = all_data[all_data['Year'] == 1997]['Kilocalories Per Day']
# # year_1996 = all_data[all_data['Year'] == 1996]['Kilocalories Per Day']
# # year_1995 = all_data[all_data['Year'] == 1995]['Kilocalories Per Day']
# # year_1994 = all_data[all_data['Year'] == 1994]['Kilocalories Per Day']
# # year_1993 = all_data[all_data['Year'] == 1993]['Kilocalories Per Day']
# # year_1992 = all_data[all_data['Year'] == 1992]['Kilocalories Per Day']
# # year_1991 = all_data[all_data['Year'] == 1991]['Kilocalories Per Day']
# # year_1990 = all_data[all_data['Year'] == 1990]['Kilocalories Per Day']
#
# # the 90's
# # year_1989 = all_data[all_data['Year'] == 1989]['Kilocalories Per Day']
# # year_1988 = all_data[all_data['Year'] == 1988]['Kilocalories Per Day']
# # year_1987 = all_data[all_data['Year'] == 1987]['Kilocalories Per Day']
# # year_1986 = all_data[all_data['Year'] == 1986]['Kilocalories Per Day']
# # year_1985 = all_data[all_data['Year'] == 1985]['Kilocalories Per Day']
# # year_1984 = all_data[all_data['Year'] == 1984]['Kilocalories Per Day']
# # year_1983 = all_data[all_data['Year'] == 1983]['Kilocalories Per Day']
# # year_1982 = all_data[all_data['Year'] == 1982]['Kilocalories Per Day']
# # year_1981 = all_data[all_data['Year'] == 1981]['Kilocalories Per Day']
# year_1980 = all_data[all_data['Year'] == 1980]['Kilocalories Per Day']
#
# #Calculate descriptive statistics (Useful to get average/mean total in a year, implemented in timeline bar)
# # the 00's
# print(year_2007.describe())
# # print(year_2006.describe())
# # print(year_2005.describe())
# # print(year_2004.describe())
# # print(year_2003.describe())
# # print(year_2002.describe())
# # print(year_2001.describe())
# # print(year_2000.describe())
#
# # the 90's
# # print(year_1999.describe())
# # print(year_1998.describe())
# # print(year_1997.describe())
# # print(year_1996.describe())
# # print(year_1995.describe())
# # print(year_1994.describe())
# # print(year_1993.describe())
# # print(year_1992.describe())
# # print(year_1991.describe())
# # print(year_1990.describe())
#
# # the 80's
# # print(year_1989.describe())
# # print(year_1988.describe())
# # print(year_1987.describe())
# # print(year_1986.describe())
# # print(year_1985.describe())
# # print(year_1984.describe())
# # print(year_1983.describe())
# # print(year_1982.describe())
# # print(year_1981.describe())
# print(year_1980.describe())
#
# #Statistical test
# # result = stats.ttest_ind(year_1980, year_2007)
# # print(result)
#
# # print(stats.shapiro(year_1980))
# # print(stats.shapiro(year_2007))
