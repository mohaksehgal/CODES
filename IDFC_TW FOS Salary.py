#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 12:58:44 2020

@author: mohaksehgal
"""


import pandas as pd
import numpy as np

A=pd.read_excel(r"/Users/mohaksehgal/Documents/Work/FOS Salary/IDFC TW/MARCH 20/MASTER FILE IDFC TW.xlsx")

A1=pd.read_excel(r'/Users/mohaksehgal/Documents/Work/MIS/IDFC TW/MARCH 20/IDFC_TW PAID FILE 30 MARCH 20.xlsx')

TC=pd.DataFrame(A.groupby('FOS')['AGREEMENTID'].count()).reset_index()

TC.to_excel(r'/Users/mohaksehgal/Documents/Work/COMBINED SALARY OF L_T AND IDFC TW/MARCH 20/IDFC CASES.xlsx',index=False)

WW=A[(A['STATUS']!='FLOW') & (A['STATUS']!='PART PAID')]

WW1=A1[A1['MODE']=='ECS']

F=pd.DataFrame(WW.groupby(['FOS','BKT'])['AGREEMENTID'].count()).reset_index()

FF=pd.DataFrame(WW1.groupby(['FOS','BKT'])['AGREEMENTID'].count()).reset_index()

FF.rename({'AGREEMENTID':'ECS_COUNT'},axis=1,inplace=True)

F=F.merge(FF,how='left')

F.fillna(0,inplace=True)

F['CASE_COUNT']=F['AGREEMENTID']-F['ECS_COUNT']

F['CASE_COUNT']=F['CASE_COUNT'].astype(int)

F1=pd.DataFrame(A.groupby(['FOS','BKT'])['POS'].sum()).reset_index()

F=F.merge(F1)

R1=pd.DataFrame(A.groupby(['FOS','BKT','STATUS'])['POS'].sum()).reset_index()

P=F.copy()

P=P.iloc[:,:2]

P['SB']=np.nan
P['RB']=np.nan
P['NM']=np.nan
P['FORECLOSE']=np.nan
P['SETTLEMENT']=np.nan

COL=list(P.columns)

for i in range(0,len(R1['FOS'])):
    for j in range(0,len(P['FOS'])):
        for k in range(0,len(COL)):
            if ((R1.loc[i,['FOS','BKT']]==P.loc[j,['FOS','BKT']]).all()) and R1.loc[i,'STATUS']==COL[k]:
                P.loc[j,COL[k]]=R1.loc[i,'POS']
                
F=F.merge(P,how='outer')

F.fillna(0,inplace=True)

F.rename({'POS':'TOTAL POS'},axis=1,inplace=True)

for i in range(0,len(F['TOTAL POS'])):
    F.loc[i,'POS']=F.loc[i,'SB']+F.loc[i,'RB']+F.loc[i,'NM']+F.loc[i,'FORECLOSE']+F.loc[i,'SETTLEMENT']
    F.loc[i,'RB+NM']=F.loc[i,'RB']+F.loc[i,'NM']
    
for i in range(0,len(F['FOS'])):
    F.loc[i,'Performance']=F.loc[i,'POS']/F.loc[i,'TOTAL POS']*100
    F.loc[i,'RB+NM%']=F.loc[i,'RB+NM']/F.loc[i,'TOTAL POS']*100
    
for i in range(0,len(F['FOS'])):
    if F.loc[i,'Performance']<60:
        F.loc[i,'PAYOUT']=F.loc[i,'CASE_COUNT']*0
    elif F.loc[i,'Performance']>=60 and F.loc[i,'Performance']<70:
        F.loc[i,'PAYOUT']=F.loc[i,'CASE_COUNT']*50
    elif F.loc[i,'Performance']>70 and F.loc[i,'Performance']<75:
        F.loc[i,'PAYOUT']=F.loc[i,'CASE_COUNT']*60
    elif F.loc[i,'Performance']>75 and F.loc[i,'Performance']<80:
        F.loc[i,'PAYOUT']=F.loc[i,'CASE_COUNT']*80
    elif F.loc[i,'Performance']>80 and F.loc[i,'Performance']<85:
        F.loc[i,'PAYOUT']=F.loc[i,'CASE_COUNT']*120
    elif F.loc[i,'Performance']>85 and F.loc[i,'Performance']<88:
        F.loc[i,'PAYOUT']=F.loc[i,'CASE_COUNT']*175
    elif F.loc[i,'Performance']>88 and F.loc[i,'Performance']<90:
        F.loc[i,'PAYOUT']=F.loc[i,'CASE_COUNT']*200
    elif F.loc[i,'Performance']>90:
        F.loc[i,'PAYOUT']=F.loc[i,'CASE_COUNT']*250
        
for i in range(0,len(F['FOS'])):
    if F.loc[i,'RB+NM%']>=30:
        F.loc[i,'ADD+PAYOUT']=5000
    if F.loc[i,'RB+NM%']>=20:
        F.loc[i,'ADD_PAYOUT']=3000
    elif F.loc[i,'RB+NM%']<20:
        F.loc[i,'ADD_PAYOUT']=0
        
for i in range(0,len(F['FOS'])):
    F.loc[i,'Performance']=round(F.loc[i,'Performance'],2)
    F.loc[i,'RB+NM%']=round(F.loc[i,'RB+NM%'],2)
    
F.fillna(0,inplace=True)

F['TOTAL PAYOUT']=F['ADD_PAYOUT']+F['PAYOUT']

F.to_excel(r'/Users/mohaksehgal/Documents/Work/COMBINED SALARY OF L_T AND IDFC TW/MARCH 20/PAYOUT IDFC.xlsx',index=False)

F.to_excel(r'/Users/mohaksehgal/Documents/Work/FOS Salary/IDFC TW/MARCH 20/FOS Performance IDFC_TW.xlsx',index=False)