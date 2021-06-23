#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 17 16:31:47 2021

@author: rishi
"""

import pandas as pd
import numpy as np

A=pd.read_excel(r"/Users/mohaksehgal/Documents/Work/MIS/FULLERTON/JUN 21/FULLERTON_OTR_ALLOCATION_21JUN21.xlsx")
B=pd.read_excel(r"/Users/mohaksehgal/Documents/Work/MIS/FULLERTON/JUN 21/FULLERTON_OTR_PAID FILE_21JUN21.xlsx")

B1=pd.DataFrame(B.groupby('AGREEMENTID')['PAID AMOUNT'].sum()).reset_index()

for i in range(0,len(A['AGREEMENTID'])):
    for k in range(0,len(B['AGREEMENTID'])):
        if A.loc[i,'AGREEMENTID']==B.loc[k,'AGREEMENTID'] and B.loc[k,'AGAINST']!='FORECLOSE' and B.loc[k,'AGAINST']!='SETTLEMENT':
            for j in range(0,len(B1['AGREEMENTID'])):
                if A.loc[i,'AGREEMENTID']==B1.loc[j,'AGREEMENTID']:
                    if B1.loc[j,'PAID AMOUNT']<A.loc[i,'EMI']:
                        A.loc[i,'STATUS']='PART PAID'
                    elif B1.loc[j,'PAID AMOUNT']>=A.loc[i,'POS']:
                        A.loc[i,'STATUS']='SETTLEMENT'
                    elif B1.loc[j,'PAID AMOUNT']>=A.loc[i,'EMI']:
                        A.loc[i,'STATUS']='SB'
        elif (A.loc[i,'AGREEMENTID']==B.loc[k,'AGREEMENTID']) and (B.loc[k,'AGAINST']=='FORECLOSE'):
            A.loc[i,'STATUS']='FORECLOSE'
        elif (A.loc[i,'AGREEMENTID']==B.loc[k,'AGREEMENTID']) and (B.loc[k,'AGAINST']=='SETTLEMENT'):
            A.loc[i,'STATUS']='SETTLEMENT'

for i in range(0,len(A['AGREEMENTID'])):
    if str(A.loc[i,'STATUS'])=='nan':
        A.loc[i,'STATUS']='FLOW'

for i in range(0,len(A['AGREEMENTID'])):
    for j in range(0,len(B1['PAID AMOUNT'])):
        if A.loc[i,'AGREEMENTID']==B1.loc[j,'AGREEMENTID']:
            A.loc[i,'TOTAL PAID']=B1.loc[j,'PAID AMOUNT']

M=pd.DataFrame(A.groupby(['PRODUCT'])['POS'].sum()).reset_index()

M.rename({'POS':'TOTAL_POS'},axis=1,inplace=True)

R=pd.DataFrame(A.groupby(['PRODUCT'])['AGREEMENTID'].count()).reset_index()

F=M.merge(R,how='outer')

F.rename({'AGREEMENTID':'TOTAL_CASES'},axis=1,inplace=True)

R1=pd.DataFrame(A.groupby(['PRODUCT','STATUS'])['AGREEMENTID'].count()).reset_index()

P=F.copy()

P.drop(['TOTAL_POS','TOTAL_CASES'],axis=1,inplace=True)

P['FLOW']=np.nan
P['SB']=np.nan
P['PART PAID']=np.nan
P['FORECLOSE']=np.nan
P['SETTLEMENT']=np.nan

COL=P.columns

for i in range(0,len(R1['PRODUCT'])):
    for j in range(0,len(P['FLOW'])):
        for k in range(0,len(COL)):
            if (R1.loc[i,'PRODUCT']==P.loc[j,'PRODUCT']) and R1.loc[i,'STATUS']==COL[k]:
                P.loc[j,COL[k]]=R1.loc[i,'AGREEMENTID']

F=F.merge(P,how='outer')

F.fillna(0,inplace=True)

F.rename({'FLOW':'FLOW_CASES','SB':'SB_CASES','FORECLOSE':'FORECLOSE_CASES','SETTLEMENT':'SETTLEMENT_CASES','PART PAID':'PART_PAID_CASES'},axis=1,inplace=True)

R2=pd.DataFrame(A.groupby(['PRODUCT','STATUS'])['POS'].sum()).reset_index()

for i in range(0,len(R2['PRODUCT'])):
    for j in range(0,len(P['PRODUCT'])):
        for k in range(0,len(COL)):
            if (R2.loc[i,'PRODUCT']==P.loc[j,'PRODUCT']) and R2.loc[i,'STATUS']==COL[k]:
                P.loc[j,COL[k]]=R2.loc[i,'POS']

F=F.merge(P,how='outer')

F.rename({'FLOW':'FLOW_POS','SB':'SB_POS','FORECLOSE':'FORECLOSE_POS','SETTLEMENT':'SETTLEMENT_POS','PART PAID':'PART_PAID_POS'},axis=1,inplace=True)

F.fillna(0,inplace=True)

for i in range(0,len(F['FLOW_CASES'])):
    F.loc[i,'FLOW_POS%']=round((F.loc[i,'FLOW_POS']/F.loc[i,'TOTAL_POS'])*100,2)
    F.loc[i,'SB_POS%']=round((F.loc[i,'SB_POS']/F.loc[i,'TOTAL_POS'])*100,2)
    F.loc[i,'FORECLOSE_POS%']=round((F.loc[i,'FORECLOSE_POS']/F.loc[i,'TOTAL_POS'])*100,2)
    F.loc[i,'SETTLEMENT_POS%']=round((F.loc[i,'SETTLEMENT_POS']/F.loc[i,'TOTAL_POS'])*100,2)
    F.loc[i,'PART_PAID_POS%']=round((F.loc[i,'PART_PAID_POS']/F.loc[i,'TOTAL_POS'])*100,2)

TP=pd.DataFrame(A.groupby(['PRODUCT'])['TOTAL PAID'].sum()).reset_index()

F=F.merge(TP,how='outer')

for i in range(0,len(F['SB_POS'])):
    F.loc[i,'PERFORMANCE']=F.loc[i,'SB_POS%']+F.loc[i,'FORECLOSE_POS%']+F.loc[i,'SETTLEMENT_POS%']

F.rename({'TOTAL_CASES':'COUNT','PART_PAID_CASES':'PP_CASES','FORECLOSE_CASES':'FC_CASES','SETTLEMENT_CASES':'SC_CASES',
         'PART_PAID_POS':'PP_POS','FORECLOSE_POS':'FC_POS','SETTLEMENT_POS':'SC_POS','FORECLOSE_POS%':'FC_POS%',
         'SETTLEMENT_POS%':'SC_POS%','PART_PAID_POS%':'PP_POS%','PERFORMANCE':'POS_RES%'},axis=1,inplace=True)

F.to_excel(r'/Users/mohaksehgal/Documents/Work/MIS/FULLERTON/JUN 21/MIS_FULLERTON_OTR.xlsx',index=False)   

for i in range(0,len(A['AGREEMENTID'])):
    s=0
    for j in range(0,len(B['AGREEMENTID'])):
        if (A.loc[i,'AGREEMENTID']==B.loc[j,'AGREEMENTID']) and (A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT' or A.loc[i,'STATUS']=='SB') and (B.loc[j,'MODE']!='ECS'):
            s=s+B.loc[j,'PAID AMOUNT']
    A.loc[i,'Billing PAID AMT.']=s

for i in range(0,len(A['AGREEMENTID'])):
    if (A.loc[i,'EMI']>A.loc[i,'TOTAL PAID']) and (A.loc[i,'STATUS']=='SB'):
        A.loc[i,'Billing PAID AMT.']=A.loc[i,'EMI']

A['TOTAL PAID'].fillna(0,inplace=True)

A['Billing PAID AMT.'].fillna(0,inplace=True)

A.to_excel(r'/Users/mohaksehgal/Documents/Work/Billing/FULLERTON/JUN 21/MASTER_FILE_FULLERTON_OTR.xlsx',index=False)

A.to_excel(r'/Users/mohaksehgal/Documents/Work/TC Performance/FULLERTON/JUN 21/MASTER_FILE_FULLERTON_OTR.xlsx',index=False)

A.to_excel(r'/Users/mohaksehgal/Documents/Work/MIS/FULLERTON/JUN 21/MASTER_FILE_FULLERTON_OTR.xlsx',index=False)

A.to_excel(r'/Users/mohaksehgal/Documents/Work/FOS Salary/FULLERTON/JUN 21/MASTER_FILE_FULLERTON_OTR.xlsx',index=False)