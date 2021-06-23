#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 08:17:59 2020

@author: mohaksehgal
"""


import pandas as pd
import numpy as np

A=pd.read_excel(r'/Users/mohaksehgal/Documents/Work/TC Performance/AB/AB_BL/MARCH 20/MASTER FILE AB_BL.xlsx')

A=A[A['FR']=='NO']

M=pd.DataFrame(A.groupby(['COMPANY','BKT','TC NAME'])['POS'].sum()).reset_index()

M=pd.DataFrame(A.groupby(['COMPANY','BKT','TC NAME'])['POS'].sum()).reset_index()

M.rename({'POS':'TOTAL_POS'},axis=1,inplace=True)

R=pd.DataFrame(A.groupby(['COMPANY','BKT','TC NAME'])['AGREEMENTID'].count()).reset_index()

F=M.merge(R,how='outer')

F.rename({'AGREEMENTID':'TOTAL_CASES'},axis=1,inplace=True)

R1=pd.DataFrame(A.groupby(['COMPANY','BKT','TC NAME','STATUS'])['AGREEMENTID'].count()).reset_index()

P=F.copy()

P=P.iloc[:,:3]

P['FLOW']=np.nan
P['SB']=np.nan
P['PART PAID']=np.nan

COL=P.columns

for i in range(0,len(R1['COMPANY'])):
    for j in range(0,len(P['COMPANY'])):
        for k in range(0,len(COL)):
            if ((R1.loc[i,['COMPANY','BKT','TC NAME']]==P.loc[j,['COMPANY','BKT','TC NAME']]).all()) and R1.loc[i,'STATUS']==COL[k]:
                P.loc[j,COL[k]]=R1.loc[i,'AGREEMENTID']

F=F.merge(P,how='outer')

F.fillna(0,inplace=True)

F.rename({'FLOW':'FLOW_CASES','SB':'SB_CASES','PART PAID':'PART_PAID_CASES'},axis=1,inplace=True)

R2=pd.DataFrame(A.groupby(['COMPANY','BKT','TC NAME','STATUS'])['POS'].sum()).reset_index()

for i in range(0,len(R2['COMPANY'])):
    for j in range(0,len(P['COMPANY'])):
        for k in range(0,len(COL)):
            if ((R2.loc[i,['COMPANY','BKT','TC NAME']]==P.loc[j,['COMPANY','BKT','TC NAME']]).all()) and R2.loc[i,'STATUS']==COL[k]:
                P.loc[j,COL[k]]=R2.loc[i,'POS']

F=F.merge(P,how='outer')

F.rename({'FLOW':'FLOW_POS','SB':'SB_POS','PART PAID':'PART_PAID_POS'},axis=1,inplace=True)

F.fillna(0,inplace=True)

for i in range(0,len(F['FLOW_CASES'])):
    F.loc[i,'FLOW_POS%']=round((F.loc[i,'FLOW_POS']/F.loc[i,'TOTAL_POS'])*100,2)
    F.loc[i,'SB_POS%']=round((F.loc[i,'SB_POS']/F.loc[i,'TOTAL_POS'])*100,2)
    F.loc[i,'PART_PAID_POS%']=round((F.loc[i,'PART_PAID_POS']/F.loc[i,'TOTAL_POS'])*100,2)

TP=pd.DataFrame(A.groupby(['COMPANY','BKT','TC NAME'])['TOTAL PAID'].sum()).reset_index()

F=F.merge(TP,how='outer')

for i in range(0,len(F['SB_POS'])):
    F.loc[i,'PERFORMANCE']=F.loc[i,'SB_POS%']

F.rename({'TOTAL_CASES':'COUNT','PART_PAID_CASES':'PP_CASES','PART_PAID_POS':'PP_POS','PART_PAID_POS%':'PP_POS%','PERFORMANCE':'POS_RES%'},axis=1,inplace=True)

F.to_excel(r'/Users/mohaksehgal/Documents/Work/TC Performance/AB/AB_BL/MARCH 20/TC Performance AB_BL.xlsx',index=False)