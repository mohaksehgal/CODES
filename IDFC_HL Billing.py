#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 15:18:48 2020

@author: mohaksehgal
"""


import pandas as pd
import numpy as np

A=pd.read_excel(r"/Users/mohaksehgal/Documents/Work/Billing/IDFC/IDFC Jun 21/MASTER FILE IDFC.xlsx")
P=pd.read_excel(r'/Users/mohaksehgal/Documents/Work/Billing/IDFC/IDFC Jun 21/Performance IDFC.xlsx')

P0=pd.read_excel(r'/Users/mohaksehgal/Documents/Work/Billing/IDFC/PAYOUT/BKT 0 Res.xlsx')
P1=pd.read_excel(r'/Users/mohaksehgal/Documents/Work/Billing/IDFC/PAYOUT/BKT 1 Res.xlsx')
R1=pd.read_excel(r'/Users/mohaksehgal/Documents/Work/Billing/IDFC/PAYOUT/BKT 1 Rollback.xlsx')
P2=pd.read_excel(r'/Users/mohaksehgal/Documents/Work/Billing/IDFC/PAYOUT/BKT 2 Res.xlsx')
R2=pd.read_excel(r'/Users/mohaksehgal/Documents/Work/Billing/IDFC/PAYOUT/BKT 2 Rollback.xlsx')
P3=pd.read_excel(r'/Users/mohaksehgal/Documents/Work/Billing/IDFC/PAYOUT/BKT 3 Res.xlsx')
R3=pd.read_excel(r'/Users/mohaksehgal/Documents/Work/Billing/IDFC/PAYOUT/BKT 3 Rollback.xlsx')
P4=pd.read_excel(r'/Users/mohaksehgal/Documents/Work/Billing/IDFC/PAYOUT/BKT 4 Res.xlsx')
R4=pd.read_excel(r'/Users/mohaksehgal/Documents/Work/Billing/IDFC/PAYOUT/BKT 4 Rollback.xlsx')
P5=pd.read_excel(r'/Users/mohaksehgal/Documents/Work/Billing/IDFC/PAYOUT/BKT 5 Res.xlsx')
R5=pd.read_excel(r'/Users/mohaksehgal/Documents/Work/Billing/IDFC/PAYOUT/BKT 5 Rollback.xlsx')
P6=pd.read_excel(r'/Users/mohaksehgal/Documents/Work/Billing/IDFC/PAYOUT/BKT 6 Res.xlsx')
R6=pd.read_excel(r'/Users/mohaksehgal/Documents/Work/Billing/IDFC/PAYOUT/BKT 6 Rollback.xlsx')
P7=pd.read_excel(r'/Users/mohaksehgal/Documents/Work/Billing/IDFC/PAYOUT/BKT 7 Res.xlsx')
R7=pd.read_excel(r'/Users/mohaksehgal/Documents/Work/Billing/IDFC/PAYOUT/BKT 7 Rollback.xlsx')
P8=pd.read_excel(r'/Users/mohaksehgal/Documents/Work/Billing/IDFC/PAYOUT/BKT 8 Res.xlsx')
R8=pd.read_excel(r'/Users/mohaksehgal/Documents/Work/Billing/IDFC/PAYOUT/BKT 8 Rollback.xlsx')
P9=pd.read_excel(r'/Users/mohaksehgal/Documents/Work/Billing/IDFC/PAYOUT/BKT 9 Res.xlsx')
R9=pd.read_excel(r'/Users/mohaksehgal/Documents/Work/Billing/IDFC/PAYOUT/BKT 9 Rollback.xlsx')
P10=pd.read_excel(r'/Users/mohaksehgal/Documents/Work/Billing/IDFC/PAYOUT/BKT 10 Res.xlsx')
R10=pd.read_excel(r'/Users/mohaksehgal/Documents/Work/Billing/IDFC/PAYOUT/BKT 10 Rollback.xlsx')
P11=pd.read_excel(r'/Users/mohaksehgal/Documents/Work/Billing/IDFC/PAYOUT/BKT 11 Res.xlsx')
R11=pd.read_excel(r'/Users/mohaksehgal/Documents/Work/Billing/IDFC/PAYOUT/BKT 11 Rollback.xlsx')
P12=pd.read_excel(r'/Users/mohaksehgal/Documents/Work/Billing/IDFC/PAYOUT/BKT 12 Res.xlsx')
R12=pd.read_excel(r'/Users/mohaksehgal/Documents/Work/Billing/IDFC/PAYOUT/BKT 12 Rollback.xlsx')
P13=pd.read_excel(r'/Users/mohaksehgal/Documents/Work/Billing/IDFC/PAYOUT/BKT 1 Res.xlsx')
R13=pd.read_excel(r'/Users/mohaksehgal/Documents/Work/Billing/IDFC/PAYOUT/BKT 1 Rollback.xlsx')

CAP=pd.DataFrame({'BKT0':5500,'BKT1':5500,'BKT2':5500,'BKT3':5500,'BKT4':5500,'BKT5':5500,'BKT6':5500,'BKT7':5500,'BKT8':5500,'BKT9':5500,'BKT10':5500,'BKT11':5500,'BKT12':5500,'BKT13':5500},index=[0])

l0=list(P0.columns)
l1=list(P1.columns)
l2=list(P2.columns)
l3=list(P3.columns)
l4=list(P4.columns)
l5=list(P5.columns)
l6=list(P6.columns)
l7=list(P7.columns)
l8=list(P8.columns)
l9=list(P9.columns)
l10=list(P10.columns)
l11=list(P11.columns)
l12=list(P12.columns)
l13=list(P13.columns)

#BKT0

for j in range(0,len(P['BKT'])):
    if P.loc[j,'BKT']=='BKT0':
        for i in range(0,len(A['BKT'])):
            if A.loc[i,'BKT']=='BKT0':
                if (P.loc[j,['BKT','STATE']]==A.loc[i,['BKT','STATE']]).all():
                    for k in range(0,len(l0)):
                        if k==0:
                            if P.loc[j,'POS_RES%']<=l0[k]:
                                if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                    a=A.loc[i,'Billing PAID AMT.']*P0.loc[0,l0[k]]/100
                                    if a>CAP.loc[0,'BKT0']:
                                        A.loc[i,'PERCENTAGE']=str(P0.loc[0,l0[k]])+'%'
                                        A.loc[i,'MOHAK']=CAP.loc[0,'BKT0']
                                        print(A.loc[i,'AGREEMENTID'],P0.loc[0,l0[k]],A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(P0.loc[0,l0[k]])+'%'
                                        A.loc[i,'MOHAK']=a
                                        print(A.loc[i,'AGREEMENTID'],P0.loc[0,l0[k]],A.loc[i,'MOHAK'])
                                elif (A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT'):
                                    b=A.loc[i,'Billing PAID AMT.']*4/100
                                    if b>25000:
                                        A.loc[i,'PERCENTAGE']=str(4)+'%'
                                        A.loc[i,'MOHAK']=25000
                                        print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(4)+'%'
                                        A.loc[i,'MOHAK']=b
                                        print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                else:
                                    A.loc[i,'PERCENTAGE']=str(0)+'%'
                                    A.loc[i,'MOHAK']=0
                                    print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                        elif k==5:
                            if (P.loc[j,'POS_RES%']>=l0[k]):
                                if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                    c=A.loc[i,'Billing PAID AMT.']*P0.loc[0,l0[k]]/100
                                    if c>CAP.loc[0,'BKT0']:
                                        A.loc[i,'PERCENTAGE']=str(P0.loc[0,l0[k]])+'%'
                                        A.loc[i,'MOHAK']=CAP.loc[0,'BKT0']
                                        print(A.loc[i,'AGREEMENTID'],P0.loc[0,l0[k]],A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(P0.loc[0,l0[k]])+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],P0.loc[0,l0[k]],A.loc[i,'MOHAK'])
                                elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                    d=A.loc[i,'Billing PAID AMT.']*4/100
                                    if d>25000:
                                        A.loc[i,'PERCENTAGE']=str(4)+'%'
                                        A.loc[i,'MOHAK']=25000
                                        print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(4)+'%'
                                        A.loc[i,'MOHAK']=d
                                        print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                else:
                                    A.loc[i,'PERCENTAGE']=str(0)+'%'
                                    A.loc[i,'MOHAK']=0
                                    print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                            elif (P.loc[j,'POS_RES%']>=l0[k]):
                                if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                    c=A.loc[i,'Billing PAID AMT.']*P0.loc[0,l0[k]]/100
                                    if c>CAP.loc[0,'BKT0']:
                                        A.loc[i,'PERCENTAGE']=str(P0.loc[0,l0[k]])+'%'
                                        A.loc[i,'MOHAK']=CAP.loc[0,'BKT0']
                                        print(A.loc[i,'AGREEMENTID'],P0.loc[0,l0[k]],A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(P0.loc[0,l0[k]])+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],P0.loc[0,l0[k]],A.loc[i,'MOHAK'])
                                elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                    d=A.loc[i,'Billing PAID AMT.']*4/100
                                    if d>25000:
                                        A.loc[i,'PERCENTAGE']=str(4)+'%'
                                        A.loc[i,'MOHAK']=25000
                                        print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(4)+'%'
                                        A.loc[i,'MOHAK']=d
                                        print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                else:
                                    A.loc[i,'PERCENTAGE']=str(0)+'%'
                                    A.loc[i,'MOHAK']=0
                                    print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                        elif k>0:
                            if (P.loc[j,'POS_RES%']>=l0[k-1]) and (P.loc[j,'POS_RES%']<l0[k]):
                                if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                    c=A.loc[i,'Billing PAID AMT.']*P0.loc[0,l0[k-1]]/100
                                    if c>CAP.loc[0,'BKT0']:
                                        A.loc[i,'PERCENTAGE']=str(P0.loc[0,l0[k-1]])+'%'
                                        A.loc[i,'MOHAK']=CAP.loc[0,'BKT0']
                                        print(A.loc[i,'AGREEMENTID'],P0.loc[0,l0[k-1]],A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(P0.loc[0,l0[k-1]])+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],P0.loc[0,l0[k-1]],A.loc[i,'MOHAK'])
                                elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                    d=A.loc[i,'Billing PAID AMT.']*4/100
                                    if d>25000:
                                        A.loc[i,'PERCENTAGE']=str(4)+'%'
                                        A.loc[i,'MOHAK']=25000
                                        print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(4)+'%'
                                        A.loc[i,'MOHAK']=d
                                        print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                else:
                                    A.loc[i,'PERCENTAGE']=str(0)+'%'
                                    A.loc[i,'MOHAK']=0
                                    print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])

#BKT1
                                    
for j in range(0,len(P['BKT'])):
    if P.loc[j,'BKT']=='BKT1':
        for i in range(0,len(A['BKT'])):
            if A.loc[i,'BKT']=='BKT1':
                if (P.loc[j,['BKT','STATE']]==A.loc[i,['BKT','STATE']]).all():
                    for k in range(0,len(l1)):
                        for l in range(0,len(R1['Target'])):
                            if k==0 and l==0:
                                if P.loc[j,'POS_RES%']<=l1[k] and P.loc[j,'Additional_Performance']<=R1.loc[l,'Target']:
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        a=A.loc[i,'Billing PAID AMT.']*P1.loc[l,l1[k]]/100
                                        if a>CAP.loc[0,'BKT1']:
                                            A.loc[i,'PERCENTAGE']=str(P1.loc[l,l1[k]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT1']
                                            print(A.loc[i,'AGREEMENTID'],P1.loc[l,l1[k]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P1.loc[l,l1[k]])+'%'
                                            A.loc[i,'MOHAK']=a
                                            print(A.loc[i,'AGREEMENTID'],P1.loc[l,l1[k]],A.loc[i,'MOHAK'])
                                    elif (A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT'):
                                        b=A.loc[i,'Billing PAID AMT.']*4/100
                                        if b>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=b
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                            elif k==6 and l==0:
                                if ((P.loc[j,'POS_RES%']>=l1[k-1]) and (P.loc[j,'POS_RES%']<l1[k])) and P.loc[j,'Additional_Performance']<=R1.loc[l,'Target']:
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P1.loc[l,l1[k-1]]/100
                                        if c>CAP.loc[0,'BKT1']:
                                            A.loc[i,'PERCENTAGE']=str(P1.loc[l,l1[k-1]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT1']
                                            print(A.loc[i,'AGREEMENTID'],P1.loc[l,l1[k-1]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P1.loc[l,l1[k-1]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P1.loc[l,l1[k-1]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                                elif (P.loc[j,'POS_RES%']>=l1[k]) and (P.loc[j,'Additional_Performance']<=R1.loc[l,'Target']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P1.loc[l,l1[k]]/100
                                        if c>CAP.loc[0,'BKT1']:
                                            A.loc[i,'PERCENTAGE']=str(P1.loc[l,l1[k]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT1']
                                            print(A.loc[i,'AGREEMENTID'],P1.loc[l,l1[k]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P1.loc[l,l1[k]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P1.loc[l,l1[k]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                            elif k>0 and l==4:
                                if (P.loc[j,'POS_RES%']>=l1[k-1] and P.loc[j,'POS_RES%']<l1[k]) and (P.loc[j,'Additional_Performance']>=R1.loc[l,'Target']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P1.loc[l,l1[k-1]]/100
                                        if c>CAP.loc[0,'BKT1']:
                                            A.loc[i,'PERCENTAGE']=str(P1.loc[l,l1[k-1]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT1']
                                            print(A.loc[i,'AGREEMENTID'],P1.loc[l,l1[k-1]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P1.loc[l,l1[k-1]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P1.loc[l,l1[k-1]],A.loc[i,'MOHAK'])
                                    elif (A.loc[i,'STATUS']=='FORECLOSE') or (A.loc[i,'STATUS']=='SETTLEMENT'):
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                            elif k==6 and l>0:
                                if ((P.loc[j,'POS_RES%']>=l1[k-1]) and (P.loc[j,'POS_RES%']<l1[k])) and ((P.loc[j,'Additional_Performance']>=R1.loc[l-1,'Target']) and (P.loc[j,'Additional_Performance']<R1.loc[l,'Target'])):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P1.loc[l-1,l1[k-1]]/100
                                        if c>CAP.loc[0,'BKT1']:
                                            A.loc[i,'PERCENTAGE']=str(P1.loc[l-1,l1[k-1]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT1']
                                            print(A.loc[i,'AGREEMENTID'],P1.loc[l-1,l1[k-1]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P1.loc[l-1,l1[k-1]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P1.loc[l-1,l1[k-1]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                                elif (P.loc[j,'POS_RES%']>=l1[k]) and ((P.loc[j,'Additional_Performance']>=R1.loc[l-1,'Target']) and (P.loc[j,'Additional_Performance']<R1.loc[l,'Target'])):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P1.loc[l-1,l1[k]]/100
                                        if c>CAP.loc[0,'BKT1']:
                                            A.loc[i,'PERCENTAGE']=str(P1.loc[l-1,l1[k]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT1']
                                            print(A.loc[i,'AGREEMENTID'],P1.loc[l-1,l1[k]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P1.loc[l-1,l1[k]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P1.loc[l-1,l1[k]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                            elif k==0 and l>0:
                                if (P.loc[j,'POS_RES%']<=l1[k]) and ((P.loc[j,'Additional_Performance']>=R1.loc[l-1,'Target']) and (P.loc[j,'Additional_Performance']<R1.loc[l,'Target'])):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P1.loc[l-1,l1[k]]/100
                                        if c>CAP.loc[0,'BKT1']:
                                            A.loc[i,'PERCENTAGE']=str(P1.loc[l-1,l1[k]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT1']
                                            print(A.loc[i,'AGREEMENTID'],P1.loc[l-1,l1[k]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P1.loc[l-1,l1[k]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P1.loc[l-1,l1[k]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                            elif k==6 and l==4:
                                if (P.loc[j,'POS_RES%']>=l1[k]) and (P.loc[j,'Additional_Performance']>=R1.loc[l,'Target']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P1.loc[l,l1[k]]/100
                                        if c>CAP.loc[0,'BKT1']:
                                            A.loc[i,'PERCENTAGE']=str(P1.loc[l,l1[k]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT1']
                                            print(A.loc[i,'AGREEMENTID'],P1.loc[l,l1[k]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P1.loc[l,l1[k]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P1.loc[l,l1[k]],A.loc[i,'MOHAK'])
                                    elif (A.loc[i,'STATUS']=='FORECLOSE') or (A.loc[i,'STATUS']=='SETTLEMENT'):
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                            elif k>0 and l==0:
                                if (P.loc[j,'POS_RES%']>=l1[k-1] and P.loc[j,'POS_RES%']<l1[k]) and (P.loc[j,'Additional_Performance']<=R1.loc[l,'Target']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P1.loc[l,l1[k-1]]/100
                                        if c>CAP.loc[0,'BKT1']:
                                            A.loc[i,'PERCENTAGE']=str(P1.loc[l,l1[k-1]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT1']
                                            print(A.loc[i,'AGREEMENTID'],P1.loc[l,l1[k-1]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P1.loc[l,l1[k-1]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P1.loc[l,l1[k-1]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                            elif k>0 and l>0:
                                if (P.loc[j,'POS_RES%']>=l1[k-1] and P.loc[j,'POS_RES%']<l1[k]) and (P.loc[j,'Additional_Performance']>=R1.loc[l-1,'Target'] and P.loc[j,'Additional_Performance']<R1.loc[l,'Traget']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P1.loc[l-1,l1[k-1]]/100
                                        if c>CAP.loc[0,'BKT1']:
                                            A.loc[i,'PERCENTAGE']=str(P1.loc[l-1,l1[k-1]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT1']
                                            print(A.loc[i,'AGREEMENTID'],P1.loc[l-1,l1[k-1]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P1.loc[l-1,l1[k-1]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P1.loc[l-1,l1[k-1]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])

#BKT2

for j in range(0,len(P['BKT'])):
    if P.loc[j,'BKT']=='BKT2':
        for i in range(0,len(A['BKT'])):
            if A.loc[i,'BKT']=='BKT2':
                if (P.loc[j,['BKT','STATE']]==A.loc[i,['BKT','STATE']]).all():
                    for k in range(0,len(l2)):
                        for l in range(0,len(R2['Target'])):
                            if k==0 and l==0:
                                if P.loc[j,'POS_RES%']<=l2[k] and P.loc[j,'Additional_Performance']<=R2.loc[l,'Target']:
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        a=A.loc[i,'Billing PAID AMT.']*P2.loc[l,l2[k]]/100
                                        if a>CAP.loc[0,'BKT2']:
                                            A.loc[i,'PERCENTAGE']=str(P2.loc[l,l2[k]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT2']
                                            print(A.loc[i,'AGREEMENTID'],P2.loc[l,l2[k]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P2.loc[l,l2[k]])+'%'
                                            A.loc[i,'MOHAK']=a
                                            print(A.loc[i,'AGREEMENTID'],P2.loc[l,l2[k]],A.loc[i,'MOHAK'])
                                    elif (A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT'):
                                        b=A.loc[i,'Billing PAID AMT.']*4/100
                                        if b>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=b
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                            elif k==4 and l==0:
                                if ((P.loc[j,'POS_RES%']>=l2[k-1]) and (P.loc[j,'POS_RES%']<l2[k])) and P.loc[j,'Additional_Performance']<=R2.loc[l,'Target']:
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P2.loc[l,l2[k-1]]/100
                                        if c>CAP.loc[0,'BKT2']:
                                            A.loc[i,'PERCENTAGE']=str(P2.loc[l,l2[k-1]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT2']
                                            print(A.loc[i,'AGREEMENTID'],P2.loc[l,l2[k-1]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P2.loc[l,l2[k-1]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P2.loc[l,l2[k-1]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                                elif (P.loc[j,'POS_RES%']>=l2[k]) and (P.loc[j,'Additional_Performance']<=R2.loc[l,'Target']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P2.loc[l,l2[k]]/100
                                        if c>CAP.loc[0,'BKT2']:
                                            A.loc[i,'PERCENTAGE']=str(P2.loc[l,l2[k]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT2']
                                            print(A.loc[i,'AGREEMENTID'],P2.loc[l,l2[k]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P2.loc[l,l2[k]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P2.loc[l,l2[k]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                            elif k==4 and l>0:
                                if ((P.loc[j,'POS_RES%']>=l2[k-1]) and (P.loc[j,'POS_RES%']<l2[k])) and ((P.loc[j,'Additional_Performance']>=R2.loc[l-1,'Target']) and (P.loc[j,'Additional_Performance']<R2.loc[l,'Target'])):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P2.loc[l-1,l2[k-1]]/100
                                        if c>CAP.loc[0,'BKT2']:
                                            A.loc[i,'PERCENTAGE']=str(P2.loc[l-1,l2[k-1]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT2']
                                            print(A.loc[i,'AGREEMENTID'],P2.loc[l-1,l2[k-1]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P2.loc[l-1,l2[k-1]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P2.loc[l-1,l2[k-1]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                                elif (P.loc[j,'POS_RES%']>=l2[k]) and ((P.loc[j,'Additional_Performance']>=R2.loc[l-1,'Target']) and (P.loc[j,'Additional_Performance']<R2.loc[l,'Target'])):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P2.loc[l-1,l2[k]]/100
                                        if c>CAP.loc[0,'BKT2']:
                                            A.loc[i,'PERCENTAGE']=str(P2.loc[l-1,l2[k]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT2']
                                            print(A.loc[i,'AGREEMENTID'],P2.loc[l-1,l2[k]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P2.loc[l-1,l2[k]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P2.loc[l-1,l2[k]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(2)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                                elif k==4 and l==4:
                                    if (P.loc[j,'POS_RES%']>=l2[k]) and (P.loc[j,'Additional_Performance']>=R2.loc[l,'Target']):
                                        if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                            c=A.loc[i,'Billing PAID AMT.']*P2.loc[l,l2[k]]/100
                                            if c>CAP.loc[0,'BKT2']:
                                                A.loc[i,'PERCENTAGE']=str(P2.loc[l,l2[k]])+'%'
                                                A.loc[i,'MOHAK']=CAP.loc[0,'BKT2']
                                                print(A.loc[i,'AGREEMENTID'],P2.loc[l,l2[k]],A.loc[i,'MOHAK'])
                                            else:
                                                A.loc[i,'PERCENTAGE']=str(P2.loc[l,l2[k]])+'%'
                                                A.loc[i,'MOHAK']=c
                                                print(A.loc[i,'AGREEMENTID'],P2.loc[l,l2[k]],A.loc[i,'MOHAK'])
                                        elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                            d=A.loc[i,'Billing PAID AMT.']*4/100
                                            if d>25000:
                                                A.loc[i,'PERCENTAGE']=str(4)+'%'
                                                A.loc[i,'MOHAK']=25000
                                                print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                            else:
                                                A.loc[i,'PERCENTAGE']=str(4)+'%'
                                                A.loc[i,'MOHAK']=d
                                                print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(0)+'%'
                                            A.loc[i,'MOHAK']=0
                                            print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                            elif k>0 and l==0:
                                if (P.loc[j,'POS_RES%']>=l2[k-1] and P.loc[j,'POS_RES%']<l2[k]) and (P.loc[j,'Additional_Performance']<=R2.loc[l,'Target']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P2.loc[l,l2[k-1]]/100
                                        if c>CAP.loc[0,'BKT2']:
                                            A.loc[i,'PERCENTAGE']=str(P2.loc[l,l2[k-1]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT2']
                                            print(A.loc[i,'AGREEMENTID'],P2.loc[l,l2[k-1]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P2.loc[l,l2[k-1]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P2.loc[l,l2[k-1]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                            elif k>0 and l>0:
                                if (P.loc[j,'POS_RES%']>=l2[k-1] and P.loc[j,'POS_RES%']<l2[k]) and (P.loc[j,'Additional_Performance']>=R2.loc[l-1,'Target'] and P.loc[j,'Additional_Performance']<R2.loc[l,'Traget']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P2.loc[l-1,l2[k-1]]/100
                                        if c>CAP.loc[0,'BKT2']:
                                            A.loc[i,'PERCENTAGE']=str(P2.loc[l-1,l2[k-1]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT2']
                                            print(A.loc[i,'AGREEMENTID'],P2.loc[l-1,l2[k-1]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P2.loc[l-1,l2[k-1]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P2.loc[l-1,l2[k-1]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
#BKT3

for j in range(0,len(P['BKT'])):
    if P.loc[j,'BKT']=='BKT3':
        for i in range(0,len(A['BKT'])):
            if A.loc[i,'BKT']=='BKT3':
                if (P.loc[j,['BKT','STATE']]==A.loc[i,['BKT','STATE']]).all():
                    for k in range(0,len(l3)):
                        for l in range(0,len(R3['Target'])):
                            if k==0 and l==0:
                                if P.loc[j,'POS_RES%']<=l3[k] and P.loc[j,'Additional_Performance']<=R3.loc[l,'Target']:
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        a=A.loc[i,'Billing PAID AMT.']*P3.loc[l,l3[k]]/100
                                        if a>CAP.loc[0,'BKT3']:
                                            A.loc[i,'PERCENTAGE']=str(P3.loc[l,l3[k]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT3']
                                            print(A.loc[i,'AGREEMENTID'],P3.loc[l,l3[k]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P3.loc[l,l3[k]])+'%'
                                            A.loc[i,'MOHAK']=a
                                            print(A.loc[i,'AGREEMENTID'],P3.loc[l,l3[k]],A.loc[i,'MOHAK'])
                                    elif (A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT'):
                                        b=A.loc[i,'Billing PAID AMT.']*4/100
                                        if b>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=b
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                            elif k==4 and l==0:
                                if ((P.loc[j,'POS_RES%']>=l3[k-1]) and (P.loc[j,'POS_RES%']<=l3[k])) and P.loc[j,'Additional_Performance']<=R3.loc[l,'Target']:
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P3.loc[l,l3[k-1]]/100
                                        if c>CAP.loc[0,'BKT3']:
                                            A.loc[i,'PERCENTAGE']=str(P3.loc[l,l3[k-1]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT3']
                                            print(A.loc[i,'AGREEMENTID'],P3.loc[l,l3[k-1]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P3.loc[l,l3[k-1]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P3.loc[l,l3[k-1]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                                elif (P.loc[j,'POS_RES%']>=l3[k]) and (P.loc[j,'Additional_Performance']<=R3.loc[l,'Target']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P3.loc[l,l3[k]]/100
                                        if c>CAP.loc[0,'BKT3']:
                                            A.loc[i,'PERCENTAGE']=str(P3.loc[l,l3[k]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT3']
                                            print(A.loc[i,'AGREEMENTID'],P3.loc[l,l3[k]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P3.loc[l,l3[k]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P3.loc[l,l3[k]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                            elif k==4 and l>0:
                                if ((P.loc[j,'POS_RES%']>=l3[k-1]) and (P.loc[j,'POS_RES%']<l3[k])) and ((P.loc[j,'Additional_Performance']>=R3.loc[l-1,'Target']) and (P.loc[j,'Additional_Performance']<R3.loc[l,'Target'])):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                            c=A.loc[i,'Billing PAID AMT.']*P3.loc[l-1,l3[k-1]]/100
                                            if c>CAP.loc[0,'BKT3']:
                                                A.loc[i,'PERCENTAGE']=str(P3.loc[l-1,l3[k-1]])+'%'
                                                A.loc[i,'MOHAK']=CAP.loc[0,'BKT3']
                                                print(A.loc[i,'AGREEMENTID'],P3.loc[l-1,l3[k-1]],A.loc[i,'MOHAK'])
                                            else:
                                                A.loc[i,'PERCENTAGE']=str(P3.loc[l-1,l3[k-1]])+'%'
                                                A.loc[i,'MOHAK']=c
                                                print(A.loc[i,'AGREEMENTID'],P3.loc[l-1,l3[k-1]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                                elif (P.loc[j,'POS_RES%']>=l3[k]) and ((P.loc[j,'Additional_Performance']>=R3.loc[l-1,'Target']) and (P.loc[j,'Additional_Performance']<R3.loc[l,'Target'])):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                            c=A.loc[i,'Billing PAID AMT.']*P3.loc[l-1,l3[k]]/100
                                            if c>CAP.loc[0,'BKT3']:
                                                A.loc[i,'PERCENTAGE']=str(P3.loc[l-1,l3[k]])+'%'
                                                A.loc[i,'MOHAK']=CAP.loc[0,'BKT3']
                                                print(A.loc[i,'AGREEMENTID'],P3.loc[l-1,l3[k]],A.loc[i,'MOHAK'])
                                            else:
                                                A.loc[i,'PERCENTAGE']=str(P3.loc[l-1,l3[k]])+'%'
                                                A.loc[i,'MOHAK']=c
                                                print(A.loc[i,'AGREEMENTID'],P3.loc[l-1,l3[k]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                                elif k==4 and l==4:
                                    if (P.loc[j,'POS_RES%']>=l3[k]) and P.loc[j,'Additional_Performance']>=R3.loc[l,'Target']:
                                        if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                            c=A.loc[i,'Billing PAID AMT.']*P3.loc[l,l3[k]]/100
                                            if c>CAP.loc[0,'BKT3']:
                                                A.loc[i,'PERCENTAGE']=str(P3.loc[l,l3[k]])+'%'
                                                A.loc[i,'MOHAK']=CAP.loc[0,'BKT3']
                                                print(A.loc[i,'AGREEMENTID'],P3.loc[l,l3[k]],A.loc[i,'MOHAK'])
                                            else:
                                                A.loc[i,'PERCENTAGE']=str(P3.loc[l,l3[k]])+'%'
                                                A.loc[i,'MOHAK']=c
                                                print(A.loc[i,'AGREEMENTID'],P3.loc[l,l3[k]],A.loc[i,'MOHAK'])
                                        elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                            d=A.loc[i,'Billing PAID AMT.']*4/100
                                            if d>25000:
                                                A.loc[i,'PERCENTAGE']=str(4)+'%'
                                                A.loc[i,'MOHAK']=25000
                                                print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                            else:
                                                A.loc[i,'PERCENTAGE']=str(4)+'%'
                                                A.loc[i,'MOHAK']=d
                                                print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(0)+'%'
                                            A.loc[i,'MOHAK']=0
                                            print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                            elif k>0 and l==0:
                                if (P.loc[j,'POS_RES%']>=l3[k-1] and P.loc[j,'POS_RES%']<l3[k]) and (P.loc[j,'Additional_Performance']<=R3.loc[l,'Target']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P3.loc[l,l3[k-1]]/100
                                        if c>CAP.loc[0,'BKT3']:
                                            A.loc[i,'PERCENTAGE']=str(P3.loc[l,l3[k-1]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT3']
                                            print(A.loc[i,'AGREEMENTID'],P3.loc[l,l3[k-1]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P3.loc[l,l3[k-1]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P3.loc[l,l3[k-1]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                            elif k>0 and l>0:
                                if (P.loc[j,'POS_RES%']>=l3[k-1] and P.loc[j,'POS_RES%']<l3[k]) and (P.loc[j,'Additional_Performance']>=R3.loc[l-1,'Target'] and P.loc[j,'Additional_Performance']<R3.loc[l,'Traget']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P3.loc[l-1,l3[k-1]]/100
                                        if c>CAP.loc[0,'BKT3']:
                                            A.loc[i,'PERCENTAGE']=str(P3.loc[l-1,l3[k-1]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT3']
                                            print(A.loc[i,'AGREEMENTID'],P3.loc[l-1,l3[k-1]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P3.loc[l-1,l3[k-1]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P3.loc[l-1,l3[k-1]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
#BKT4
                                        
for j in range(0,len(P['BKT'])):
    if P.loc[j,'BKT']=='BKT4':
        for i in range(0,len(A['BKT'])):
            if A.loc[i,'BKT']=='BKT4':
                if (P.loc[j,['BKT','STATE']]==A.loc[i,['BKT','STATE']]).all():
                    for k in range(0,len(l4)):
                        for l in range(0,len(R4['Target'])):
                            if k==0 and l==0:
                                if P.loc[j,'POS_RES%']<=l4[k] and P.loc[j,'Additional_Performance']<=R4.loc[l,'Target']:
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        a=A.loc[i,'Billing PAID AMT.']*P4.loc[l,l4[k]]/100
                                        if a>CAP.loc[0,'BKT4']:
                                            A.loc[i,'PERCENTAGE']=str(P4.loc[l,l4[k]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT4']
                                            print(A.loc[i,'AGREEMENTID'],P4.loc[l,l4[k]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P4.loc[l,l4[k]])+'%'
                                            A.loc[i,'MOHAK']=a
                                            print(A.loc[i,'AGREEMENTID'],P4.loc[l,l4[k]],A.loc[i,'MOHAK'])
                                    elif (A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT'):
                                        b=A.loc[i,'Billing PAID AMT.']*4/100
                                        if b>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=b
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                            elif k==4 and l==0:
                                if ((P.loc[j,'POS_RES%']>=l4[k-1]) and (P.loc[j,'POS_RES%']<l4[k])) and (P.loc[j,'Additional_Performance']<=R4.loc[l,'Target']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P4.loc[l,l4[k-1]]/100
                                        if c>CAP.loc[0,'BKT4']:
                                            A.loc[i,'PERCENTAGE']=str(P4.loc[l,l4[k-1]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT4']
                                            print(A.loc[i,'AGREEMENTID'],P4.loc[l,l4[k-1]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P4.loc[l,l4[k-1]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P4.loc[l,l4[k-1]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                                elif (P.loc[j,'POS_RES%']>=l4[k]) and (P.loc[j,'Additional_Performance']<=R4.loc[l,'Target']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P4.loc[l,l4[k]]/100
                                        if c>CAP.loc[0,'BKT4']:
                                            A.loc[i,'PERCENTAGE']=str(P4.loc[l,l4[k]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT4']
                                            print(A.loc[i,'AGREEMENTID'],P4.loc[l,l4[k]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P4.loc[l,l4[k]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P4.loc[l,l4[k]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                            elif k==4 and l>0:
                                if ((P.loc[j,'POS_RES%']>=l4[k-1]) and (P.loc[j,'POS_RES%']<l4[k])) and ((P.loc[j,'Additional_Performance']>=R4.loc[l-1,'Target']) and (P.loc[j,'Additional_Performance']<R4.loc[l,'Target'])):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P4.loc[l-1,l4[k-1]]/100
                                        if c>CAP.loc[0,'BKT4']:
                                            A.loc[i,'PERCENTAGE']=str(P4.loc[l-1,l4[k-1]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT4']
                                            print(A.loc[i,'AGREEMENTID'],P4.loc[l-1,l4[k-1]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P4.loc[l-1,l4[k-1]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P4.loc[l-1,l4[k-1]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                                elif (P.loc[j,'POS_RES%']>=l4[k]) and ((P.loc[j,'Additional_Performance']>=R4.loc[l-1,'Target']) and (P.loc[j,'Additional_Performance']<R4.loc[l,'Target'])):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P4.loc[l-1,l4[k]]/100
                                        if c>CAP.loc[0,'BKT4']:
                                            A.loc[i,'PERCENTAGE']=str(P4.loc[l-1,l4[k]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT4']
                                            print(A.loc[i,'AGREEMENTID'],P4.loc[l-1,l4[k]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P4.loc[l-1,l4[k]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P4.loc[l-1,l4[k]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                                elif k==4 and l==4:
                                    if (P.loc[j,'POS_RES%']>=l4[k]) and P.loc[j,'Additional_Performance']>=R4.loc[l,'Target']:
                                        if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                            c=A.loc[i,'Billing PAID AMT.']*P4.loc[l,l4[k]]/100
                                            if c>CAP.loc[0,'BKT4']:
                                                A.loc[i,'PERCENTAGE']=str(P4.loc[l,l4[k]])+'%'
                                                A.loc[i,'MOHAK']=CAP.loc[0,'BKT4']
                                                print(A.loc[i,'AGREEMENTID'],P4.loc[l,l4[k]],A.loc[i,'MOHAK'])
                                            else:
                                                A.loc[i,'PERCENTAGE']=str(P4.loc[l,l4[k]])+'%'
                                                A.loc[i,'MOHAK']=c
                                                print(A.loc[i,'AGREEMENTID'],P4.loc[l,l4[k]],A.loc[i,'MOHAK'])
                                        elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                            d=A.loc[i,'Billing PAID AMT.']*4/100
                                            if d>25000:
                                                A.loc[i,'PERCENTAGE']=str(4)+'%'
                                                A.loc[i,'MOHAK']=25000
                                                print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                            else:
                                                A.loc[i,'PERCENTAGE']=str(4)+'%'
                                                A.loc[i,'MOHAK']=d
                                                print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(0)+'%'
                                            A.loc[i,'MOHAK']=0
                                            print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                            elif k>0 and l==0:
                                if (P.loc[j,'POS_RES%']>=l4[k-1] and P.loc[j,'POS_RES%']<l4[k]) and (P.loc[j,'Additional_Performance']<=R4.loc[l,'Target']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P4.loc[l,l4[k-1]]/100
                                        if c>CAP.loc[0,'BKT4']:
                                            A.loc[i,'PERCENTAGE']=str(P4.loc[l,l4[k-1]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT4']
                                            print(A.loc[i,'AGREEMENTID'],P4.loc[l,l4[k-1]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P4.loc[l,l4[k-1]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P4.loc[l,l4[k-1]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                            elif k>0 and l>0:
                                if (P.loc[j,'POS_RES%']>=l4[k-1] and P.loc[j,'POS_RES%']<l4[k]) and (P.loc[j,'Additional_Performance']>=R4.loc[l-1,'Target'] and P.loc[j,'Additional_Performance']<R4.loc[l,'Traget']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P4.loc[l-1,l4[k-1]]/100
                                        if c>CAP.loc[0,'BKT4']:
                                            A.loc[i,'PERCENTAGE']=str(P4.loc[l-1,l4[k-1]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT4']
                                            print(A.loc[i,'AGREEMENTID'],P4.loc[l-1,l4[k-1]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P4.loc[l-1,l4[k-1]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P4.loc[l-1,l4[k-1]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
#BKT5
                                        
for j in range(0,len(P['BKT'])):
    if P.loc[j,'BKT']=='BKT5':
        for i in range(0,len(A['BKT'])):
            if A.loc[i,'BKT']=='BKT5':
                if (P.loc[j,['BKT','STATE']]==A.loc[i,['BKT','STATE']]).all():
                    for k in range(0,len(l5)):
                        for l in range(0,len(R5['Target'])):
                            if k==0 and l==0:
                                if P.loc[j,'POS_RES%']<=l5[k] and P.loc[j,'Additional_Performance']<=R5.loc[l,'Target']:
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        a=A.loc[i,'Billing PAID AMT.']*P5.loc[l,l5[k]]/100
                                        if a>CAP.loc[0,'BKT5']:
                                            A.loc[i,'PERCENTAGE']=str(P5.loc[l,l5[k]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT5']
                                            print(A.loc[i,'AGREEMENTID'],P5.loc[l,l5[k]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P5.loc[l,l5[k]])+'%'
                                            A.loc[i,'MOHAK']=a
                                            print(A.loc[i,'AGREEMENTID'],P5.loc[l,l5[k]],A.loc[i,'MOHAK'])
                                    elif (A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT'):
                                        b=A.loc[i,'Billing PAID AMT.']*4/100
                                        if b>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=b
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                            elif k==4 and l==0:
                                if ((P.loc[j,'POS_RES%']>=l5[k-1]) and (P.loc[i,'POS_RES%']<l5[k])) and P.loc[j,'Additional_Performance']<=R5.loc[l,'Target']:
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P5.loc[l,l5[k-1]]/100
                                        if c>CAP.loc[0,'BKT5']:
                                            A.loc[i,'PERCENTAGE']=str(P5.loc[l,l5[k-1]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT5']
                                            print(A.loc[i,'AGREEMENTID'],P5.loc[l,l5[k-1]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P5.loc[l,l5[k-1]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P5.loc[l,l5[k-1]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                                elif (P.loc[j,'POS_RES%']>=l5[k]) and (P.loc[j,'Additional_Performance']<=R5.loc[l,'Target']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P5.loc[l,l5[k]]/100
                                        if c>CAP.loc[0,'BKT5']:
                                            A.loc[i,'PERCENTAGE']=str(P5.loc[l,l5[k]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT5']
                                            print(A.loc[i,'AGREEMENTID'],P5.loc[l,l5[k]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P5.loc[l,l5[k]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P5.loc[l,l5[k]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                            elif k==4 and l>0:
                                if ((P.loc[j,'POS_RES%']>=l5[k-1]) and (P.loc[j,'POS_RES%']<l5[k])) and ((P.loc[j,'Additional_Performance']>=R5.loc[l-1,'Target']) and (P.loc[j,'Additional_Performance']<R5.loc[l,'Target'])):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P5.loc[l-1,l5[k-1]]/100
                                        if c>CAP.loc[0,'BKT5']:
                                            A.loc[i,'PERCENTAGE']=str(P5.loc[l-1,l5[k-1]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT5']
                                            print(A.loc[i,'AGREEMENTID'],P5.loc[l-1,l5[k-1]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P5.loc[l-1,l5[k-1]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P5.loc[l-1,l5[k-1]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                                elif (P.loc[j,'POS_RES%']>=l5[k]) and ((P.loc[j,'Additional_Performance']>=R5.loc[l-1,'Target']) and (P.loc[j,'Additional_Performance']<R5.loc[l,'Target'])):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P5.loc[l-1,l5[k]]/100
                                        if c>CAP.loc[0,'BKT5']:
                                            A.loc[i,'PERCENTAGE']=str(P5.loc[l-1,l5[k]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT5']
                                            print(A.loc[i,'AGREEMENTID'],P5.loc[l-1,l5[k]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P5.loc[l-1,l5[k]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P5.loc[l-1,l5[k]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                                elif k==4 and l==4:
                                    if (P.loc[j,'POS_RES%']>=l5[k]) and P.loc[j,'Additional_Performance']>=R5.loc[l,'Target']:
                                        if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                            c=A.loc[i,'Billing PAID AMT.']*P5.loc[l,l5[k]]/100
                                            if c>CAP.loc[0,'BKT5']:
                                                A.loc[i,'PERCENTAGE']=str(P5.loc[l,l5[k]])+'%'
                                                A.loc[i,'MOHAK']=CAP.loc[0,'BKT5']
                                                print(A.loc[i,'AGREEMENTID'],P5.loc[l,l5[k]],A.loc[i,'MOHAK'])
                                            else:
                                                A.loc[i,'PERCENTAGE']=str(P5.loc[l,l5[k]])+'%'
                                                A.loc[i,'MOHAK']=c
                                                print(A.loc[i,'AGREEMENTID'],P5.loc[l,l5[k]],A.loc[i,'MOHAK'])
                                        elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                            d=A.loc[i,'Billing PAID AMT.']*4/100
                                            if d>25000:
                                                A.loc[i,'PERCENTAGE']=str(4)+'%'
                                                A.loc[i,'MOHAK']=25000
                                                print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                            else:
                                                A.loc[i,'PERCENTAGE']=str(4)+'%'
                                                A.loc[i,'MOHAK']=d
                                                print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(0)+'%'
                                            A.loc[i,'MOHAK']=0
                                            print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                            elif k>0 and l==0:
                                if (P.loc[j,'POS_RES%']>=l5[k-1] and P.loc[j,'POS_RES%']<l5[k]) and (P.loc[j,'Additional_Performance']<=R5.loc[l,'Target']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P5.loc[l,l5[k-1]]/100
                                        if c>CAP.loc[0,'BKT5']:
                                            A.loc[i,'PERCENTAGE']=str(P5.loc[l,l5[k-1]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT5']
                                            print(A.loc[i,'AGREEMENTID'],P5.loc[l,l5[k-1]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P5.loc[l,l5[k-1]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P5.loc[l,l5[k-1]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                            elif k>0 and l>0:
                                if (P.loc[j,'POS_RES%']>=l5[k-1] and P.loc[j,'POS_RES%']<l5[k]) and (P.loc[j,'Additional_Performance']>=R5.loc[l-1,'Target'] and P.loc[j,'Additional_Performance']<R5.loc[l,'Traget']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P5.loc[l-1,l5[k-1]]/100
                                        if c>CAP.loc[0,'BKT5']:
                                            A.loc[i,'PERCENTAGE']=str(P5.loc[l-1,l5[k-1]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT5']
                                            print(A.loc[i,'AGREEMENTID'],P5.loc[l-1,l5[k-1]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P5.loc[l-1,l5[k-1]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P5.loc[l-1,l5[k-1]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
#BKT6
                                        
for j in range(0,len(P['BKT'])):
    if P.loc[j,'BKT']=='BKT6':
        for i in range(0,len(A['BKT'])):
            if A.loc[i,'BKT']=='BKT6':
                if (P.loc[j,['BKT','STATE']]==A.loc[i,['BKT','STATE']]).all():
                    for k in range(0,len(l6)):
                        for l in range(0,len(R6['Target'])):
                            if k==0 and l==0:
                                if P.loc[j,'POS_RES%']<=l6[k] and P.loc[j,'Additional_Performance']<=R6.loc[l,'Target']:
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        a=A.loc[i,'Billing PAID AMT.']*P6.loc[l,l6[k]]/100
                                        if a>CAP.loc[0,'BKT6']:
                                            A.loc[i,'PERCENTAGE']=str(P6.loc[l,l6[k]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT6']
                                            print(A.loc[i,'AGREEMENTID'],P6.loc[l,l6[k]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P6.loc[l,l6[k]])+'%'
                                            A.loc[i,'MOHAK']=a
                                            print(A.loc[i,'AGREEMENTID'],P6.loc[l,l6[k]],A.loc[i,'MOHAK'])
                                    elif (A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT'):
                                        b=A.loc[i,'Billing PAID AMT.']*4/100
                                        if b>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=b
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                            elif k==4 and l==0:
                                if ((P.loc[j,'POS_RES%']>=l6[k-1]) and (P.loc[j,'POS_RES%']<l6[k])) and P.loc[j,'Additional_Performance']<=R6.loc[l,'Target']:
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P6.loc[l,l6[k-1]]/100
                                        if c>CAP.loc[0,'BKT6']:
                                            A.loc[i,'PERCENTAGE']=str(P6.loc[l,l6[k-1]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT6']
                                            print(A.loc[i,'AGREEMENTID'],P6.loc[l,l6[k-1]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P6.loc[l,l6[k-1]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P6.loc[l,l6[k-1]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                                elif (P.loc[j,'POS_RES%']>=l6[k]) and (P.loc[j,'Additional_Performance']<=R6.loc[l,'Target']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P6.loc[l,l6[k]]/100
                                        if c>CAP.loc[0,'BKT6']:
                                            A.loc[i,'PERCENTAGE']=str(P6.loc[l,l6[k]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT6']
                                            print(A.loc[i,'AGREEMENTID'],P6.loc[l,l6[k]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P6.loc[l,l6[k]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P6.loc[l,l6[k]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                            elif k==4 and l>0:
                                if ((P.loc[j,'POS_RES%']>=l6[k-1]) and (P.loc[j,'POS_RES%']<l6[k])) and ((P.loc[j,'Additional_Performance']>=R6.loc[l-1,'Target']) and (P.loc[j,'Additional_Performance']<R6.loc[l,'Target'])):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P6.loc[l-1,l6[k-1]]/100
                                        if c>CAP.loc[0,'BKT6']:
                                            A.loc[i,'PERCENTAGE']=str(P6.loc[l-1,l6[k-1]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT6']
                                            print(A.loc[i,'AGREEMENTID'],P6.loc[l-1,l6[k-1]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P6.loc[l-1,l6[k-1]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P6.loc[l-1,l6[k-1]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                                elif (P.loc[j,'POS_RES%']>=l6[k]) and ((P.loc[j,'Additional_Performance']>=R6.loc[l-1,'Target']) and (P.loc[j,'Additional_Performance']<R6.loc[l,'Target'])):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P6.loc[l-1,l6[k]]/100
                                        if c>CAP.loc[0,'BKT6']:
                                            A.loc[i,'PERCENTAGE']=str(P6.loc[l-1,l6[k]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT6']
                                            print(A.loc[i,'AGREEMENTID'],P6.loc[l-1,l6[k]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P6.loc[l-1,l6[k]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P6.loc[l-1,l6[k]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                                elif k==4 or l==4:
                                    if (P.loc[j,'POS_RES%']>=l6[k]) and P.loc[j,'Additional_Performance']>=R6.loc[l,'Target']:
                                        if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                            c=A.loc[i,'Billing PAID AMT.']*P6.loc[l,l6[k]]/100
                                            if c>CAP.loc[0,'BKT6']:
                                                A.loc[i,'PERCENTAGE']=str(P6.loc[l,l6[k]])+'%'
                                                A.loc[i,'MOHAK']=CAP.loc[0,'BKT6']
                                                print(A.loc[i,'AGREEMENTID'],P6.loc[l,l6[k]],A.loc[i,'MOHAK'])
                                            else:
                                                A.loc[i,'PERCENTAGE']=str(P6.loc[l,l6[k]])+'%'
                                                A.loc[i,'MOHAK']=c
                                                print(A.loc[i,'AGREEMENTID'],P6.loc[l,l6[k]],A.loc[i,'MOHAK'])
                                        elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                            d=A.loc[i,'Billing PAID AMT.']*4/100
                                            if d>25000:
                                                A.loc[i,'PERCENTAGE']=str(4)+'%'
                                                A.loc[i,'MOHAK']=25000
                                                print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                            else:
                                                A.loc[i,'PERCENTAGE']=str(4)+'%'
                                                A.loc[i,'MOHAK']=d
                                                print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(0)+'%'
                                            A.loc[i,'MOHAK']=0
                                            print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                            elif k>0 and l==0:
                                if (P.loc[j,'POS_RES%']>=l6[k-1] and P.loc[j,'POS_RES%']<l6[k]) and (P.loc[j,'Additional_Performance']<=R6.loc[l,'Target']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P6.loc[l,l6[k-1]]/100
                                        if c>CAP.loc[0,'BKT6']:
                                            A.loc[i,'PERCENTAGE']=str(P6.loc[l,l6[k-1]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT6']
                                            print(A.loc[i,'AGREEMENTID'],P6.loc[l,l6[k-1]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P6.loc[l,l6[k-1]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P6.loc[l,l6[k-1]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                            elif k>0 and l>0:
                                if (P.loc[j,'POS_RES%']>=l6[k-1] and P.loc[j,'POS_RES%']<l6[k]) and (P.loc[j,'Additional_Performance']>=R6.loc[l-1,'Target'] and P.loc[j,'Additional_Performance']<R6.loc[l,'Traget']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P6.loc[l-1,l6[k-1]]/100
                                        if c>CAP.loc[0,'BKT6']:
                                            A.loc[i,'PERCENTAGE']=str(P6.loc[l-1,l6[k-1]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT6']
                                            print(A.loc[i,'AGREEMENTID'],P6.loc[l-1,l6[k-1]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P6.loc[l-1,l6[k-1]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P6.loc[l-1,l6[k-1]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
#BKT7

for j in range(0,len(P['BKT'])):
    if P.loc[j,'BKT']=='BKT7':
        for i in range(0,len(A['BKT'])):
            if A.loc[i,'BKT']=='BKT7':
                if (P.loc[j,['BKT','STATE']]==A.loc[i,['BKT','STATE']]).all():
                    for k in range(0,len(l7)):
                        for l in range(0,len(R7['Target'])):
                            if k==0 and l==0:
                                if P.loc[j,'POS_RES%']<=l7[k] and P.loc[j,'Additional_Performance']<=R7.loc[l,'Target']:
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        a=A.loc[i,'Billing PAID AMT.']*P7.loc[l,l7[k]]/100
                                        if a>CAP.loc[0,'BKT7']:
                                            A.loc[i,'PERCENTAGE']=str(P7.loc[l,l7[k]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT7']
                                            print(A.loc[i,'AGREEMENTID'],P7.loc[l,l7[k]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P7.loc[l,l7[k]])+'%'
                                            A.loc[i,'MOHAK']=a
                                            print(A.loc[i,'AGREEMENTID'],P7.loc[l,l7[k]],A.loc[i,'MOHAK'])
                                    elif (A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT'):
                                        b=A.loc[i,'Billing PAID AMT.']*4/100
                                        if b>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=b
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                            elif k==4 and l==0:
                                if ((P.loc[j,'POS_RES%']>=l7[k-1]) and (P.loc[j,'POS_RES%']<l7[k])) and (P.loc[j,'Additional_Performance']<=R7.loc[l,'Target']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P7.loc[l,l7[k-1]]/100
                                        if c>CAP.loc[0,'BKT7']:
                                            A.loc[i,'PERCENTAGE']=str(P7.loc[l,l7[k-1]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT7']
                                            print(A.loc[i,'AGREEMENTID'],P7.loc[l,l7[k-1]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P7.loc[l,l7[k-1]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P7.loc[l,l7[k-1]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                                elif (P.loc[j,'POS_RES%']>=l7[k]) and (P.loc[j,'Additional_Performance']<=R7.loc[l,'Target']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P7.loc[l,l7[k]]/100
                                        if c>CAP.loc[0,'BKT7']:
                                            A.loc[i,'PERCENTAGE']=str(P7.loc[l,l7[k]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT7']
                                            print(A.loc[i,'AGREEMENTID'],P7.loc[l,l7[k]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P7.loc[l,l7[k]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P7.loc[l,l7[k]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                            elif k==4 and l>0:
                                if ((P.loc[j,'POS_RES%']>=l7[k-1]) and (P.loc[j,'POS_RES%']<l7[k])) and ((P.loc[j,'Additional_Performance']>=R7.loc[l-1,'Target']) and (P.loc[j,'Additional_Performance']<R7.loc[l,'Target'])):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P7.loc[l-1,l7[k-1]]/100
                                        if c>CAP.loc[0,'BKT7']:
                                            A.loc[i,'PERCENTAGE']=str(P7.loc[l-1,l7[k-1]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT7']
                                            print(A.loc[i,'AGREEMENTID'],P7.loc[l-1,l7[k-1]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P7.loc[l-1,l7[k-1]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P7.loc[l-1,l7[k-1]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                                elif (P.loc[j,'POS_RES%']>=l7[k]) and ((P.loc[j,'Additional_Performance']>=R7.loc[l-1,'Target']) and (P.loc[j,'Additional_Performance']<R7.loc[l,'Target'])):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P7.loc[l-1,l7[k]]/100
                                        if c>CAP.loc[0,'BKT7']:
                                            A.loc[i,'PERCENTAGE']=str(P7.loc[l-1,l7[k]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT7']
                                            print(A.loc[i,'AGREEMENTID'],P7.loc[l-1,l7[k]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P7.loc[l-1,l7[k]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P7.loc[l-1,l7[k]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                                elif k==4 and l==4:
                                    if (P.loc[j,'POS_RES%']>=l7[k]) and P.loc[j,'Additional_Performance']>=R7.loc[l,'Target']:
                                        if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                            c=A.loc[i,'Billing PAID AMT.']*P7.loc[l,l7[k]]/100
                                            if c>CAP.loc[0,'BKT7']:
                                                A.loc[i,'PERCENTAGE']=str(P7.loc[l,l7[k]])+'%'
                                                A.loc[i,'MOHAK']=CAP.loc[0,'BKT7']
                                                print(A.loc[i,'AGREEMENTID'],P7.loc[l,l7[k]],A.loc[i,'MOHAK'])
                                            else:
                                                A.loc[i,'PERCENTAGE']=str(P7.loc[l,l7[k]])+'%'
                                                A.loc[i,'MOHAK']=c
                                                print(A.loc[i,'AGREEMENTID'],P7.loc[l,l7[k]],A.loc[i,'MOHAK'])
                                        elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                            d=A.loc[i,'Billing PAID AMT.']*4/100
                                            if d>25000:
                                                A.loc[i,'PERCENTAGE']=str(4)+'%'
                                                A.loc[i,'MOHAK']=25000
                                                print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                            else:
                                                A.loc[i,'PERCENTAGE']=str(4)+'%'
                                                A.loc[i,'MOHAK']=d
                                                print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(0)+'%'
                                            A.loc[i,'MOHAK']=0
                                            print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                            elif k>0 and l==0:
                                if (P.loc[j,'POS_RES%']>=l7[k-1] and P.loc[j,'POS_RES%']<l7[k]) and (P.loc[j,'Additional_Performance']<=R7.loc[l,'Target']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P7.loc[l,l7[k-1]]/100
                                        if c>CAP.loc[0,'BKT7']:
                                            A.loc[i,'PERCENTAGE']=str(P7.loc[l,l7[k-1]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT7']
                                            print(A.loc[i,'AGREEMENTID'],P7.loc[l,l7[k-1]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P7.loc[l,l7[k-1]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P7.loc[l,l7[k-1]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                            elif k>0 and l>0:
                                if (P.loc[j,'POS_RES%']>=l7[k-1] and P.loc[j,'POS_RES%']<l7[k]) and (P.loc[j,'Additional_Performance']>=R7.loc[l-1,'Target'] and P.loc[j,'Additional_Performance']<R7.loc[l,'Traget']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P7.loc[l-1,l7[k-1]]/100
                                        if c>CAP.loc[0,'BKT7']:
                                            A.loc[i,'PERCENTAGE']=str(P7.loc[l-1,l7[k-1]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT7']
                                            print(A.loc[i,'AGREEMENTID'],P7.loc[l-1,l7[k-1]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P7.loc[l-1,l7[k-1]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P7.loc[l-1,l7[k-1]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
#BKT8

for j in range(0,len(P['BKT'])):
    if P.loc[j,'BKT']=='BKT8':
        for i in range(0,len(A['BKT'])):
            if A.loc[i,'BKT']=='BKT8':
                if (P.loc[j,['BKT','STATE']]==A.loc[i,['BKT','STATE']]).all():
                    for k in range(0,len(l8)):
                        for l in range(0,len(R8['Target'])):
                            if k==0 and l==0:
                                if P.loc[j,'POS_RES%']<=l8[k] and P.loc[j,'Additional_Performance']<=R8.loc[l,'Target']:
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        a=A.loc[i,'Billing PAID AMT.']*P8.loc[l,l8[k]]/100
                                        if a>CAP.loc[0,'BKT8']:
                                            A.loc[i,'PERCENTAGE']=str(P8.loc[l,l8[k]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT8']
                                            print(A.loc[i,'AGREEMENTID'],P8.loc[l,l8[k]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P8.loc[l,l8[k]])+'%'
                                            A.loc[i,'MOHAK']=a
                                            print(A.loc[i,'AGREEMENTID'],P8.loc[l,l8[k]],A.loc[i,'MOHAK'])
                                    elif (A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT'):
                                        b=A.loc[i,'Billing PAID AMT.']*4/100
                                        if b>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=b
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                            elif k==4 and l==0:
                                if ((P.loc[j,'POS_RES%']>=l8[k-1]) and (P.loc[j,'POS_RES%']<l8[k])) and (P.loc[j,'Additional_Performance']<=R8.loc[l,'Target']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P8.loc[l,l8[k-1]]/100
                                        if c>CAP.loc[0,'BKT8']:
                                            A.loc[i,'PERCENTAGE']=str(P8.loc[l,l8[k-1]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT8']
                                            print(A.loc[i,'AGREEMENTID'],P8.loc[l,l8[k-1]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P8.loc[l,l8[k-1]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P8.loc[l,l8[k-1]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                                elif (P.loc[j,'POS_RES%']>=l8[k]) and (P.loc[j,'Additional_Performance']<=R8.loc[l,'Target']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P8.loc[l,l8[k]]/100
                                        if c>CAP.loc[0,'BKT8']:
                                            A.loc[i,'PERCENTAGE']=str(P8.loc[l,l8[k]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT8']
                                            print(A.loc[i,'AGREEMENTID'],P8.loc[l,l8[k]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P8.loc[l,l8[k]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P8.loc[l,l8[k]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                            elif k==4 and l>0:
                                if ((P.loc[j,'POS_RES%']>=l8[k-1]) and (P.loc[j,'POS_RES%']<l8[k])) and ((P.loc[j,'Additional_Performance']>=R8.loc[l-1,'Target']) and (P.loc[j,'Additional_Performance']<R8.loc[l,'Target'])):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P8.loc[l-1,l8[k-1]]/100
                                        if c>CAP.loc[0,'BKT8']:
                                            A.loc[i,'PERCENTAGE']=str(P8.loc[l-1,l8[k-1]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT8']
                                            print(A.loc[i,'AGREEMENTID'],P8.loc[l-1,l8[k-1]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P8.loc[l-1,l8[k-1]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P8.loc[l-1,l8[k-1]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                                elif (P.loc[j,'POS_RES%']>=l8[k]) and ((P.loc[j,'Additional_Performance']>=R8.loc[l-1,'Target']) and (P.loc[j,'Additional_Performance']<R8.loc[l,'Target'])):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P8.loc[l-1,l8[k]]/100
                                        if c>CAP.loc[0,'BKT8']:
                                            A.loc[i,'PERCENTAGE']=str(P8.loc[l-1,l8[k]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT8']
                                            print(A.loc[i,'AGREEMENTID'],P8.loc[l-1,l8[k]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P8.loc[l-1,l8[k]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P8.loc[l-1,l8[k]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                                elif k==4 and l==4:
                                    if (P.loc[j,'POS_RES%']>=l8[k]) and P.loc[j,'Additional_Performance']>=R8.loc[l,'Target']:
                                        if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                            c=A.loc[i,'Billing PAID AMT.']*P8.loc[l,l8[k]]/100
                                            if c>CAP.loc[0,'BKT8']:
                                                A.loc[i,'PERCENTAGE']=str(P8.loc[l,l8[k]])+'%'
                                                A.loc[i,'MOHAK']=CAP.loc[0,'BKT8']
                                                print(A.loc[i,'AGREEMENTID'],P8.loc[l,l8[k]],A.loc[i,'MOHAK'])
                                            else:
                                                A.loc[i,'PERCENTAGE']=str(P8.loc[l,l8[k]])+'%'
                                                A.loc[i,'MOHAK']=c
                                                print(A.loc[i,'AGREEMENTID'],P8.loc[l,l8[k]],A.loc[i,'MOHAK'])
                                        elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                            d=A.loc[i,'Billing PAID AMT.']*4/100
                                            if d>25000:
                                                A.loc[i,'PERCENTAGE']=str(4)+'%'
                                                A.loc[i,'MOHAK']=25000
                                                print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                            else:
                                                A.loc[i,'PERCENTAGE']=str(4)+'%'
                                                A.loc[i,'MOHAK']=d
                                                print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(0)+'%'
                                            A.loc[i,'MOHAK']=0
                                            print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                            elif k>0 and l==0:
                                if (P.loc[j,'POS_RES%']>=l8[k-1] and P.loc[j,'POS_RES%']<l8[k]) and (P.loc[j,'Additional_Performance']<=R8.loc[l,'Target']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P8.loc[l,l8[k-1]]/100
                                        if c>CAP.loc[0,'BKT8']:
                                            A.loc[i,'PERCENTAGE']=str(P8.loc[l,l8[k-1]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT8']
                                            print(A.loc[i,'AGREEMENTID'],P8.loc[l,l8[k-1]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P8.loc[l,l8[k-1]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P8.loc[l,l8[k-1]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                            elif k>0 and l>0:
                                if (P.loc[j,'POS_RES%']>=l8[k-1] and P.loc[j,'POS_RES%']<l8[k]) and (P.loc[j,'Additional_Performance']>=R8.loc[l-1,'Target'] and P.loc[j,'Additional_Performance']<R8.loc[l,'Traget']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P8.loc[l-1,l8[k-1]]/100
                                        if c>CAP.loc[0,'BKT8']:
                                            A.loc[i,'PERCENTAGE']=str(P8.loc[l-1,l8[k-1]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT8']
                                            print(A.loc[i,'AGREEMENTID'],P8.loc[l-1,l8[k-1]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P8.loc[l-1,l8[k-1]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P8.loc[l-1,l8[k-1]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
#BKT9

for j in range(0,len(P['BKT'])):
    if P.loc[j,'BKT']=='BKT9':
        for i in range(0,len(A['BKT'])):
            if A.loc[i,'BKT']=='BKT9':
                if (P.loc[j,['BKT','STATE']]==A.loc[i,['BKT','STATE']]).all():
                    for k in range(0,len(l9)):
                        for l in range(0,len(R9['Target'])):
                            if k==0 and l==0:
                                if P.loc[j,'POS_RES%']<=l9[k] and P.loc[j,'Additional_Performance']<=R9.loc[l,'Target']:
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        a=A.loc[i,'Billing PAID AMT.']*P9.loc[l,l9[k]]/100
                                        if a>CAP.loc[0,'BKT9']:
                                            A.loc[i,'PERCENTAGE']=str(P9.loc[l,l9[k]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT9']
                                            print(A.loc[i,'AGREEMENTID'],P9.loc[l,l9[k]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P9.loc[l,l9[k]])+'%'
                                            A.loc[i,'MOHAK']=a
                                            print(A.loc[i,'AGREEMENTID'],P9.loc[l,l9[k]],A.loc[i,'MOHAK'])
                                    elif (A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT'):
                                        b=A.loc[i,'Billing PAID AMT.']*4/100
                                        if b>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=b
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                            elif k==4 and l==0:
                                if ((P.loc[j,'POS_RES%']>=l9[k-1]) and (P.loc[j,'POS_RES%']<l9[k])) and (P.loc[j,'Additional_Performance']<=R9.loc[l,'Target']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P9.loc[l,l9[k-1]]/100
                                        if c>CAP.loc[0,'BKT9']:
                                            A.loc[i,'PERCENTAGE']=str(P9.loc[l,l9[k-1]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT9']
                                            print(A.loc[i,'AGREEMENTID'],P9.loc[l,l9[k-1]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P9.loc[l,l9[k-1]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P9.loc[l,l9[k-1]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                                elif (P.loc[j,'POS_RES%']>=l9[k]) and (P.loc[j,'Additional_Performance']<=R9.loc[l,'Target']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P9.loc[l,l9[k]]/100
                                        if c>CAP.loc[0,'BKT9']:
                                            A.loc[i,'PERCENTAGE']=str(P9.loc[l,l9[k]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT9']
                                            print(A.loc[i,'AGREEMENTID'],P9.loc[l,l9[k]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P9.loc[l,l9[k]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P9.loc[l,l9[k]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                            elif k==4 and l>0:
                                if ((P.loc[j,'POS_RES%']>=l9[k-1]) and (P.loc[j,'POS_RES%']<l9[k])) and ((P.loc[j,'Additional_Performance']>=R9.loc[l-1,'Target']) and (P.loc[j,'Additional_Performance']<=R9.loc[l,'Target'])):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P9.loc[l-1,l9[k-1]]/100
                                        if c>CAP.loc[0,'BKT9']:
                                            A.loc[i,'PERCENTAGE']=str(P9.loc[l-1,l9[k-1]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT9']
                                            print(A.loc[i,'AGREEMENTID'],P9.loc[l-1,l9[k-1]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P9.loc[l-1,l9[k-1]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P9.loc[l-1,l9[k-1]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])   
                                elif (P.loc[j,'POS_RES%']>=l9[k]) and ((P.loc[j,'Additional_Performance']>=R9.loc[l-1,'Target']) and (P.loc[j,'Additional_Performance']<R9.loc[l,'Target'])):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P9.loc[l-1,l9[k]]/100
                                        if c>CAP.loc[0,'BKT9']:
                                            A.loc[i,'PERCENTAGE']=str(P9.loc[l-1,l9[k]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT9']
                                            print(A.loc[i,'AGREEMENTID'],P9.loc[l-1,l9[k]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P9.loc[l-1,l9[k]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P9.loc[l-1,l9[k]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                                elif k==4 and l==4:
                                    if (P.loc[j,'POS_RES%']>=l9[k]) and P.loc[j,'Additional_Performance']>=R9.loc[l,'Target']:
                                        if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                            c=A.loc[i,'Billing PAID AMT.']*P9.loc[l,l9[k]]/100
                                            if c>CAP.loc[0,'BKT9']:
                                                A.loc[i,'PERCENTAGE']=str(P9.loc[l,l9[k]])+'%'
                                                A.loc[i,'MOHAK']=CAP.loc[0,'BKT9']
                                                print(A.loc[i,'AGREEMENTID'],P9.loc[l,l9[k]],A.loc[i,'MOHAK'])
                                            else:
                                                A.loc[i,'PERCENTAGE']=str(P9.loc[l,l9[k]])+'%'
                                                A.loc[i,'MOHAK']=c
                                                print(A.loc[i,'AGREEMENTID'],P9.loc[l,l9[k]],A.loc[i,'MOHAK'])
                                        elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                            d=A.loc[i,'Billing PAID AMT.']*4/100
                                            if d>25000:
                                                A.loc[i,'PERCENTAGE']=str(4)+'%'
                                                A.loc[i,'MOHAK']=25000
                                                print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                            else:
                                                A.loc[i,'PERCENTAGE']=str(4)+'%'
                                                A.loc[i,'MOHAK']=d
                                                print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(0)+'%'
                                            A.loc[i,'MOHAK']=0
                                            print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                                elif k==4 and l==4:
                                    if (P.loc[j,'POS_RES%']>=l9[k]) and (P.loc[j,'Additional_Performance']>=R9.loc[l,'Target']):
                                        if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                            c=A.loc[i,'Billing PAID AMT.']*P9.loc[l,l9[k]]/100
                                            if c>CAP.loc[0,'BKT9']:
                                                A.loc[i,'PERCENTAGE']=str(P9.loc[l,l9[k]])+'%'
                                                A.loc[i,'MOHAK']=CAP.loc[0,'BKT9']
                                                print(A.loc[i,'AGREEMENTID'],P9.loc[l,l9[k]],A.loc[i,'MOHAK'])
                                            else:
                                                A.loc[i,'PERCENTAGE']=str(P9.loc[l,l9[k]])+'%'
                                                A.loc[i,'MOHAK']=c
                                                print(A.loc[i,'AGREEMENTID'],P9.loc[l,l9[k]],A.loc[i,'MOHAK'])
                                        elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                            d=A.loc[i,'Billing PAID AMT.']*4/100
                                            if d>25000:
                                                A.loc[i,'PERCENTAGE']=str(4)+'%'
                                                A.loc[i,'MOHAK']=25000
                                                print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                            else:
                                                A.loc[i,'PERCENTAGE']=str(4)+'%'
                                                A.loc[i,'MOHAK']=d
                                                print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(0)+'%'
                                            A.loc[i,'MOHAK']=0
                                            print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                            elif k>0 and l==0:
                                if (P.loc[j,'POS_RES%']>=l9[k-1] and P.loc[j,'POS_RES%']<l9[k]) and (P.loc[j,'Additional_Performance']<=R9.loc[l,'Target']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P9.loc[l,l9[k-1]]/100
                                        if c>CAP.loc[0,'BKT9']:
                                            A.loc[i,'PERCENTAGE']=str(P9.loc[l,l9[k-1]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT9']
                                            print(A.loc[i,'AGREEMENTID'],P9.loc[l,l9[k-1]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P9.loc[l,l9[k-1]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P9.loc[l,l9[k-1]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                            elif k>0 and l>0:
                                if (P.loc[j,'POS_RES%']>=l9[k-1] and P.loc[j,'POS_RES%']<l9[k]) and (P.loc[j,'Additional_Performance']>=R9.loc[l-1,'Target'] and P.loc[j,'Additional_Performance']<R9.loc[l,'Traget']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P9.loc[l-1,l9[k-1]]/100
                                        if c>CAP.loc[0,'BKT9']:
                                            A.loc[i,'PERCENTAGE']=str(P9.loc[l-1,l9[k-1]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT9']
                                            print(A.loc[i,'AGREEMENTID'],P9.loc[l-1,l9[k-1]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P9.loc[l-1,l9[k-1]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P9.loc[l-1,l9[k-1]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
#BKT10
                                        
for j in range(0,len(P['BKT'])):
    if P.loc[j,'BKT']=='BKT10':
        for i in range(0,len(A['BKT'])):
            if A.loc[i,'BKT']=='BKT10':
                if (P.loc[j,['BKT','STATE']]==A.loc[i,['BKT','STATE']]).all():
                    for k in range(0,len(l10)):
                        for l in range(0,len(R10['Target'])):
                            if k==0 and l==0:
                                if P.loc[j,'POS_RES%']<=l10[k] and P.loc[j,'Additional_Performance']<=R10.loc[l,'Target']:
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        a=A.loc[i,'Billing PAID AMT.']*P10.loc[l,l10[k]]/100
                                        if a>CAP.loc[0,'BKT10']:
                                            A.loc[i,'PERCENTAGE']=str(P10.loc[l,l10[k]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT10']
                                            print(A.loc[i,'AGREEMENTID'],P10.loc[l,l10[k]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P10.loc[l,l10[k]])+'%'
                                            A.loc[i,'MOHAK']=a
                                            print(A.loc[i,'AGREEMENTID'],P10.loc[l,l10[k]],A.loc[i,'MOHAK'])
                                    elif (A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT'):
                                        b=A.loc[i,'Billing PAID AMT.']*4/100
                                        if b>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=b
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                            elif k==4 and l==0:
                                if ((P.loc[j,'POS_RES%']>=l10[k-1]) and (P.loc[j,'POS_RES%']<l10[k])) and (P.loc[j,'Additional_Performance']<=R10.loc[l,'Target']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P10.loc[l,l10[k-1]]/100
                                        if c>CAP.loc[0,'BKT10']:
                                            A.loc[i,'PERCENTAGE']=str(P10.loc[l,l10[k-1]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT10']
                                            print(A.loc[i,'AGREEMENTID'],P10.loc[l,l10[k-1]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P10.loc[l,l10[k-1]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P10.loc[l,l10[k-1]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                                elif (P.loc[j,'POS_RES%']>=l10[k]) and (P.loc[j,'Additional_Performance']<=R10.loc[l,'Target']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P10.loc[l,l10[k]]/100
                                        if c>CAP.loc[0,'BKT10']:
                                            A.loc[i,'PERCENTAGE']=str(P10.loc[l,l10[k]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT10']
                                            print(A.loc[i,'AGREEMENTID'],P10.loc[l,l10[k]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P10.loc[l,l10[k]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P10.loc[l,l10[k]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                            elif k==4 and l>0:
                                if ((P.loc[j,'POS_RES%']>=l10[k-1]) and (P.loc[j,'POS_RES%']<l10[k])) and ((P.loc[j,'Additional_Performance']>=R10.loc[l-1,'Target']) and (P.loc[j,'Additional_Performance']<R10.loc[l,'Target'])):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P10.loc[l-1,l10[k-1]]/100
                                        if c>CAP.loc[0,'BKT10']:
                                            A.loc[i,'PERCENTAGE']=str(P10.loc[l-1,l10[k-1]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT10']
                                            print(A.loc[i,'AGREEMENTID'],P10.loc[l-1,l10[k-1]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P10.loc[l-1,l10[k-1]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P10.loc[l-1,l10[k-1]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                                elif (P.loc[j,'POS_RES%']>=l10[k]) and ((P.loc[j,'Additional_Performance']>=R10.loc[l-1,'Target']) and (P.loc[j,'Additional_Performance']<R10.loc[l,'Target'])):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P10.loc[l-1,l10[k]]/100
                                        if c>CAP.loc[0,'BKT10']:
                                            A.loc[i,'PERCENTAGE']=str(P10.loc[l-1,l10[k]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT10']
                                            print(A.loc[i,'AGREEMENTID'],P10.loc[l-1,l10[k]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P10.loc[l-1,l10[k]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P10.loc[l-1,l10[k]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                                elif k==4 and l==4:
                                    if (P.loc[j,'POS_RES%']>=l10[k]) and P.loc[j,'Additional_Performance']>=R10.loc[l,'Target']:
                                        if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                            c=A.loc[i,'Billing PAID AMT.']*P10.loc[l,l10[k]]/100
                                            if c>CAP.loc[0,'BKT10']:
                                                A.loc[i,'PERCENTAGE']=str(P10.loc[l,l10[k]])+'%'
                                                A.loc[i,'MOHAK']=CAP.loc[0,'BKT10']
                                                print(A.loc[i,'AGREEMENTID'],P10.loc[l,l10[k]],A.loc[i,'MOHAK'])
                                            else:
                                                A.loc[i,'PERCENTAGE']=str(P10.loc[l,l10[k]])+'%'
                                                A.loc[i,'MOHAK']=c
                                                print(A.loc[i,'AGREEMENTID'],P10.loc[l,l10[k]],A.loc[i,'MOHAK'])
                                        elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                            d=A.loc[i,'Billing PAID AMT.']*4/100
                                            if d>25000:
                                                A.loc[i,'PERCENTAGE']=str(4)+'%'
                                                A.loc[i,'MOHAK']=25000
                                                print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                            else:
                                                A.loc[i,'PERCENTAGE']=str(4)+'%'
                                                A.loc[i,'MOHAK']=d
                                                print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(0)+'%'
                                            A.loc[i,'MOHAK']=0
                                            print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                            elif k>0 and l==0:
                                if (P.loc[j,'POS_RES%']>=l10[k-1] and P.loc[j,'POS_RES%']<l10[k]) and (P.loc[j,'Additional_Performance']<=R10.loc[l,'Target']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P10.loc[l,l10[k-1]]/100
                                        if c>CAP.loc[0,'BKT10']:
                                            A.loc[i,'PERCENTAGE']=str(P10.loc[l,l10[k-1]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT10']
                                            print(A.loc[i,'AGREEMENTID'],P10.loc[l,l10[k-1]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P10.loc[l,l10[k-1]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P10.loc[l,l10[k-1]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                            elif k>0 and l>0:
                                if (P.loc[j,'POS_RES%']>=l10[k-1] and P.loc[j,'POS_RES%']<l10[k]) and (P.loc[j,'Additional_Performance']>=R10.loc[l-1,'Target'] and P.loc[j,'Additional_Performance']<R10.loc[l,'Traget']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P10.loc[l-1,l10[k-1]]/100
                                        if c>CAP.loc[0,'BKT10']:
                                            A.loc[i,'PERCENTAGE']=str(P10.loc[l-1,l10[k-1]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT10']
                                            print(A.loc[i,'AGREEMENTID'],P10.loc[l-1,l10[k-1]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P10.loc[l-1,l10[k-1]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P10.loc[l-1,l10[k-1]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
#BKT11
                                        
for j in range(0,len(P['BKT'])):
    if P.loc[j,'BKT']=='BKT11':
        for i in range(0,len(A['BKT'])):
            if A.loc[i,'BKT']=='BKT11':
                if (P.loc[j,['BKT','STATE']]==A.loc[i,['BKT','STATE']]).all():
                    for k in range(0,len(l11)):
                        for l in range(0,len(R11['Target'])):
                            if k==0 and l==0:
                                if P.loc[j,'POS_RES%']<=l11[k] and P.loc[j,'Additional_Performance']<=R11.loc[l,'Target']:
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        a=A.loc[i,'Billing PAID AMT.']*P11.loc[l,l11[k]]/100
                                        if a>CAP.loc[0,'BKT11']:
                                            A.loc[i,'PERCENTAGE']=str(P11.loc[l,l11[k]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT11']
                                            print(A.loc[i,'AGREEMENTID'],P11.loc[l,l11[k]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P11.loc[l,l11[k]])+'%'
                                            A.loc[i,'MOHAK']=a
                                            print(A.loc[i,'AGREEMENTID'],P11.loc[l,l11[k]],A.loc[i,'MOHAK'])
                                    elif (A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT'):
                                        b=A.loc[i,'Billing PAID AMT.']*4/100
                                        if b>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=b
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                            elif k==4 and l==0:
                                if ((P.loc[j,'POS_RES%']>=l11[k-1]) and (P.loc[j,'POS_RES%']<l11[k])) and (P.loc[j,'Additional_Performance']<=R11.loc[l,'Target']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P11.loc[l,l11[k-1]]/100
                                        if c>CAP.loc[0,'BKT11']:
                                            A.loc[i,'PERCENTAGE']=str(P11.loc[l,l11[k-1]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT11']
                                            print(A.loc[i,'AGREEMENTID'],P11.loc[l,l11[k-1]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P11.loc[l,l11[k-1]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P11.loc[l,l11[k-1]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                                elif (P.loc[j,'POS_RES%']>=l11[k]) and (P.loc[j,'Additional_Performance']<=R11.loc[l,'Target']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P11.loc[l,l11[k]]/100
                                        if c>CAP.loc[0,'BKT11']:
                                            A.loc[i,'PERCENTAGE']=str(P11.loc[l,l11[k]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT11']
                                            print(A.loc[i,'AGREEMENTID'],P11.loc[l,l11[k]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P11.loc[l,l11[k]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P11.loc[l,l11[k]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                            elif k==4 and l>0:
                                if ((P.loc[j,'POS_RES%']>=l11[k-1]) and (P.loc[j,'POS_RES%']<l11[k])) and ((P.loc[j,'Additional_Performance']>=R11.loc[l-1,'Target']) and (P.loc[j,'Additional_Performance']<R11.loc[l,'Target'])):
                                        if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                            c=A.loc[i,'Billing PAID AMT.']*P11.loc[l-1,l11[k-1]]/100
                                            if c>CAP.loc[0,'BKT11']:
                                                A.loc[i,'PERCENTAGE']=str(P11.loc[l-1,l11[k-1]])+'%'
                                                A.loc[i,'MOHAK']=CAP.loc[0,'BKT11']
                                                print(A.loc[i,'AGREEMENTID'],P11.loc[l-1,l11[k-1]],A.loc[i,'MOHAK'])
                                            else:
                                                A.loc[i,'PERCENTAGE']=str(P11.loc[l-1,l11[k-1]])+'%'
                                                A.loc[i,'MOHAK']=c
                                                print(A.loc[i,'AGREEMENTID'],P11.loc[l-1,l11[k-1]],A.loc[i,'MOHAK'])
                                        elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                            d=A.loc[i,'Billing PAID AMT.']*4/100
                                            if d>25000:
                                                A.loc[i,'PERCENTAGE']=str(4)+'%'
                                                A.loc[i,'MOHAK']=25000
                                                print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                            else:
                                                A.loc[i,'PERCENTAGE']=str(4)+'%'
                                                A.loc[i,'MOHAK']=d
                                                print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(0)+'%'
                                            A.loc[i,'MOHAK']=0
                                            print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                                elif (P.loc[j,'POS_RES%']>=l11[k]) and ((P.loc[j,'Additional_Performance']>=R11.loc[l-1,'Target']) and (P.loc[j,'Additional_Performance']<R11.loc[l,'Target'])):
                                        if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                            c=A.loc[i,'Billing PAID AMT.']*P11.loc[l-1,l11[k]]/100
                                            if c>CAP.loc[0,'BKT11']:
                                                A.loc[i,'PERCENTAGE']=str(P11.loc[l-1,l11[k]])+'%'
                                                A.loc[i,'MOHAK']=CAP.loc[0,'BKT11']
                                                print(A.loc[i,'AGREEMENTID'],P11.loc[l-1,l11[k]],A.loc[i,'MOHAK'])
                                            else:
                                                A.loc[i,'PERCENTAGE']=str(P11.loc[l-1,l11[k]])+'%'
                                                A.loc[i,'MOHAK']=c
                                                print(A.loc[i,'AGREEMENTID'],P11.loc[l-1,l11[k]],A.loc[i,'MOHAK'])
                                        elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                            d=A.loc[i,'Billing PAID AMT.']*4/100
                                            if d>25000:
                                                A.loc[i,'PERCENTAGE']=str(4)+'%'
                                                A.loc[i,'MOHAK']=25000
                                                print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                            else:
                                                A.loc[i,'PERCENTAGE']=str(4)+'%'
                                                A.loc[i,'MOHAK']=d
                                                print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(0)+'%'
                                            A.loc[i,'MOHAK']=0
                                            print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                                elif k==4 and l==4:
                                    if (P.loc[j,'POS_RES%']>=l11[k]) and P.loc[j,'Additional_Performance']>=R11.loc[l,'Target']:
                                        if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                            c=A.loc[i,'Billing PAID AMT.']*P11.loc[l,l11[k]]/100
                                            if c>CAP.loc[0,'BKT11']:
                                                A.loc[i,'PERCENTAGE']=str(P11.loc[l,l11[k]])+'%'
                                                A.loc[i,'MOHAK']=CAP.loc[0,'BKT11']
                                                print(A.loc[i,'AGREEMENTID'],P11.loc[l,l11[k]],A.loc[i,'MOHAK'])
                                            else:
                                                A.loc[i,'PERCENTAGE']=str(P11.loc[l,l11[k]])+'%'
                                                A.loc[i,'MOHAK']=c
                                                print(A.loc[i,'AGREEMENTID'],P11.loc[l,l11[k]],A.loc[i,'MOHAK'])
                                        elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                            d=A.loc[i,'Billing PAID AMT.']*4/100
                                            if d>25000:
                                                A.loc[i,'PERCENTAGE']=str(4)+'%'
                                                A.loc[i,'MOHAK']=25000
                                                print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                            else:
                                                A.loc[i,'PERCENTAGE']=str(4)+'%'
                                                A.loc[i,'MOHAK']=d
                                                print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(0)+'%'
                                            A.loc[i,'MOHAK']=0
                                            print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                            elif k>0 and l==0:
                                if (P.loc[j,'POS_RES%']>=l11[k-1] and P.loc[j,'POS_RES%']<l11[k]) and (P.loc[j,'Additional_Performance']<=R11.loc[l,'Target']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P11.loc[l,l11[k-1]]/100
                                        if c>CAP.loc[0,'BKT11']:
                                            A.loc[i,'PERCENTAGE']=str(P11.loc[l,l11[k-1]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT11']
                                            print(A.loc[i,'AGREEMENTID'],P11.loc[l,l11[k-1]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P11.loc[l,l11[k-1]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P11.loc[l,l11[k-1]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                            elif k>0 and l>0:
                                if (P.loc[j,'POS_RES%']>=l11[k-1] and P.loc[j,'POS_RES%']<l11[k]) and (P.loc[j,'Additional_Performance']>=R11.loc[l-1,'Target'] and P.loc[j,'Additional_Performance']<R11.loc[l,'Traget']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P11.loc[l-1,l11[k-1]]/100
                                        if c>CAP.loc[0,'BKT11']:
                                            A.loc[i,'PERCENTAGE']=str(P11.loc[l-1,l11[k-1]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT11']
                                            print(A.loc[i,'AGREEMENTID'],P11.loc[l-1,l11[k-1]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P11.loc[l-1,l11[k-1]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P11.loc[l-1,l11[k-1]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
#BKT12
                                        
for j in range(0,len(P['BKT'])):
    if P.loc[j,'BKT']=='BKT12':
        for i in range(0,len(A['BKT'])):
            if A.loc[i,'BKT']=='BKT12':
                if (P.loc[j,['BKT','STATE']]==A.loc[i,['BKT','STATE']]).all():
                    for k in range(0,len(l12)):
                        for l in range(0,len(R12['Target'])):
                            if k==0 and l==0:
                                if P.loc[j,'POS_RES%']<=l12[k] and P.loc[j,'Additional_Performance']<=R12.loc[l,'Target']:
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        a=A.loc[i,'Billing PAID AMT.']*P12.loc[l,l12[k]]/100
                                        if a>CAP.loc[0,'BKT12']:
                                            A.loc[i,'PERCENTAGE']=str(P12.loc[l,l12[k]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT12']
                                            print(A.loc[i,'AGREEMENTID'],P12.loc[l,l12[k]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P12.loc[l,l12[k]])+'%'
                                            A.loc[i,'MOHAK']=a
                                            print(A.loc[i,'AGREEMENTID'],P12.loc[l,l12[k]],A.loc[i,'MOHAK'])
                                    elif (A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT'):
                                        b=A.loc[i,'Billing PAID AMT.']*4/100
                                        if b>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=b
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                            elif k==4 and l==0:
                                if ((P.loc[j,'POS_RES%']>=l12[k-1]) and (P.loc[j,'POS_RES%']<l12[k])) and (P.loc[j,'Additional_Performance']<=R12.loc[l,'Target']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P12.loc[l,l12[k-1]]/100
                                        if c>CAP.loc[0,'BKT12']:
                                            A.loc[i,'PERCENTAGE']=str(P12.loc[l,l12[k-1]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT12']
                                            print(A.loc[i,'AGREEMENTID'],P12.loc[l,l12[k-1]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P12.loc[l,l12[k-1]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P12.loc[l,l12[k-1]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                                elif (P.loc[j,'POS_RES%']>=l12[k]) and (P.loc[j,'Additional_Performance']<=R12.loc[l,'Target']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P12.loc[l,l12[k]]/100
                                        if c>CAP.loc[0,'BKT12']:
                                            A.loc[i,'PERCENTAGE']=str(P12.loc[l,l12[k]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT12']
                                            print(A.loc[i,'AGREEMENTID'],P12.loc[l,l12[k]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P12.loc[l,l12[k]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P12.loc[l,l12[k]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                            elif k==4 and l>0:
                                if ((P.loc[j,'POS_RES%']>=l12[k-1]) and (P.loc[j,'POS_RES%']<l12[k])) and ((P.loc[j,'Additional_Performance']>=R12.loc[l-1,'Target']) and (P.loc[j,'Additional_Performance']<R12.loc[l,'Target'])):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P12.loc[l-1,l12[k-1]]/100
                                        if c>CAP.loc[0,'BKT12']:
                                            A.loc[i,'PERCENTAGE']=str(P12.loc[l-1,l12[k-1]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT12']
                                            print(A.loc[i,'AGREEMENTID'],P12.loc[l-1,l12[k-1]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P12.loc[l-1,l12[k-1]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P12.loc[l-1,l12[k-1]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                                elif (P.loc[j,'POS_RES%']>=l12[k]) and ((P.loc[j,'Additional_Performance']>=R12.loc[l-1,'Target']) and (P.loc[j,'Additional_Performance']<R12.loc[l,'Target'])):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P12.loc[l-1,l12[k]]/100
                                        if c>CAP.loc[0,'BKT12']:
                                            A.loc[i,'PERCENTAGE']=str(P12.loc[l-1,l12[k]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT12']
                                            print(A.loc[i,'AGREEMENTID'],P12.loc[l-1,l12[k]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P12.loc[l-1,l12[k]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P12.loc[l-1,l12[k]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                                elif k==4 and l==4:
                                    if (P.loc[j,'POS_RES%']>=l12[k]) and P.loc[j,'Additional_Performance']>=R12.loc[l,'Target']:
                                        if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                            c=A.loc[i,'Billing PAID AMT.']*P12.loc[l,l12[k]]/100
                                            if c>CAP.loc[0,'BKT12']:
                                                A.loc[i,'PERCENTAGE']=str(P12.loc[l,l12[k]])+'%'
                                                A.loc[i,'MOHAK']=CAP.loc[0,'BKT12']
                                                print(A.loc[i,'AGREEMENTID'],P12.loc[l,l12[k]],A.loc[i,'MOHAK'])
                                            else:
                                                A.loc[i,'PERCENTAGE']=str(P12.loc[l,l12[k]])+'%'
                                                A.loc[i,'MOHAK']=c
                                                print(A.loc[i,'AGREEMENTID'],P12.loc[l,l12[k]],A.loc[i,'MOHAK'])
                                        elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                            d=A.loc[i,'Billing PAID AMT.']*4/100
                                            if d>25000:
                                                A.loc[i,'PERCENTAGE']=str(4)+'%'
                                                A.loc[i,'MOHAK']=25000
                                                print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                            else:
                                                A.loc[i,'PERCENTAGE']=str(4)+'%'
                                                A.loc[i,'MOHAK']=d
                                                print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(0)+'%'
                                            A.loc[i,'MOHAK']=0
                                            print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                            elif k>0 and l==0:
                                if (P.loc[j,'POS_RES%']>=l12[k-1] and P.loc[j,'POS_RES%']<l12[k]) and (P.loc[j,'Additional_Performance']<=R12.loc[l,'Target']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P12.loc[l,l12[k-1]]/100
                                        if c>CAP.loc[0,'BKT12']:
                                            A.loc[i,'PERCENTAGE']=str(P12.loc[l,l12[k-1]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT12']
                                            print(A.loc[i,'AGREEMENTID'],P12.loc[l,l12[k-1]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P12.loc[l,l12[k-1]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P12.loc[l,l12[k-1]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                            elif k>0 and l>0:
                                if (P.loc[j,'POS_RES%']>=l12[k-1] and P.loc[j,'POS_RES%']<l12[k]) and (P.loc[j,'Additional_Performance']>=R12.loc[l-1,'Target'] and P.loc[j,'Additional_Performance']<R12.loc[l,'Traget']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P12.loc[l-1,l12[k-1]]/100
                                        if c>CAP.loc[0,'BKT12']:
                                            A.loc[i,'PERCENTAGE']=str(P12.loc[l-1,l12[k-1]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT12']
                                            print(A.loc[i,'AGREEMENTID'],P12.loc[l-1,l12[k-1]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P12.loc[l-1,l12[k-1]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P12.loc[l-1,l12[k-1]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
#BKT13
                                        
for j in range(0,len(P['BKT'])):
    if P.loc[j,'BKT']=='BKT13':
        for i in range(0,len(A['BKT'])):
            if A.loc[i,'BKT']=='BKT13':
                if (P.loc[j,['BKT','STATE']]==A.loc[i,['BKT','STATE']]).all():
                    for k in range(0,len(l13)):
                        for l in range(0,len(R13['Target'])):
                            if k==0 and l==0:
                                if P.loc[j,'POS_RES%']<=l13[k] and P.loc[j,'Additional_Performance']<=R13.loc[l,'Target']:
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        a=A.loc[i,'Billing PAID AMT.']*P13.loc[l,l13[k]]/100
                                        if a>CAP.loc[0,'BKT13']:
                                            A.loc[i,'PERCENTAGE']=str(P13.loc[l,l13[k]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT13']
                                            print(A.loc[i,'AGREEMENTID'],P13.loc[l,l13[k]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P13.loc[l,l13[k]])+'%'
                                            A.loc[i,'MOHAK']=a
                                            print(A.loc[i,'AGREEMENTID'],P13.loc[l,l13[k]],A.loc[i,'MOHAK'])
                                    elif (A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT'):
                                        b=A.loc[i,'Billing PAID AMT.']*4/100
                                        if b>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=b
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                            elif k==4 and l==0:
                                if ((P.loc[j,'POS_RES%']>=l13[k-1]) and (P.loc[j,'POS_RES%']<l13[k])) and (P.loc[j,'Additional_Performance']<=R13.loc[l,'Target']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P13.loc[l,l13[k-1]]/100
                                        if c>CAP.loc[0,'BKT13']:
                                            A.loc[i,'PERCENTAGE']=str(P13.loc[l,l13[k-1]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT13']
                                            print(A.loc[i,'AGREEMENTID'],P13.loc[l,l13[k-1]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P13.loc[l,l13[k-1]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P13.loc[l,l13[k-1]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                                elif (P.loc[j,'POS_RES%']>=l13[k]) and (P.loc[j,'Additional_Performance']<=R13.loc[l,'Target']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P13.loc[l,l13[k]]/100
                                        if c>CAP.loc[0,'BKT12']:
                                            A.loc[i,'PERCENTAGE']=str(P13.loc[l,l13[k]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT13']
                                            print(A.loc[i,'AGREEMENTID'],P13.loc[l,l13[k]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P13.loc[l,l13[k]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P13.loc[l,l13[k]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                            elif k==4 and l>0:
                                if ((P.loc[j,'POS_RES%']>=l13[k-1]) and (P.loc[j,'POS_RES%']<l13[k])) and ((P.loc[j,'Additional_Performance']>=R13.loc[l-1,'Target']) and (P.loc[j,'Additional_Performance']<R13.loc[l,'Target'])):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P13.loc[l-1,l13[k-1]]/100
                                        if c>CAP.loc[0,'BKT13']:
                                            A.loc[i,'PERCENTAGE']=str(P13.loc[l-1,l13[k-1]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT13']
                                            print(A.loc[i,'AGREEMENTID'],P13.loc[l-1,l13[k-1]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P13.loc[l-1,l13[k-1]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P13.loc[l-1,l13[k-1]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                                elif (P.loc[j,'POS_RES%']>=l13[k]) and ((P.loc[j,'Additional_Performance']>=R13.loc[l-1,'Target']) and (P.loc[j,'Additional_Performance']<R13.loc[l,'Target'])):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P13.loc[l-1,l13[k]]/100
                                        if c>CAP.loc[0,'BKT13']:
                                            A.loc[i,'PERCENTAGE']=str(P13.loc[l-1,l13[k]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT13']
                                            print(A.loc[i,'AGREEMENTID'],P13.loc[l-1,l13[k]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P13.loc[l-1,l13[k]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P13.loc[l-1,l13[k]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                                elif k==4 and l==4:
                                    if (P.loc[j,'POS_RES%']>=l13[k]) and P.loc[j,'Additional_Performance']>=R13.loc[l,'Target']:
                                        if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                            c=A.loc[i,'Billing PAID AMT.']*P13.loc[l,l13[k]]/100
                                            if c>CAP.loc[0,'BKT13']:
                                                A.loc[i,'PERCENTAGE']=str(P13.loc[l,l13[k]])+'%'
                                                A.loc[i,'MOHAK']=CAP.loc[0,'BKT13']
                                                print(A.loc[i,'AGREEMENTID'],P13.loc[l,l13[k]],A.loc[i,'MOHAK'])
                                            else:
                                                A.loc[i,'PERCENTAGE']=str(P13.loc[l,l13[k]])+'%'
                                                A.loc[i,'MOHAK']=c
                                                print(A.loc[i,'AGREEMENTID'],P13.loc[l,l13[k]],A.loc[i,'MOHAK'])
                                        elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                            d=A.loc[i,'Billing PAID AMT.']*4/100
                                            if d>25000:
                                                A.loc[i,'PERCENTAGE']=str(4)+'%'
                                                A.loc[i,'MOHAK']=25000
                                                print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                            else:
                                                A.loc[i,'PERCENTAGE']=str(4)+'%'
                                                A.loc[i,'MOHAK']=d
                                                print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(0)+'%'
                                            A.loc[i,'MOHAK']=0
                                            print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                            elif k>0 and l==0:
                                if (P.loc[j,'POS_RES%']>=l13[k-1] and P.loc[j,'POS_RES%']<l13[k]) and (P.loc[j,'Additional_Performance']<=R13.loc[l,'Target']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P13.loc[l,l13[k-1]]/100
                                        if c>CAP.loc[0,'BKT13']:
                                            A.loc[i,'PERCENTAGE']=str(P13.loc[l,l13[k-1]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT13']
                                            print(A.loc[i,'AGREEMENTID'],P13.loc[l,l13[k-1]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P13.loc[l,l13[k-1]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P13.loc[l,l13[k-1]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])
                            elif k>0 and l>0:
                                if (P.loc[j,'POS_RES%']>=l13[k-1] and P.loc[j,'POS_RES%']<l13[k]) and (P.loc[j,'Additional_Performance']>=R13.loc[l-1,'Target'] and P.loc[j,'Additional_Performance']<R13.loc[l,'Traget']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*P13.loc[l-1,l13[k-1]]/100
                                        if c>CAP.loc[0,'BKT12']:
                                            A.loc[i,'PERCENTAGE']=str(P13.loc[l-1,l13[k-1]])+'%'
                                            A.loc[i,'MOHAK']=CAP.loc[0,'BKT13']
                                            print(A.loc[i,'AGREEMENTID'],P13.loc[l-1,l13[k-1]],A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(P13.loc[l-1,l13[k-1]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],P13.loc[l-1,l13[k-1]],A.loc[i,'MOHAK'])
                                    elif A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT':
                                        d=A.loc[i,'Billing PAID AMT.']*4/100
                                        if d>25000:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=25000
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(4)+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],4,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'PERCENTAGE']=str(0)+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],0,A.loc[i,'MOHAK'])

A.rename({'MOHAK':'PAYOUT'},axis=1,inplace=True)

A.to_excel(r'/Users/mohaksehgal/Documents/Work/FOS Salary/IDFC/JUN 21/MASTER FILE IDFC.xlsx',index=False)

A.to_excel(r'/Users/mohaksehgal/Documents/Work/Billing/IDFC/IDFC Jun 21/Final Billing IDFC.xlsx',index=False)