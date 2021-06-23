#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 17 16:08:18 2021

@author: rishi
"""

import pandas as pd
import numpy as np

A=pd.read_excel(r"/Users/mohaksehgal/Documents/Work/FOS SALARY/FULLERTON/APR 21/MASTER_FILE_FULLERTON_RECOVERY.xlsx")
B=pd.read_excel(r"/Users/mohaksehgal/Documents/Work/MIS/FULLERTON/APR 21/FULLERTON_RECOVERY_PAID FILE_23APR21.xlsx")

U=pd.read_excel('/Users/mohaksehgal/Documents/Work/COMBINED SALARY OF L_T AND IDFC TW/Unique Names.xlsx')

dr=list(B[B['MODE']=='ECS'].index)

B.drop(dr,axis=0,inplace=True)

B=B.reset_index(drop=True)

B.groupby(['AGREEMENTID','FOS'])['FOS'].count()

B1=pd.DataFrame(B.groupby(['AGREEMENTID','FOS'])['MODE'].count()).reset_index()

B1.drop('MODE',axis=1,inplace=True)

B1.rename({'FOS':'FINAL PAID FOS'},axis=1,inplace=True)

A=A.merge(B1,how='outer')

A[A['STATUS']=='FLOW']['FINAL PAID FOS'].unique()

A['FINAL PAID FOS'].fillna('--',inplace=True)

UN=list(U[U['DESIGNATION']=='OFFICE']['NAMES'])

for i in range(0,len(A['AGREEMENTID'])):
    if (A.loc[i,'FOS'] in UN) and (A.loc[i,'FINAL PAID FOS'] in UN):
        A.loc[i,'FOS']='NO FOS'
        A.loc[i,'FINAL PAID FOS']='NO FOS'
    elif A.loc[i,'FINAL PAID FOS'] in UN:
        A.loc[i,'FINAL PAID FOS']='NO FOS'
    elif A.loc[i,'FOS'] in UN:
        A.loc[i,'FOS']='NO FOS'

M=pd.DataFrame(A.groupby(['FOS'])['POS'].sum()).reset_index()

M.rename({'POS':'TOTAL_POS'},axis=1,inplace=True)

R=pd.DataFrame(A.groupby(['FOS'])['AGREEMENTID'].count()).reset_index()

F=M.merge(R,how='outer')

F.rename({'AGREEMENTID':'TOTAL_CASES'},axis=1,inplace=True)

R1=pd.DataFrame(A.groupby(['FOS','STATUS'])['AGREEMENTID'].count()).reset_index()

P=F.copy()

P.drop(['TOTAL_POS','TOTAL_CASES'],axis=1,inplace=True)

P['FLOW']=np.nan
P['PAID']=np.nan

COL=P.columns

for i in range(0,len(R1['FOS'])):
    for j in range(0,len(P['FLOW'])):
        for k in range(0,len(COL)):
            if (R1.loc[i,'FOS']==P.loc[j,'FOS']) and R1.loc[i,'STATUS']==COL[k]:
                P.loc[j,COL[k]]=R1.loc[i,'AGREEMENTID']

F=F.merge(P,how='outer')

F.fillna(0,inplace=True)

F.rename({'FLOW':'FLOW_CASES','PAID':'PAID_CASES'},axis=1,inplace=True)

R2=pd.DataFrame(A.groupby(['FINAL PAID FOS','STATUS'])['TOTAL PAID'].sum()).reset_index()

dr=[]
for i in range(0,len(R2['FINAL PAID FOS'])):
    if (R2.loc[i,'FINAL PAID FOS']=='--') or (R2.loc[i,'FINAL PAID FOS']=='NO FOS'):
        dr.append(i)

R2.drop(dr,axis=0,inplace=True)

R2=R2.reset_index(drop=True)

R2.rename({'FINAL PAID FOS':'FOS'},axis=1,inplace=True)

for i in range(0,len(R2['FOS'])):
    for j in range(0,len(P['FOS'])):
        for k in range(0,len(COL)):
            if (R2.loc[i,'FOS']==P.loc[j,'FOS']) and R2.loc[i,'STATUS']==COL[k]:
                P.loc[j,COL[k]]=R2.loc[i,'TOTAL PAID']

F=F.merge(P,how='outer')

F.rename({'FLOW':'FLOW_POS','PAID':'PAID_POS'},axis=1,inplace=True)

F.fillna(0,inplace=True)

F.drop('FLOW_POS',axis=1,inplace=True)

F.rename({'PAID_POS':'MONEY_COLLECTION'},axis=1,inplace=True)

F['FIXED_PAYOUT']=F['TOTAL_CASES']*100

for i in range(0,len(F['FOS'])):
    if F.loc[i,'MONEY_COLLECTION']<500000:
        F.loc[i,'INCENTIVE%']='6%'
        F.loc[i,'INCENTIVE']=F.loc[i,'MONEY_COLLECTION']*6/100
    elif F.loc[i,'MONEY_COLLECTION']>500000:
        F.loc[i,'INCENTIVE%']='7%'
        F.loc[i,'INCENTIVE']=F.loc[i,'MONEY_COLLECTION']*7/100

F['TOTAL_SALARY']=F['FIXED_PAYOUT']+F['INCENTIVE']

dr=list(F[F['FOS']=='NO FOS'].index)

F.drop(dr,axis=0,inplace=True)

F.reset_index(drop=True)

F.to_excel(r'/Users/mohaksehgal/Documents/Work/FOS Salary/FULLERTON/APR 21/FOS_SALARY_FULLERTON_RECOVERY.xlsx',index=False)   