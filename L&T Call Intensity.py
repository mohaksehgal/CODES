#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 14:42:09 2020

@author: mohaksehgal
"""


import pandas as pd
import numpy as np

ALLOCATION=pd.read_excel(r'/Users/mohaksehgal/Documents/Work/MIS/L_T/MARCH 20/L_T Allocation 09 MAR 20.xlsx')

ALLOCATION['AGREEMENTID']=ALLOCATION['AGREEMENTID'].astype(str)

A1=pd.read_csv(r'/Users/mohaksehgal/Documents/Work/Call Intensity/L_T/MARCH 20/12-03-2020_Dump_Report M.csv')

A2=pd.read_csv(r'/Users/mohaksehgal/Documents/Work/Call Intensity/L_T/MARCH 20/12-03-2020_Dump_Report R.csv')

A3=pd.read_csv(r'/Users/mohaksehgal/Documents/Work/Call Intensity/L_T/MARCH 20/12-03-2020_Dump_Report V.csv')

A=pd.concat([A1,A2])

A=pd.concat([A,A3])

A=A.reset_index(drop=True)

A['LOAN NO.']=A['LOAN NO.'].astype(str)

C=pd.DataFrame(A.groupby(['LOAN NO.'])['Agent ID'].count()).reset_index()

for i in range(0,len(ALLOCATION['AGREEMENTID'])):
    for j in range(0,len(C['LOAN NO.'])):
        if ALLOCATION.loc[i,'AGREEMENTID']==C.loc[j,'LOAN NO.']:
            ALLOCATION.loc[i,'CALL INTENSITY']=C.loc[j,'Agent ID']
    
ALLOCATION.to_excel(r'C/Users/mohaksehgal/Documents/Work/Call Intensity/L_T/MARCH 20/L&T Call Intensity.xlsx',index=False)