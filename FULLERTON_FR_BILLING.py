#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 11:27:47 2021

@author: rishi
"""

import pandas as pd
import numpy as np

A=pd.read_excel(r"/Users/mohaksehgal/Documents/Work/Billing/FULLERTON/JUN 21/MASTER_FILE_FULLERTON_FR.xlsx")

P=pd.read_excel(r'/Users/mohaksehgal/Documents/Work/MIS/FULLERTON/JUN 21/MIS_FULLERTON_FR.xlsx')

PAID_FILE=pd.read_excel(r"/Users/mohaksehgal/Documents/Work/MIS/FULLERTON/JUN 21/FULLERTON_FR_PAID FILE_22JUN21.xlsx")

for i in range(0,len(A['COMPANY'])):
    if A.loc[i,'COMPANY']=='FULLERTON':
        for j in range(0,len(P['COMPANY'])):
            if (A.loc[i,'COMPANY']==P.loc[j,'COMPANY']):
                if P.loc[j,'POS_RES%']<75:
                    if A.loc[i,'STATUS']=='SB':
                        a=A.loc[i,'Billing PAID AMT.']*4/100
                        A.loc[i,'PERCENTAGE']=str(4)+'%'
                        A.loc[i,'MOHAK']=a
                        print(A.loc[i,'AGREEMENTID'],A.loc[i,'COMPANY'],P.loc[j,'POS_RES%'],A.loc[i,'Billing PAID AMT.'],str(4),a,P.loc[j,'COMPANY'])
                elif (P.loc[j,'POS_RES%']>=75) and (P.loc[j,'POS_RES%']<78):
                    if A.loc[i,'STATUS']=='SB':
                        a=A.loc[i,'Billing PAID AMT.']*4.25/100
                        A.loc[i,'PERCENTAGE']=str(4.25)+'%'
                        A.loc[i,'MOHAK']=a
                        print(A.loc[i,'AGREEMENTID'],A.loc[i,'COMPANY'],P.loc[j,'POS_RES%'],A.loc[i,'Billing PAID AMT.'],str(4.25),a,P.loc[j,'COMPANY'])
                elif (P.loc[j,'POS_RES%']>=78) and (P.loc[j,'POS_RES%']<80):
                    if A.loc[i,'STATUS']=='SB':
                        a=A.loc[i,'Billing PAID AMT.']*4.5/100
                        A.loc[i,'PERCENTAGE']=str(4.5)+'%'
                        A.loc[i,'MOHAK']=a
                        print(A.loc[i,'AGREEMENTID'],A.loc[i,'COMPANY'],P.loc[j,'POS_RES%'],A.loc[i,'Billing PAID AMT.'],str(4.5),a,P.loc[j,'COMPANY'])
                elif (P.loc[j,'POS_RES%']>=80) and (P.loc[j,'POS_RES%']<82):
                    if A.loc[i,'STATUS']=='SB':
                        a=A.loc[i,'Billing PAID AMT.']*4.75/100
                        A.loc[i,'PERCENTAGE']=str(4.75)+'%'
                        A.loc[i,'MOHAK']=a
                        print(A.loc[i,'AGREEMENTID'],A.loc[i,'COMPANY'],P.loc[j,'POS_RES%'],A.loc[i,'Billing PAID AMT.'],str(4.75),a,P.loc[j,'COMPANY'])
                elif (P.loc[j,'POS_RES%']>=82) and (P.loc[j,'POS_RES%']<84):
                    if A.loc[i,'STATUS']=='SB':
                        a=A.loc[i,'Billing PAID AMT.']*5/100
                        A.loc[i,'PERCENTAGE']=str(5)+'%'
                        A.loc[i,'MOHAK']=a
                        print(A.loc[i,'AGREEMENTID'],A.loc[i,'COMPANY'],P.loc[j,'POS_RES%'],A.loc[i,'Billing PAID AMT.'],str(5),a,P.loc[j,'COMPNAY'])
                elif (P.loc[j,'POS_RES%']>=84) and (P.loc[j,'POS_RES%']<86):
                    if A.loc[i,'STATUS']=='SB':
                        a=A.loc[i,'Billing PAID AMT.']*5.25/100
                        A.loc[i,'PERCENTAGE']=str(5.25)+'%'
                        A.loc[i,'MOHAK']=a
                        print(A.loc[i,'AGREEMENTID'],A.loc[i,'COMPANY'],A.loc[j,'POS_RES%'],A.loc[i,'Billing PAID AMT.'],str(5.25),a,P.loc[j,'COMPNAY'])
                elif (P.loc[j,'POS_RES%']>=86) and (P.loc[j,'POS_RES%']<88):
                    if A.loc[i,'STATUS']=='SB':
                        a=A.loc[i,'Billing PAID AMT.']*5.5/100
                        A.loc[i,'PERCENTAGE']=str(5.5)+'%'
                        A.loc[i,'MOHAK']=a
                        print(A.loc[i,'AGREEMENTID'],A.loc[i,'COMPANY'],P.loc[j,'POS_RES%'],A.loc[i,'Billing PAID AMT.'],str(5.5),a,P.loc[j,'COMPNAY'])
                elif (P.loc[j,'POS_RES%']>=88) and (P.loc[j,'POS_RES%']<90):
                    if A.loc[i,'STATUS']=='SB':
                        a=A.loc[i,'Billing PAID AMT.']*5.75/100
                        A.loc[i,'PERCENTAGE']=str(5.75)+'%'
                        A.loc[i,'MOHAK']=a
                        print(A.loc[i,'AGREEMENTID'],A.loc[i,'COMPANY'],P.loc[j,'POS_RES%'],A.loc[i,'Billing PAID AMT.'],str(5.75),a,P.loc[j,'COMPNAY'])
                elif (P.loc[j,'POS_RES%']>=90) and (P.loc[j,'POS_RES%']<92):
                    if A.loc[i,'STATUS']=='SB':
                        a=A.loc[i,'Billing PAID AMT.']*6/100
                        A.loc[i,'PERCENTAGE']=str(6)+'%'
                        A.loc[i,'MOHAK']=a
                        print(A.loc[i,'AGREEMENTID'],A.loc[i,'COMPANY'],P.loc[j,'POS_RES%'],A.loc[i,'Billing PAID AMT.'],str(6),a,P.loc[j,'COMPNAY'])
                elif (P.loc[j,'POS_RES%']>=92):
                    if A.loc[i,'STATUS']=='SB':
                        a=A.loc[i,'Billing PAID AMT.']*6.25/100
                        A.loc[i,'PERCENTAGE']=str(6.25)+'%'
                        A.loc[i,'MOHAK']=a
                        print(A.loc[i,'AGREEMENTID'],A.loc[i,'COMPANY'],P.loc[j,'POS_RES%'],A.loc[i,'Billing PAID AMT.'],str(6.25),a,P.loc[j,'COMPANY'])
# PL-SELF
    # elif A.loc[i,'PRODUCT']=='PL Self':
    #     for j in range(0,len(P['PRODUCT'])):
    #         if (A.loc[i,'PRODUCT']==P.loc[j,'PRODUCT']):
    #             if P.loc[j,'POS_RES%']<55:
    #                 if A.loc[i,'STATUS']=='SB':
    #                     a=A.loc[i,'Billing PAID AMT.']*6/100
    #                     A.loc[i,'PERCENTAGE']=str(6)+'%'
    #                     A.loc[i,'MOHAK']=a
    #                     print(A.loc[i,'AGREEMENTID'],A.loc[i,'PRODUCT'],P.loc[j,'POS_RES%'],A.loc[i,'Billing PAID AMT.'],str(6),a,P.loc[j,'PRODUCT'])
    #             elif (P.loc[j,'POS_RES%']>=55) and (P.loc[j,'POS_RES%']<65):
    #                 if A.loc[i,'STATUS']=='SB':
    #                     a=A.loc[i,'Billing PAID AMT.']*8/100
    #                     A.loc[i,'PERCENTAGE']=str(8)+'%'
    #                     A.loc[i,'MOHAK']=a
    #                     print(A.loc[i,'AGREEMENTID'],A.loc[i,'PRODUCT'],P.loc[j,'POS_RES%'],A.loc[i,'Billing PAID AMT.'],str(8),a,P.loc[j,'PRODUCT'])
    #             elif (P.loc[j,'POS_RES%']>=65) and (P.loc[j,'POS_RES%']<70):
    #                 if A.loc[i,'STATUS']=='SB':
    #                     a=A.loc[i,'Billing PAID AMT.']*10/100
    #                     A.loc[i,'PERCENTAGE']=str(10)+'%'
    #                     A.loc[i,'MOHAK']=a
    #                     print(A.loc[i,'AGREEMENTID'],A.loc[i,'PRODUCT'],P.loc[j,'POS_RES%'],A.loc[i,'Billing PAID AMT.'],str(10),a,P.loc[j,'PRODUCT'])
    #             elif (P.loc[j,'POS_RES%']>=70) and (P.loc[j,'POS_RES%']<75):
    #                 if A.loc[i,'STATUS']=='SB':
    #                     a=A.loc[i,'Billing PAID AMT.']*12/100
    #                     A.loc[i,'PERCENTAGE']=str(12)+'%'
    #                     A.loc[i,'MOHAK']=a
    #                     print(A.loc[i,'AGREEMENTID'],A.loc[i,'PRODUCT'],P.loc[j,'POS_RES%'],A.loc[i,'Billing PAID AMT.'],str(12),a,P.loc[j,'PRODUCT'])
    #             elif (P.loc[j,'POS_RES%']>=75) and (P.loc[j,'POS_RES%']<80):
    #                 if A.loc[i,'STATUS']=='SB':
    #                     a=A.loc[i,'Billing PAID AMT.']*14/100
    #                     A.loc[i,'PERCENTAGE']=str(14)+'%'
    #                     A.loc[i,'MOHAK']=a
    #                     print(A.loc[i,'AGREEMENTID'],A.loc[i,'PRODUCT'],P.loc[j,'POS_RES%'],A.loc[i,'Billing PAID AMT.'],str(14),a,P.loc[j,'PRODUCT'])
    #             elif (P.loc[j,'POS_RES%']>=80) and (P.loc[j,'POS_RES%']<85):
    #                 if A.loc[i,'STATUS']=='SB':
    #                     a=A.loc[i,'Billing PAID AMT.']*16/100
    #                     A.loc[i,'PERCENTAGE']=str(16)+'%'
    #                     A.loc[i,'MOHAK']=a
    #                     print(A.loc[i,'AGREEMENTID'],A.loc[i,'PRODUCT'],P.loc[j,'POS_RES%'],A.loc[i,'Billing PAID AMT.'],str(16),a,P.loc[j,'PRODUCT'])
    #             elif (P.loc[j,'POS_RES%']>=85) and (P.loc[j,'POS_RES%']<90):
    #                 if A.loc[i,'STATUS']=='SB':
    #                     a=A.loc[i,'Billing PAID AMT.']*18/100
    #                     A.loc[i,'PERCENTAGE']=str(18)+'%'
    #                     A.loc[i,'MOHAK']=a
    #                     print(A.loc[i,'AGREEMENTID'],A.loc[i,'PRODUCT'],P.loc[j,'POS_RES%'],A.loc[i,'Billing PAID AMT.'],str(18),a,P.loc[j,'PRODUCT'])
    #             elif (P.loc[j,'POS_RES%']>=90):
    #                 if A.loc[i,'STATUS']=='SB':
    #                     a=A.loc[i,'Billing PAID AMT.']*20/100
    #                     A.loc[i,'PERCENTAGE']=str(20)+'%'
    #                     A.loc[i,'MOHAK']=a
    #                     print(A.loc[i,'AGREEMENTID'],A.loc[i,'PRODUCT'],P.loc[j,'POS_RES%'],A.loc[i,'Billing PAID AMT.'],str(20),a,P.loc[j,'PRODUCT'])

FLOWLIST=A[A['STATUS']=='FLOW'].index

for i in range(0,len(FLOWLIST)):
    A.loc[FLOWLIST[i],'MOHAK']=0

A[A['MOHAK'].isnull()]['STATUS'].value_counts()

# for i in range(0,len(A['AGREEMENTID'])):
#     if A.loc[i,'STATUS']=='SETTLEMENT':
#         for j in range(0,len(PAID_FILE['AGREEMENTID'])):
#             if A.loc[i,'AGREEMENTID']==PAID_FILE.loc[j,'AGREEMENTID']:
#                 wavier=100-round(PAID_FILE.loc[j,'SETTLEMENT_TOTAL_AMOUNT']/A.loc[i,'POS']*100)
#                 if (A.loc[i,'POS']<100000):
#                     if wavier==0:
#                         a=A.loc[i,'Billing PAID AMT.']*18/100
#                         if a>=20000:
#                             A.loc[i,'MOHAK']=20000
#                         elif a<20000:
#                             A.loc[i,'MOHAK']=a
#                         A.loc[i,'PERCENTAGE']=str(18)+'%'
#                         print(A.loc[i,'AGREEMENTID'],A.loc[i,'Billing PAID AMT.'],str(18),A.loc[i,'MOHAK'],wavier)
#                     elif (wavier>0) and (wavier<=25):
#                         a=A.loc[i,'Billing PAID AMT.']*15/100
#                         if a>=15000:
#                             A.loc[i,'MOHAK']=15000
#                         elif a<15000:
#                             A.loc[i,'MOHAK']=a
#                         A.loc[i,'PERCENTAGE']=str(15)+'%'
#                         print(A.loc[i,'AGREEMENTID'],A.loc[i,'Billing PAID AMT.'],str(15),A.loc[i,'MOHAK'],wavier)
#                     elif (wavier>25) and (wavier<=50):
#                         a=A.loc[i,'Billing PAID AMT.']*12/100
#                         if a>=10000:
#                             A.loc[i,'MOHAK']=10000
#                         elif a<10000:
#                             A.loc[i,'MOHAK']=a
#                         A.loc[i,'PERCENTAGE']=str(12)+'%'
#                         print(A.loc[i,'AGREEMENTID'],A.loc[i,'Billing PAID AMT.'],str(12),A.loc[i,'MOHAK'],wavier)
#                 elif (A.loc[i,'POS']>=100000) and (A.loc[i,'POS']<200000):
#                     if wavier==0:
#                         a=A.loc[i,'Billing PAID AMT.']*21/100
#                         if a>=30000:
#                             A.loc[i,'MOHAK']=30000
#                         elif a<30000:
#                             A.loc[i,'MOHAK']=a
#                         A.loc[i,'PERCENTAGE']=str(21)+'%'
#                         print(A.loc[i,'AGREEMENTID'],A.loc[i,'Billing PAID AMT.'],str(21),A.loc[i,'MOHAK'],wavier)
#                     elif (wavier>0) and (wavier<=25):
#                         a=A.loc[i,'Billing PAID AMT.']*18/100
#                         if a>=25000:
#                             A.loc[i,'MOHAK']=25000
#                         elif a<25000:
#                             A.loc[i,'MOHAK']=a
#                         A.loc[i,'PERCENTAGE']=str(18)+'%'
#                         print(A.loc[i,'AGREEMENTID'],A.loc[i,'Billing PAID AMT.'],str(18),A.loc[i,'MOHAK'],wavier)
#                     elif (wavier>25) and (wavier<=50):
#                         a=A.loc[i,'Billing PAID AMT.']*15/100
#                         if a>=20000:
#                             A.loc[i,'MOHAK']=20000
#                         elif a<20000:
#                             A.loc[i,'MOHAK']=a
#                         A.loc[i,'PERCENTAGE']=str(15)+'%'
#                         print(A.loc[i,'AGREEMENTID'],A.loc[i,'Billing PAID AMT.'],str(15),A.loc[i,'MOHAK'],wavier)
#                 elif (A.loc[i,'POS']>=200000) and (A.loc[i,'POS']<300000):
#                     if wavier==0:
#                         a=A.loc[i,'Billing PAID AMT.']*25/100
#                         if a>=35000:
#                             A.loc[i,'MOHAK']=35000
#                         elif a<35000:
#                             A.loc[i,'MOHAK']=a
#                         A.loc[i,'PERCENTAGE']=str(25)+'%'
#                         print(A.loc[i,'AGREEMENTID'],A.loc[i,'Billing PAID AMT.'],str(25),A.loc[i,'MOHAK'],wavier)
#                     elif (wavier>0) and (wavier<=25):
#                         a=A.loc[i,'Billing PAID AMT.']*22/100
#                         if a>=30000:
#                             A.loc[i,'MOHAK']=30000
#                         elif a<30000:
#                             A.loc[i,'MOHAK']=a
#                         A.loc[i,'PERCENTAGE']=str(22)+'%'
#                         print(A.loc[i,'AGREEMENTID'],A.loc[i,'Billing PAID AMT.'],str(22),A.loc[i,'MOHAK'],wavier)
#                     elif (wavier>25) and (wavier<=50):
#                         a=A.loc[i,'Billing PAID AMT.']*19/100
#                         if a>=25000:
#                             A.loc[i,'MOHAK']=25000
#                         elif a<25000:
#                             A.loc[i,'MOHAK']=a
#                         A.loc[i,'PERCENTAGE']=str(19)+'%'
#                         print(A.loc[i,'AGREEMENTID'],A.loc[i,'Billing PAID AMT.'],str(19),A.loc[i,'MOHAK'],wavier)
#                 elif (A.loc[i,'POS']>=300000):
#                     if wavier==0:
#                         a=A.loc[i,'Billing PAID AMT.']*30/100
#                         if a>=40000:
#                             A.loc[i,'MOHAK']=40000
#                         elif a<40000:
#                             A.loc[i,'MOHAK']=a
#                         A.loc[i,'PERCENTAGE']=str(30)+'%'
#                         print(A.loc[i,'AGREEMENTID'],A.loc[i,'Billing PAID AMT.'],str(30),A.loc[i,'MOHAK'],wavier)
#                     elif (wavier>0) and (wavier<=25):
#                         a=A.loc[i,'Billing PAID AMT.']*27/100
#                         if a>=35000:
#                             A.loc[i,'MOHAK']=35000
#                         elif a<35000:
#                             A.loc[i,'MOHAK']=a
#                         A.loc[i,'PERCENTAGE']=str(27)+'%'
#                         print(A.loc[i,'AGREEMENTID'],A.loc[i,'Billing PAID AMT.'],str(27),A.loc[i,'MOHAK'],wavier)
#                     elif (wavier>25) and (wavier<=50):
#                         a=A.loc[i,'Billing PAID AMT.']*24/100
#                         if a>=30000:
#                             A.loc[i,'MOHAK']=30000
#                         elif a<30000:
#                             A.loc[i,'MOHAK']=a
#                         A.loc[i,'PERCENTAGE']=str(24)+'%'
#                         print(A.loc[i,'AGREEMENTID'],A.loc[i,'Billing PAID AMT.'],str(24),A.loc[i,'MOHAK'],wavier)

A.rename({'MOHAK':'PAYOUT'},axis=1,inplace=True)

A.to_excel(r'/Users/mohaksehgal/Documents/Work/Billing/FULLERTON/JUN 21/PAYOUT_FULLERTON_FR.xlsx',index=False)