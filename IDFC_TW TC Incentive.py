#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 09:21:52 2020

@author: mohaksehgal
"""


import pandas as pd
import numpy as np

A=pd.read_excel(r"/Users/mohaksehgal/Documents/Work/TC Incentive/IDFC_TW/MARCH 20/MASTER FILE IDFC TW.xlsx")

F1=pd.DataFrame(A.groupby(['TC NAME','BKT'])['POS'].sum()).reset_index()

F=F1.copy()

R1=pd.DataFrame(A.groupby(['TC NAME','BKT','STATUS'])['POS'].sum()).reset_index()

P=F.copy()

P=P.iloc[:,:2]

P['SB']=np.nan
P['RB']=np.nan
P['NM']=np.nan
P['FORECLOSE']=np.nan
P['SETTLEMENT']=np.nan

COL=list(P.columns)

for i in range(0,len(R1['TC NAME'])):
    for j in range(0,len(P['TC NAME'])):
        for k in range(0,len(COL)):
            if ((R1.loc[i,['TC NAME','BKT']]==P.loc[j,['TC NAME','BKT']]).all()) and R1.loc[i,'STATUS']==COL[k]:
                P.loc[j,COL[k]]=R1.loc[i,'POS']

F=F.merge(P,how='outer')

F.fillna(0,inplace=True)

F.rename({'POS':'TOTAL POS'},axis=1,inplace=True)

for i in range(0,len(F['TOTAL POS'])):
    F.loc[i,'POS']=F.loc[i,'SB']+F.loc[i,'RB']+F.loc[i,'NM']+F.loc[i,'FORECLOSE']+F.loc[i,'SETTLEMENT']
    F.loc[i,'Performance']=F.loc[i,'POS']/F.loc[i,'TOTAL POS']*100

F['Performance']=round(F['Performance'],2)

for i in range(0,len(F['TC NAME'])):
    if F.loc[i,'Performance']<75:
        F.loc[i,'PAYOUT']=0
    elif F.loc[i,'Performance']>=75 and F.loc[i,'Performance']<78:
        F.loc[i,'PAYOUT']=1000
    elif F.loc[i,'Performance']>=78 and F.loc[i,'Performance']<80:
        F.loc[i,'PAYOUT']=1200
    elif F.loc[i,'Performance']>=80 and F.loc[i,'Performance']<85:
        F.loc[i,'PAYOUT']=1500
    elif F.loc[i,'Performance']>=85 and F.loc[i,'Performance']<90:
        F.loc[i,'PAYOUT']=2000
    elif F.loc[i,'Performance']>=90:
        F.loc[i,'PAYOUT']=3000

F.to_excel(r'/Users/mohaksehgal/Documents/Work/TC Incentive/IDFC_TW/MARCH 20/IDFC_TW TC Incentive.xlsx',index=False)