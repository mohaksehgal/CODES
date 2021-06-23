#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 12 13:08:50 2021

@author: rishi
"""

import pandas as pd
import numpy as np
pd.set_option('Display.max_columns',None)

A=pd.read_excel(r"/Users/mohaksehgal/Documents/Work/MIS/BAJAJ/JUN 21/BAJAJ Allocation 21 JUN 21.xlsx")

B=pd.read_excel(r"/Users/mohaksehgal/Documents/Work/MIS/BAJAJ/JUN 21/BAJAJ_PAID_FILE_22JUN21.xlsx")

B1=pd.DataFrame(B.groupby('AGREEMENTID')['PAID AMOUNT'].sum()).reset_index()

B2=pd.DataFrame(B.groupby(['AGREEMENTID','TC'])['PAID AMOUNT'].count()).reset_index()

ECS=pd.DataFrame(B.groupby(['AGREEMENTID','MODE'])['PAID AMOUNT'].sum()).reset_index()

ECS=ECS[ECS['MODE']=='ECS']

ECS.rename({'PAID AMOUNT':'ECS'},axis=1,inplace=True)

B1=B1.merge(ECS,how='left')

B1.drop('MODE',axis=1,inplace=True)

B1.fillna(0,inplace=True)

B1['FINAL PAID AMOUNT']=B1['PAID AMOUNT']-B1['ECS']

B2.drop('PAID AMOUNT',axis=1,inplace=True)

B2.rename({'TC':'PAID TC','AGREEMENTID':'LOAN_NUMBER'},axis=1,inplace=True)

B1.drop(['PAID AMOUNT','ECS'],axis=1,inplace=True)

B1.rename({'FINAL PAID AMOUNT':'PAID AMOUNT'},axis=1,inplace=True)

B1.rename({'AGREEMENTID':'LOAN_NUMBER'},axis=1,inplace=True)

A=A.merge(B2,how='left')

A=A.merge(B1,how='left')

for i in range(0,len(A['LOAN_NUMBER'])):
    if str(A.loc[i,'PAID AMOUNT'])=='nan':
        A.loc[i,'MOHAK STATUS']='UNPAID'
    elif str(A.loc[i,'PAID AMOUNT'])!='nan':
        A.loc[i,'MOHAK STATUS']='PAID'

A['MOHAK STATUS'].unique()

for i in range(0,len(A['PAID AMOUNT'])):
    if A.loc[i,'MOHAK STATUS']=='UNPAID':
        A.loc[i,'PAID AMOUNT']=0

A['PAID TC'].fillna('--',inplace=True)

A.rename({'MOHAK STATUS':'STATUS'},axis=1,inplace=True)

A.to_excel(r'/Users/mohaksehgal/Documents/Work/MIS/BAJAJ/JUN 21/MASTER_FILE_BAJAJ.xlsx',index=False)

MIS=pd.DataFrame(A.groupby(['LOAN_STATUS','TC NAME'])['POS'].sum().reset_index())

dr=[]
for i in range(0,len(MIS['TC NAME'])):
    if MIS.loc[i,'TC NAME']=='NO TC':
        dr.append(i)

MIS.drop(dr,axis=0,inplace=True)

MIS=MIS.reset_index(drop=True)

for i in range(0,len(A['LOAN_NUMBER'])):
    if A.loc[i,'STATUS']=='PAID':
        if A.loc[i,'PAID TC']!='SYS. PAID':
            if A.loc[i,'TC NAME']!=A.loc[i,'PAID TC']:
                print("ACTUAL TC-",A.loc[i,'TC NAME'],"PAID TC-",A.loc[i,'PAID TC'])

P=pd.DataFrame(A.groupby(['LOAN_STATUS','PAID TC'])['PAID AMOUNT'].sum().reset_index())

MIS=MIS.merge(P,left_on='TC NAME',right_on='PAID TC',how='left')

MIS.drop(['PAID TC','LOAN_STATUS_y'],axis=1,inplace=True)

MIS.rename({'LOAN_STATUS_x':'LOAN_STATUS'},axis=1,inplace=True)

MIS['PERFORMANCE']=MIS['PAID AMOUNT']/MIS['POS']*100

for i in range(0,len(MIS['TC NAME'])):
    if (MIS.loc[i,'PAID AMOUNT']>=150000) and (MIS.loc[i,'PAID AMOUNT']<200000):
        MIS.loc[i,'FLAT INCENTIVE']=1500
    elif (MIS.loc[i,'PAID AMOUNT']>=200000) and (MIS.loc[i,'PAID AMOUNT']<250000):
        MIS.loc[i,'FLAT INCENTIVE']=2500
    elif (MIS.loc[i,'PAID AMOUNT']>=250000) and (MIS.loc[i,'PAID AMOUNT']<300000):
        MIS.loc[i,'FLAT INCENTIVE']=4000
    elif (MIS.loc[i,'PAID AMOUNT']>=300000) and (MIS.loc[i,'PAID AMOUNT']<350000):
        MIS.loc[i,'FLAT INCENTIVE']=7000
    elif (MIS.loc[i,'PAID AMOUNT']>=350000) and (MIS.loc[i,'PAID AMOUNT']<400000):
        MIS.loc[i,'FLAT INCENTIVE']=10000
    elif (MIS.loc[i,'PAID AMOUNT']>=400000):
        MIS.loc[i,'FLAT INCENTIVE']=12000
    else:
        MIS.loc[i,'FLAT INCENTIVE']=0

SS=pd.DataFrame(A.groupby(['LOAN_STATUS','BUCKET'])['POS','PAID AMOUNT'].sum()).reset_index()

for i in range(0,len(SS['LOAN_STATUS'])):
    if (SS.loc[i,'LOAN_STATUS']=='EXPIRE') & (SS.loc[i,'BUCKET']==3):
        # if (SS.loc[i,'PAID AMOUNT']/SS.loc[i,'POS'])*100<=7:
        SS.loc[i,'PERFORMANCE']=(SS.loc[i,'PAID AMOUNT']/SS.loc[i,'POS'])*100
        SS.loc[i,'PAYOUT PERCENTAGE']='18%'
        SS.loc[i,'PAYOUT']=SS.loc[i,'PAID AMOUNT']*18/100
    elif (SS.loc[i,'LOAN_STATUS']=='EXPIRE') & (SS.loc[i,'BUCKET']==2):
        # if (SS.loc[i,'PAID AMOUNT']/SS.loc[i,'POS'])*100<=7:
        SS.loc[i,'PERFORMANCE']=(SS.loc[i,'PAID AMOUNT']/SS.loc[i,'POS'])*100
        SS.loc[i,'PAYOUT PERCENTAGE']='18%'
        SS.loc[i,'PAYOUT']=SS.loc[i,'PAID AMOUNT']*18/100
    elif (SS.loc[i,'LOAN_STATUS']=='ACTIVE') & (SS.loc[i,'BUCKET']==3):
        if (SS.loc[i,'PAID AMOUNT']/SS.loc[i,'POS'])*100<=7:
            SS.loc[i,'PERFORMANCE']=(SS.loc[i,'PAID AMOUNT']/SS.loc[i,'POS'])*100
            SS.loc[i,'PAYOUT PERCENTAGE']='12%'
            SS.loc[i,'PAYOUT']=SS.loc[i,'PAID AMOUNT']*12/100
        elif ((SS.loc[i,'PAID AMOUNT']/SS.loc[i,'POS'])*100>7) and ((SS.loc[i,'PAID AMOUNT']/SS.loc[i,'POS'])*100<=8):
            SS.loc[i,'PERFORMANCE']=(SS.loc[i,'PAID AMOUNT']/SS.loc[i,'POS'])*100
            SS.loc[i,'PAYOUT PERCENTAGE']='13%'
            SS.loc[i,'PAYOUT']=SS.loc[i,'PAID AMOUNT']*13/100
        elif ((SS.loc[i,'PAID AMOUNT']/SS.loc[i,'POS'])*100>8) and ((SS.loc[i,'PAID AMOUNT']/SS.loc[i,'POS'])*100<=9):
            SS.loc[i,'PERFORMANCE']=(SS.loc[i,'PAID AMOUNT']/SS.loc[i,'POS'])*100
            SS.loc[i,'PAYOUT PERCENTAGE']='14%'
            SS.loc[i,'PAYOUT']=SS.loc[i,'PAID AMOUNT']*14/100
        elif ((SS.loc[i,'PAID AMOUNT']/SS.loc[i,'POS'])*100>9) and ((SS.loc[i,'PAID AMOUNT']/SS.loc[i,'POS'])*100<=10):
            SS.loc[i,'PERFORMANCE']=(SS.loc[i,'PAID AMOUNT']/SS.loc[i,'POS'])*100
            SS.loc[i,'PAYOUT PERCENTAGE']='15%'
            SS.loc[i,'PAYOUT']=SS.loc[i,'PAID AMOUNT']*15/100
        elif ((SS.loc[i,'PAID AMOUNT']/SS.loc[i,'POS'])*100>10) and ((SS.loc[i,'PAID AMOUNT']/SS.loc[i,'POS'])*100<=11):
            SS.loc[i,'PERFORMANCE']=(SS.loc[i,'PAID AMOUNT']/SS.loc[i,'POS'])*100
            SS.loc[i,'PAYOUT PERCENTAGE']='16%'
            SS.loc[i,'PAYOUT']=SS.loc[i,'PAID AMOUNT']*16/100
        elif ((SS.loc[i,'PAID AMOUNT']/SS.loc[i,'POS'])*100>11) and ((SS.loc[i,'PAID AMOUNT']/SS.loc[i,'POS'])*100<=12):
            SS.loc[i,'PERFORMANCE']=(SS.loc[i,'PAID AMOUNT']/SS.loc[i,'POS'])*100
            SS.loc[i,'PAYOUT PERCENTAGE']='17%'
            SS.loc[i,'PAYOUT']=SS.loc[i,'PAID AMOUNT']*17/100
        elif ((SS.loc[i,'PAID AMOUNT']/SS.loc[i,'POS'])*100>12):
            SS.loc[i,'PERFORMANCE']=(SS.loc[i,'PAID AMOUNT']/SS.loc[i,'POS'])*100
            SS.loc[i,'PAYOUT PERCENTAGE']='18%'
            SS.loc[i,'PAYOUT']=SS.loc[i,'PAID AMOUNT']*18/100
    elif (SS.loc[i,'LOAN_STATUS']=='ACTIVE') & (SS.loc[i,'BUCKET']==4):
        if (SS.loc[i,'PAID AMOUNT']/SS.loc[i,'POS'])*100<=1:
            SS.loc[i,'PERFORMANCE']=(SS.loc[i,'PAID AMOUNT']/SS.loc[i,'POS'])*100
            SS.loc[i,'PAYOUT PERCENTAGE']='13%'
            SS.loc[i,'PAYOUT']=SS.loc[i,'PAID AMOUNT']*13/100
        elif ((SS.loc[i,'PAID AMOUNT']/SS.loc[i,'POS'])*100>1) and ((SS.loc[i,'PAID AMOUNT']/SS.loc[i,'POS'])*100<2):
            SS.loc[i,'PERFORMANCE']=(SS.loc[i,'PAID AMOUNT']/SS.loc[i,'POS'])*100
            SS.loc[i,'PAYOUT PERCENTAGE']='15%'
            SS.loc[i,'PAYOUT']=SS.loc[i,'PAID AMOUNT']*15/100
        elif ((SS.loc[i,'PAID AMOUNT']/SS.loc[i,'POS'])*100>2) and ((SS.loc[i,'PAID AMOUNT']/SS.loc[i,'POS'])*100<3):
            SS.loc[i,'PERFORMANCE']=(SS.loc[i,'PAID AMOUNT']/SS.loc[i,'POS'])*100
            SS.loc[i,'PAYOUT PERCENTAGE']='17%'
            SS.loc[i,'PAYOUT']=SS.loc[i,'PAID AMOUNT']*17/100
        elif ((SS.loc[i,'PAID AMOUNT']/SS.loc[i,'POS'])*100>3) and ((SS.loc[i,'PAID AMOUNT']/SS.loc[i,'POS'])*100<4):
            SS.loc[i,'PERFORMANCE']=(SS.loc[i,'PAID AMOUNT']/SS.loc[i,'POS'])*100
            SS.loc[i,'PAYOUT PERCENTAGE']='18%'
            SS.loc[i,'PAYOUT']=SS.loc[i,'PAID AMOUNT']*18/100
        elif ((SS.loc[i,'PAID AMOUNT']/SS.loc[i,'POS'])*100>4) and ((SS.loc[i,'PAID AMOUNT']/SS.loc[i,'POS'])*100<5):
            SS.loc[i,'PERFORMANCE']=(SS.loc[i,'PAID AMOUNT']/SS.loc[i,'POS'])*100
            SS.loc[i,'PAYOUT PERCENTAGE']='19%'
            SS.loc[i,'PAYOUT']=SS.loc[i,'PAID AMOUNT']*19/100
        elif ((SS.loc[i,'PAID AMOUNT']/SS.loc[i,'POS'])*100>1) and ((SS.loc[i,'PAID AMOUNT']/SS.loc[i,'POS'])*100<2):
            SS.loc[i,'PERFORMANCE']=(SS.loc[i,'PAID AMOUNT']/SS.loc[i,'POS'])*100
            SS.loc[i,'PAYOUT PERCENTAGE']='20%'
            SS.loc[i,'PAYOUT']=SS.loc[i,'PAID AMOUNT']*20/100
    elif (SS.loc[i,'LOAN_STATUS']=='ACTIVE') & ((SS.loc[i,'BUCKET']==5) or (SS.loc[i,'BUCKET']==6)):
        if (SS.loc[i,'PAID AMOUNT']/SS.loc[i,'POS'])*100<=1:
            SS.loc[i,'PERFORMANCE']=(SS.loc[i,'PAID AMOUNT']/SS.loc[i,'POS'])*100
            SS.loc[i,'PAYOUT PERCENTAGE']='14%'
            SS.loc[i,'PAYOUT']=SS.loc[i,'PAID AMOUNT']*14/100
        elif ((SS.loc[i,'PAID AMOUNT']/SS.loc[i,'POS'])*100>1) and ((SS.loc[i,'PAID AMOUNT']/SS.loc[i,'POS'])*100<2):
            SS.loc[i,'PERFORMANCE']=(SS.loc[i,'PAID AMOUNT']/SS.loc[i,'POS'])*100
            SS.loc[i,'PAYOUT PERCENTAGE']='16%'
            SS.loc[i,'PAYOUT']=SS.loc[i,'PAID AMOUNT']*16/100
        elif ((SS.loc[i,'PAID AMOUNT']/SS.loc[i,'POS'])*100>2) and ((SS.loc[i,'PAID AMOUNT']/SS.loc[i,'POS'])*100<3):
            SS.loc[i,'PERFORMANCE']=(SS.loc[i,'PAID AMOUNT']/SS.loc[i,'POS'])*100
            SS.loc[i,'PAYOUT PERCENTAGE']='17%'
            SS.loc[i,'PAYOUT']=SS.loc[i,'PAID AMOUNT']*17/100
        elif ((SS.loc[i,'PAID AMOUNT']/SS.loc[i,'POS'])*100>3) and ((SS.loc[i,'PAID AMOUNT']/SS.loc[i,'POS'])*100<4):
            SS.loc[i,'PERFORMANCE']=(SS.loc[i,'PAID AMOUNT']/SS.loc[i,'POS'])*100
            SS.loc[i,'PAYOUT PERCENTAGE']='18%'
            SS.loc[i,'PAYOUT']=SS.loc[i,'PAID AMOUNT']*18/100
        elif ((SS.loc[i,'PAID AMOUNT']/SS.loc[i,'POS'])*100>4) and ((SS.loc[i,'PAID AMOUNT']/SS.loc[i,'POS'])*100<5):
            SS.loc[i,'PERFORMANCE']=(SS.loc[i,'PAID AMOUNT']/SS.loc[i,'POS'])*100
            SS.loc[i,'PAYOUT PERCENTAGE']='20%'
            SS.loc[i,'PAYOUT']=SS.loc[i,'PAID AMOUNT']*20/100
        elif ((SS.loc[i,'PAID AMOUNT']/SS.loc[i,'POS'])*100>1) and ((SS.loc[i,'PAID AMOUNT']/SS.loc[i,'POS'])*100<2):
            SS.loc[i,'PERFORMANCE']=(SS.loc[i,'PAID AMOUNT']/SS.loc[i,'POS'])*100
            SS.loc[i,'PAYOUT PERCENTAGE']='21%'
            SS.loc[i,'PAYOUT']=SS.loc[i,'PAID AMOUNT']*21/100

MIS.to_excel(r'/Users/mohaksehgal/Documents/Work/MIS/BAJAJ/JUN 21/BAJAJ TC-WISE MIS.xlsx',index=False)

SS.to_excel(r'/Users/mohaksehgal/Documents/Work/Billing/BAJAJ/JUN 21/BAJAJ PAYOUT.xlsx',index=False)