#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 17:44:04 2022

@author: peteloudovaris
"""

import pandas as pd
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import math
# read in the data
df = pd.read_excel(r'/Users/peteloudovaris/Desktop/FinMath Project/Assignment 2/project_data.xlsx')

# get the data from the time interval Jan 2007 - December 2010
setA = df.iloc[72:120, 1:]
# get the data from the time interval Jan 2016 - December 2019

setB = df.iloc[180:228, 1:]

setA_norm = np.log(setA+1)
setA_mean = np.mean(setA_norm)
print("Means - Set A: Jan '07 - Dec '10")
print(setA_mean)
setB_norm = np.log(setB+1)

setB_mean = np.mean(setB_norm)
print("Means - Set B: Jan '16 - Dec '19")

print(setB_mean)

B_setA = setA_norm.cov()
B_setB = setB_norm.cov()

print(B_setA)

A_07 = np.sum(setA_norm[:12])
A_08= np.sum(setA_norm[12:24])
A_09 = np.sum(setA_norm[24:36])
A_10 = np.sum(setA_norm[36:48])


mean_A = (A_07 + A_08 +A_09 +A_10)/4
print(mean_A)

setA_07_cov = setA_norm.iloc[:12].cov()
setA_08_cov = setA_norm.iloc[12:24].cov()
setA_09_cov = setA_norm.iloc[24:36].cov()
setA_10_cov = setA_norm.iloc[36:48].cov()

setA_07_corr = setA_norm.iloc[:12].corr()
setA_08_corr = setA_norm.iloc[12:24].corr()
setA_09_corr = setA_norm.iloc[24:36].corr()
setA_10_corr = setA_norm.iloc[36:48].corr()

print(setA_07_corr)