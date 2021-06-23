#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 15:23:04 2020

@author: mohaksehgal
"""


import pandas as pd
import numpy as np

A=pd.read_excel(r'/Users/mohaksehgal/Documents/Work/MIS/AB/BL/MARCH 20/MASTER FILE AB_BL.xlsx')

F=pd.DataFrame(A.groupby(['FOS','STATUS'])['AGREEMENTID'].count()).reset_index()

SC=F[(F['FOS']!='N.A') & (F['STATUS']=='SB')]

SC=SC.reset_index(drop=True)

Q=pd.DataFrame(A.groupby(['FOS'])['POS'].sum()).reset_index()

Q=Q[Q['FOS']!='N.A']

Q=Q.reset_index(drop=True)

AA=pd.DataFrame(A.groupby(['FOS','STATUS'])['POS'].sum()).reset_index()

for i in range(0,len(Q['FOS'])):
    for j in range(0,len(AA['FOS'])):
        if (Q.loc[i,'FOS']==AA.loc[j,'FOS']) and (AA.loc[j,'STATUS']=='SB'):
            Q.loc[i,'SB_POS']=AA.loc[j,'POS']

Q['SB_POS']=Q['SB_POS'].astype(int)

Q['Performance']=round((Q['SB_POS']/Q['POS'])*100,2)

for i in range(0,len(Q['FOS'])):
    for j in range(0,len(SC['FOS'])):
        if Q.loc[i,'FOS']==SC.loc[j,'FOS']:
            Q.loc[i,'CASE_COUNT']=SC.loc[j,'AGREEMENTID']

for i in range(0,len(Q['FOS'])):
    if Q.loc[i,'Performance']<90:
        Q.loc[i,'PAYOUT']=Q.loc[i,'CASE_COUNT']*100
    elif Q.loc[i,'Performance']>=90 and Q.loc[i,'Performance']<93:
        Q.loc[i,'PAYOUT']=Q.loc[i,'CASE_COUNT']*125
    elif Q.loc[i,'Performance']>=93 and Q.loc[i,'Performance']<95:
        Q.loc[i,'PAYOUT']=Q.loc[i,'CASE_COUNT']*150
    elif Q.loc[i,'Performance']>=95 and Q.loc[i,'Performance']<97:
        Q.loc[i,'PAYOUT']=Q.loc[i,'CASE_COUNT']*175
    elif Q.loc[i,'Performance']>=97:
        Q.loc[i,'PAYOUT']=Q.loc[i,'CASE_COUNT']*200

Q.to_excel(r'/Users/mohaksehgal/Documents/Work/FOS Salary/AB_BL/MARCH 20/FOS Salary AB_BL.xlsx',index=False)