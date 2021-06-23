#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 08:23:50 2020

@author: mohaksehgal
"""

import pandas as pd
import numpy as np

P=pd.read_excel(r'/Users/mohaksehgal/Documents/Work/Billing/AB/AB_BL/MARCH 20/Overall AB Performance.xlsx')

PA=pd.DataFrame({'RESO%':[90,92,94,95,96,97,98,99,100],'PAYOUT':[25000,25000,25000,25000,25000,25000,25000,25000,25000],
                 'Additional_Performance':[0,2000,4000,7000,11000,16000,22000,29000,37000]})


for i in range(0,len(PA['RESO%'])):
    if i==0: 
        if P.loc[0,'POS_RES%']<=PA.loc[i,'RESO%']:
            A=(PA.loc[i,'PAYOUT']*3)
            print(PA.loc[i,'PAYOUT']*3)
    if i>0:
        if P.loc[0,'POS_RES%']>PA.loc[i-1,'RESO%'] and P.loc<=PA.loc[i,'RESO%']:
            A=((PA.loc[i,'PAYOUT']+PA.loc[i,'Additional_Performance'])*3)
            print((PA.loc[i,'PAYOUT']+PA.loc[i,'Additional_Performance'])*3)
            
AA=pd.DataFrame(columns=['Payout'])
AA.loc[0,'Payout']=A

AA.to_excel(r'/Users/mohaksehgal/Documents/Work/Billing/AB/AB_BL/MARCH 20/Final Billing AB_BL.xlsx', index=False)