#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 15 18:48:21 2020

@author: mohaksehgal
"""


import pandas as pd
import numpy as np

A=pd.read_excel(r"/Users/mohaksehgal/Documents/Work/TC Incentive/AB/MARCH 20/MASTER FILE AB_BL.xlsx")

F1=pd.DataFrame(A.groupby(['TC NAME'])['POS'].sum()).reset_index()

F=F1.copy()

R1=pd.DataFrame(A.groupby(['TC NAME','STATUS'])['POS'].sum()).reset_index()

P=F.copy()

P.head()

P=P.iloc[:,:2]

P['SB']=np.nan

COL=list(P.columns)

for i in range(0,len(R1['TC NAME'])):
    for j in range(0,len(P['TC NAME'])):
        for k in range(0,len(COL)):
            if ((R1.loc[i,['TC NAME']]==P.loc[j,['TC NAME']]).all()) and R1.loc[i,'STATUS']==COL[k]:
                P.loc[j,COL[k]]=R1.loc[i,'POS']

F=F.merge(P,how='outer')

F.fillna(0,inplace=True)

F.rename({'POS':'TOTAL POS'},axis=1,inplace=True)

for i in range(0,len(F['TOTAL POS'])):
    F.loc[i,'POS']=F.loc[i,'SB']
    F.loc[i,'Performance']=F.loc[i,'POS']/F.loc[i,'TOTAL POS']*100

F['Performance']=round(F['Performance'],2)

for i in range(0,len(F['TC NAME'])):
    if F.loc[i,'Performance']<94:
        F.loc[i,'PAYOUT']=0
    elif F.loc[i,'Performance']>=94 and F.loc[i,'Performance']<=96:
        F.loc[i,'PAYOUT']=1000
    elif F.loc[i,'Performance']>96 and F.loc[i,'Performance']<=97:
        F.loc[i,'PAYOUT']=2000
    elif F.loc[i,'Performance']>97 and F.loc[i,'Performance']<=98:
        F.loc[i,'PAYOUT']=4000
    elif F.loc[i,'Performance']>98 and F.loc[i,'Performance']<=99:
        F.loc[i,'PAYOUT']=5000
    elif F.loc[i,'Performance']>99:
        F.loc[i,'PAYOUT']=7000

F.to_excel(r'/Users/mohaksehgal/Documents/Work/TC Incentive/AB/MARCH 20/AB_BL TC Incentive.xlsx',index=False)