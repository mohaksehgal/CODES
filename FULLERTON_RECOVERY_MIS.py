#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 17 15:11:05 2021

@author: rishi
"""

import pandas as pd
import numpy as np

A=pd.read_excel(r"/Users/mohaksehgal/Documents/Work/MIS/FULLERTON/JUN 21/FULLERTON_RECOVERY_ALLOCATION_15JUN21.xlsx")
B=pd.read_excel(r"/Users/mohaksehgal/Documents/Work/MIS/FULLERTON/JUN 21/FULLERTON_RECOVERY_PAID FILE_22JUN21.xlsx")

dr=list(B[B['MODE']=='ECS'].index)

B.drop(dr,axis=0,inplace=True)

B=B.reset_index(drop=True)

B1=pd.DataFrame(B.groupby('AGREEMENTID')['PAID AMOUNT'].sum()).reset_index()

for i in range(0,len(A['AGREEMENTID'])):
    for j in range(0,len(B1['PAID AMOUNT'])):
        if A.loc[i,'AGREEMENTID']==B1.loc[j,'AGREEMENTID']:
            A.loc[i,'TOTAL PAID']=B1.loc[j,'PAID AMOUNT']

for i in range(0,len(A['AGREEMENTID'])):
    if A.loc[i,'TOTAL PAID']>0:
        A.loc[i,'STATUS']='PAID'
    else:
        A.loc[i,'STATUS']='FLOW'

M=pd.DataFrame(A.groupby(['PRODUCT','VINTAGE'])['POS'].sum()).reset_index()

M.rename({'POS':'TOTAL_POS'},axis=1,inplace=True)

R=pd.DataFrame(A.groupby(['PRODUCT','VINTAGE'])['AGREEMENTID'].count()).reset_index()

F=M.merge(R,how='outer')

F.rename({'AGREEMENTID':'TOTAL_CASES'},axis=1,inplace=True)

R1=pd.DataFrame(A.groupby(['PRODUCT','VINTAGE','STATUS'])['AGREEMENTID'].count()).reset_index()

P=F.copy()

P.drop(['TOTAL_POS','TOTAL_CASES'],axis=1,inplace=True)

P['FLOW']=np.nan
P['PAID']=np.nan

COL=P.columns

for i in range(0,len(R1['PRODUCT'])):
    for j in range(0,len(P['FLOW'])):
        for k in range(0,len(COL)):
            if ((R1.loc[i,['PRODUCT','VINTAGE']]==P.loc[j,['PRODUCT','VINTAGE']]).all()) and R1.loc[i,'STATUS']==COL[k]:
                P.loc[j,COL[k]]=R1.loc[i,'AGREEMENTID']

F=F.merge(P,how='outer')

F.fillna(0,inplace=True)

F.rename({'FLOW':'FLOW_CASES','PAID':'PAID_CASES'},axis=1,inplace=True)

R2=pd.DataFrame(A.groupby(['PRODUCT','VINTAGE','STATUS'])['TOTAL PAID'].sum()).reset_index()

for i in range(0,len(R2['PRODUCT'])):
    for j in range(0,len(P['PRODUCT'])):
        for k in range(0,len(COL)):
            if ((R2.loc[i,['PRODUCT','VINTAGE']]==P.loc[j,['PRODUCT','VINTAGE']]).all()) and R2.loc[i,'STATUS']==COL[k]:
                P.loc[j,COL[k]]=R2.loc[i,'TOTAL PAID']

F=F.merge(P,how='outer')

F.rename({'FLOW':'FLOW_POS','PAID':'PAID_POS'},axis=1,inplace=True)

F.fillna(0,inplace=True)

for i in range(0,len(F['FLOW_CASES'])):
    F.loc[i,'FLOW_POS%']=round((F.loc[i,'FLOW_POS']/F.loc[i,'TOTAL_POS'])*100,2)
    F.loc[i,'PAID_POS%']=round((F.loc[i,'PAID_POS']/F.loc[i,'TOTAL_POS'])*100,2)

F.rename({'PAID_POS%':'PERFORMANCE','PAID_POS':'MONEY_COLLECTION'},axis=1,inplace=True)

F.drop(['FLOW_POS%','FLOW_POS'],axis=1,inplace=True)

F.to_excel(r'/Users/mohaksehgal/Documents/Work/MIS/FULLERTON/JUN 21/MIS_FULLERTON_RECOVERY.xlsx',index=False)   

for i in range(0,len(F['PRODUCT'])):

# PL-SAL
    
    if (F.loc[i,'PRODUCT']=='PL Sal') and (F.loc[i,'VINTAGE']=='V1'):
        if F.loc[i,'PERFORMANCE']<6:
            F.loc[i,'PAYOUT%']='16%'
            F.loc[i,'PAYOUT']=F.loc[i,'MONEY_COLLECTION']*16/100
        elif F.loc[i,'PERFORMANCE']>=6 and F.loc[i,'PERFORMANCE']<8:
            F.loc[i,'PAYOUT%']='17.5%'
            F.loc[i,'PAYOUT']=F.loc[i,'MONEY_COLLECTION']*17.5/100
        elif F.loc[i,'PERFORMANCE']>=8:
            F.loc[i,'PAYOUT%']='20%'
            F.loc[i,'PAYOUT']=F.loc[i,'MONEY_COLLECTION']*20/100
    elif (F.loc[i,'PRODUCT']=='PL Sal') and (F.loc[i,'VINTAGE']=='V2'):
        if F.loc[i,'PERFORMANCE']<5:
            F.loc[i,'PAYOUT%']='17.5%'
            F.loc[i,'PAYOUT']=F.loc[i,'MONEY_COLLECTION']*17.5/100
        elif F.loc[i,'PERFORMANCE']>=5 and F.loc[i,'PERFORMANCE']<6:
            F.loc[i,'PAYOUT%']='20%'
            F.loc[i,'PAYOUT']=F.loc[i,'MONEY_COLLECTION']*20/100
        elif F.loc[i,'PERFORMANCE']>=6:
            F.loc[i,'PAYOUT%']='22.5%'
            F.loc[i,'PAYOUT']=F.loc[i,'MONEY_COLLECTION']*22.5/100
    elif (F.loc[i,'PRODUCT']=='PL Sal') and (F.loc[i,'VINTAGE']=='V3'):
        if F.loc[i,'PERFORMANCE']<4:
            F.loc[i,'PAYOUT%']='20%'
            F.loc[i,'PAYOUT']=F.loc[i,'MONEY_COLLECTION']*20/100
        elif F.loc[i,'PERFORMANCE']>=4 and F.loc[i,'PERFORMANCE']<5:
            F.loc[i,'PAYOUT%']='22.5%'
            F.loc[i,'PAYOUT']=F.loc[i,'MONEY_COLLECTION']*22.5/100
        elif F.loc[i,'PERFORMANCE']>=5:
            F.loc[i,'PAYOUT%']='25%'
            F.loc[i,'PAYOUT']=F.loc[i,'MONEY_COLLECTION']*25/100
    elif (F.loc[i,'PRODUCT']=='PL Sal') and (F.loc[i,'VINTAGE']=='V4'):
        if F.loc[i,'PERFORMANCE']<3:
            F.loc[i,'PAYOUT%']='22.5%'
            F.loc[i,'PAYOUT']=F.loc[i,'MONEY_COLLECTION']*22.5/100
        elif F.loc[i,'PERFORMANCE']>=4 and F.loc[i,'PERFORMANCE']<5:
            F.loc[i,'PAYOUT%']='25%'
            F.loc[i,'PAYOUT']=F.loc[i,'MONEY_COLLECTION']*25/100
        elif F.loc[i,'PERFORMANCE']>=5:
            F.loc[i,'PAYOUT%']='27.5%'
            F.loc[i,'PAYOUT']=F.loc[i,'MONEY_COLLECTION']*27.5/100
    elif (F.loc[i,'PRODUCT']=='PL Sal') and (F.loc[i,'VINTAGE']=='V5'):
        if F.loc[i,'PERFORMANCE']<2:
            F.loc[i,'PAYOUT%']='25%'
            F.loc[i,'PAYOUT']=F.loc[i,'MONEY_COLLECTION']*25/100
        elif F.loc[i,'PERFORMANCE']>=2 and F.loc[i,'PERFORMANCE']<3:
            F.loc[i,'PAYOUT%']='27.5%'
            F.loc[i,'PAYOUT']=F.loc[i,'MONEY_COLLECTION']*27.5/100
        elif F.loc[i,'PERFORMANCE']>=3:
            F.loc[i,'PAYOUT%']='30%'
            F.loc[i,'PAYOUT']=F.loc[i,'MONEY_COLLECTION']*30/100
    elif (F.loc[i,'PRODUCT']=='PL Sal') and (F.loc[i,'VINTAGE']=='V6'):
        if F.loc[i,'PERFORMANCE']<1:
            F.loc[i,'PAYOUT%']='30%'
            F.loc[i,'PAYOUT']=F.loc[i,'MONEY_COLLECTION']*30/100
        elif F.loc[i,'PERFORMANCE']>=1 and F.loc[i,'PERFORMANCE']<2:
            F.loc[i,'PAYOUT%']='32.5%'
            F.loc[i,'PAYOUT']=F.loc[i,'MONEY_COLLECTION']*32.5/100
        elif F.loc[i,'PERFORMANCE']>=2:
            F.loc[i,'PAYOUT%']='35%'
            F.loc[i,'PAYOUT']=F.loc[i,'MONEY_COLLECTION']*35/100
    
# PL-SELF
    
    elif (F.loc[i,'PRODUCT']=='PL Self') and (F.loc[i,'VINTAGE']=='V1'):
        if F.loc[i,'PERFORMANCE']<5:
            F.loc[i,'PAYOUT%']='16%'
            F.loc[i,'PAYOUT']=F.loc[i,'MONEY_COLLECTION']*16/100
        elif F.loc[i,'PERFORMANCE']>=5 and F.loc[i,'PERFORMANCE']<6:
            F.loc[i,'PAYOUT%']='17.5%'
            F.loc[i,'PAYOUT']=F.loc[i,'MONEY_COLLECTION']*17.5/100
        elif F.loc[i,'PERFORMANCE']>=6:
            F.loc[i,'PAYOUT%']='20%'
            F.loc[i,'PAYOUT']=F.loc[i,'MONEY_COLLECTION']*20/100
    elif (F.loc[i,'PRODUCT']=='PL Self') and (F.loc[i,'VINTAGE']=='V2'):
        if F.loc[i,'PERFORMANCE']<4:
            F.loc[i,'PAYOUT%']='17.5%'
            F.loc[i,'PAYOUT']=F.loc[i,'MONEY_COLLECTION']*17.5/100
        elif F.loc[i,'PERFORMANCE']>=4 and F.loc[i,'PERFORMANCE']<5:
            F.loc[i,'PAYOUT%']='20%'
            F.loc[i,'PAYOUT']=F.loc[i,'MONEY_COLLECTION']*20/100
        elif F.loc[i,'PERFORMANCE']>=5:
            F.loc[i,'PAYOUT%']='22.5%'
            F.loc[i,'PAYOUT']=F.loc[i,'MONEY_COLLECTION']*22.5/100
    elif (F.loc[i,'PRODUCT']=='PL Self') and (F.loc[i,'VINTAGE']=='V3'):
        if F.loc[i,'PERFORMANCE']<3:
            F.loc[i,'PAYOUT%']='20%'
            F.loc[i,'PAYOUT']=F.loc[i,'MONEY_COLLECTION']*20/100
        elif F.loc[i,'PERFORMANCE']>=3 and F.loc[i,'PERFORMANCE']<4:
            F.loc[i,'PAYOUT%']='22.5%'
            F.loc[i,'PAYOUT']=F.loc[i,'MONEY_COLLECTION']*22.5/100
        elif F.loc[i,'PERFORMANCE']>=4:
            F.loc[i,'PAYOUT%']='25%'
            F.loc[i,'PAYOUT']=F.loc[i,'MONEY_COLLECTION']*25/100
    elif (F.loc[i,'PRODUCT']=='PL Self') and (F.loc[i,'VINTAGE']=='V4'):
        if F.loc[i,'PERFORMANCE']<2:
            F.loc[i,'PAYOUT%']='22.5%'
            F.loc[i,'PAYOUT']=F.loc[i,'MONEY_COLLECTION']*22.5/100
        elif F.loc[i,'PERFORMANCE']>=2 and F.loc[i,'PERFORMANCE']<3:
            F.loc[i,'PAYOUT%']='25%'
            F.loc[i,'PAYOUT']=F.loc[i,'MONEY_COLLECTION']*25/100
        elif F.loc[i,'PERFORMANCE']>=3:
            F.loc[i,'PAYOUT%']='27.5%'
            F.loc[i,'PAYOUT']=F.loc[i,'MONEY_COLLECTION']*27.5/100
    elif (F.loc[i,'PRODUCT']=='PL Self') and (F.loc[i,'VINTAGE']=='V5'):
        if F.loc[i,'PERFORMANCE']<1:
            F.loc[i,'PAYOUT%']='25%'
            F.loc[i,'PAYOUT']=F.loc[i,'MONEY_COLLECTION']*25/100
        elif F.loc[i,'PERFORMANCE']>=1 and F.loc[i,'PERFORMANCE']<2:
            F.loc[i,'PAYOUT%']='27.5%'
            F.loc[i,'PAYOUT']=F.loc[i,'MONEY_COLLECTION']*27.5/100
        elif F.loc[i,'PERFORMANCE']>=2:
            F.loc[i,'PAYOUT%']='30%'
            F.loc[i,'PAYOUT']=F.loc[i,'MONEY_COLLECTION']*30/100
    elif (F.loc[i,'PRODUCT']=='PL Self') and (F.loc[i,'VINTAGE']=='V6'):
        if F.loc[i,'PERFORMANCE']<1:
            F.loc[i,'PAYOUT%']='30%'
            F.loc[i,'PAYOUT']=F.loc[i,'MONEY_COLLECTION']*30/100
        elif F.loc[i,'PERFORMANCE']>=1 and F.loc[i,'PERFORMANCE']<1.5:
            F.loc[i,'PAYOUT%']='32.5%'
            F.loc[i,'PAYOUT']=F.loc[i,'MONEY_COLLECTION']*32.5/100
        elif F.loc[i,'PERFORMANCE']>=1.5:
            F.loc[i,'PAYOUT%']='35%'
            F.loc[i,'PAYOUT']=F.loc[i,'MONEY_COLLECTION']*35/100

A['TOTAL PAID'].fillna(0,inplace=True)

F.to_excel(r'/Users/mohaksehgal/Documents/Work/Billing/FULLERTON/JUN 21/PAYOUT_FULLERTON_RECOVERY.xlsx',index=False)

A.to_excel(r'/Users/mohaksehgal/Documents/Work/TC Performance/FULLERTON/JUN 21/MASTER_FILE_FULLERTON_RECOVERY.xlsx',index=False)

A.to_excel(r'/Users/mohaksehgal/Documents/Work/MIS/FULLERTON/JUN 21/MASTER_FILE_FULLERTON_RECOVERY.xlsx',index=False)

A.to_excel(r'/Users/mohaksehgal/Documents/Work/FOS Salary/FULLERTON/JUN 21/MASTER_FILE_FULLERTON_RECOVERY.xlsx',index=False)