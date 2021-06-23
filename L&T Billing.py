#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 07:45:28 2020

@author: mohaksehgal
"""


import pandas as pd
import numpy as np

A=pd.read_excel(r"/Users/mohaksehgal/Documents/Work/Billing/L_T/L_T JUN 21/MASTER FILE L_T.xlsx")

P=pd.read_excel(r'/Users/mohaksehgal/Documents/Work/Billing/L_T/L_T JUN 21/Performance L_T.xlsx')

PA=pd.read_excel(r'/Users/mohaksehgal/Documents/Work/Billing/L_T/Payout.xlsx')
R=pd.read_excel(r'/Users/mohaksehgal/Documents/Work/Billing/L_T/Resolution.xlsx')

APA=pd.read_excel(r'/Users/mohaksehgal/Documents/Work/Billing/L_T/AddPayout.xlsx')

AR=pd.read_excel(r'/Users/mohaksehgal/Documents/Work/Billing/L_T/AddResolution.xlsx')

l1=R.columns

# =============================================================================
# BKT 1
# =============================================================================

for i in range(0,len(A['BKT'])):
    if A.loc[i,'BKT']==1:
        for j in range(0,len(P['BKT'])):
            if (A.loc[i,'BKT']==P.loc[j,'BKT']):
                for k in range(0,len(l1)):
                    if l1[k]==A.loc[i,'BKT']:
                        for l in range(0,len(PA[1])):
                             for y in range(0,len(APA[1])):
                                if l==0:
                                    if P.loc[j,'POS_RES%']<=R.loc[l,l1[k]] and (P.loc[j,'Additional_Performance']<AR.loc[y,l1[k]]):
                                        if A.loc[i,'STATUS']=='SB' or (A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                            a=A.loc[i,'Billing PAID AMT.']*PA.loc[l,l1[k]]/100
                                            A.loc[i,'PERCENTAGE']=str(PA.loc[l,l1[k]])+'%'
                                            A.loc[i,'MOHAK']=a
                                            print(A.loc[i,'AGREEMENTID'],A.loc[i,'BKT'],P.loc[j,'POS_RES%'],A.loc[i,'Billing PAID AMT.'],PA.loc[l,l1[k]],a,P.loc[j,'BKT'])
# =============================================================================
#                                         elif (A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
#                                             a=(A.loc[i,'Billing PAID AMT.']*PA.loc[l,l1[k]]/100)+APA[1]
#                                             A.loc[i,'PERCENTAGE']=str(PA.loc[l,l1[k]])+'%'
#                                             A.loc[i,'MOHAK']=a
#                                             print(A.loc[i,'AGREEMENTID'],A.loc[i,'BKT'],P.loc[j,'POS_RES%'],A.loc[i,'Billing PAID AMT.'],PA.loc[l,l1[k]],a,P.loc[j,'BKT'])
# =============================================================================
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(PA.loc[l,l1[k]])+'%'
                                            A.loc[i,'MOHAK']=0
                                            print(A.loc[i,'AGREEMENTID'],A.loc[i,'BKT'],P.loc[j,'POS_RES%'],A.loc[i,'Billing PAID AMT.'],PA.loc[l,l1[k]],0,P.loc[j,'BKT'])
                                elif l>0:
                                     if (P.loc[j,'POS_RES%']>R.loc[l-1,l1[k]] and P.loc[j,'POS_RES%']<=R.loc[l,l1[k]]) and (P.loc[j,'Additional_Performance']<AR.loc[y,l1[k]]):
# =============================================================================
#                                          if (A.loc[i,'STATUS']=='RB') or (A.loc[i,'STATUS']=='NM'):
#                                              c=(A.loc[i,'Billing PAID AMT.']*PA.loc[l,l1[k]]/100)+APA[1]
#                                              A.loc[i,'PERCENTAGE']=str(PA.loc[l,l1[k]])+'%'
#                                              A.loc[i,'MOHAK']=int(c)
#                                              print(A.loc[i,'AGREEMENTID'],A.loc[i,'BKT'],P.loc[j,'POS_RES%'],A.loc[i,'Billing PAID AMT.'],PA.loc[l-1,l1[k]],c,P.loc[j,'BKT'])
# =============================================================================
                                        if A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='NM' or A.loc[i,'STATUS']=='RB':
                                            d=A.loc[i,'Billing PAID AMT.']*(PA.loc[l,l1[k]])/100
                                            A.loc[i,'PERCENTAGE']=str(PA.loc[l,l1[k]])+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],A.loc[i,'BKT'],P.loc[j,'POS_RES%'],A.loc[i,'Billing PAID AMT.'],PA.loc[l,l1[k]],d,P.loc[j,'BKT'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(PA.loc[l,l1[k]])+'%'
                                            A.loc[i,'MOHAK']=0
                                            print(A.loc[i,'AGREEMENTID'],A.loc[i,'BKT'],P.loc[j,'POS_RES%'],A.loc[i,'Billing PAID AMT.'],PA.loc[l,l1[k]],0,P.loc[j,'BKT'])
                                elif l==6:
                                    if ((P.loc[j,'POS_RES%']>R.loc[l-1,l1[k]]) and (P.loc[j,'POS_RES%']<=R.loc[l,l1[k]])) and \
                                    ((P.loc[j,'Additional_Performance']>AR.loc[y-1,l1[k]]) and (P.loc[j,'Additional_Performance']<=AR.loc[y,l1[k]])):                                        
                                        if (A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                            c=A.loc[i,'Billing PAID AMT.']*(PA.loc[l,l1[k]]+APA.loc[y-1,l1[k]])/100
                                            A.loc[i,'PERCENTAGE']=str(PA.loc[l,l1[k]]+APA.loc[y-1,l1[k]])+'%'
                                            A.loc[i,'MOHAK']=c
                                            print(A.loc[i,'AGREEMENTID'],A.loc[i,'AGREEMENTID'],A.loc[i,'BKT'],P.loc[j,'POS_RES%'],A.loc[i,'Billing PAID AMT.'],PA.loc[l-1,l1[k]],APA.loc[y,l1[k]],c,P.loc[j,'BKT'])
                                        elif A.loc[i,'STATUS']=='SB':
                                            d=A.loc[i,'Billing PAID AMT.']*(PA.loc[l,l1[k]])/100
                                            A.loc[i,'PERCENTAGE']=str(PA.loc[l,l1[k]])+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],A.loc[i,'BKT'],P.loc[j,'POS_RES%'],A.loc[i,'Billing PAID AMT.'],PA.loc[l,l1[k]],APA.loc[y,l1[k]],d,P.loc[j,'BKT'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(PA.loc[l,l1[k]])+'%'
                                            A.loc[i,'MOHAK']=0
                                            print(A.loc[i,'AGREEMENTID'],A.loc[i,'BKT'],P.loc[j,'POS_RES%'],A.loc[i,'Billing PAID AMT.'],PA.loc[l,l1[k]],APA.loc[y,l1[k]],0,P.loc[j,'BKT'])


# =============================================================================
# BKT 2
# =============================================================================

for i in range(0,len(A['BKT'])):
    if A.loc[i,'BKT']==2:
        for j in range(0,len(P['BKT'])):
            if (A.loc[i,'BKT']==P.loc[j,'BKT']):
                for k in range(0,len(l1)):
                    if l1[k]==A.loc[i,'BKT']:
                        for l in range(0,len(PA[2])):
                            for y in range(0,len(APA[1])):
                                if l==0:
                                    if P.loc[j,'POS_RES%']<=R.loc[l,l1[k]] and (P.loc[j,'Additional_Performance']<AR.loc[y,l1[k]]):
                                        if A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM':
                                            a=A.loc[i,'Billing PAID AMT.']*PA.loc[l,l1[k]]/100
                                            A.loc[i,'PERCENTAGE']=str(PA.loc[l,l1[k]])+'%'
                                            A.loc[i,'MOHAK']=a
                                            print(A.loc[i,'AGREEMENTID'],A.loc[i,'BKT'],P.loc[j,'POS_RES%'],A.loc[i,'Billing PAID AMT.'],PA.loc[l,l1[k]],a,P.loc[j,'BKT'])
# =============================================================================
#                                         elif (A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
#                                             a=(A.oc[i,'Billing PAID AMT.']*PA.loc[l,l1[k]]/100)+APA[2]
#                                             A.loc[i,'PERCENTAGE']=str(PA.loc[l,l1[k]])+'%'
#                                             A.loc[i,'MOHAK']=a
#                                             print(A.loc[i,'AGREEMENTID'],A.loc[i,'BKT'],P.loc[j,'POS_RES%'],A.loc[i,'Billing PAID AMT.'],PA.loc[l,l1[k]],a,P.loc[j,'BKT'])
# =============================================================================
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(PA.loc[l,l1[k]])+'%'
                                            A.loc[i,'MOHAK']=0
                                            print(A.loc[i,'AGREEMENTID'],A.loc[i,'BKT'],P.loc[j,'POS_RES%'],A.loc[i,'Billing PAID AMT.'],PA.loc[l,l1[k]],0,P.loc[j,'BKT'])
                                elif l>0:
                                    if ((P.loc[j,'POS_RES%']>R.loc[l-1,l1[k]]) and (P.loc[j,'POS_RES%']<=R.loc[l,l1[k]])) and (P.loc[j,'Additional_Performance']<AR.loc[y,l1[k]]):                                        
# =============================================================================
#                                         if (A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
#                                             c=(A.loc[i,'Billing PAID AMT.']*(PA.loc[l,l1[k]])/100)+APA[2]
#                                             A.loc[i,'PERCENTAGE']=str(PA.loc[l,l1[k]])+'%'
#                                             A.loc[i,'MOHAK']=int(c)
#                                             print(A.loc[i,'AGREEMENTID'],A.loc[i,'BKT'],P.loc[j,'POS_RES%'],A.loc[i,'Billing PAID AMT.'],PA.loc[l-1,l1[k]],c,P.loc[j,'BKT'])
# =============================================================================
                                        if A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='NM' or A.loc[i,'STATUS']=='RB':
                                            d=A.loc[i,'Billing PAID AMT.']*(PA.loc[l,l1[k]])/100
                                            A.loc[i,'PERCENTAGE']=str(PA.loc[l,l1[k]])+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],A.loc[i,'BKT'],P.loc[j,'POS_RES%'],A.loc[i,'Billing PAID AMT.'],PA.loc[l-1,l1[k]],d,P.loc[j,'BKT'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(PA.loc[l,l1[k]])+'%'
                                            A.loc[i,'MOHAK']=0
                                            print(A.loc[i,'AGREEMENTID'],A.loc[i,'BKT'],P.loc[j,'POS_RES%'],A.loc[i,'Billing PAID AMT.'],PA.loc[l,l1[k]],0,P.loc[j,'BKT'])
                                # elif l>0:
                                #     if ((P.loc[j,'POS_RES%']>R.loc[l-1,l1[k]]) and (P.loc[j,'POS_RES%']<=R.loc[l,l1[k]])) and \
                                #     ((P.loc[j,'Additional_Performance']>AR.loc[y-1,l1[k]]) and (P.loc[j,'Additional_Performance']<=AR.loc[y,l1[k]])):                                        
                                #         if (A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                #             c=A.loc[i,'Billing PAID AMT.']*(PA.loc[l,l1[k]]+APA.loc[y-1,l1[k]])/100
                                #             A.loc[i,'PERCENTAGE']=str(PA.loc[l,l1[k]]+APA.loc[y-1,l1[k]])+'%'
                                #             A.loc[i,'MOHAK']=c
                                #             print(A.loc[i,'AGREEMENTID'],A.loc[i,'AGREEMENTID'],A.loc[i,'BKT'],P.loc[j,'POS_RES%'],A.loc[i,'Billing PAID AMT.'],PA.loc[l-1,l1[k]],APA.loc[y,l1[k]],c,P.loc[j,'BKT'])
                                #         elif A.loc[i,'STATUS']=='SB':
                                #             d=A.loc[i,'Billing PAID AMT.']*(PA.loc[l,l1[k]])/100
                                #             A.loc[i,'PERCENTAGE']=str(PA.loc[l,l1[k]])+'%'
                                #             A.loc[i,'MOHAK']=d
                                #             print(A.loc[i,'AGREEMENTID'],A.loc[i,'BKT'],P.loc[j,'POS_RES%'],A.loc[i,'Billing PAID AMT.'],PA.loc[l,l1[k]],APA.loc[y,l1[k]],d,P.loc[j,'BKT'])
                                #         else:
                                #             A.loc[i,'PERCENTAGE']=str(PA.loc[l,l1[k]])+'%'
                                #             A.loc[i,'MOHAK']=0
                                #             print(A.loc[i,'AGREEMENTID'],A.loc[i,'BKT'],P.loc[j,'POS_RES%'],A.loc[i,'Billing PAID AMT.'],PA.loc[l,l1[k]],APA.loc[y,l1[k]],0,P.loc[j,'BKT'])

# =============================================================================
# BKT 3
# =============================================================================

for i in range(0,len(A['BKT'])):
    if A.loc[i,'BKT']==3:
        for j in range(0,len(P['BKT'])):
            if (A.loc[i,'BKT']==P.loc[j,'BKT']):
                for k in range(0,len(l1)):
                    if l1[k]==A.loc[i,'BKT']:
                        for l in range(0,len(PA[3])):
                            for y in range(0,len(APA[1])):
                                if l==0:
                                    if P.loc[j,'POS_RES%']<=R.loc[l,l1[k]] and (P.loc[j,'Additional_Performance']<AR.loc[y,l1[k]]):
                                        if A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM':
                                            a=A.loc[i,'Billing PAID AMT.']*PA.loc[l,l1[k]]/100
                                            A.loc[i,'PERCENTAGE']=str(PA.loc[l,l1[k]])+'%'
                                            A.loc[i,'MOHAK']=a
                                            print(A.loc[i,'AGREEMENTID'],A.loc[i,'BKT'],P.loc[j,'POS_RES%'],A.loc[i,'Billing PAID AMT.'],PA.loc[l,l1[k]],a,P.loc[j,'BKT'])
# =============================================================================
#                                         elif (A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
#                                             a=(A.oc[i,'Billing PAID AMT.']*PA.loc[l,l1[k]]/100)+APA[2]
#                                             A.loc[i,'PERCENTAGE']=str(PA.loc[l,l1[k]])+'%'
#                                             A.loc[i,'MOHAK']=a
#                                             print(A.loc[i,'AGREEMENTID'],A.loc[i,'BKT'],P.loc[j,'POS_RES%'],A.loc[i,'Billing PAID AMT.'],PA.loc[l,l1[k]],a,P.loc[j,'BKT'])
# =============================================================================
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(PA.loc[l,l1[k]])+'%'
                                            A.loc[i,'MOHAK']=0
                                            print(A.loc[i,'AGREEMENTID'],A.loc[i,'BKT'],P.loc[j,'POS_RES%'],A.loc[i,'Billing PAID AMT.'],PA.loc[l,l1[k]],0,P.loc[j,'BKT'])
                                elif l>0:
                                    if ((P.loc[j,'POS_RES%']>R.loc[l-1,l1[k]]) and (P.loc[j,'POS_RES%']<=R.loc[l,l1[k]])) and (P.loc[j,'Additional_Performance']<AR.loc[y,l1[k]]):                                        
# =============================================================================
#                                         if (A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
#                                             c=(A.loc[i,'Billing PAID AMT.']*(PA.loc[l,l1[k]])/100)+APA[2]
#                                             A.loc[i,'PERCENTAGE']=str(PA.loc[l,l1[k]])+'%'
#                                             A.loc[i,'MOHAK']=int(c)
#                                             print(A.loc[i,'AGREEMENTID'],A.loc[i,'BKT'],P.loc[j,'POS_RES%'],A.loc[i,'Billing PAID AMT.'],PA.loc[l-1,l1[k]],c,P.loc[j,'BKT'])
# =============================================================================
                                        if A.loc[i,'STATUS']=='SB' or A.loc[i,'STATUS']=='NM' or A.loc[i,'STATUS']=='RB':
                                            d=A.loc[i,'Billing PAID AMT.']*(PA.loc[l,l1[k]])/100
                                            A.loc[i,'PERCENTAGE']=str(PA.loc[l,l1[k]])+'%'
                                            A.loc[i,'MOHAK']=d
                                            print(A.loc[i,'AGREEMENTID'],A.loc[i,'BKT'],P.loc[j,'POS_RES%'],A.loc[i,'Billing PAID AMT.'],PA.loc[l-1,l1[k]],d,P.loc[j,'BKT'])
                                        else:
                                            A.loc[i,'PERCENTAGE']=str(PA.loc[l,l1[k]])+'%'
                                            A.loc[i,'MOHAK']=0
                                            print(A.loc[i,'AGREEMENTID'],A.loc[i,'BKT'],P.loc[j,'POS_RES%'],A.loc[i,'Billing PAID AMT.'],PA.loc[l,l1[k]],0,P.loc[j,'BKT'])
                                # elif l>0 and y>0:
                                #     if ((P.loc[j,'POS_RES%']>R.loc[l-1,l1[k]]) and (P.loc[j,'POS_RES%']<=R.loc[l,l1[k]])) and \
                                #     ((P.loc[j,'Additional_Performance']>AR.loc[y-1,l1[k]]) and (P.loc[j,'Additional_Performance']<=AR.loc[y,l1[k]])):                                        
                                #         if (A.loc[i,'STATUS']=='RB' or A.loc[i,'STATUS']=='NM'):
                                #             c=A.loc[i,'Billing PAID AMT.']*(PA.loc[l,l1[k]]+APA.loc[y-1,l1[k]])/100
                                #             A.loc[i,'PERCENTAGE']=str(PA.loc[l,l1[k]]+APA.loc[y-1,l1[k]])+'%'
                                #             A.loc[i,'MOHAK']=c
                                #             print(A.loc[i,'AGREEMENTID'],A.loc[i,'AGREEMENTID'],A.loc[i,'BKT'],P.loc[j,'POS_RES%'],A.loc[i,'Billing PAID AMT.'],PA.loc[l-1,l1[k]],APA.loc[y,l1[k]],c,P.loc[j,'BKT'])
                                #         elif A.loc[i,'STATUS']=='SB':
                                #             d=A.loc[i,'Billing PAID AMT.']*(PA.loc[l,l1[k]])/100
                                #             A.loc[i,'PERCENTAGE']=str(PA.loc[l,l1[k]])+'%'
                                #             A.loc[i,'MOHAK']=d
                                #             print(A.loc[i,'AGREEMENTID'],A.loc[i,'BKT'],P.loc[j,'POS_RES%'],A.loc[i,'Billing PAID AMT.'],PA.loc[l,l1[k]],APA.loc[y,l1[k]],d,P.loc[j,'BKT'])
                                #         else:
                                #             A.loc[i,'PERCENTAGE']=str(PA.loc[l,l1[k]])+'%'
                                #             A.loc[i,'MOHAK']=0
                                #             print(A.loc[i,'AGREEMENTID'],A.loc[i,'BKT'],P.loc[j,'POS_RES%'],A.loc[i,'Billing PAID AMT.'],PA.loc[l,l1[k]],APA.loc[y,l1[k]],0,P.loc[j,'BKT'])


for i in range(0,len(A['BKT'])):
    if A.loc[i,'STATUS']=='SETTLEMENT':
        dd=A.loc[i,'Billing PAID AMT.']*12/100
        A.loc[i,'MOHAK']=dd
        A.loc[i,'PERCENTAGE']=str(12)+'%'
    elif A.loc[i,'STATUS']=='FORECLOSE':
        dd=A.loc[i,'Billing PAID AMT.']*20/100
        A.loc[i,'MOHAK']=dd
        A.loc[i,'PERCENTAGE']=str(20)+'%'
# =============================================================================
#     elif (A.loc[i,'BKT']==2 or A.loc[i,'BKT']==3) and A.loc[i,'STATUS']=='FORECLOSE':
#         c=A.loc[i,'TOTAL COLLECTABLE']*16/100
#         A.loc[i,'MOHAK']=c
# =============================================================================

A['MOHAK'].replace(np.nan,0,inplace=True)

A.rename({'MOHAK':'PAYOUT'},axis=1,inplace=True)

A.to_excel(r'/Users/mohaksehgal/Documents/Work/Billing/L_T/L_T JUN 21/Final Billing L_T.xlsx',index=False)

# =============================================================================
# A.to_excel(r'/Users/mohaksehgal/Documents/Work/FOS Salary/L_T/MASTER FILE L_T.xlsx',index=False)
# =============================================================================
