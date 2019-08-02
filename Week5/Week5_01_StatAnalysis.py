# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 16:17:21 2019

@author: user
"""
#Reference: https://scipy-lectures.org/packages/statistics/index.html

import os
os.chdir('C:/Users/user/Documents/CUHKPyTutorial2019-20190711T013955Z-001/CUHKPyTutorial2019/Week5')

import pandas as pd
data = pd.read_csv('brain_size.csv', sep=';', na_values=".")
data
data.info()
data.describe()

from scipy import stats
stats.describe(data['VIQ'])
#1-sample t-test
stats.ttest_1samp(data['VIQ'], 0)
#2-sample independent t-test
female_viq = data[data['Gender'] == 'Female']['VIQ']
male_viq = data[data['Gender'] == 'Male']['VIQ']
stats.ttest_ind(female_viq, male_viq)
#2-sample comparative t-test
stats.ttest_rel(data['FSIQ'], data['PIQ']) 
stats.ttest_1samp(data['FSIQ'] - data['PIQ'], 0)

#Exercise
#Q1. Test the difference between weights in males and females.
#Q2. Use non parametric statistics to test the difference between VIQ in males and females.
#(Hint: using scipy.stats.mannwhitneyu())

from statsmodels.formula.api import ols

model = ols("VIQ ~ Gender + 1", data)
results = model.fit()
print(results.summary())
model2 = ols('VIQ ~ Gender + Weight + Height + MRI_Count', data)
results2 = model2.fit()
print(results2.summary())
#Influence point checking
infl = results2.get_influence()
print(infl.summary_table())

from statsmodels.stats.api import anova_lm
#ANOVA for Model Comparison
table1 = anova_lm(results, results2)
print(table1)