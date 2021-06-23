#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 09:18:12 2020

@author: mohaksehgal
"""


import pandas as pd
import numpy as np

A=pd.read_excel(r"/Users/mohaksehgal/Documents/Work/TC Incentive/AB 90+/MARCH 20/MASTER FILE AB 90+.xlsx")

F1=pd.DataFrame(A.groupby(['TC NAME'])['PAID AMOUNT'].sum()).reset_index()

F=F1.copy()

for i in range(0,len(F['TC NAME'])):
    if F.loc[i,'PAID AMOUNT']<100000:
        F.loc[i,'PAYOUT']=0
    elif F.loc[i,'PAID AMOUNT']>=100000 and F.loc[i,'PAID AMOUNT']<150000:
        F.loc[i,'PAYOUT']=(F.loc[i,'PAID AMOUNT']*1)/100
    elif F.loc[i,'PAID AMOUNT']>=150000 and F.loc[i,'PAID AMOUNT']<200000:
        F.loc[i,'PAYOUT']=(F.loc[i,'PAID AMOUNT']*1.5)/100
    elif F.loc[i,'PAID AMOUNT']>=200000 and F.loc[i,'PAID AMOUNT']<250000:
        F.loc[i,'PAYOUT']=(F.loc[i,'PAID AMOUNT']*2)/100
    elif F.loc[i,'PAID AMOUNT']>=250000 and F.loc[i,'PAID AMOUNT']<300000:
        F.loc[i,'PAYOUT']=(F.loc[i,'PAID AMOUNT']*2.5)/100
    elif F.loc[i,'PAID AMOUNT']>=300000 and F.loc[i,'PAID AMOUNT']<350000:
        F.loc[i,'PAYOUT']=(F.loc[i,'PAID AMOUNT']*3)/100
    elif F.loc[i,'PAID AMOUNT']>=350000 and F.loc[i,'PAID AMOUNT']<400000:
        F.loc[i,'PAYOUT']=(F.loc[i,'PAID AMOUNT']*3.5)/100
    elif F.loc[i,'PAID AMOUNT']>=400000 and F.loc[i,'PAID AMOUNT']<450000:
        F.loc[i,'PAYOUT']=(F.loc[i,'PAID AMOUNT']*4)/100

F.to_excel(r'/Users/mohaksehgal/Documents/Work/TC Incentive/AB 90+/MARCH 20/AB 90+ TC Incentive.xlsx',index=False)