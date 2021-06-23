#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 16:05:22 2020

@author: mohaksehgal
"""


import pandas as pd
import numpy as np

D=pd.read_excel(r'/Users/mohaksehgal/Documents/Work/Dump/Master File.xlsx')

D['Status'].replace(['RNG','REDIAL','CDC','DIS','FRCLS_RQST','FORECLSD','WRN','NACH','SOA','SUFF_BAL','LOANCNLCD',
                     'STLMNT','BNC_CNFRM','DNC','ALTDIAL','NI','HotTransfer','LOANCNLD','SOARQRD','LOANCNCLD','DEATH',
                    'LP','FRLSD','CPURQST','TWSRNDR','FRCLSD','BNC_CNF','WN'],
                   ['RNR','RNR','RNR','DIS','CBK','CBK','NC','CBK','CBK','PTP','CBK','CBK','CBK','NC','RNR','NC',
                    'RNR','CBK','CBK','CBK','RTP','CBK','CBK','PTP','CBK','CBK','CBK','NC'],inplace=True)

D.replace('PAID', 10, inplace=True)
D.replace('ICBL', 9, inplace=True)
D.replace('CPU', 8, inplace=True)
D.replace('PTP', 7, inplace=True)
D.replace('FPTP', 6, inplace=True)
D.replace('RTP', 5, inplace=True)
D.replace('DIS', 4, inplace=True)
D.replace('CBK', 3, inplace=True)
D.replace('RNR', 2, inplace=True)
D.replace('NC', 1, inplace=True)

def s(x):
    d=''
    for i in str(x):
        if i==' ':
            break
        else:
            d=d+i
    return(d)

D=D.reset_index(drop=True)

D['Call Date']=D['Call Date'].apply(s)

DAY_WISE=pd.DataFrame(D.groupby(['LOAN NO.','Call Date'])['Status'].max()).reset_index()

DAY_WISE.to_excel(r'/Users/mohaksehgal/Documents/Work/Best Codes/Day_Wise_Best_Code.xlsx',index=False)

DAY_WISE.replace(10,'PAID', inplace=True)
DAY_WISE.replace(9,'ICBL', inplace=True)
DAY_WISE.replace(8,'CPU', inplace=True)
DAY_WISE.replace(7,'PTP', inplace=True)
DAY_WISE.replace(6,'FPTP', inplace=True)
DAY_WISE.replace(5,'RTP', inplace=True)
DAY_WISE.replace(4,'DIS', inplace=True)
DAY_WISE.replace(3,'CBK', inplace=True)
DAY_WISE.replace(2,'RNR', inplace=True)
DAY_WISE.replace(1,'NC', inplace=True)

DAY_WISE.to_excel(r'/Users/mohaksehgal/Documents/Work/Best Codes/Master_Day_Wise.xlsx',index=False)