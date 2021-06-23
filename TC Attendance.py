#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 14:24:33 2020

@author: mohaksehgal
"""


import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

AP=pd.read_csv(r'/Users/mohaksehgal/Documents/Work/TC Daily Tracking/MARCH 20/Performance Report.csv')

AL=pd.read_csv(r'/Users/mohaksehgal/Documents/Work/TC Daily Tracking/MARCH 20/Login Report.csv')

for i in range(0,len(AP['DATE DAY'])):
    AP.loc[i,'DATE DAY']=pd.to_datetime(AP.loc[i,'DATE DAY']).date()

for i in range(0,len(AL['Date & Day'])):
    AL.loc[i,'Date & Day']=pd.to_datetime(AL.loc[i,'Date & Day']).date()

A=AP.merge(AL,left_on=['FULL NAME','AGENT ID','PROCESS','DATE DAY'],right_on=['Full Name','Agent ID','Process','Date & Day'],how='inner')

M=A[['FULL NAME','AGENT ID','DATE DAY','CONNECTED']]

M.rename({'CONNECTED':'TOTAL_CALLS'},axis=1,inplace=True)

for i in range(0,len(A['First Login Time'])):
    if len(A.loc[i,'First Login Time'])==3:
        M.loc[i,'LOGIN']=pd.to_datetime('00:00:00').time()
    elif len(A.loc[i,'First Login Time'])!=3:
        M.loc[i,'LOGIN']=pd.to_datetime(A.loc[i,'First Login Time']).time()
        
for i in range(0,len(A['Last Logout Time'])):
    if len(A.loc[i,'Last Logout Time'])==3:
        M.loc[i,'LOGOUT']=pd.to_datetime('00:00:00').time()
    elif len(A.loc[i,'Last Logout Time'])!=3:
        M.loc[i,'LOGOUT']=pd.to_datetime(A.loc[i,'Last Logout Time']).time()
        
for i in range(0,len(A['Login Duration'])):
    if len(A.loc[i,'Login Duration'])==3:
        M.loc[i,'Working Duration']=pd.to_datetime('00:00:00').time()
    elif len(A.loc[i,'Login Duration'])!=3:
        M.loc[i,'Working Duration']=pd.to_datetime(A.loc[i,'Login Duration']).time()
        
for i in  range(0,len(A['IDLE TIME'])):
    if len(A.loc[i,'TALK TIME'])==3:
        M.loc[i,'TALK TIME']=pd.to_datetime('00:00:00').time()
    elif len(A.loc[i,'TALK TIME'])!=3:
        M.loc[i,'TALK TIME']=pd.to_datetime(A.loc[i,'TALK TIME']).time()
        
for i in range(0,len(A['HOLD TIME'])):
    if len(A.loc[i,'HOLD TIME'])==3:
        M.loc[i,'HOLD TIME']=pd.to_datetime('00:00:00').time()
    else:
        M.loc[i,'HOLD TIME']=pd.to_datetime(A.loc[i,'HOLD TIME']).time()
        
for i in range(0,len(A['HOLD TIME'])):
    if len(A.loc[i,'WRAP UP'])==3:
        M.loc[i,'WRAP UP']=pd.to_datetime('00:00:00').time()
    else:
        M.loc[i,'WRAP UP']=pd.to_datetime(A.loc[i,'WRAP UP']).time()

for i in range(0,len(A['HOLD TIME'])):
    if len(A.loc[i,'IDLE TIME'])==3:
        M.loc[i,'IDLE TIME']=pd.to_datetime('00:00:00').time()
    else:
        M.loc[i,'IDLE TIME']=pd.to_datetime(A.loc[i,'IDLE TIME']).time()
        
for i in range(0,len(A['HOLD TIME.1'])):
    if A.loc[i,'BREAKCOUNT']==0:
        M.loc[i,'BREAKCOUNT']=0
    else:
        M.loc[i,'BREAKCOUNT']=A.loc[i,'BREAKCOUNT']
        
M['BREAKCOUNT']=M['BREAKCOUNT'].astype(int)

for i in range(0,len(A['HOLD TIME'])):
    if len(A.loc[i,'OUTBOUND'])==3:
        M.loc[i,'OUTBOUND']=pd.to_datetime('00:00:00').time()
    else:
        M.loc[i,'OUTBOUND']=pd.to_datetime(A.loc[i,'OUTBOUND']).time()
        
for i in range(0,len(A['HOLD TIME'])):
    if len(A.loc[i,'LUNCH'])==3:
        M.loc[i,'LUNCH']=pd.to_datetime('00:00:00').time()
    else:
        M.loc[i,'LUNCH']=pd.to_datetime(A.loc[i,'LUNCH']).time()
        
for i in range(0,len(A['HOLD TIME'])):
    if len(A.loc[i,'TEA'])==3:
        M.loc[i,'TEA']=pd.to_datetime('00:00:00').time()
    else:
        M.loc[i,'TEA']=pd.to_datetime(A.loc[i,'TEA']).time()
        
for i in range(0,len(A['HOLD TIME'])):
    if len(A.loc[i,'Others'])==3:
        M.loc[i,'Others']=pd.to_datetime('00:00:00').time()
    else:
        M.loc[i,'Others']=pd.to_datetime(A.loc[i,'Others']).time()
        
for i in range(0,len(A['HOLD TIME'])):
    if len(A.loc[i,'Diksha'])==3:
        M.loc[i,'Diksha']=pd.to_datetime('00:00:00').time()
    else:
        M.loc[i,'Diksha']=pd.to_datetime(A.loc[i,'Diksha']).time()
        
for i in range(0,len(A['HOLD TIME'])):
    if len(A.loc[i,'MALA'])==3:
        M.loc[i,'MALA']=pd.to_datetime('00:00:00').time()
    else:
        M.loc[i,'MALA']=pd.to_datetime(A.loc[i,'MALA']).time()
        
for i in  range(0,len(A['IDLE TIME'])):
    if len(A.loc[i,'TALK TIME.1'])==3:
        M.loc[i,'AVG. TALK TIME']=pd.to_datetime('00:00:00').time()
    else:
        M.loc[i,'AVG. TALK TIME']=pd.to_datetime(A.loc[i,'TALK TIME.1']).time()
        
for i in range(0,len(A['HOLD TIME'])):
    if len(A.loc[i,'HOLD TIME.1'])==3:
        M.loc[i,'AVG. HOLD TIME']=pd.to_datetime('00:00:00').time()
    else:
        M.loc[i,'AVG. HOLD TIME']=pd.to_datetime(A.loc[i,'HOLD TIME.1']).time()
        
for i in range(0,len(A['HOLD TIME'])):
    if len(A.loc[i,'WRAP UP.1'])==3:
        M.loc[i,'AVG. WRAP UP']=pd.to_datetime('00:00:00').time()
    else:
        M.loc[i,'AVG. WRAP UP']=pd.to_datetime(A.loc[i,'WRAP UP.1']).time()

for i in range(0,len(A['HOLD TIME'])):
    if len(A.loc[i,'IDLE TIME.1'])==3:
        M.loc[i,'AVG. IDLE TIME']=pd.to_datetime('00:00:00').time()
    else:
        M.loc[i,'AVG. IDLE TIME']=pd.to_datetime(A.loc[i,'IDLE TIME.1']).time()
        
def LOGIN (Date):
    criteria=Date<=pd.to_datetime('10:00:00').time()
    return['background-color:green' if i else '' for i in criteria]

def LOGIN1 (Date):
    criteria=Date>pd.to_datetime('10:00:00').time()
    return['background-color:yellow' if i else '' for i in criteria]

def LOGIN2 (Date):
    criteria=Date>pd.to_datetime('10:10:00').time()
    return['background-color:red' if i else '' for i in criteria]

def LOGIN3 (Date):
    criteria=Date==pd.to_datetime('00:00:00').time()
    return['background-color:red' if i else '' for i in criteria]

def LOGOUT (Date):
    criteria=Date>pd.to_datetime('17:00:00').time()
    return['background-color:green' if i else '' for i in criteria]

def LOGOUT1 (Date):
    criteria=Date<=pd.to_datetime('17:00:00').time()
    return['background-color:Yellow' if i else '' for i in criteria]

def LOGOUT2 (Date):
    criteria=Date<=pd.to_datetime('14:00:00').time()
    return['background-color:red' if i else '' for i in criteria]

def LOGOUT3 (Date):
    criteria=Date==pd.to_datetime('00:00:00').time()
    return['background-color:red' if i else '' for i in criteria]

def WD (Date):
    criteria=Date>pd.to_datetime('7:00:00').time()
    return['background-color:green' if i else '' for i in criteria]

def WD1 (Date):
    criteria=Date<=pd.to_datetime('7:00:00').time()
    return['background-color:Yellow' if i else '' for i in criteria]

def WD2 (Date):
    criteria=Date<pd.to_datetime('4:00:00').time()
    return['background-color:red' if i else '' for i in criteria]

def WD3 (Date):
    criteria=Date==pd.to_datetime('00:00:00').time()
    return['background-color:red' if i else '' for i in criteria]

def TT (Date):
    criteria=Date>=pd.to_datetime('01:00:00').time()
    return['background-color:green' if i else '' for i in criteria]

def TT1 (Date):
    criteria=Date<pd.to_datetime('01:00:00').time()
    return['background-color:yellow' if i else '' for i in criteria]

def TT2 (Date):
    criteria=Date<pd.to_datetime('00:45:00').time()
    return['background-color:red' if i else '' for i in criteria]

def TT3 (Date):
    criteria=Date==pd.to_datetime('00:00:00').time()
    return['background-color:red' if i else '' for i in criteria]

def WU (Date):
    criteria=Date>pd.to_datetime('01:15:00').time()
    return['background-color:red' if i else '' for i in criteria]

def WU1 (Date):
    criteria=Date<=pd.to_datetime('01:15:00').time()
    return['background-color:yellow' if i else '' for i in criteria]

def WU2 (Date):
    criteria=Date<=pd.to_datetime('01:00:00').time()
    return['background-color:green' if i else '' for i in criteria]

def WU3 (Date):
    criteria=Date==pd.to_datetime('00:00:00').time()
    return['background-color:red' if i else '' for i in criteria]

def IT (Date):
    criteria=Date<=pd.to_datetime('00:05:00').time()
    return['background-color:green' if i else '' for i in criteria]

def IT1 (Date):
    criteria=Date>pd.to_datetime('00:05:00').time()
    return['background-color:yellow' if i else '' for i in criteria]

def IT2 (Date):
    criteria=Date>pd.to_datetime('00:15:00').time()
    return['background-color:red' if i else '' for i in criteria]

def BC (Date):
    criteria=Date>70
    return['background-color:red' if i else '' for i in criteria]

def BC1 (Date):
    criteria=Date<=70
    return['background-color:green' if i else '' for i in criteria]

def BC2 (Date):
    criteria=Date==0
    return['background-color:red' if i else '' for i in criteria]

def O (Date):
    criteria=Date<=pd.to_datetime('00:10:00').time()
    return['background-color:green' if i else '' for i in criteria]

def O1 (Date):
    criteria=Date>pd.to_datetime('00:10:00').time()
    return['background-color:red' if i else '' for i in criteria]

def LUNCH (Date):
    criteria=Date<=pd.to_datetime('00:30:00').time()
    return['background-color:green' if i else '' for i in criteria]

def LUNCH1 (Date):
    criteria=Date>pd.to_datetime('00:30:00').time()
    return['background-color:yellow' if i else '' for i in criteria]

def LUNCH2 (Date):
    criteria=Date>pd.to_datetime('00:35:00').time()
    return['background-color:red' if i else '' for i in criteria]

def LUNCH3 (Date):
    criteria=Date==pd.to_datetime('00:00:00').time()
    return['background-color:red' if i else '' for i in criteria]

def TEA (Date):
    criteria=Date<=pd.to_datetime('00:30:00').time()
    return['background-color:green' if i else '' for i in criteria]

def TEA1 (Date):
    criteria=Date>pd.to_datetime('00:30:00').time()
    return['background-color:yellow' if i else '' for i in criteria]

def TEA2 (Date):
    criteria=Date>pd.to_datetime('00:35:00').time()
    return['background-color:red' if i else '' for i in criteria]

def TEA3 (Date):
    criteria=Date==pd.to_datetime('00:00:00').time()
    return['background-color:red' if i else '' for i in criteria]

def Others (Date):
    criteria=Date<=pd.to_datetime('00:30:00').time()
    return['background-color:green' if i else '' for i in criteria]

def Others1 (Date):
    criteria=Date>pd.to_datetime('00:30:00').time()
    return['background-color:yellow' if i else '' for i in criteria]

def Others2 (Date):
    criteria=Date>pd.to_datetime('00:45:00').time()
    return['background-color:red' if i else '' for i in criteria]

def Others3 (Date):
    criteria=Date==pd.to_datetime('00:00:00').time()
    return['background-color:red' if i else '' for i in criteria]

def Diksha (Date):
    criteria=Date<pd.to_datetime('02:00:00').time()
    return['background-color:green' if i else '' for i in criteria]

def Diksha1 (Date):
    criteria=Date>pd.to_datetime('02:00:00').time()
    return['background-color:yellow' if i else '' for i in criteria]

def Diksha2 (Date):
    criteria=Date>pd.to_datetime('02:30:00').time()
    return['background-color:red' if i else '' for i in criteria]

def Diksha3 (Date):
    criteria=Date==pd.to_datetime('00:00:00').time()
    return['background-color:red' if i else '' for i in criteria]

def MALA (Date):
    criteria=Date<pd.to_datetime('02:00:00').time()
    return['background-color:green' if i else '' for i in criteria]

def MALA1 (Date):
    criteria=Date>pd.to_datetime('02:00:00').time()
    return['background-color:yellow' if i else '' for i in criteria]

def MALA2 (Date):
    criteria=Date>pd.to_datetime('02:30:00').time()
    return['background-color:red' if i else '' for i in criteria]

def MALA3 (Date):
    criteria=Date==pd.to_datetime('00:00:00').time()
    return['background-color:red' if i else '' for i in criteria]

def ATT (Date):
    criteria=Date>=pd.to_datetime('00:01:15').time()
    return['background-color:green' if i else '' for i in criteria]

def ATT1 (Date):
    criteria=Date<pd.to_datetime('00:01:15').time()
    return['background-color:yellow' if i else '' for i in criteria]

def ATT2 (Date):
    criteria=Date<pd.to_datetime('00:00:45').time()
    return['background-color:red' if i else '' for i in criteria]

def ATT3 (Date):
    criteria=Date==pd.to_datetime('00:00:00').time()
    return['background-color:red' if i else '' for i in criteria]

def AWU (Date):
    criteria=Date<pd.to_datetime('00:01:00').time()
    return['background-color:green' if i else '' for i in criteria]

def AWU1 (Date):
    criteria=Date>pd.to_datetime('00:01:00').time()
    return['background-color:yellow' if i else '' for i in criteria]

def AWU2 (Date):
    criteria=Date>pd.to_datetime('00:01:30').time()
    return['background-color:red' if i else '' for i in criteria]

def AWU3 (Date):
    criteria=Date==pd.to_datetime('00:00:00').time()
    return['background-color:red' if i else '' for i in criteria]

def AIT (Date):
    criteria=Date<=pd.to_datetime('00:00:10').time()
    return['background-color:green' if i else '' for i in criteria]

def AIT1 (Date):
    criteria=Date>pd.to_datetime('00:00:10').time()
    return['background-color:yellow' if i else '' for i in criteria]

def AIT2 (Date):
    criteria=Date>pd.to_datetime('00:00:30').time()
    return['background-color:red' if i else '' for i in criteria]

def AIT3 (Date):
    criteria=Date==pd.to_datetime('00:00:00').time()
    return['background-color:green' if i else '' for i in criteria]

M=M.style.apply(LOGIN,subset=['LOGIN']).apply(LOGIN1, subset=['LOGIN']).apply(LOGIN2, subset=['LOGIN']).apply\
(LOGIN3, subset=['LOGIN']).apply(LOGOUT, subset=['LOGOUT']).apply(LOGOUT1, subset=['LOGOUT']).apply\
(LOGOUT2, subset=['LOGOUT']).apply(LOGOUT3,subset=['LOGOUT']).apply(WD, subset=['Working Duration']).apply\
(WD1,subset=['Working Duration']).apply(WD2,subset=['Working Duration']).apply(WD3,subset=['Working Duration']).apply\
(TT, subset=['TALK TIME']).apply(TT1,subset=['TALK TIME']).apply(TT2,subset=['TALK TIME']).apply\
(TT3,subset=['TALK TIME']).apply(WU, subset=['WRAP UP']).apply(WU1,subset=['WRAP UP']).apply\
(WU2, subset=['WRAP UP']).apply(WU3, subset=['WRAP UP']).apply(IT, subset=['IDLE TIME']).apply\
(IT1,subset=['IDLE TIME']).apply(IT2,subset=['IDLE TIME']).apply(BC, subset=['BREAKCOUNT']).apply\
(BC1, subset=['BREAKCOUNT']).apply(BC2, subset=['BREAKCOUNT']).apply(O, subset=['OUTBOUND']).apply\
(O1, subset=['OUTBOUND']).apply(LUNCH, subset=['LUNCH']).apply(LUNCH1, subset=['LUNCH']).apply\
(LUNCH2, subset=['LUNCH']).apply(LUNCH3, subset=['LUNCH']).apply(TEA, subset=['TEA']).apply\
(TEA1, subset=['TEA']).apply(TEA2, subset=['TEA']).apply(TEA3, subset=['TEA']).apply(Others, subset=['Others']).apply\
(Others1, subset=['Others']).apply(Others2, subset=['Others']).apply(Others3, subset=['Others']).apply\
(Diksha, subset=['Diksha']).apply(Diksha1, subset=['Diksha']).apply(Diksha2, subset=['Diksha']).apply\
(Diksha3, subset=['Diksha']).apply(MALA, subset=['MALA']).apply(MALA1, subset=['MALA']).apply\
(MALA2, subset=['MALA']).apply(MALA3, subset=['MALA']).apply(ATT, subset=['AVG. TALK TIME']).apply\
(ATT1, subset=['AVG. TALK TIME']).apply(ATT2, subset=['AVG. TALK TIME']).apply(ATT3, subset=['AVG. TALK TIME']).apply\
(AWU, subset=['AVG. WRAP UP']).apply(AWU1, subset=['AVG. WRAP UP']).apply(AWU2, subset=['AVG. WRAP UP']).apply\
(AWU3, subset=['AVG. WRAP UP']).apply(AIT, subset=['AVG. IDLE TIME']).apply(AIT1, subset=['AVG. IDLE TIME']).apply\
(AIT2, subset=['AVG. IDLE TIME']).apply(AIT3, subset=['AVG. IDLE TIME'])

M.to_excel(r'/Users/mohaksehgal/Documents/Work/TC Daily Tracking/MARCH 20/Performance.xlsx',index=False)