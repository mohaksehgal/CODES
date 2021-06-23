#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 08:04:58 2020

@author: mohaksehgal
"""


import pandas as pd
import numpy as np

A=pd.read_excel(r'/Users/mohaksehgal/Documents/Work/TC Performance/L_T/MARCH 20/MASTER FILE L_T.xlsx')

M=pd.DataFrame(A.groupby(['COMPANY','BKT','TC NAME'])['POS'].sum()).reset_index()

M.rename({'POS':'TOTAL_POS'},axis=1,inplace=True)

R=pd.DataFrame(A.groupby(['COMPANY','BKT','TC NAME'])['AGREEMENTID'].count()).reset_index()

F=M.merge(R,how='outer')

F.rename({'AGREEMENTID':'TOTAL_CASES'},axis=1,inplace=True)

R1=pd.DataFrame(A.groupby(['COMPANY','BKT','TC NAME','STATUS'])['AGREEMENTID'].count()).reset_index()

P=F.copy()

P=P.iloc[:,:3]

P.head()

P['FLOW']=np.nan
P['SB']=np.nan
P['RB']=np.nan
P['NM']=np.nan
P['PART PAID']=np.nan
P['FORECLOSE']=np.nan
P['SETTLEMENT']=np.nan

COL=P.columns

for i in range(0,len(R1['COMPANY'])):
    for j in range(0,len(P['COMPANY'])):
        for k in range(0,len(COL)):
            if ((R1.loc[i,['COMPANY','BKT','TC NAME']]==P.loc[j,['COMPANY','BKT','TC NAME']]).all()) and R1.loc[i,'STATUS']==COL[k]:
                P.loc[j,COL[k]]=R1.loc[i,'AGREEMENTID']

F=F.merge(P, how='outer')

F.fillna(0,inplace=True)

F.rename({'FLOW':'FLOW_CASES','SB':'SB_CASES','RB':'RB_CASES','FORECLOSE':'FORECLOSE_CASES','SETTLEMENT':'SETTLEMENT_CASES','NM':'NM_CASES','PART PAID':'PART_PAID_CASES'},axis=1,inplace=True)

R2=pd.DataFrame(A.groupby(['COMPANY','BKT','TC NAME','STATUS'])['POS'].sum()).reset_index()

for i in range(0,len(R2['COMPANY'])):
    for j in range(0,len(P['COMPANY'])):
        for k in range(0,len(COL)):
            if ((R2.loc[i,['COMPANY','BKT','TC NAME']]==P.loc[j,['COMPANY','BKT','TC NAME']]).all()) and R2.loc[i,'STATUS']==COL[k]:
                P.loc[j,COL[k]]=R2.loc[i,'POS']

F=F.merge(P,how='outer')

F.rename({'FLOW':'FLOW_POS','SB':'SB_POS','RB':'RB_POS','FORECLOSE':'FORECLOSE_POS', 'NM':'NM_POS','SETTLEMENT':'SETTLEMENT_POS','PART PAID':'PART_PAID_POS'},axis=1,inplace=True)

F.fillna(0,inplace=True)

for i in range(0,len(F['FLOW_CASES'])):
    F.loc[i,'FLOW_POS%']=round((F.loc[i,'FLOW_POS']/F.loc[i,'TOTAL_POS'])*100,2)
    F.loc[i,'SB_POS%']=round((F.loc[i,'SB_POS']/F.loc[i,'TOTAL_POS'])*100,2)
    F.loc[i,'RB_POS%']=round((F.loc[i,'RB_POS']/F.loc[i,'TOTAL_POS'])*100,2)
    F.loc[i,'FORECLOSE_POS%']=round((F.loc[i,'FORECLOSE_POS']/F.loc[i,'TOTAL_POS'])*100,2)
    F.loc[i,'SETTLEMENT_POS%']=round((F.loc[i,'SETTLEMENT_POS']/F.loc[i,'TOTAL_POS'])*100,2)
    F.loc[i,'NM_POS%']=round((F.loc[i,'NM_POS']/F.loc[i,'TOTAL_POS'])*100,2)
    F.loc[i,'PART_PAID_POS%']=round((F.loc[i,'PART_PAID_POS']/F.loc[i,'TOTAL_POS'])*100,2)

TP=pd.DataFrame(A.groupby(['COMPANY','BKT','TC NAME'])['TOTAL PAID'].sum()).reset_index()

F=F.merge(TP,how='outer')

for i in range(0,len(F['SB_POS'])):
    F.loc[i,'PERFORMANCE']=F.loc[i,'SB_POS%']+F.loc[i,'RB_POS%']+F.loc[i,'FORECLOSE_POS%']+F.loc[i,'NM_POS%']+F.loc[i,'SETTLEMENT_POS%']

F.rename({'TOTAL_CASES':'COUNT','PART_PAID_CASES':'PP_CASES','FORECLOSE_CASES':'FC_CASES','SETTLEMENT_CASES':'SC_CASES',
         'PART_PAID_POS':'PP_POS','FORECLOSE_POS':'FC_POS','SETTLEMENT_POS':'SC_POS','FORECLOSE_POS%':'FC_POS%',
         'SETTLEMENT_POS%':'SC_POS%','PART_PAID_POS%':'PP_POS%','PERFORMANCE':'POS_RES%'},axis=1,inplace=True)

F.replace(0,np.nan,inplace=True)

F.to_excel(r'/Users/mohaksehgal/Documents/Work/TC Performance/L_T/MARCH 20/TC Performance L_T.xlsx',index=False)