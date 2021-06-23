#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 09:17:11 2020

@author: mohaksehgal
"""


import pandas as pd
import numpy as np

A=pd.read_excel(r"/Users/mohaksehgal/Documents/Work/Billing/AB/AB 90+/MARCH 20/MASTER AB 90+.xlsx")

C=pd.DataFrame(A.groupby('BKT')['POS'].sum()).reset_index()

bkt=list(C[(C['BKT']!=5) & (C['BKT']!=6) & (C['BKT']!='T2') & (C['BKT']!='T3') & (C['BKT']!='T4') & (C['BKT']!='T5') & (C['BKT']!=7)].index)

C.drop(bkt,axis=0,inplace=True)

C=C.reset_index(drop=True)

PP=pd.DataFrame(A.groupby(['BKT','STATUS'])['POS'].sum()).reset_index()

bktP=list(PP[(PP['BKT']!=5) & (PP['BKT']!=6) & (PP['BKT']!='T2') & (PP['BKT']!='T3') & (PP['BKT']!='T4') & (PP['BKT']!='T5') & (PP['BKT']!=7)].index)

PP.drop(bktP,axis=0,inplace=True)

PP=PP.reset_index(drop=True)

C['PAID']=np.nan
C['UNPAID']=np.nan

for i in range(0,len(C['BKT'])):
    for j in range(0,len(PP['BKT'])):
        if C.loc[i,'BKT']==PP.loc[j,'BKT']:
            if PP.loc[j,'STATUS']=='PAID':
                C.loc[i,'PAID']=PP.loc[j,'POS']
            elif PP.loc[j,'STATUS']=='UNPAID':
                C.loc[i,'UNPAID']=PP.loc[j,'POS']
                
C.fillna(0,inplace=True)

C['Reso']=round((C['PAID']/C['POS'])*100,2)

for i in range(0,len(C['Reso'])):
    for j in range(0,len(A['PAID AMOUNT'])):
        if (A.loc[j,'BKT']==5) and (C.loc[i,'BKT']==5):
            if C.loc[i,'Reso']>=30:
                A.loc[j,'PAYOUT']=(A.loc[j,'PAID AMOUNT']*24)/100
            elif C.loc[i,'Reso']>=27:
                A.loc[j,'PAYOUT']=(A.loc[j,'PAID AMOUNT']*22)/100
            elif C.loc[i,'Reso']<27:
                A.loc[j,'PAYOUT']=(A.loc[j,'PAID AMOUNT']*18)/100
        elif (A.loc[j,'BKT']==6) and (C.loc[i,'BKT']==6):
            if C.loc[i,'Reso']>=25:
                A.loc[j,'PAYOUT']=(A.loc[j,'PAID AMOUNT']*24)/100
            elif C.loc[i,'Reso']>=21:
                A.loc[j,'PAYOUT']=(A.loc[j,'PAID AMOUNT']*22)/100
            elif C.loc[i,'Reso']<21:
                A.loc[j,'PAYOUT']=(A.loc[j,'PAID AMOUNT']*18)/100
        elif (A.loc[j,'BKT']=='T2') and (C.loc[i,'BKT']=='T2'):
            if C.loc[i,'Reso']>=30:
                A.loc[j,'PAYOUT']=(A.loc[j,'PAID AMOUNT']*25)/100
            elif C.loc[i,'Reso']>=25:
                A.loc[j,'PAYOUT']=(A.loc[j,'PAID AMOUNT']*23)/100
            elif C.loc[i,'Reso']<25:
                A.loc[j,'PAYOUT']=(A.loc[j,'PAID AMOUNT']*18)/100
        elif (A.loc[j,'BKT']=='T3') and (C.loc[i,'BKT']=='T3'):
            if C.loc[i,'Reso']>=30:
                A.loc[j,'PAYOUT']=(A.loc[j,'PAID AMOUNT']*25)/100
            elif C.loc[i,'Reso']>=25:
                A.loc[j,'PAYOUT']=(A.loc[j,'PAID AMOUNT']*23)/100
            elif C.loc[i,'Reso']<25:
                A.loc[j,'PAYOUT']=(A.loc[j,'PAID AMOUNT']*18)/100
        elif (A.loc[j,'BKT']=='T4') and (C.loc[i,'BKT']=='T4'):
            if C.loc[i,'Reso']>=30:
                A.loc[j,'PAYOUT']=(A.loc[j,'PAID AMOUNT']*25)/100
            elif C.loc[i,'Reso']>=25:
                A.loc[j,'PAYOUT']=(A.loc[j,'PAID AMOUNT']*23)/100
            elif C.loc[i,'Reso']<25:
                A.loc[j,'PAYOUT']=(A.loc[j,'PAID AMOUNT']*18)/100
        elif (A.loc[j,'BKT']=='T5') and (C.loc[i,'BKT']=='T5'):
            if C.loc[i,'Reso']>=30:
                A.loc[j,'PAYOUT']=(A.loc[j,'PAID AMOUNT']*25)/100
            elif C.loc[i,'Reso']>=25:
                A.loc[j,'PAYOUT']=(A.loc[j,'PAID AMOUNT']*23)/100
            elif C.loc[i,'Reso']<25:
                A.loc[j,'PAYOUT']=(A.loc[j,'PAID AMOUNT']*18)/100
                
above7=A[(A['BKT']!=5) & (A['BKT']!=6) & (A['BKT']!="T2") & (A['BKT']!="T3") & (A['BKT']!='T4') & (A['BKT']!='T5')]

DD=pd.DataFrame(above7.groupby('BKT')['POS'].sum()).reset_index()

DQ=pd.DataFrame(above7.groupby(['BKT','STATUS'])['POS'].sum()).reset_index()

DD['PAID']=np.nan
DD['UNPAID']=np.nan

for i in range(0,len(DD['BKT'])):
    for j in range(0,len(DQ['BKT'])):
        if DD.loc[i,'BKT']==DQ.loc[j,'BKT']:
            if DQ.loc[j,'STATUS']=='PAID':
                DD.loc[i,'PAID']=DQ.loc[j,'POS']
            elif DQ.loc[j,'STATUS']=='UNPAID':
                DD.loc[i,'UNPAID']=DQ.loc[j,'POS']
                
DD['Rate of Recovery']=(DD['PAID']/DD['POS'])*100

for i in range(0,len(DD['Rate of Recovery'])):
    for j in range(0,len(A['PAID AMOUNT'])):
        if (A.loc[j,'BKT']==8) and (DD.loc[i,'BKT']==8):
            if DD.loc[i,'Rate of Recovery']>2:
                A.loc[j,'PAYOUT']=(A.loc[j,'PAID AMOUNT']*25)/100
            elif DD.loc[i,'Rate of Recovery']>1.75:
                A.loc[j,'PAYOUT']=(A.loc[j,'PAID AMOUNT']*23)/100
            elif DD.loc[i,'Rate of Recovery']>1.5:
                A.loc[j,'PAYOUT']=(A.loc[j,'PAID AMOUNT']*22)/100
            elif DD.loc[i,'Rate of Recovery']>1.25:
                A.loc[j,'PAYOUT']=(A.loc[j,'PAID AMOUNT']*21)/100
            elif DD.loc[i,'Rate of Recovery']<1.25:
                A.loc[j,'PAYOUT']=(A.loc[j,'PAID AMOUNT']*20)/100
        elif (A.loc[j,'BKT']==9) and (DD.loc[i,'BKT']==9):
            if DD.loc[i,'Rate of Recovery']>2:
                A.loc[j,'PAYOUT']=(A.loc[j,'PAID AMOUNT']*25)/100
            elif DD.loc[i,'Rate of Recovery']>1.75:
                A.loc[j,'PAYOUT']=(A.loc[j,'PAID AMOUNT']*23)/100
            elif DD.loc[i,'Rate of Recovery']>1.5:
                A.loc[j,'PAYOUT']=(A.loc[j,'PAID AMOUNT']*22)/100
            elif DD.loc[i,'Rate of Recovery']>1.25:
                A.loc[j,'PAYOUT']=(A.loc[j,'PAID AMOUNT']*21)/100
            elif DD.loc[i,'Rate of Recovery']<1.25:
                A.loc[j,'PAYOUT']=(A.loc[j,'PAID AMOUNT']*20)/100
        elif (A.loc[j,'BKT']==11) and (DD.loc[i,'BKT']==11):
            if DD.loc[i,'Rate of Recovery']>2:
                A.loc[j,'PAYOUT']=(A.loc[j,'PAID AMOUNT']*25)/100
            elif DD.loc[i,'Rate of Recovery']>1.75:
                A.loc[j,'PAYOUT']=(A.loc[j,'PAID AMOUNT']*23)/100
            elif DD.loc[i,'Rate of Recovery']>1.5:
                A.loc[j,'PAYOUT']=(A.loc[j,'PAID AMOUNT']*22)/100
            elif DD.loc[i,'Rate of Recovery']>1.25:
                A.loc[j,'PAYOUT']=(A.loc[j,'PAID AMOUNT']*21)/100
            elif DD.loc[i,'Rate of Recovery']<1.25:
                A.loc[j,'PAYOUT']=(A.loc[j,'PAID AMOUNT']*20)/100
        elif (A.loc[j,'BKT']==12) and (DD.loc[i,'BKT']==12):
            if DD.loc[i,'Rate of Recovery']>2:
                A.loc[j,'PAYOUT']=(A.loc[j,'PAID AMOUNT']*25)/100
            elif DD.loc[i,'Rate of Recovery']>1.75:
                A.loc[j,'PAYOUT']=(A.loc[j,'PAID AMOUNT']*23)/100
            elif DD.loc[i,'Rate of Recovery']>1.5:
                A.loc[j,'PAYOUT']=(A.loc[j,'PAID AMOUNT']*22)/100
            elif DD.loc[i,'Rate of Recovery']>1.25:
                A.loc[j,'PAYOUT']=(A.loc[j,'PAID AMOUNT']*21)/100
            elif DD.loc[i,'Rate of Recovery']<1.25:
                A.loc[j,'PAYOUT']=(A.loc[j,'PAID AMOUNT']*20)/100
        elif (A.loc[j,'BKT']==14) and (DD.loc[i,'BKT']==14):
            if DD.loc[i,'Rate of Recovery']>2:
                A.loc[j,'PAYOUT']=(A.loc[j,'PAID AMOUNT']*25)/100
            elif DD.loc[i,'Rate of Recovery']>1.75:
                A.loc[j,'PAYOUT']=(A.loc[j,'PAID AMOUNT']*23)/100
            elif DD.loc[i,'Rate of Recovery']>1.5:
                A.loc[j,'PAYOUT']=(A.loc[j,'PAID AMOUNT']*22)/100
            elif DD.loc[i,'Rate of Recovery']>1.25:
                A.loc[j,'PAYOUT']=(A.loc[j,'PAID AMOUNT']*21)/100
            elif DD.loc[i,'Rate of Recovery']<1.25:
                A.loc[j,'PAYOUT']=(A.loc[j,'PAID AMOUNT']*20)/100
        elif (A.loc[j,'BKT']==15) and (DD.loc[i,'BKT']==15):
            if DD.loc[i,'Rate of Recovery']>2:
                A.loc[j,'PAYOUT']=(A.loc[j,'PAID AMOUNT']*25)/100
            elif DD.loc[i,'Rate of Recovery']>1.75:
                A.loc[j,'PAYOUT']=(A.loc[j,'PAID AMOUNT']*23)/100
            elif DD.loc[i,'Rate of Recovery']>1.5:
                A.loc[j,'PAYOUT']=(A.loc[j,'PAID AMOUNT']*22)/100
            elif DD.loc[i,'Rate of Recovery']>1.25:
                A.loc[j,'PAYOUT']=(A.loc[j,'PAID AMOUNT']*21)/100
            elif DD.loc[i,'Rate of Recovery']<1.25:
                A.loc[j,'PAYOUT']=(A.loc[j,'PAID AMOUNT']*20)/100
                
print(A[A['PAYOUT'].isnull()])

A.to_excel(r'/Users/mohaksehgal/Documents/Work/Billing/AB/AB 90+/MARCH 20/Final Billing AB_90+.xlsx',index=False)