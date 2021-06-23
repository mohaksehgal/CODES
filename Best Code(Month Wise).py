#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 16:15:54 2020

@author: mohaksehgal
"""


import pandas as pd
import numpy as np

A=pd.read_excel(r"/Users/mohaksehgal/Documents/Work/MIS/AB/BL/MARCH 20/ABFL_BL ALLOCATION 12 MARCH 20.xlsx")

A=pd.DataFrame(A['AGREEMENTID'])

A['Process']='ABFL_BL'

A1=pd.read_excel(r"/Users/mohaksehgal/Documents/Work/MIS/IDFC TW/MARCH 20/IDFC_TW ALLOCATION 13 MARCH 20.xlsx")

A1=pd.DataFrame(A1['AGREEMENTID'])

A1['Process']='IDFC TW'

A2=pd.read_excel(r"/Users/mohaksehgal/Documents/Work/MIS/L_T/MARCH 20/L_T Allocation 13 MAR 20.xlsx")

A2=pd.DataFrame(A2['AGREEMENTID'])

A2['Process']='L&T'

A3=pd.read_excel(r"/Users/mohaksehgal/Documents/Work/MIS/AB/90+/MARCH 20/ABFL_90+ Allocation 11 MARCH 20.xlsx")

A3=pd.DataFrame(A3['AGREEMENTID'])

A3['Process']='AB 90+'

M=pd.concat([A,A1])
M=pd.concat([M,A2])
M=pd.concat([M,A3])

S=pd.read_excel(r'/Users/mohaksehgal/Documents/Work/Best Codes/Day_Wise_Best_Code.xlsx')

M=M.reset_index(drop=True)

for i in range(0,len(M['AGREEMENTID'])):
    M.loc[i,'AGREEMENTID']=str(M.loc[i,'AGREEMENTID'])

for i in range(0,len(S['LOAN NO.'])):
    S.loc[i,'LOAN NO.']=str(S.loc[i,'LOAN NO.'])
    
S=S.reset_index(drop=True)

l1=list(S['Call Date'].unique())

for i in range(0,len(l1)):
    M[l1[i]]=np.nan
    
Q=pd.DataFrame(S['LOAN NO.'].unique())

S1=M.merge(Q,left_on='AGREEMENTID',right_on=0, how='inner')

l1=list(M['AGREEMENTID'])

S1.drop(0,axis=1,inplace=True)

Col=S1.columns[2:]

LO=list(S1['AGREEMENTID'])

k=[]
for i in range(0,len(LO)):
    k.append(S[S['LOAN NO.']==LO[i]].index)
    
for i in range(0,len(k)):
    for j in range(0,len(k[i])):
        for d in range(0,len(Col)):
            if S.loc[k[i][j],'Call Date']==Col[d]:
                S1.loc[i,Col[d]]=S.loc[k[i][j],'Status']
                
S1.fillna(0,inplace=True)

for i in range(0,len(Col)):
    S1[Col[i]]=S1[Col[i]].astype(int)
    
e=S1[Col]

BC=[]
for i in range(0,len(e)):
    BC.append(e.iloc[i].max())

S1['Best Codes']=BC

S1.replace(10,'PAID', inplace=True)
S1.replace(9,'ICBL', inplace=True)
S1.replace(8,'CPU', inplace=True)
S1.replace(7,'PTP', inplace=True)
S1.replace(6,'FPTP', inplace=True)
S1.replace(5,'RTP', inplace=True)
S1.replace(4,'DIS', inplace=True)
S1.replace(3,'CBK', inplace=True)
S1.replace(2,'RNR', inplace=True)
S1.replace(1,'NC',inplace=True)

S1.replace(0,np.nan,inplace=True)

S1.to_excel(r'/Users/mohaksehgal/Documents/Work/Best Codes/Month_Wise_Best_Code.xlsx',index=False)