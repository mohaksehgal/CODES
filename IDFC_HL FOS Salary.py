#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 07:26:02 2020

@author: mohaksehgal
"""


import pandas as pd
import numpy as np

A=pd.read_excel(r"/Users/mohaksehgal/Documents/Work/FOS Salary/IDFC/MAR 21/MASTER FILE IDFC.xlsx")
PAID_FILE=pd.read_excel(r"/Users/mohaksehgal/Documents/Work/MIS/IDFC/MAR 21/IDFC_PAID FILE_31MAR21.xlsx")


BKT1B=[]
for i in range(0,len(PAID_FILE['BKT'])):
    if (PAID_FILE.loc[i,'BKT']==1) and (PAID_FILE.loc[i,'BOUNCING AMT.']!=0) and (PAID_FILE.loc[i,'MODE']!='CASH'):
        BKT1B.append(i)

PAID_FILE.drop(BKT1B,axis=0,inplace=True)

PAID_FILE=PAID_FILE.reset_index(drop=True)

BOU_AMT=pd.DataFrame(PAID_FILE.groupby(['FOS','BKT'])['BOUNCING AMT.'].sum()).reset_index()

PAID_FILE=PAID_FILE[PAID_FILE['BOUNCING AMT.']>=200]

BOU=pd.DataFrame(PAID_FILE.groupby(['FOS','BKT','AGREEMENTID'])['BOUNCING AMT.'].sum()).reset_index()

d=[]
for i in range(0,len(BOU['FOS'])):
    if BOU.loc[i,'BOUNCING AMT.']==0:
        d.append(i)

BOU.drop(d,axis=0,inplace=True)

BOU=BOU.reset_index(drop=True)

BOUNCING_CASE_COUNT=pd.DataFrame(BOU.groupby(['FOS','BKT'])['AGREEMENTID'].count()).reset_index()

F=pd.DataFrame(A.groupby(['FOS','BKT'])['POS'].sum()).reset_index()

R1=pd.DataFrame(A.groupby(['FOS','BKT','STATUS'])['POS'].sum()).reset_index()

AA=pd.DataFrame(A.groupby(['FOS','BKT'])['AGREEMENTID'].count()).reset_index()

F=F.merge(AA,how='outer')

F=F.reset_index(drop=True)

F.rename({'AGREEMENTID':'CASE_COUNT'},axis=1,inplace=True)

# BOUNCING_CASE_COUNT.rename({'PROCESS':'COMPANY'},axis=1,inplace=True)

for i in range(0,len(BOUNCING_CASE_COUNT['FOS'])):
    if BOUNCING_CASE_COUNT.loc[i,'BKT']==0:
        BOUNCING_CASE_COUNT.loc[i,'BKT']='BKT0'
    elif BOUNCING_CASE_COUNT.loc[i,'BKT']==1:
        BOUNCING_CASE_COUNT.loc[i,'BKT']='BKT1'

F=F.merge(BOUNCING_CASE_COUNT,how='outer')

F.rename({'AGREEMENTID':'BOUNCING_CASE_COUNT'},axis=1,inplace=True)

# BOU_AMT.rename({'PROCESS':'COMPANY'},axis=1,inplace=True)

for i in range(0,len(BOU_AMT['FOS'])):
    if BOU_AMT.loc[i,'BKT']==0:
        BOU_AMT.loc[i,'BKT']='BKT0'
    elif BOU_AMT.loc[i,'BKT']==1:
        BOU_AMT.loc[i,'BKT']='BKT1'
    elif BOU_AMT.loc[i,'BKT']==6:
        BOU_AMT.loc[i,'BKT']='BKT6'

F=F.merge(BOU_AMT,how='outer')

P=F.copy()

P=P.iloc[:,:3]

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
    F.loc[i,'RB+NM']=F.loc[i,'RB']+F.loc[i,'NM']+F.loc[i,'FORECLOSE']+F.loc[i,'SETTLEMENT']

for i in range(0,len(F['FOS'])):
    F.loc[i,'Performance']=F.loc[i,'POS']/F.loc[i,'TOTAL POS']*100
    F.loc[i,'RB+NM%']=F.loc[i,'RB+NM']/F.loc[i,'TOTAL POS']*100

F.fillna(0,inplace=True)

for i in range(0,len(A['AGREEMENTID'])):
    for j in range(0,len(F['FOS'])):
        if (A.loc[i,'BKT']=='BKT0' and F.loc[j,'BKT']=='BKT0'):
            # and ((A.loc[i,'COMPANY']=='HFC') and (F.loc[j,'COMPANY']=='HFC')):
            if (A.loc[i,['FOS','BKT']]==F.loc[j,['FOS','BKT']]).all():
                if (A.loc[i,'STATUS']!='SETTLEMENT') and (A.loc[i,'STATUS']!='FORECLOSE'):
                    if F.loc[j,'Performance']<88:
                        A.loc[i,'FOS PERCENTAGE']=str(0)+'%'
                        A.loc[i,'PER PAID CASE']=A.loc[i,'Billing PAID AMT.']*0/100
                    elif F.loc[j,'Performance']>=88 and F.loc[j,'Performance']<90:
                        A.loc[i,'FOS PERCENTAGE']=str(0.65)+'%'
                        A.loc[i,'PER PAID CASE']=A.loc[i,'Billing PAID AMT.']*0.65/100
                    elif F.loc[j,'Performance']>=90 and F.loc[j,'Performance']<92:
                        A.loc[i,'FOS PERCENTAGE']=str(1)+'%'
                        A.loc[i,'MOHAK']=A.loc[i,'Billing PAID AMT.']*1/100
                    elif F.loc[j,'Performance']>=92 and F.loc[j,'Performance']<94:
                        A.loc[i,'FOS PERCENTAGE']=str(1.5)+'%'
                        A.loc[i,'PER PAID CASE']=A.loc[i,'Billing PAID AMT.']*1.5/100
                    elif F.loc[j,'Performance']>=94:
                        A.loc[i,'FOS PERCENTAGE']=str(2)+'%'
                        A.loc[i,'PER PAID CASE']=A.loc[i,'Billing PAID AMT.']*2/100
        elif (A.loc[i,'BKT']=='BKT0' and F.loc[j,'BKT']=='BKT0'): 
            # and ((A.loc[i,'COMPANY']=='SUVIDHA') and (F.loc[j,'COMPANY']=='SUVIDHA')):
            if (A.loc[i,['FOS','BKT']]==F.loc[j,['FOS','BKT']]).all():
                if (A.loc[i,'STATUS']!='SETTLEMENT') and (A.loc[i,'STATUS']!='FORECLOSE'):
                    if F.loc[j,'Performance']<84:
                        A.loc[i,'FOS PERCENTAGE']=str(0)+'%'
                        A.loc[i,'PER PAID CASE']=A.loc[i,'Billing PAID AMT.']*0/100
                    elif F.loc[j,'Performance']>=84 and F.loc[j,'Performance']<88:
                        A.loc[i,'FOS PERCENTAGE']=str(1)+'%'
                        A.loc[i,'PER PAID CASE']=A.loc[i,'Billing PAID AMT.']*1/100
                    elif F.loc[j,'Performance']>=88 and F.loc[j,'Performance']<90:
                        A.loc[i,'FOS PERCENTAGE']=str(1.5)+'%'
                        A.loc[i,'MOHAK']=A.loc[i,'Billing PAID AMT.']*1.5/100
                    elif F.loc[j,'Performance']>=90:
                        A.loc[i,'FOS PERCENTAGE']=str(2)+'%'
                        A.loc[i,'PER PAID CASE']=A.loc[i,'Billing PAID AMT.']*2/100

for i in range(0,len(A['AGREEMENTID'])):
    for j in range(0,len(F['FOS'])):
        if (A.loc[i,'BKT']=='BKT1' and F.loc[j,'BKT']=='BKT1'):
            # and ((A.loc[i,'COMPANY']=='HFC') and (F.loc[j,'COMPANY']=='HFC')):
            if (A.loc[i,['FOS','BKT']]==F.loc[j,['FOS','BKT']]).all():
                if (A.loc[i,'STATUS']!='SETTLEMENT') and (A.loc[i,'STATUS']!='FORECLOSE'):
                    if F.loc[j,'Performance']<82:
                        A.loc[i,'FOS PERCENTAGE']=str(0)+'%'
                        A.loc[i,'PER PAID CASE']=A.loc[i,'Billing PAID AMT.']*0/100
                    elif F.loc[j,'Performance']>=82 and F.loc[j,'Performance']<84:
                        A.loc[i,'FOS PERCENTAGE']=str(0.5)+'%'
                        A.loc[i,'PER PAID CASE']=A.loc[i,'Billing PAID AMT.']*0.5/100
                    elif F.loc[j,'Performance']>=84 and F.loc[j,'Performance']<86:
                        A.loc[i,'FOS PERCENTAGE']=str(1)+'%'
                        A.loc[i,'MOHAK']=A.loc[i,'Billing PAID AMT.']*1/100
                    elif F.loc[j,'Performance']>=86 and F.loc[j,'Performance']<90:
                        A.loc[i,'FOS PERCENTAGE']=str(1.5)+'%'
                        A.loc[i,'PER PAID CASE']=A.loc[i,'Billing PAID AMT.']*1.5/100
                    elif F.loc[j,'Performance']>=90:
                        A.loc[i,'FOS PERCENTAGE']=str(2)+'%'
                        A.loc[i,'PER PAID CASE']=A.loc[i,'Billing PAID AMT.']*2/100
        elif (A.loc[i,'BKT']=='BKT1' and F.loc[j,'BKT']=='BKT1'): 
            # and ((A.loc[i,'COMPANY']=='SUVIDHA') and (F.loc[j,'COMPANY']=='SUVIDHA')):
            if (A.loc[i,['FOS','BKT']]==F.loc[j,['FOS','BKT']]).all():
                if (A.loc[i,'STATUS']!='SETTLEMENT') and (A.loc[i,'STATUS']!='FORECLOSE'):
                    if F.loc[j,'Performance']<82:
                        A.loc[i,'FOS PERCENTAGE']=str(0)+'%'
                        A.loc[i,'PER PAID CASE']=A.loc[i,'Billing PAID AMT.']*0/100
                    elif F.loc[j,'Performance']>=82 and F.loc[j,'Performance']<84:
                        A.loc[i,'FOS PERCENTAGE']=str(1)+'%'
                        A.loc[i,'PER PAID CASE']=A.loc[i,'Billing PAID AMT.']*1/100
                    elif F.loc[j,'Performance']>=84 and F.loc[j,'Performance']<86:
                        A.loc[i,'FOS PERCENTAGE']=str(1.5)+'%'
                        A.loc[i,'MOHAK']=A.loc[i,'Billing PAID AMT.']*1.5/100
                    elif F.loc[j,'Performance']>=86:
                        A.loc[i,'FOS PERCENTAGE']=str(2)+'%'
                        A.loc[i,'PER PAID CASE']=A.loc[i,'Billing PAID AMT.']*2/100

for i in range(0,len(F['FOS'])):
    if F.loc[i,'BKT']=='BKT1':
        if (F.loc[i,'RB+NM%']<10):
            F.loc[i,'EXTRA INCENTIVE']='Deduction of 10%'
        elif (F.loc[i,'RB+NM%']>=10) and (F.loc[i,'RB+NM%']<15):
            F.loc[i,'EXTRA INCENTIVE']='Deduction of 5%'
        elif ((F.loc[i,'RB+NM%']>=15) and (F.loc[i,'RB+NM%']<18)):
            F.loc[i,'EXTRA INCENTIVE']=0
        elif ((F.loc[i,'RB+NM%']>=18) and (F.loc[i,'RB+NM%']<22)):
            F.loc[i,'EXTRA INCENTIVE']=1000
        elif ((F.loc[i,'RB+NM%']>=22) and (F.loc[i,'RB+NM%']<24)):
            F.loc[i,'EXTRA INCENTIVE']=2000
        elif ((F.loc[i,'RB+NM%']>=24) and (F.loc[i,'RB+NM%']<30)):
            F.loc[i,'EXTRA INCENTIVE']=3000
        elif (F.loc[i,'RB+NM%']>=30):
            F.loc[i,'EXTRA INCENTIVE']=5000

for i in range(0,len(F['BOUNCING_CASE_COUNT'])):
    F.loc[i,'PENALTY_CHARGES']=F.loc[i,'BOUNCING_CASE_COUNT']/F.loc[i,'CASE_COUNT']*100

for i in range(0,len(F['FOS'])):
    if F.loc[i,'PENALTY_CHARGES']>=70:
        F.loc[i,'PENALTY_PAYOUT']=(F.loc[i,'BOUNCING AMT.'])*(8/100)
    else:
        F.loc[i,'PENALTY_PAYOUT']=0

for i in range(0,len(A['PER PAID CASE'])):
    if (A.loc[i,'STATUS']=='PART PAID') or (A.loc[i,'STATUS']=='FLOW'):
        A.loc[i,'FOS PERCENTAGE']=str(0)+'%'
        A.loc[i,'PER PAID CASE']=0

for i in range(0,len(A['STATUS'])):
    if (A.loc[i,'STATUS']=='SETTLEMENT') or (A.loc[i,'STATUS']=='FORECLOSE'):
        if A.loc[i,'BKT']=='BKT0':
            if A.loc[i,'Billing PAID AMT.']>A.loc[i,'EMI']:
                A.loc[i,'Billing PAID AMT.']=A.loc[i,'EMI']
            elif A.loc[i,'Billing PAID AMT.']<A.loc[i,'EMI']:
                A.loc[i,'Billing PAID AMT.']=0
        elif A.loc[i,'BKT']=='BKT1':
            if A.loc[i,'Billing PAID AMT.']>A.loc[i,'EMI']*2:
                A.loc[i,'Billing PAID AMT.']=A.loc[i,'EMI']*2
            elif (A.loc[i,'Billing PAID AMT.']>A.loc[i,'EMI']) and (A.loc[i,'Billing PAID AMT.']<A.loc[i,'EMI']*2):
                A.loc[i,'Billing PAID AMT.']=A.loc[i,'EMI']
            elif (A.loc[i,'Billing PAID AMT.']<A.loc[i,'EMI']):
                A.loc[i,'Billing PAID AMT']=0

for i in range(0,len(A['AGREEMENTID'])):
    for j in range(0,len(F['FOS'])):
        if (A.loc[i,'BKT']=='BKT0' and F.loc[j,'BKT']=='BKT0'): 
            # and ((A.loc[i,'COMPANY']=='HFC') and (F.loc[j,'COMPANY']=='HFC')):
            if (A.loc[i,['FOS','BKT']]==F.loc[j,['FOS','BKT']]).all():
                if (A.loc[i,'STATUS']=='SETTLEMENT') or (A.loc[i,'STATUS']=='FORECLOSE'):
                    if F.loc[j,'Performance']<88:
                        A.loc[i,'FOS PERCENTAGE']=str(0)+'%'
                        A.loc[i,'PER PAID CASE']=A.loc[i,'Billing PAID AMT.']*0/100
                    elif F.loc[j,'Performance']>=88 and F.loc[j,'Performance']<90:
                        A.loc[i,'FOS PERCENTAGE']=str(0.65)+'%'
                        A.loc[i,'PER PAID CASE']=A.loc[i,'Billing PAID AMT.']*0.65/100
                    elif F.loc[j,'Performance']>=90 and F.loc[j,'Performance']<92:
                        A.loc[i,'FOS PERCENTAGE']=str(1)+'%'
                        A.loc[i,'MOHAK']=A.loc[i,'Billing PAID AMT.']*1/100
                    elif F.loc[j,'Performance']>=92 and F.loc[j,'Performance']<94:
                        A.loc[i,'FOS PERCENTAGE']=str(1.5)+'%'
                        A.loc[i,'PER PAID CASE']=A.loc[i,'Billing PAID AMT.']*1.5/100
                    elif F.loc[j,'Performance']>=94:
                        A.loc[i,'FOS PERCENTAGE']=str(2)+'%'
                        A.loc[i,'PER PAID CASE']=A.loc[i,'Billing PAID AMT.']*2/100
        elif (A.loc[i,'BKT']=='BKT0' and F.loc[j,'BKT']=='BKT0'): 
            # and ((A.loc[i,'COMPANY']=='SUVIDHA') and (F.loc[j,'COMPANY']=='SUVIDHA')):
            if (A.loc[i,['FOS','BKT']]==F.loc[j,['FOS','BKT']]).all():
                if (A.loc[i,'STATUS']=='SETTLEMENT') or (A.loc[i,'STATUS']=='FORECLOSE'):
                    if F.loc[j,'Performance']<84:
                        A.loc[i,'FOS PERCENTAGE']=str(0)+'%'
                        A.loc[i,'PER PAID CASE']=A.loc[i,'Billing PAID AMT.']*0/100
                    elif F.loc[j,'Performance']>=84 and F.loc[j,'Performance']<88:
                        A.loc[i,'FOS PERCENTAGE']=str(1)+'%'
                        A.loc[i,'PER PAID CASE']=A.loc[i,'Billing PAID AMT.']*1/100
                    elif F.loc[j,'Performance']>=88 and F.loc[j,'Performance']<90:
                        A.loc[i,'FOS PERCENTAGE']=str(1.5)+'%'
                        A.loc[i,'MOHAK']=A.loc[i,'Billing PAID AMT.']*1.5/100
                    elif F.loc[j,'Performance']>=90:
                        A.loc[i,'FOS PERCENTAGE']=str(2)+'%'
                        A.loc[i,'PER PAID CASE']=A.loc[i,'Billing PAID AMT.']*2/100

for i in range(0,len(A['AGREEMENTID'])):
    for j in range(0,len(F['FOS'])):
        if (A.loc[i,'BKT']=='BKT1' and F.loc[j,'BKT']=='BKT1'):
            # and ((A.loc[i,'COMPANY']=='HFC') and (F.loc[j,'COMPANY']=='HFC')):
            if (A.loc[i,['FOS','BKT']]==F.loc[j,['FOS','BKT']]).all():
                if (A.loc[i,'STATUS']=='SETTLEMENT') or (A.loc[i,'STATUS']=='FORECLOSE'):
                    if F.loc[j,'Performance']<82:
                        A.loc[i,'FOS PERCENTAGE']=str(0)+'%'
                        A.loc[i,'PER PAID CASE']=A.loc[i,'Billing PAID AMT.']*0/100
                    elif F.loc[j,'Performance']>=82 and F.loc[j,'Performance']<84:
                        A.loc[i,'FOS PERCENTAGE']=str(0.5)+'%'
                        A.loc[i,'PER PAID CASE']=A.loc[i,'Billing PAID AMT.']*0.5/100
                    elif F.loc[j,'Performance']>=84 and F.loc[j,'Performance']<86:
                        A.loc[i,'FOS PERCENTAGE']=str(1)+'%'
                        A.loc[i,'MOHAK']=A.loc[i,'Billing PAID AMT.']*1/100
                    elif F.loc[j,'Performance']>=86 and F.loc[j,'Performance']<90:
                        A.loc[i,'FOS PERCENTAGE']=str(1.5)+'%'
                        A.loc[i,'PER PAID CASE']=A.loc[i,'Billing PAID AMT.']*1.5/100
                    elif F.loc[j,'Performance']>=90:
                        A.loc[i,'FOS PERCENTAGE']=str(2)+'%'
                        A.loc[i,'PER PAID CASE']=A.loc[i,'Billing PAID AMT.']*2/100
        elif (A.loc[i,'BKT']=='BKT1' and F.loc[j,'BKT']=='BKT1'):
            # and ((A.loc[i,'COMPANY']=='SUVIDHA') and (F.loc[j,'COMPANY']=='SUVIDHA')):
            if (A.loc[i,['FOS','BKT']]==F.loc[j,['FOS','BKT']]).all():
                if (A.loc[i,'STATUS']=='SETTLEMENT') or (A.loc[i,'STATUS']=='FORECLOSE'):
                    if F.loc[j,'Performance']<82:
                        A.loc[i,'FOS PERCENTAGE']=str(0)+'%'
                        A.loc[i,'PER PAID CASE']=A.loc[i,'Billing PAID AMT.']*0/100
                    elif F.loc[j,'Performance']>=82 and F.loc[j,'Performance']<84:
                        A.loc[i,'FOS PERCENTAGE']=str(1)+'%'
                        A.loc[i,'PER PAID CASE']=A.loc[i,'Billing PAID AMT.']*1/100
                    elif F.loc[j,'Performance']>=84 and F.loc[j,'Performance']<86:
                        A.loc[i,'FOS PERCENTAGE']=str(1.5)+'%'
                        A.loc[i,'MOHAK']=A.loc[i,'Billing PAID AMT.']*1.5/100
                    elif F.loc[j,'Performance']>=86:
                        A.loc[i,'FOS PERCENTAGE']=str(2)+'%'
                        A.loc[i,'PER PAID CASE']=A.loc[i,'Billing PAID AMT.']*2/100

for i in range(0,len(A['AGREEMENTID'])):
    if A.loc[i,'STATUS']=='SB':
        if A.loc[i,'PER PAID CASE']>500:
            A.loc[i,'PER PAID CASE']=500
    elif (A.loc[i,'STATUS']=='RB') or (A.loc[i,'STATUS']=='NM'):
        if A.loc[i,'PER PAID CASE']>1000:
            if A.loc[i,'Billing PAID AMT.']==A.loc[i,'EMI']:
                A.loc[i,'PER PAID CASE']=500
            elif A.loc[i,'Billing PAID AMT.']>=(A.loc[i,'EMI']*2):
                A.loc[i,'PER PAID CASE']=1000

F.fillna(0,inplace=True)

PPC=pd.DataFrame(A.groupby(['FOS','BKT'])['PER PAID CASE'].sum()).reset_index()

COMBINED_SALARY=F.merge(PPC)

COMBINED_SALARY=COMBINED_SALARY.reset_index(drop=True)

COMBINED_SALARY.drop(['SB','RB','NM','FORECLOSE','SETTLEMENT','POS','RB+NM'],axis=1,inplace=True)

A=pd.read_excel(r"/Users/mohaksehgal/Documents/Work/FOS Salary/IDFC/MAR 21/MASTER FILE IDFC.xlsx")

PAID_FILE=pd.read_excel(r"/Users/mohaksehgal/Documents/Work/MIS/IDFC/MAR 21/IDFC_PAID FILE_31MAR21.xlsx")

dr=[]
for i in range(0,len(PAID_FILE['DATE'])):
    if int(str(PAID_FILE.loc[i,'DATE'].date())[-2:])>10:
        dr.append(i)

PAID_FILE.drop(dr,axis=0,inplace=True)

q=pd.DataFrame(PAID_FILE.groupby(['AGREEMENTID'])['PAID AMOUNT'].sum()).reset_index()

ff=[]
for i in range(0,len(A['AGREEMENTID'])):
    if A.loc[i,'AGREEMENTID'] not in list(q['AGREEMENTID']):
        ff.append(i)

for i in range(0,len(q['AGREEMENTID'])):
    for j in range(0,len(A['AGREEMENTID'])):
        if q.loc[i,'AGREEMENTID']==A.loc[j,'AGREEMENTID']:
            if q.loc[i,'PAID AMOUNT']>=A.loc[j,'EMI']:
                A.loc[j,'STATUS']='SB'

F=pd.DataFrame(A.groupby(['FOS','BKT'])['POS'].sum()).reset_index()

R1=pd.DataFrame(A.groupby(['FOS','BKT','STATUS'])['POS'].sum()).reset_index()

AA=pd.DataFrame(A.groupby(['FOS','BKT'])['AGREEMENTID'].count()).reset_index()

F=F.merge(AA,how='outer')

F=F.reset_index(drop=True)

F.rename({'AGREEMENTID':'CASE_COUNT'},axis=1,inplace=True)

P=F.copy()

P=P.iloc[:,:3]

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
    F.loc[i,'RB+NM']=F.loc[i,'RB']+F.loc[i,'NM']+F.loc[i,'FORECLOSE']+F.loc[i,'SETTLEMENT']

for i in range(0,len(F['FOS'])):
    F.loc[i,'Performance']=F.loc[i,'POS']/F.loc[i,'TOTAL POS']*100
    F.loc[i,'RB+NM%']=F.loc[i,'RB+NM']/F.loc[i,'TOTAL POS']*100

one=F[['FOS','BKT','Performance']]

one.rename({'Performance':'10th Milestone'},axis=1,inplace=True)

COMBINED_SALARY=COMBINED_SALARY.merge(one)

A=pd.read_excel(r"/Users/mohaksehgal/Documents/Work/FOS Salary/IDFC/MAR 21/MASTER FILE IDFC.xlsx")

PAID_FILE=pd.read_excel(r"/Users/mohaksehgal/Documents/Work/MIS/IDFC/MAR 21/IDFC_PAID FILE_31MAR21.xlsx")

dr=[]
for i in range(0,len(PAID_FILE['DATE'])):
    if int(str(PAID_FILE.loc[i,'DATE'].date())[-2:])>20:
        dr.append(i)

PAID_FILE.drop(dr,axis=0,inplace=True)

q=pd.DataFrame(PAID_FILE.groupby(['AGREEMENTID'])['PAID AMOUNT'].sum()).reset_index()

ff=[]
for i in range(0,len(A['AGREEMENTID'])):
    if A.loc[i,'AGREEMENTID'] not in list(q['AGREEMENTID']):
        ff.append(i)

for i in range(0,len(q['AGREEMENTID'])):
    for j in range(0,len(A['AGREEMENTID'])):
        if q.loc[i,'AGREEMENTID']==A.loc[j,'AGREEMENTID']:
            if q.loc[i,'PAID AMOUNT']>=A.loc[j,'EMI']:
                A.loc[j,'STATUS']='SB'

F=pd.DataFrame(A.groupby(['FOS','BKT'])['POS'].sum()).reset_index()

R1=pd.DataFrame(A.groupby(['FOS','BKT','STATUS'])['POS'].sum()).reset_index()

AA=pd.DataFrame(A.groupby(['FOS','BKT'])['AGREEMENTID'].count()).reset_index()

F=F.merge(AA,how='outer')

F=F.reset_index(drop=True)

F.rename({'AGREEMENTID':'CASE_COUNT'},axis=1,inplace=True)

P=F.copy()

P=P.iloc[:,:3]

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
    F.loc[i,'RB+NM']=F.loc[i,'RB']+F.loc[i,'NM']+F.loc[i,'FORECLOSE']+F.loc[i,'SETTLEMENT']

for i in range(0,len(F['FOS'])):
    F.loc[i,'Performance']=F.loc[i,'POS']/F.loc[i,'TOTAL POS']*100
    F.loc[i,'RB+NM%']=F.loc[i,'RB+NM']/F.loc[i,'TOTAL POS']*100

two=F[['FOS','BKT','Performance']]

two.rename({'Performance':'20th Milestone'},axis=1,inplace=True)

COMBINED_SALARY=COMBINED_SALARY.merge(two)

A=pd.read_excel(r"/Users/mohaksehgal/Documents/Work/FOS Salary/IDFC/MAR 21/MASTER FILE IDFC.xlsx")

PAID_FILE=pd.read_excel(r"/Users/mohaksehgal/Documents/Work/MIS/IDFC/MAR 21/IDFC_PAID FILE_31MAR21.xlsx")

dr=[]
for i in range(0,len(PAID_FILE['DATE'])):
    if int(str(PAID_FILE.loc[i,'DATE'].date())[-2:])>25:
        dr.append(i)

PAID_FILE.drop(dr,axis=0,inplace=True)

q=pd.DataFrame(PAID_FILE.groupby(['AGREEMENTID'])['PAID AMOUNT'].sum()).reset_index()

ff=[]
for i in range(0,len(A['AGREEMENTID'])):
    if A.loc[i,'AGREEMENTID'] not in list(q['AGREEMENTID']):
        ff.append(i)

for i in range(0,len(q['AGREEMENTID'])):
    for j in range(0,len(A['AGREEMENTID'])):
        if q.loc[i,'AGREEMENTID']==A.loc[j,'AGREEMENTID']:
            if q.loc[i,'PAID AMOUNT']>=A.loc[j,'EMI']:
                A.loc[j,'STATUS']='SB'

F=pd.DataFrame(A.groupby(['FOS','BKT'])['POS'].sum()).reset_index()

R1=pd.DataFrame(A.groupby(['FOS','BKT','STATUS'])['POS'].sum()).reset_index()

AA=pd.DataFrame(A.groupby(['FOS','BKT'])['AGREEMENTID'].count()).reset_index()

F=F.merge(AA,how='outer')

F=F.reset_index(drop=True)

F.rename({'AGREEMENTID':'CASE_COUNT'},axis=1,inplace=True)

P=F.copy()

P=P.iloc[:,:3]

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
    F.loc[i,'RB+NM']=F.loc[i,'RB']+F.loc[i,'NM']+F.loc[i,'FORECLOSE']+F.loc[i,'SETTLEMENT']

for i in range(0,len(F['FOS'])):
    F.loc[i,'Performance']=F.loc[i,'POS']/F.loc[i,'TOTAL POS']*100
    F.loc[i,'RB+NM%']=F.loc[i,'RB+NM']/F.loc[i,'TOTAL POS']*100

three=F[['FOS','BKT','Performance']]

three.rename({'Performance':'25th Milestone'},axis=1,inplace=True)

COMBINED_SALARY=COMBINED_SALARY.merge(three)

COMBINED_SALARY.fillna(0,inplace=True)

a=COMBINED_SALARY.copy()





COMBINED_SALARY=a

for i in range(0,len(COMBINED_SALARY)):
    if COMBINED_SALARY.loc[i,'BKT']=='BKT0':
        if COMBINED_SALARY.loc[i,'20th Milestone']<50:
            COMBINED_SALARY.loc[i,'20th Milestone Incentive']='Deduction of 5%'
        elif (COMBINED_SALARY.loc[i,'20th Milestone']>=50) and (COMBINED_SALARY.loc[i,'20th Milestone']<65):
            COMBINED_SALARY.loc[i,'20th Milestone Incentive']=0
        elif COMBINED_SALARY.loc[i,'20th Milestone']>=65:
            COMBINED_SALARY.loc[i,'20th Milestone Incentive']=500

for i in range(0,len(COMBINED_SALARY)):
    if COMBINED_SALARY.loc[i,'BKT']=='BKT0':
        if COMBINED_SALARY.loc[i,'25th Milestone']<70:
            COMBINED_SALARY.loc[i,'25th Milestone Incentive']='Deduction of 5%'
        elif (COMBINED_SALARY.loc[i,'25th Milestone']>=70) and (COMBINED_SALARY.loc[i,'25th Milestone']<85):
            COMBINED_SALARY.loc[i,'25th Milestone Incentive']=0
        elif COMBINED_SALARY.loc[i,'25th Milestone']>=85:
            COMBINED_SALARY.loc[i,'25th Milestone Incentive']=500

for i in range(0,len(COMBINED_SALARY['FOS'])):
    if COMBINED_SALARY.loc[i,'BKT']=='BKT1':
        if COMBINED_SALARY.loc[i,'20th Milestone']<50:
            COMBINED_SALARY.loc[i,'20th Milestone Incentive']='Deduction of 5%'
        elif (COMBINED_SALARY.loc[i,'20th Milestone']>=50) and (COMBINED_SALARY.loc[i,'20th Milestone']<60):
            COMBINED_SALARY.loc[i,'20th Milestone Incentive']=0
        elif COMBINED_SALARY.loc[i,'20th Milestone']>=60:
            COMBINED_SALARY.loc[i,'20th Milestone Incentive']=500

for i in range(0,len(COMBINED_SALARY['FOS'])):
    if COMBINED_SALARY.loc[i,'BKT']=='BKT1':
        if COMBINED_SALARY.loc[i,'25th Milestone']<70:
            COMBINED_SALARY.loc[i,'25th Milestone Incentive']='Deduction of 5%'
        elif (COMBINED_SALARY.loc[i,'25th Milestone']>=70) and (COMBINED_SALARY.loc[i,'25th Milestone']<85):
            COMBINED_SALARY.loc[i,'25th Milestone Incentive']=0
        elif COMBINED_SALARY.loc[i,'25th Milestone']>=85:
            COMBINED_SALARY.loc[i,'25th Milestone Incentive']=500

for i in range(0,len(COMBINED_SALARY['FOS'])):
    if COMBINED_SALARY.loc[i,'BKT']=='BKT1':
        if COMBINED_SALARY.loc[i,'10th Milestone']<20:
            COMBINED_SALARY.loc[i,'10th Milestone Incentive']='Deduction of 5%'
        elif (COMBINED_SALARY.loc[i,'10th Milestone']>=20) and (COMBINED_SALARY.loc[i,'10th Milestone']<35):
            COMBINED_SALARY.loc[i,'10th Milestone Incentive']=0
        elif COMBINED_SALARY.loc[i,'10th Milestone']>=35:
            COMBINED_SALARY.loc[i,'10th Milestone Incentive']=500

COMBINED_SALARY.fillna(0,inplace=True)

COMBINED_SALARY=COMBINED_SALARY[['FOS','BKT','TOTAL POS','CASE_COUNT','BOUNCING_CASE_COUNT','BOUNCING AMT.','Performance','RB+NM%','PENALTY_CHARGES','10th Milestone','20th Milestone','25th Milestone','PER PAID CASE','EXTRA INCENTIVE','PENALTY_PAYOUT','10th Milestone Incentive','20th Milestone Incentive','25th Milestone Incentive']]

COMBINED_SALARY.to_excel('/Users/mohaksehgal/Documents/Work/FOS Salary/IDFC/MAR 21/COMBINED_SALARY.xlsx',index=False)

A.to_excel('/Users/mohaksehgal/Documents/Work/FOS Salary/IDFC/MAR 21/PER PAID CASE.xlsx',index=False)