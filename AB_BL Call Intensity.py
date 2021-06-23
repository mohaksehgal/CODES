#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 14:58:08 2020

@author: mohaksehgal
"""


import pandas as pd
import numpy as np

ALLOCATION=pd.read_excel(r'/Users/mohaksehgal/Documents/Work/MIS/AB/BL/MARCH 20/ABFL_BL ALLOCATION 17 JAN 20.xlsx')

ALLOCATION['AGREEMENTID']=ALLOCATION['AGREEMENTID'].astype(str)

A=pd.read_csv(r'/Users/mohaksehgal/Documents/Work/Call Intensity/AB_BL/MARCH 20/14-03-2020_Dump_Report.csv')

A=A.reset_index(drop=True)

A['LOAN NO.']=A['LOAN NO.'].astype(str)

C=pd.DataFrame(A.groupby(['LOAN NO.'])['Agent ID'].count()).reset_index()

for i in range(0,len(ALLOCATION['AGREEMENTID'])):
    for j in range(0,len(C['LOAN NO.'])):
        if ALLOCATION.loc[i,'AGREEMENTID']==C.loc[j,'LOAN NO.']:
            ALLOCATION.loc[i,'CALL INTENSITY']=C.loc[j,'Agent ID']
            
ALLOCATION.to_excel(r'/Users/mohaksehgal/Documents/Work/Call Intensity/AB_BL/MARCH 20/Overall Call Intensity.xlsx',index=False)