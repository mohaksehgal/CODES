#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 10:48:12 2020

@author: mohaksehgal
"""


import pandas as pd
import numpy as np

A=pd.read_excel(r"/Users/mohaksehgal/Documents/Work/Billing/IDFC TW/IDFC TW Jun 21/MASTER FILE IDFC TW.xlsx")

P=pd.read_excel(r'/Users/mohaksehgal/Documents/Work/Billing/IDFC TW/IDFC TW Jun 21/Performance TW.xlsx')

BKT0=pd.read_excel('/Users/mohaksehgal/Documents/Work/Billing/IDFC TW/PAYOUT/BKT0.xlsx')
BKT1=pd.read_excel('/Users/mohaksehgal/Documents/Work/Billing/IDFC TW/PAYOUT/BKT 1.xlsx')
BKT1T=pd.read_excel('/Users/mohaksehgal/Documents/Work/Billing/IDFC TW/PAYOUT/BKT 1 Target.xlsx')
BKT2=pd.read_excel('/Users/mohaksehgal/Documents/Work/Billing/IDFC TW/PAYOUT/BKT 2.xlsx')
BKT2T=pd.read_excel('/Users/mohaksehgal/Documents/Work/Billing/IDFC TW/PAYOUT/BKT 2 Target.xlsx')
BKT3=pd.read_excel('/Users/mohaksehgal/Documents/Work/Billing/IDFC TW/PAYOUT/BKT 3.xlsx')
BKT3T=pd.read_excel('/Users/mohaksehgal/Documents/Work/Billing/IDFC TW/PAYOUT/BKT 3 Target.xlsx')
BKT4=pd.read_excel('/Users/mohaksehgal/Documents/Work/Billing/IDFC TW/PAYOUT/BKT 4.xlsx')
BKT4T=pd.read_excel('/Users/mohaksehgal/Documents/Work/Billing/IDFC TW/PAYOUT/BKT 4 Target.xlsx')
BKT5=pd.read_excel('/Users/mohaksehgal/Documents/Work/Billing/IDFC TW/PAYOUT/BKT 5.xlsx')
BKT5T=pd.read_excel('/Users/mohaksehgal/Documents/Work/Billing/IDFC TW/PAYOUT/BKT 5 Target.xlsx')
BKT6=pd.read_excel('/Users/mohaksehgal/Documents/Work/Billing/IDFC TW/PAYOUT/BKT 6.xlsx')
BKT6T=pd.read_excel('/Users/mohaksehgal/Documents/Work/Billing/IDFC TW/PAYOUT/BKT 6 Target.xlsx')



l1=list(BKT1.columns)
l2=list(BKT2.columns)
l3=list(BKT3.columns)
l4=list(BKT4.columns)
l5=list(BKT5.columns)
l6=list(BKT6.columns)



#BKT 0

for j in range(0,len(P['BKT'])):
    if P.loc[j,'BKT']==0:
        for i in range(0,len(A['BKT'])):
            if A.loc[i,'BKT']==0:
                for l in range(0,len(BKT0)):
                    if l==0:
                        if A.loc[i,'STATUS']=='RT':
                            A.loc[i,'MOHAK']=0
                        elif A.loc[i,'STATUS']=='SB'or A.loc[i,'STATUS']=='NM' or A.loc[i,'STATUS']=='RB':
                            if P.loc[j,'POS_RES%']<=BKT0.loc[l,'TARGET']:
                                a=A.loc[i,'Billing PAID AMT.']*BKT0.loc[l,'CAT C']/100
                                A.loc[i,'percentage']=str(BKT0.loc[l,'CAT C'])+'%'
                                A.loc[i,'MOHAK']=a
                                print(A.loc[i,'AGREEMENTID'],BKT0.loc[l,'CAT C'],A.loc[i,'MOHAK'])
                            elif l>0:
                                if P.loc[j,'POS_RES%']>=BKT0.loc[l-1,'TARGET'] and P.loc[j,'POS_RES%']<BKT0.loc[l,'TARGET']:
                                    a=A.loc[i,'Billing PAID AMT.']*BKT0.loc[l-1,'CAT C']/100
                                    A.loc[i,'percentage']=str(BKT0.loc[l-1,'CAT C'])+'%'
                                    A.loc[i,'MOHAK']=a
                                    print(A.loc[i,'AGREEMENTID'],BKT0.loc[l,'CAT C'],A.loc[i,'MOHAK'])
                            elif l==9:
                                if P.loc[j,'POS_RES%']>=BKT0.loc[l,'TARGET']:
                                    a=A.loc[i,'Billing PAID AMT.']*BKT0.loc[l,'CAT C']/100
                                    A.loc[i,'percentage']=str(BKT0.loc[l,'CAT C'])+'%'
                                    A.loc[i,'MOHAK']=a
                                    print(A.loc[i,'AGREEMENTID'],BKT0.loc[l,'CAT C'],A.loc[i,'MOHAK'])
                        else:
                            A.loc[i,'percentage']=str(BKT0.loc[l,'CAT C'])+'%'
                            A.loc[i,'MOHAK']=0
                            
#BKT 1

for j in range(0,len(P['BKT'])):
    if P.loc[j,'BKT']==1:
        for i in range(0,len(A['BKT'])):
            if A.loc[i,'BKT']==1:
                for k in range(0,len(l1)):
                    for l in range(0,len(BKT1)):
                            if k==0 and l==0:
                                if A.loc[i,'STATUS']=='RT':
                                    A.loc[i,'MOHAK']=0
                                elif P.loc[j,'Additional_Performance']<l1[k] and P.loc[j,'POS_RES%']<=BKT1T.loc[l,'TARGET']:
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM' or A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT'):
                                        a=A.loc[i,'Billing PAID AMT.']*BKT1.loc[l,l1[k]]/100
                                        A.loc[i,'percentage']=str(BKT1.loc[l,l1[k]])+'%'
                                        A.loc[i,'MOHAK']=a
                                        print(A.loc[i,'AGREEMENTID'],BKT1.loc[l,l1[k]],A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'percentage']=str(BKT1.loc[l,l1[k]])+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],BKT1.loc[l,l1[k]],A.loc[i,'MOHAK'])
                            elif k==7 and l==0:
                                if A.loc[i,'STATUS']=='RT':
                                    A.loc[i,'MOHAK']=0
                                elif (P.loc[j,'Additional_Performance']>=l1[k-1]) and (P.loc[j,'POS_RES%']<=BKT1T.loc[l,'TARGET']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM' or A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT'):
                                        c=A.loc[i,'Billing PAID AMT.']*BKT1.loc[l,l1[k]]/100
                                        A.loc[i,'percentage']=str(BKT1.loc[l,l1[k]])+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],BKT1.loc[l,l1[k]],A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'percentage']=str(BKT1.loc[l,l1[k]])+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],BKT1.loc[l,l1[k]],A.loc[i,'MOHAK'])
                            elif k==0 and l>0:
                                if A.loc[i,'STATUS']=='RT':
                                    A.loc[i,'MOHAK']=0
                                elif (P.loc[j,'Additional_Performance']<l1[k]) and ((P.loc[j,'POS_RES%']>=BKT1T.loc[l-1,'TARGET']) and (P.loc[j,'POS_RES%']<BKT1T.loc[l,'TARGET'])):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM' or A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT'):
                                        c=A.loc[i,'Billing PAID AMT.']*BKT1.loc[l,l1[k]]/100
                                        A.loc[i,'percentage']=str(BKT1.loc[l,l1[k]])+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],BKT1.loc[l,l1[k]],A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'percentage']=str(BKT1.loc[l,l1[k]])+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],BKT1.loc[l,l1[k]],A.loc[i,'MOHAK'])
                            elif k==7 and l>0:
                                if A.loc[i,'STATUS']=='RT':
                                    A.loc[i,'MOHAK']=0
                                elif (P.loc[j,'Additional_Performance']>=l1[k-1]) and ((P.loc[j,'POS_RES%']>=BKT1T.loc[l-1,'TARGET']) and (P.loc[j,'POS_RES%']<BKT1T.loc[l,'TARGET'])):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM' or A.loc[i,'STATUS']=='SETTLEMENT' or A.loc[i,'STATUS']=='FORECLOSE'):
                                        c=A.loc[i,'Billing PAID AMT.']*BKT1.loc[l-1,l1[k]]/100
                                        A.loc[i,'percentage']=str(BKT1.loc[l-1,l1[k]])+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],BKT1.loc[l-1,l1[k]],A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'percentage']=str(BKT1.loc[l,l1[k]])+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],BKT1.loc[l,l1[k]],A.loc[i,'MOHAK'])
                            elif k==7 and l==9:
                                if A.loc[i,'STATUS']=='RT':
                                    A.loc[i,'MOHAK']=0
                                elif (P.loc[j,'Additional_Performance']>=l1[k]) and P.loc[j,'POS_RES%']>=BKT1T.loc[l,'TARGET']:
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM' or A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT'):
                                        c=A.loc[i,'Billing PAID AMT.']*BKT1.loc[l,l1[k]]/100
                                        A.loc[i,'percentage']=str(BKT1.loc[l,l1[k]])+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],BKT1.loc[l,l1[k]],A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'percentage']=str(BKT1.loc[l,l1[k]])+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],BKT1.loc[l,l1[k]],A.loc[i,'MOHAK'])
                            elif k>0 and l==0:
                                if A.loc[i,'STATUS']=='RT':
                                    A.loc[i,'MOHAK']=0
                                elif (P.loc[j,'Additional_Performance']>=l1[k-1] and P.loc[j,'Additional_Performance']<l1[k]) and (P.loc[j,'POS_RES%']<=BKT1T.loc[l,'TARGET']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM' or A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT'):
                                        c=A.loc[i,'Billing PAID AMT.']*BKT1.loc[l,l1[k]]/100
                                        A.loc[i,'percentage']=str(BKT1.loc[l,l1[k]])+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],BKT1.loc[l,l1[k]],A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'percentage']=str(BKT1.loc[l,l1[k]])+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],BKT1.loc[l,l1[k]],A.loc[i,'MOHAK'])
                            elif k>0 and l>0:
                                if (P.loc[j,'Additional_Performance']>=l1[k-1] and P.loc[j,'Additional_Performance']<l1[k]) and (P.loc[j,'POS_RES%']>BKT1T.loc[l-1,'TARGET'] and P.loc[j,'POS_RES%']<=BKT1T.loc[l,'TARGET']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM' or A.loc[i,'STATUS']=='SETTLEMENT' or A.loc[i,'STATUS']=='FORECLOSE'):
                                        c=A.loc[i,'Billing PAID AMT.']*BKT1.loc[l-1,l1[k]]/100
                                        A.loc[i,'percentage']=str(BKT1.loc[l-1,l1[k]])+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],BKT1.loc[l-1,l1[k]],A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'percentage']=str(BKT1.loc[l,l1[k]])+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],BKT1.loc[l,l1[k]],A.loc[i,'MOHAK'])
                                        
# =============================================================================
# BKT-2
# =============================================================================

for j in range(0,len(P['BKT'])):
    if P.loc[j,'BKT']==2:
        for i in range(0,len(A['BKT'])):
            if A.loc[i,'BKT']==2:
                for k in range(0,len(l2)):
                    for l in range(0,len(BKT2)):
                            if k==0 and l==0:
                                if A.loc[i,'STATUS']=='RT':
                                    A.loc[i,'MOHAK']=250
                                elif P.loc[j,'Additional_Performance']<=l2[k] and P.loc[j,'POS_RES%']<=BKT2T.loc[l,'TARGET']:
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM' or A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT'):
                                        a=A.loc[i,'Billing PAID AMT.']*BKT2.loc[l,l2[k]]/100
                                        A.loc[i,'percentage']=str(BKT2.loc[l,l2[k]])+'%'
                                        A.loc[i,'MOHAK']=a
                                        print(A.loc[i,'AGREEMENTID'],BKT2.loc[l,l2[k]],A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'percentage']=str(BKT2.loc[l,l2[k]])+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],BKT2.loc[l,l2[k]],A.loc[i,'MOHAK'])
                            elif k==7 and l==0:
                                if A.loc[i,'STATUS']=='RT':
                                    A.loc[i,'MOHAK']=250
                                elif ((P.loc[j,'Additional_Performance']>=l2[k-1]) and (P.loc[j,'Additional_Performance']<l2[k])) and P.loc[j,'POS_RES%']<=BKT2T.loc[l,'TARGET']:
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM' or A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT'):
                                        c=A.loc[i,'Billing PAID AMT.']*BKT2.loc[l,l2[k-1]]/100
                                        A.loc[i,'percentage']=str(BKT2.loc[l,l2[k-1]])+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],BKT2.loc[l,l2[k-1]],A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'percentage']=str(BKT2.loc[l,l2[k]])+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],BKT2.loc[l,l2[k]],A.loc[i,'MOHAK'])
                                elif (P.loc[j,'Additional_Performance']>=int(l2[k])) and (P.loc[j,'POS_RES%']<=BKT2T.loc[l,'TARGET']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM' or A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT'):
                                        c=A.loc[i,'Billing PAID AMT.']*BKT2.loc[l,l2[k]]/100
                                        A.loc[i,'percentage']=str(BKT2.loc[l,l2[k]])+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],BKT2.loc[l,l2[k]],A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'percentage']=str(BKT2.loc[l,l2[k]])+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],BKT2.loc[l,l2[k]],A.loc[i,'MOHAK'])
                            elif k==0 and l>0:
                                if A.loc[i,'STATUS']=='RT':
                                    A.loc[i,'MOHAK']=250
                                elif (P.loc[j,'Additional_Performance']<=l2[k]) and ((P.loc[j,'POS_RES%']>=BKT2T.loc[l-1,'TARGET']) and (P.loc[j,'POS_RES%']<BKT2T.loc[l,'TARGET'])):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM' or A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT'):
                                        c=A.loc[i,'Billing PAID AMT.']*BKT2.loc[l,l2[k]]/100
                                        A.loc[i,'percentage']=str(BKT2.loc[l,l2[k]])+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],BKT2.loc[l,l2[k]],A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'percentage']=str(BKT2.loc[l,l2[k]])+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],BKT2.loc[l,l2[k]],A.loc[i,'MOHAK'])
                                elif (P.loc[j,'Additional_Performance']>=l2[k]) and P.loc[j,'POS_RES%']<=BKT2T.loc[l,'TARGET']:
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM' or A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT'):
                                        c=A.loc[i,'Billing PAID AMT.']*BKT2.loc[l,l2[k]]/100
                                        A.loc[i,'percentage']=str(BKT2.loc[l,l2[k]])+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],BKT2.loc[l,l2[k]],A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'percentage']=str(BKT2.loc[l,l2[k]])+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],BKT2.loc[l,l2[k]],A.loc[i,'MOHAK'])
                            elif k==7 and l>0:
                                if A.loc[i,'STATUS']=='RT':
                                    A.loc[i,'MOHAK']=250
                                elif ((P.loc[j,'Additional_Performance']>=l2[k-1]) and (P.loc[j,'Additional_Performance']<l2[k])) and ((P.loc[j,'POS_RES%']>=BKT2T.loc[l-1,'TARGET']) and (P.loc[j,'POS_RES%']<BKT2T.loc[l,'TARGET'])):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM' or A.loc[i,'STATUS']=='SETTLEMENT' or A.loc[i,'STATUS']=='FORECLOSE'):
                                        c=A.loc[i,'Billing PAID AMT.']*BKT2.loc[l-1,l2[k-1]]/100
                                        A.loc[i,'percentage']=str(BKT2.loc[l-1,l2[k-1]])+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],BKT2.loc[l-1,l2[k-1]],A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'percentage']=str(BKT2.loc[l,l2[k]])+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],BKT2.loc[l,l1[k]],A.loc[i,'MOHAK'])
                                elif (P.loc[j,'Additional_Performance']>=l2[k]) and ((P.loc[j,'POS_RES%']>=BKT2T.loc[l-1,'TARGET']) and (P.loc[j,'POS_RES%']<BKT2T.loc[l,'TARGET'])):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM' or A.loc[i,'STATUS']=="FORECLOSE" or A.loc[i,'STATUS']=='SETTLEMENT'):
                                        c=A.loc[i,'Billing PAID AMT.']*BKT2.loc[l-1,l2[k]]/100
                                        A.loc[i,'percentage']=str(BKT2.loc[l-1,l2[k]])+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],BKT2.loc[l-1,l2[k]],A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'percentage']=str(BKT2.loc[l,l2[k]])+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],BKT2.loc[l,l2[k]],A.loc[i,'MOHAK'])
                            elif k==7 and l==9:
                                if A.loc[i,'STATUS']=='RT':
                                    A.loc[i,'MOHAK']=250
                                elif (P.loc[j,'Additional_Performance']>=l2[k]) and P.loc[j,'POS_RES%']>=BKT2T.loc[l,'TARGET']:
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM' or A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT'):
                                        c=A.loc[i,'Billing PAID AMT.']*BKT2.loc[l,l2[k]]/100
                                        A.loc[i,'percentage']=str(BKT2.loc[l,l2[k]])+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],BKT2.loc[l,l2[k]],A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'percentage']=str(BKT2.loc[l,l2[k]])+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],BKT2.loc[l,l2[k]],A.loc[i,'MOHAK'])
                            elif k>0 and l==0:
                                if A.loc[i,'STATUS']=='RT':
                                    A.loc[i,'MOHAK']=250
                                elif (P.loc[j,'Additional_Performance']>float(l2[k-1]) and P.loc[j,'Additional_Performance']<=l2[k]) and (P.loc[j,'POS_RES%']<=BKT2T.loc[l,'TARGET']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM' or A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT'):
                                        c=A.loc[i,'Billing PAID AMT.']*BKT2.loc[l,l2[k-1]]/100
                                        A.loc[i,'percentage']=str(BKT2.loc[l,l2[k-1]])+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],BKT2.loc[l,l2[k-1]],A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'percentage']=str(BKT2.loc[l,l2[k]])+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],BKT2.loc[l,l2[k]],A.loc[i,'MOHAK'])
                            elif k>0 and l>0:
                                if (P.loc[j,'Additional_Performance']>l2[k-1] and P.loc[j,'Additional_Performance']<=l2[k]) and (P.loc[j,'POS_RES%']>BKT2T.loc[l-1,'TARGET'] and P.loc[j,'POS_RES%']<=BKT2T.loc[l,'TARGET']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM' or A.loc[i,'STATUS']=='SETTLEMENT' or A.loc[i,'STATUS']=='FORECLOSE'):
                                        c=A.loc[i,'Billing PAID AMT.']*BKT2.loc[l-1,l2[k-1]]/100
                                        A.loc[i,'percentage']=str(BKT2.loc[l-1,l2[k-1]])+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],BKT2.loc[l-1,l2[k-1]],A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'percentage']=str(BKT2.loc[l,l2[k]])+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],BKT2.loc[l,l2[k]],A.loc[i,'MOHAK'])
                                    
# =============================================================================
# BKT-3
# =============================================================================

for j in range(0,len(P['BKT'])):
    if P.loc[j,'BKT']==3:
        for i in range(0,len(A['BKT'])):
            if A.loc[i,'BKT']==3:
                for k in range(0,len(l3)):
                    for l in range(0,len(BKT3)):
                            if k==0 and l==0:
                                if A.loc[i,'STATUS']=='RT':
                                    A.loc[i,'MOHAK']=150
                                elif P.loc[j,'Additional_Performance']<=l3[k] and P.loc[j,'POS_RES%']<=BKT3T.loc[l,'TARGET']:
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        a=A.loc[i,'Billing PAID AMT.']*BKT3.loc[l,l3[k]]/100
                                        A.loc[i,'percentage']=str(BKT3.loc[l,l3[k]])+'%'
                                        A.loc[i,'MOHAK']=a
                                        print(A.loc[i,'AGREEMENTID'],BKT3.loc[l,l3[k]],A.loc[i,'MOHAK'])
                                    elif (A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT'):
                                        a=A.loc[i,'Billing PAID AMT.']*15/100
                                        A.loc[i,'percentage']=str(15)+'%'
                                        A.loc[i,'MOHAK']=a
                                        print(A.loc[i,'AGREEMENTID'],str(15),A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'percentage']=str(BKT3.loc[l,l3[k]])+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],BKT3.loc[l,l3[k]],A.loc[i,'MOHAK'])
                            elif k==6 and l==0:
                                if A.loc[i,'STATUS']=='RT':
                                    A.loc[i,'MOHAK']=150
                                elif ((P.loc[j,'Additional_Performance']>=l3[k-1]) and (P.loc[j,'Additional_Performance']<l3[k])) and P.loc[j,'POS_RES%']<=BKT3T.loc[l,'TARGET']:
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*BKT3.loc[l,l3[k-1]]/100
                                        A.loc[i,'percentage']=str(BKT3.loc[l,l3[k-1]])+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],BKT3.loc[l,l3[k-1]],A.loc[i,'MOHAK'])
                                    elif (A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT'):
                                        c=A.loc[i,'Billing PAID AMT.']*BKT3.loc[l,l3[k-1]]/100
                                        A.loc[i,'percentage']=str(15)+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],str(15),A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'percentage']=str(BKT3.loc[l,l3[k]])+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],BKT3.loc[l,l3[k]],A.loc[i,'MOHAK'])
                                elif (P.loc[j,'Additional_Performance']>=int(l3[k])) and (P.loc[j,'POS_RES%']<=BKT3T.loc[l,'TARGET']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*BKT3.loc[l,l3[k]]/100
                                        A.loc[i,'percentage']=str(BKT3.loc[l,l3[k]])+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],BKT3.loc[l,l3[k]],A.loc[i,'MOHAK'])
                                    elif (A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT'):
                                        c=A.loc[i,'Billing PAID AMT.']*BKT3.loc[l,l3[k]]/100
                                        A.loc[i,'percentage']=str(15)+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],BKT3.loc[l,l3[k]],A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'percentage']=str(BKT3.loc[l,l3[k]])+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],BKT3.loc[l,l3[k]],A.loc[i,'MOHAK'])
                            elif k==0 and l>0:
                                if A.loc[i,'STATUS']=='RT':
                                    A.loc[i,'MOHAK']=150
                                elif (P.loc[j,'Additional_Performance']<=l3[k]) and ((P.loc[j,'POS_RES%']>=BKT3T.loc[l-1,'TARGET']) and (P.loc[j,'POS_RES%']<BKT3T.loc[l,'TARGET'])):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*BKT3.loc[l,l3[k]]/100
                                        A.loc[i,'percentage']=str(BKT3.loc[l,l3[k]])+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],BKT3.loc[l,l3[k]],A.loc[i,'MOHAK'])
                                    elif (A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT'):
                                        c=A.loc[i,'Billing PAID AMT.']*15/100
                                        A.loc[i,'percentage']=str(15)+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],str(15),A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'percentage']=str(BKT3.loc[l,l3[k]])+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],BKT3.loc[l,l3[k]],A.loc[i,'MOHAK'])
                                elif (P.loc[j,'Additional_Performance']>=l3[k]) and P.loc[j,'POS_RES%']<=BKT3T.loc[l,'TARGET']:
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*BKT3.loc[l,l3[k]]/100
                                        A.loc[i,'percentage']=str(BKT3.loc[l,l3[k]])+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],BKT3.loc[l,l3[k]],A.loc[i,'MOHAK'])
                                    elif (A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT'):
                                        c=A.loc[i,'Billing PAID AMT.']*15/100
                                        A.loc[i,'percentage']=str(15)+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],str(15),A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'percentage']=str(BKT3.loc[l,l3[k]])+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],BKT3.loc[l,l3[k]],A.loc[i,'MOHAK'])
                            elif k==6 and l>0:
                                if A.loc[i,'STATUS']=='RT':
                                    A.loc[i,'MOHAK']=150
                                elif ((P.loc[j,'Additional_Performance']>=l3[k-1]) and (P.loc[j,'Additional_Performance']<l3[k])) and ((P.loc[j,'POS_RES%']>=BKT3T.loc[l-1,'TARGET']) and (P.loc[j,'POS_RES%']<BKT3T.loc[l,'TARGET'])):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*BKT3.loc[l-1,l3[k-1]]/100
                                        A.loc[i,'percentage']=str(BKT3.loc[l-1,l3[k-1]])+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],BKT3.loc[l-1,l3[k-1]],A.loc[i,'MOHAK'])
                                    elif (A.loc[i,'STATUS']=='SETTLEMENT' or A.loc[i,'STATUS']=='FORECLOSE'):
                                        c=A.loc[i,'Billing PAID AMT.']*BKT3.loc[l-1,l3[k-1]]/100
                                        A.loc[i,'percentage']=str(15)+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],BKT3.loc[l-1,l3[k-1]],A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'percentage']=str(BKT3.loc[l,l3[k]])+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],BKT3.loc[l,l3[k]],A.loc[i,'MOHAK'])
                                elif (P.loc[j,'Additional_Performance']>=l3[k]) and ((P.loc[j,'POS_RES%']>=BKT3T.loc[l-1,'TARGET']) and (P.loc[j,'POS_RES%']<BKT3T.loc[l,'TARGET'])):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*BKT3.loc[l-1,l3[k]]/100
                                        A.loc[i,'percentage']=str(BKT3.loc[l-1,l3[k]])+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],BKT3.loc[l-1,l3[k]],A.loc[i,'MOHAK'])
                                    elif (A.loc[i,'STATUS']=="FORECLOSE" or A.loc[i,'STATUS']=='SETTLEMENT'):
                                        c=A.loc[i,'Billing PAID AMT.']*15/100
                                        A.loc[i,'percentage']=str(15)+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],BKT3.loc[l-1,l3[k]],A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'percentage']=str(BKT3.loc[l,l3[k]])+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],BKT3.loc[l,l3[k]],A.loc[i,'MOHAK'])
                            elif k==6 and l==9:
                                if A.loc[i,'STATUS']=='RT':
                                    A.loc[i,'MOHAK']=150
                                elif (P.loc[j,'Additional_Performance']>=l3[k]) and P.loc[j,'POS_RES%']>=BKT3T.loc[l,'TARGET']:
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*BKT3.loc[l,l3[k]]/100
                                        A.loc[i,'percentage']=str(BKT3.loc[l,l3[k]])+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],BKT3.loc[l,l3[k]],A.loc[i,'MOHAK'])
                                    elif (A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT'):
                                        c=A.loc[i,'Billing PAID AMT.']*15/100
                                        A.loc[i,'percentage']=str(15)+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],str(15),A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'percentage']=str(BKT3.loc[l,l3[k]])+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],BKT3.loc[l,l3[k]],A.loc[i,'MOHAK'])
                            elif k==0 and l==7:
                                if A.loc[i,'STATUS']=='RT':
                                    A.loc[i,'MOHAK']=150
                                elif (P.loc[j,'Additional_Performance']<=l3[k]) and (P.loc[j,'POS_RES%']>=BKT3T.loc[l,'TARGET']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*BKT3.loc[l,l3[k]]/100
                                        A.loc[i,'percentage']=str(BKT3.loc[l,l3[k]])+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],BKT3.loc[l,l3[k]],A.loc[i,'MOHAK'])
                                    elif (A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT'):
                                        c=A.loc[i,'Billing PAID AMT.']*15/100
                                        A.loc[i,'percentage']=str(15)+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],str(15),A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'percentage']=str(BKT3.loc[l,l3[k]])+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],BKT3.loc[l,l3[k]],A.loc[i,'MOHAK'])
                            elif k>0 and l==0:
                                if A.loc[i,'STATUS']=='RT':
                                    A.loc[i,'MOHAK']=150
                                elif (P.loc[j,'Additional_Performance']>l3[k-1] and P.loc[j,'Additional_Performance']<=l3[k]) and (P.loc[j,'POS_RES%']<=BKT3T.loc[l,'TARGET']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*BKT3.loc[l,l3[k-1]]/100
                                        A.loc[i,'percentage']=str(BKT3.loc[l,l3[k-1]])+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],BKT3.loc[l,l3[k-1]],A.loc[i,'MOHAK'])
                                    elif (A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT'):
                                        c=A.loc[i,'Billing PAID AMT.']*15/100
                                        A.loc[i,'percentage']=str(15)+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],str(15),A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'percentage']=str(BKT3.loc[l,l3[k]])+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],BKT3.loc[l,l3[k]],A.loc[i,'MOHAK'])
                            elif k>0 and l>0:
                                if (P.loc[j,'Additional_Performance']>l3[k-1] and P.loc[j,'Additional_Performance']<=l3[k]) and (P.loc[j,'POS_RES%']>BKT3T.loc[l-1,'TARGET'] and P.loc[j,'POS_RES%']<=BKT3T.loc[l,'TARGET']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*BKT3.loc[l-1,l3[k-1]]/100
                                        A.loc[i,'percentage']=str(BKT3.loc[l-1,l3[k-1]])+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],BKT3.loc[l-1,l3[k-1]],A.loc[i,'MOHAK'])
                                    elif (A.loc[i,'STATUS']=='SETTLEMENT' or A.loc[i,'STATUS']=='FORECLOSE'):
                                        c=A.loc[i,'Billing PAID AMT.']*15/100
                                        A.loc[i,'percentage']=str(15)+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],str(15),A.loc[i,'MOHAK'])                                        
                                    else:
                                        A.loc[i,'percentage']=str(BKT3.loc[l,l3[k]])+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],BKT3.loc[l,l3[k]],A.loc[i,'MOHAK'])

# =============================================================================
# BKT-4
# =============================================================================

for j in range(0,len(P['BKT'])):
    if P.loc[j,'BKT']==4:
        for i in range(0,len(A['BKT'])):
            if A.loc[i,'BKT']==4:
                for k in range(0,len(l4)):
                    for l in range(0,len(BKT4)):
                            if k==0 and l==0:
                                if A.loc[i,'STATUS']=='RT':
                                    A.loc[i,'MOHAK']=150
                                elif P.loc[j,'Additional_Performance']<=l4[k] and P.loc[j,'POS_RES%']<=BKT4T.loc[l,'TARGET']:
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        a=A.loc[i,'Billing PAID AMT.']*BKT4.loc[l,l4[k]]/100
                                        A.loc[i,'percentage']=str(BKT4.loc[l,l4[k]])+'%'
                                        A.loc[i,'MOHAK']=a
                                        print(A.loc[i,'AGREEMENTID'],BKT4.loc[l,l4[k]],A.loc[i,'MOHAK'])
                                    elif (A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT'):
                                        a=A.loc[i,'Billing PAID AMT.']*15/100
                                        A.loc[i,'percentage']=str(15)+'%'
                                        A.loc[i,'MOHAK']=a
                                        print(A.loc[i,'AGREEMENTID'],str(15),A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'percentage']=str(BKT4.loc[l,l4[k]])+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],BKT4.loc[l,l4[k]],A.loc[i,'MOHAK'])
                            elif k==6 and l==0:
                                if A.loc[i,'STATUS']=='RT':
                                    A.loc[i,'MOHAK']=150
                                elif ((P.loc[j,'Additional_Performance']>=l4[k-1]) and (P.loc[j,'Additional_Performance']<l4[k])) and P.loc[j,'POS_RES%']<=BKT4T.loc[l,'TARGET']:
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*BKT4.loc[l,l4[k-1]]/100
                                        A.loc[i,'percentage']=str(BKT4.loc[l,l4[k-1]])+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],BKT4.loc[l,l4[k-1]],A.loc[i,'MOHAK'])
                                    elif (A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT'):
                                        c=A.loc[i,'Billing PAID AMT.']*BKT4.loc[l,l4[k-1]]/100
                                        A.loc[i,'percentage']=str(15)+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],str(15),A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'percentage']=str(BKT4.loc[l,l4[k]])+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],BKT4.loc[l,l4[k]],A.loc[i,'MOHAK'])
                                elif (P.loc[j,'Additional_Performance']>=int(l4[k])) and (P.loc[j,'POS_RES%']<=BKT4T.loc[l,'TARGET']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*BKT4.loc[l,l4[k]]/100
                                        A.loc[i,'percentage']=str(BKT4.loc[l,l4[k]])+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],BKT4.loc[l,l4[k]],A.loc[i,'MOHAK'])
                                    elif (A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT'):
                                        c=A.loc[i,'Billing PAID AMT.']*BKT4.loc[l,l4[k]]/100
                                        A.loc[i,'percentage']=str(15)+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],BKT4.loc[l,l4[k]],A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'percentage']=str(BKT4.loc[l,l4[k]])+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],BKT4.loc[l,l4[k]],A.loc[i,'MOHAK'])
                            elif k==0 and l>0:
                                if A.loc[i,'STATUS']=='RT':
                                    A.loc[i,'MOHAK']=150
                                elif (P.loc[j,'Additional_Performance']<=l4[k]) and ((P.loc[j,'POS_RES%']>=BKT4T.loc[l-1,'TARGET']) and (P.loc[j,'POS_RES%']<BKT4T.loc[l,'TARGET'])):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*BKT4.loc[l,l4[k]]/100
                                        A.loc[i,'percentage']=str(BKT4.loc[l,l4[k]])+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],BKT4.loc[l,l4[k]],A.loc[i,'MOHAK'])
                                    elif (A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT'):
                                        c=A.loc[i,'Billing PAID AMT.']*15/100
                                        A.loc[i,'percentage']=str(15)+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],str(15),A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'percentage']=str(BKT4.loc[l,l4[k]])+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],BKT4.loc[l,l4[k]],A.loc[i,'MOHAK'])
                                elif (P.loc[j,'Additional_Performance']>=l4[k]) and P.loc[j,'POS_RES%']<=BKT4T.loc[l,'TARGET']:
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*BKT4.loc[l,l4[k]]/100
                                        A.loc[i,'percentage']=str(BKT4.loc[l,l4[k]])+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],BKT4.loc[l,l4[k]],A.loc[i,'MOHAK'])
                                    elif (A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT'):
                                        c=A.loc[i,'Billing PAID AMT.']*15/100
                                        A.loc[i,'percentage']=str(15)+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],str(15),A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'percentage']=str(BKT4.loc[l,l4[k]])+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],BKT4.loc[l,l4[k]],A.loc[i,'MOHAK'])
                            elif k==6 and l>0:
                                if A.loc[i,'STATUS']=='RT':
                                    A.loc[i,'MOHAK']=150
                                elif ((P.loc[j,'Additional_Performance']>=l4[k-1]) and (P.loc[j,'Additional_Performance']<l4[k])) and ((P.loc[j,'POS_RES%']>=BKT4T.loc[l-1,'TARGET']) and (P.loc[j,'POS_RES%']<BKT4T.loc[l,'TARGET'])):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*BKT4.loc[l-1,l4[k-1]]/100
                                        A.loc[i,'percentage']=str(BKT4.loc[l-1,l4[k-1]])+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],BKT4.loc[l-1,l4[k-1]],A.loc[i,'MOHAK'])
                                    elif (A.loc[i,'STATUS']=='SETTLEMENT' or A.loc[i,'STATUS']=='FORECLOSE'):
                                        c=A.loc[i,'Billing PAID AMT.']*BKT4.loc[l-1,l4[k-1]]/100
                                        A.loc[i,'percentage']=str(15)+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],BKT4.loc[l-1,l4[k-1]],A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'percentage']=str(BKT4.loc[l,l4[k]])+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],BKT4.loc[l,l4[k]],A.loc[i,'MOHAK'])
                                elif (P.loc[j,'Additional_Performance']>=l4[k]) and ((P.loc[j,'POS_RES%']>=BKT4T.loc[l-1,'TARGET']) and (P.loc[j,'POS_RES%']<BKT4T.loc[l,'TARGET'])):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*BKT4.loc[l-1,l4[k]]/100
                                        A.loc[i,'percentage']=str(BKT4.loc[l-1,l4[k]])+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],BKT4.loc[l-1,l4[k]],A.loc[i,'MOHAK'])
                                    elif (A.loc[i,'STATUS']=="FORECLOSE" or A.loc[i,'STATUS']=='SETTLEMENT'):
                                        c=A.loc[i,'Billing PAID AMT.']*15/100
                                        A.loc[i,'percentage']=str(15)+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],BKT4.loc[l-1,l4[k]],A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'percentage']=str(BKT4.loc[l,l4[k]])+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],BKT4.loc[l,l4[k]],A.loc[i,'MOHAK'])
                            elif k==6 and l==9:
                                if A.loc[i,'STATUS']=='RT':
                                    A.loc[i,'MOHAK']=150
                                elif (P.loc[j,'Additional_Performance']>=l4[k]) and P.loc[j,'POS_RES%']>=BKT4T.loc[l,'TARGET']:
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*BKT4.loc[l,l4[k]]/100
                                        A.loc[i,'percentage']=str(BKT4.loc[l,l4[k]])+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],BKT4.loc[l,l4[k]],A.loc[i,'MOHAK'])
                                    elif (A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT'):
                                        c=A.loc[i,'Billing PAID AMT.']*15/100
                                        A.loc[i,'percentage']=str(15)+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],str(15),A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'percentage']=str(BKT4.loc[l,l4[k]])+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],BKT4.loc[l,l4[k]],A.loc[i,'MOHAK'])
                            elif k>0 and l==0:
                                if A.loc[i,'STATUS']=='RT':
                                    A.loc[i,'MOHAK']=150
                                elif (P.loc[j,'Additional_Performance']>l4[k-1] and P.loc[j,'Additional_Performance']<=l4[k]) and (P.loc[j,'POS_RES%']<=BKT4T.loc[l,'TARGET']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*BKT4.loc[l,l4[k-1]]/100
                                        A.loc[i,'percentage']=str(BKT4.loc[l,l4[k-1]])+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],BKT4.loc[l,l4[k-1]],A.loc[i,'MOHAK'])
                                    elif (A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT'):
                                        c=A.loc[i,'Billing PAID AMT.']*15/100
                                        A.loc[i,'percentage']=str(15)+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],str(15),A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'percentage']=str(BKT4.loc[l,l4[k]])+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],BKT4.loc[l,l4[k]],A.loc[i,'MOHAK'])
                            elif k>0 and l>0:
                                if (P.loc[j,'Additional_Performance']>l4[k-1] and P.loc[j,'Additional_Performance']<=l4[k]) and (P.loc[j,'POS_RES%']>BKT4T.loc[l-1,'TARGET'] and P.loc[j,'POS_RES%']<=BKT4T.loc[l,'TARGET']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*BKT4.loc[l-1,l4[k-1]]/100
                                        A.loc[i,'percentage']=str(BKT4.loc[l-1,l4[k-1]])+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],BKT4.loc[l-1,l4[k-1]],A.loc[i,'MOHAK'])
                                    elif (A.loc[i,'STATUS']=='SETTLEMENT' or A.loc[i,'STATUS']=='FORECLOSE'):
                                        c=A.loc[i,'Billing PAID AMT.']*15/100
                                        A.loc[i,'percentage']=str(15)+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],str(15),A.loc[i,'MOHAK'])                                        
                                    else:
                                        A.loc[i,'percentage']=str(BKT4.loc[l,l4[k]])+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],BKT4.loc[l,l4[k]],A.loc[i,'MOHAK'])


# =============================================================================
# BKT-5
# =============================================================================

for j in range(0,len(P['BKT'])):
    if P.loc[j,'BKT']==5:
        for i in range(0,len(A['BKT'])):
            if A.loc[i,'BKT']==5:
                for k in range(0,len(l5)):
                    for l in range(0,len(BKT5)):
                            if k==0 and l==0:
                                if A.loc[i,'STATUS']=='RT':
                                    A.loc[i,'MOHAK']=150
                                elif P.loc[j,'Additional_Performance']<=l5[k] and P.loc[j,'POS_RES%']<=BKT5T.loc[l,'TARGET']:
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        a=A.loc[i,'Billing PAID AMT.']*BKT5.loc[l,l5[k]]/100
                                        A.loc[i,'percentage']=str(BKT5.loc[l,l5[k]])+'%'
                                        A.loc[i,'MOHAK']=a
                                        print(A.loc[i,'AGREEMENTID'],BKT5.loc[l,l5[k]],A.loc[i,'MOHAK'])
                                    elif (A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT'):
                                        a=A.loc[i,'Billing PAID AMT.']*15/100
                                        A.loc[i,'percentage']=str(15)+'%'
                                        A.loc[i,'MOHAK']=a
                                        print(A.loc[i,'AGREEMENTID'],str(15),A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'percentage']=str(BKT5.loc[l,l5[k]])+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],BKT5.loc[l,l5[k]],A.loc[i,'MOHAK'])
                            elif k==6 and l==0:
                                if A.loc[i,'STATUS']=='RT':
                                    A.loc[i,'MOHAK']=150
                                elif ((P.loc[j,'Additional_Performance']>=l5[k-1]) and (P.loc[j,'Additional_Performance']<l5[k])) and P.loc[j,'POS_RES%']<=BKT5T.loc[l,'TARGET']:
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*BKT5.loc[l,l5[k-1]]/100
                                        A.loc[i,'percentage']=str(BKT5.loc[l,l5[k-1]])+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],BKT5.loc[l,l5[k-1]],A.loc[i,'MOHAK'])
                                    elif (A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT'):
                                        c=A.loc[i,'Billing PAID AMT.']*BKT5.loc[l,l5[k-1]]/100
                                        A.loc[i,'percentage']=str(15)+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],str(15),A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'percentage']=str(BKT5.loc[l,l5[k]])+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],BKT5.loc[l,l5[k]],A.loc[i,'MOHAK'])
                                elif (P.loc[j,'Additional_Performance']>=int(l5[k])) and (P.loc[j,'POS_RES%']<=BKT5T.loc[l,'TARGET']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*BKT5.loc[l,l5[k]]/100
                                        A.loc[i,'percentage']=str(BKT5.loc[l,l5[k]])+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],BKT5.loc[l,l5[k]],A.loc[i,'MOHAK'])
                                    elif (A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT'):
                                        c=A.loc[i,'Billing PAID AMT.']*BKT5.loc[l,l5[k]]/100
                                        A.loc[i,'percentage']=str(15)+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],BKT5.loc[l,l5[k]],A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'percentage']=str(BKT5.loc[l,l5[k]])+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],BKT5.loc[l,l5[k]],A.loc[i,'MOHAK'])
                            elif k==0 and l>0:
                                if A.loc[i,'STATUS']=='RT':
                                    A.loc[i,'MOHAK']=150
                                elif (P.loc[j,'Additional_Performance']<=l5[k]) and ((P.loc[j,'POS_RES%']>=BKT5T.loc[l-1,'TARGET']) and (P.loc[j,'POS_RES%']<BKT5T.loc[l,'TARGET'])):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*BKT5.loc[l,l5[k]]/100
                                        A.loc[i,'percentage']=str(BKT5.loc[l,l5[k]])+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],BKT5.loc[l,l5[k]],A.loc[i,'MOHAK'])
                                    elif (A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT'):
                                        c=A.loc[i,'Billing PAID AMT.']*15/100
                                        A.loc[i,'percentage']=str(15)+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],str(15),A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'percentage']=str(BKT5.loc[l,l5[k]])+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],BKT5.loc[l,l5[k]],A.loc[i,'MOHAK'])
                                elif (P.loc[j,'Additional_Performance']>=l5[k]) and P.loc[j,'POS_RES%']<=BKT5T.loc[l,'TARGET']:
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*BKT5.loc[l,l5[k]]/100
                                        A.loc[i,'percentage']=str(BKT5.loc[l,l5[k]])+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],BKT5.loc[l,l5[k]],A.loc[i,'MOHAK'])
                                    elif (A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT'):
                                        c=A.loc[i,'Billing PAID AMT.']*15/100
                                        A.loc[i,'percentage']=str(15)+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],str(15),A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'percentage']=str(BKT5.loc[l,l5[k]])+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],BKT5.loc[l,l5[k]],A.loc[i,'MOHAK'])
                            elif k==6 and l>0:
                                if A.loc[i,'STATUS']=='RT':
                                    A.loc[i,'MOHAK']=150
                                elif ((P.loc[j,'Additional_Performance']>=l5[k-1]) and (P.loc[j,'Additional_Performance']<l5[k])) and ((P.loc[j,'POS_RES%']>=BKT5T.loc[l-1,'TARGET']) and (P.loc[j,'POS_RES%']<BKT5T.loc[l,'TARGET'])):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*BKT5.loc[l-1,l5[k-1]]/100
                                        A.loc[i,'percentage']=str(BKT5.loc[l-1,l5[k-1]])+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],BKT5.loc[l-1,l5[k-1]],A.loc[i,'MOHAK'])
                                    elif (A.loc[i,'STATUS']=='SETTLEMENT' or A.loc[i,'STATUS']=='FORECLOSE'):
                                        c=A.loc[i,'Billing PAID AMT.']*BKT5.loc[l-1,l5[k-1]]/100
                                        A.loc[i,'percentage']=str(15)+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],BKT5.loc[l-1,l5[k-1]],A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'percentage']=str(BKT5.loc[l,l5[k]])+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],BKT5.loc[l,l5[k]],A.loc[i,'MOHAK'])
                                elif (P.loc[j,'Additional_Performance']>=l5[k]) and ((P.loc[j,'POS_RES%']>=BKT5T.loc[l-1,'TARGET']) and (P.loc[j,'POS_RES%']<BKT5T.loc[l,'TARGET'])):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*BKT5.loc[l-1,l4[k]]/100
                                        A.loc[i,'percentage']=str(BKT5.loc[l-1,l5[k]])+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],BKT5.loc[l-1,l5[k]],A.loc[i,'MOHAK'])
                                    elif (A.loc[i,'STATUS']=="FORECLOSE" or A.loc[i,'STATUS']=='SETTLEMENT'):
                                        c=A.loc[i,'Billing PAID AMT.']*15/100
                                        A.loc[i,'percentage']=str(15)+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],BKT5.loc[l-1,l5[k]],A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'percentage']=str(BKT5.loc[l,l5[k]])+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],BKT5.loc[l,l5[k]],A.loc[i,'MOHAK'])
                            elif k==6 and l==9:
                                if A.loc[i,'STATUS']=='RT':
                                    A.loc[i,'MOHAK']=150
                                elif (P.loc[j,'Additional_Performance']>=l5[k]) and P.loc[j,'POS_RES%']>=BKT5T.loc[l,'TARGET']:
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*BKT5.loc[l,l5[k]]/100
                                        A.loc[i,'percentage']=str(BKT5.loc[l,l5[k]])+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],BKT5.loc[l,l5[k]],A.loc[i,'MOHAK'])
                                    elif (A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT'):
                                        c=A.loc[i,'Billing PAID AMT.']*15/100
                                        A.loc[i,'percentage']=str(15)+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],str(15),A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'percentage']=str(BKT5.loc[l,l5[k]])+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],BKT5.loc[l,l5[k]],A.loc[i,'MOHAK'])
                            elif k>0 and l==0:
                                if A.loc[i,'STATUS']=='RT':
                                    A.loc[i,'MOHAK']=150
                                elif (P.loc[j,'Additional_Performance']>l5[k-1] and P.loc[j,'Additional_Performance']<=l5[k]) and (P.loc[j,'POS_RES%']<=BKT5T.loc[l,'TARGET']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*BKT5.loc[l,l5[k-1]]/100
                                        A.loc[i,'percentage']=str(BKT5.loc[l,l5[k-1]])+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],BKT5.loc[l,l5[k-1]],A.loc[i,'MOHAK'])
                                    elif (A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT'):
                                        c=A.loc[i,'Billing PAID AMT.']*15/100
                                        A.loc[i,'percentage']=str(15)+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],str(15),A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'percentage']=str(BKT5.loc[l,l5[k]])+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],BKT5.loc[l,l5[k]],A.loc[i,'MOHAK'])
                            elif k>0 and l>0:
                                if (P.loc[j,'Additional_Performance']>l5[k-1] and P.loc[j,'Additional_Performance']<=l5[k]) and (P.loc[j,'POS_RES%']>BKT5T.loc[l-1,'TARGET'] and P.loc[j,'POS_RES%']<=BKT5T.loc[l,'TARGET']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*BKT5.loc[l-1,l5[k-1]]/100
                                        A.loc[i,'percentage']=str(BKT5.loc[l-1,l5[k-1]])+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],BKT5.loc[l-1,l5[k-1]],A.loc[i,'MOHAK'])
                                    elif (A.loc[i,'STATUS']=='SETTLEMENT' or A.loc[i,'STATUS']=='FORECLOSE'):
                                        c=A.loc[i,'Billing PAID AMT.']*15/100
                                        A.loc[i,'percentage']=str(15)+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],str(15),A.loc[i,'MOHAK'])                                        
                                    else:
                                        A.loc[i,'percentage']=str(BKT5.loc[l,l5[k]])+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],BKT5.loc[l,l5[k]],A.loc[i,'MOHAK'])


# =============================================================================
# BKT-6
# =============================================================================

for j in range(0,len(P['BKT'])):
    if P.loc[j,'BKT']==6:
        for i in range(0,len(A['BKT'])):
            if A.loc[i,'BKT']==6:
                for k in range(0,len(l6)):
                    for l in range(0,len(BKT6)):
                            if k==0 and l==0:
                                if A.loc[i,'STATUS']=='RT':
                                    A.loc[i,'MOHAK']=150
                                elif P.loc[j,'Additional_Performance']<=l6[k] and P.loc[j,'POS_RES%']<=BKT6T.loc[l,'TARGET']:
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        a=A.loc[i,'Billing PAID AMT.']*BKT6.loc[l,l6[k]]/100
                                        A.loc[i,'percentage']=str(BKT6.loc[l,l6[k]])+'%'
                                        A.loc[i,'MOHAK']=a
                                        print(A.loc[i,'AGREEMENTID'],BKT6.loc[l,l6[k]],A.loc[i,'MOHAK'])
                                    elif (A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT'):
                                        a=A.loc[i,'Billing PAID AMT.']*20/100
                                        A.loc[i,'percentage']=str(20)+'%'
                                        A.loc[i,'MOHAK']=a
                                        print(A.loc[i,'AGREEMENTID'],20,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'percentage']=str(BKT6.loc[l,l6[k]])+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],BKT6.loc[l,l6[k]],A.loc[i,'MOHAK'])
                            elif k==6 and l==0:
                                if A.loc[i,'STATUS']=='RT':
                                    A.loc[i,'MOHAK']=150
                                elif ((P.loc[j,'Additional_Performance']>=l6[k-1]) and (P.loc[j,'Additional_Performance']<l6[k])) and P.loc[j,'POS_RES%']<=BKT6T.loc[l,'TARGET']:
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*BKT6.loc[l,l6[k-1]]/100
                                        A.loc[i,'percentage']=str(BKT6.loc[l,l6[k-1]])+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],BKT6.loc[l,l6[k-1]],A.loc[i,'MOHAK'])
                                    elif (A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT'):
                                        c=A.loc[i,'Billing PAID AMT.']*20/100
                                        A.loc[i,'percentage']=str(20)+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],20,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'Percentage']=str(BKT6.loc[l,l6[k]])+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],BKT6.loc[l,l6[k]],A.loc[i,'MOHAK'])
                                elif (P.loc[j,'Additional_Performance']>=l1[k]) and P.loc[j,'POS_RES%']<=BKT6T.loc[l,'TARGET']:
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'): 
                                        c=A.loc[i,'Billing PAID AMT.']*BKT6.loc[l,l6[k]]/100
                                        A.loc[i,'percentage']=str(BKT6.loc[l,l6[k]])+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],BKT6.loc[l,l6[k]],A.loc[i,'MOHAK'])
                                    elif (A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT'):
                                        c=A.loc[i,'Billing PAID AMT.']*20/100
                                        A.loc[i,'percentage']=str(20)+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],20,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'percentage']=str(BKT6.loc[l,l6[k]])+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],BKT6.loc[l,l6[k]],A.loc[i,'MOHAK'])
                            elif k==6 and l>0:
                                if A.loc[i,'STATUS']=='RT':
                                    A.loc[i,'MOHAK']=150
                                elif ((P.loc[j,'Additional_Performance']>=l6[k-1]) and (P.loc[j,'Additional_Performance']<l6[k])) and ((P.loc[j,'POS_RES%']>=BKT6T.loc[l-1,'TARGET']) and (P.loc[j,'POS_RES%']<BKT6T.loc[l,'TARGET'])):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'): 
                                        c=A.loc[i,'Billing PAID AMT.']*BKT6.loc[l-1,l6[k-1]]/100
                                        A.loc[i,'percentage']=str(BKT6.loc[l-1,l6[k-1]])+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],BKT6.loc[l-1,l6[k-1]],A.loc[i,'MOHAK'])
                                    elif (A.loc[i,'STATUS']=='SETTLEMENT' or A.loc[i,'STATUS']=='FORECLOSE'):
                                        c=A.loc[i,'Billing PAID AMT.']*20/100
                                        A.loc[i,'percentage']=str(20)+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],20,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'Percentage']=str(BKT6.loc[l,l6[k]])+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],BKT6.loc[l,l6[k]],A.loc[i,'MOHAK'])
                                elif (P.loc[j,'Additional_Performance']>=l6[k]) and ((P.loc[j,'POS_RES%']>=BKT6T.loc[l-1,'TARGET']) and (P.loc[j,'POS_RES%']<BKT6T.loc[l,'TARGET'])):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*BKT6.loc[l-1,l6[k]]/100
                                        A.loc[i,'percentage']=str(BKT6.loc[l-1,l6[k]])+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],BKT6.loc[l-1,l6[k]],A.loc[i,'MOHAK'])
                                    elif (A.loc[i,'STATUS']=="FORECLOSE" or A.loc[i,'STATUS']=='SETTLEMENT'):
                                        c=A.loc[i,'Billing PAID AMT.']*20/100
                                        A.loc[i,'percentage']=str(20)+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],20,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'percentage']=str(BKT6.loc[l,l6[k]])+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],BKT6.loc[l,l6[k]],A.loc[i,'MOHAK'])
                            elif k==6 and l==6:
                                if A.loc[i,'STATUS']=='RT':
                                    A.loc[i,'MOHAK']=150
                                elif (P.loc[j,'Additional_Performance']>=l6[k]) and P.loc[j,'POS_RES%']>=BKT6T.loc[l,'TARGET']:
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                        c=A.loc[i,'Billing PAID AMT.']*BKT6.loc[l,l6[k]]/100
                                        A.loc[i,'percentage']=str(BKT6.loc[l,l6[k]])+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],BKT6.loc[l,l6[k]],A.loc[i,'MOHAK'])
                                    elif (A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT'):
                                        c=A.loc[i,'Billing PAID AMT.']*20/100
                                        A.loc[i,'percentage']=str(20)+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],20,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'percentage']=str(BKT6.loc[l,l6[k]])+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],BKT6.loc[l,l6[k]],A.loc[i,'MOHAK'])
                            elif k>0 and l==0:
                                if A.loc[i,'STATUS']=='RT':
                                    A.loc[i,'MOHAK']=150
                                elif (P.loc[j,'Additional_Performance']>l6[k-1] and P.loc[j,'Additional_Performance']<=l6[k]) and (P.loc[j,'POS_RES%']<=BKT6T.loc[l,'TARGET']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'): 
                                        c=A.loc[i,'Billing PAID AMT.']*BKT6.loc[l,l6[k-1]]/100
                                        A.loc[i,'percentage']=str(BKT6.loc[l,l6[k-1]])+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],BKT6.loc[l,l6[k-1]],A.loc[i,'MOHAK'])
                                    elif (A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT'):
                                        c=A.loc[i,'Billing PAID AMT.']*20/100
                                        A.loc[i,'percentage']=str(20)+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],20,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'percentage']=str(BKT6.loc[l,l6[k]])+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],BKT6.loc[l,l6[k]],A.loc[i,'MOHAK'])
                            elif k>0 and l>0:
                                if (P.loc[j,'Additional_Performance']>l6[k-1] and P.loc[j,'Additional_Performance']<=l1[k]) and (P.loc[j,'POS_RES%']>BKT6T.loc[l-1,'TARGET'] and P.loc[j,'POS_RES%']<=BKT6T.loc[l,'TARGET']):
                                    if (A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'): 
                                        c=A.loc[i,'Billing PAID AMT.']*BKT6.loc[l-1,l6[k-1]]/100
                                        A.loc[i,'percentage']=str(BKT6.loc[l-1,l6[k-1]])+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],BKT6.loc[l-1,l6[k-1]],A.loc[i,'MOHAK'])
                                    elif (A.loc[i,'STATUS']=='SETTLEMENT' or A.loc[i,'STATUS']=='FORECLOSE'):
                                        c=A.loc[i,'Billing PAID AMT.']*20/100
                                        A.loc[i,'percentage']=str(20)+'%'
                                        A.loc[i,'MOHAK']=c
                                        print(A.loc[i,'AGREEMENTID'],20,A.loc[i,'MOHAK'])
                                    else:
                                        A.loc[i,'percentage']=str(BKT6.loc[l,l6[k]])+'%'
                                        A.loc[i,'MOHAK']=0
                                        print(A.loc[i,'AGREEMENTID'],BKT6.loc[l,l6[k]],A.loc[i,'MOHAK'])

A.rename({'MOHAK':'PAYOUT'},axis=1,inplace=True)

A.to_excel(r'/Users/mohaksehgal/Documents/Work/FOS Salary/IDFC TW/JUN 21/MASTER FILE IDFC TW.xlsx',index=False)

A.to_excel(r'/Users/mohaksehgal/Documents/Work/Billing/IDFC TW/IDFC TW Jun 21/Final Billing TW.xlsx',index=False)