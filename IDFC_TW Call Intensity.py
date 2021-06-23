#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 14:42:07 2020

@author: mohaksehgal
"""


import pandas as pd
import numpy as np

ALLOCATION=pd.read_excel(r'/Users/mohaksehgal/Documents/Work/MIS/IDFC TW/MARCH 20/IDFC_TW Allocation 09 MARCH 20.xlsx')

A=pd.read_csv(r'/Users/mohaksehgal/Documents/Work/Call Intensity/IDFC TW/MARCH 20/12-03-2020_Dump_Report.csv')

C=pd.DataFrame(A.groupby(['LOAN NO.'])['Agent ID'].count()).reset_index()

for i in range(0,len(ALLOCATION['AGREEMENTID'])):
    for j in range(0,len(C['LOAN NO.'])):
        if ALLOCATION.loc[i,'AGREEMENTID']==C.loc[j,'LOAN NO.']:
            ALLOCATION.loc[i,'CALL INTENSITY']=C.loc[j,'Agent ID']
            
ALLOCATION.to_excel(r'/Users/mohaksehgal/Documents/Work/Call Intensity/IDFC TW/MARCH 20/ONLY 1 Call.xlsx',index=False)

