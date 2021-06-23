#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 15:26:53 2020

@author: mohaksehgal
"""


import pandas as pd
import numpy as np

## Payouts

IDFC_HL=pd.read_excel('/Users/mohaksehgal/Documents/Work/Billing/IDFC/IDFC March 20/Final Billing IDFC.xlsx')

IDFC_TW=pd.read_excel('/Users/mohaksehgal/Documents/Work/Billing/IDFC TW/IDFC TW March 20/Final Billing TW.xlsx')

L_T=pd.read_excel('/Users/mohaksehgal/Documents/Work/Billing/L_T/L_T MARCH 20/Final Billing L_T.xlsx')

AB=pd.read_excel(r'/Users/mohaksehgal/Documents/Work/Billing/AB/AB_BL/MARCH 20/Final Billing AB_BL.xlsx')

AB_90=pd.read_excel(r'/Users/mohaksehgal/Documents/Work/Billing/AB/AB 90+/MARCH 20/Final Billing AB_90+.xlsx')

AB_90_Payout=AB_90['PAYOUT'].sum()

IDFC_Payout=IDFC_HL['PAYOUT'].sum()

L_T_Payout=L_T['PAYOUT'].sum()

IDFC_TW_Payout=IDFC_TW['PAYOUT'].sum()

TP=pd.DataFrame(columns=['IDFC','L&T','IDFC_TW','AB_BL'])

TP.loc[0,'IDFC']=IDFC_Payout
TP.loc[0,'L&T']=L_T_Payout
TP.loc[0,'IDFC_TW']=IDFC_TW_Payout
TP.loc[0,'AB_BL']=AB.loc[0,'Payout']
TP.loc[0,'AB_90+']=AB_90_Payout

TP.to_excel(r'/Users/mohaksehgal/Documents/Work/P&L/P&L Automate/Income.xlsx',index=False)