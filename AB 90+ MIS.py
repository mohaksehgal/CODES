#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 18:31:34 2020

@author: mohaksehgal
"""


import pandas as pd
import numpy as np

A=pd.read_excel(r"/Users/mohaksehgal/Documents/Work/MIS/AB/90+/AUG 20/ABFL_90+ ALLOCATION 05 MARCH 20.xlsx")

B=pd.read_excel(r"/Users/mohaksehgal/Documents/Work/MIS/AB/90+/AUG 20/ABFL_90+ PAID FILE 31 MARCH 20.xlsx")

B1=pd.DataFrame(B.groupby('AGREEMENTID')['PAID AMOUNT'].sum()).reset_index()

for i in range(0,len(A['AGREEMENTID'])):
    for k in range(0,len(B['AGREEMENTID'])):
        if (A.loc[i,'AGREEMENTID']==B.loc[k,'AGREEMENTID']):
            for j in range(0,len(B1['AGREEMENTID'])):
                if A.loc[i,'AGREEMENTID']==B1.loc[j,'AGREEMENTID']:
                    A.loc[i,'PAID AMOUNT']=B1.loc[j,'PAID AMOUNT']

A['PAID AMOUNT'].fillna(0,inplace=True)

A['PAID AMOUNT']=A['PAID AMOUNT'].astype(int)

for i in range(0,len(A['PAID AMOUNT'])):
    if A.loc[i,'PAID AMOUNT']>=A.loc[i,'EMI']:
        A.loc[i,'STATUS']='PAID'
    else:
        A.loc[i,'STATUS']='UNPAID'
        
A.to_excel(r'/Users/mohaksehgal/Documents/Work/Billing/AB/AB 90+/AUG 20/MASTER FILE AB 90+.xlsx',index=False)

A.to_excel(r'/Users/mohaksehgal/Documents/Work/TC Incentive/AB 90+/AUG 20/MASTER FILE AB 90+.xlsx',index=False)

print(A.groupby('BKT')['PAID AMOUNT'].sum())

print(A.groupby(['TC NAME'])['PAID AMOUNT'].sum())

print(A.groupby(['TC NAME','BKT'])['PAID AMOUNT'].sum())

print(B1['PAID AMOUNT'].sum() )