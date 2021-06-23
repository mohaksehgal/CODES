#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 15:29:57 2020

@author: mohaksehgal
"""


import pandas as pd
import numpy as np

## Salary IDFC-HL

IDFC=pd.read_excel(r'/Users/mohaksehgal/Documents/Work/FOS Salary/IDFC/March 20/FOS SALARY AND BILLING PAID AMOUNT IDFC.xlsx',sheet_name='Sheet1')

IDFC_Salary=pd.DataFrame(IDFC.groupby('FOS')['FOS INCENTIVES'].sum()).reset_index()

## Salary L&T & IDFC TW

LT_IDFCTW_combined_salary=pd.read_excel(r'/Users/mohaksehgal/Documents/Work/COMBINED SALARY OF L_T AND IDFC TW/March 20/FINAL SALARY(L_I).xlsx')

LTIDFCTW=LT_IDFCTW_combined_salary[['FOS','FINAL_PAYOUT']]

## TC Incentive IDFC_TW & L&T

TIncentive=pd.read_excel(r'/Users/mohaksehgal/Documents/Work/TC Incentive/L_T/MARCH 20/L_T TC Incentive.xlsx')

IDFCIncentive=pd.read_excel(r'/Users/mohaksehgal/Documents/Work/TC Incentive/IDFC_TW/MARCH 20/IDFC_TW TC Incentive.xlsx')

IDFC_TW_TC_Incentive=IDFCIncentive[['TC NAME','PAYOUT']]

L_T_TC_Incentive=TIncentive[['TC NAME','PAYOUT']]

## Salary AB_BL

AB_BL=pd.read_excel(r'/Users/mohaksehgal/Documents/Work/FOS Salary/AB_BL/MARCH 20/FOS Salary AB_BL.xlsx')

AB_BL=AB_BL[['FOS','PAYOUT']]

Final_salary_sheet=pd.read_excel(r'/Users/mohaksehgal/Documents/Work/P&L/Dummy Files/Dummy salary.xlsx')

## TC Incentive AB_BL & AB 90+

ABIncentive=pd.read_excel(r'/Users/mohaksehgal/Documents/Work/TC Incentive/AB/MARCH 20/AB_BL TC Incentive.xlsx')

AB_BL_TC_Incentive=ABIncentive[['TC NAME','PAYOUT']]

AB90Incentive=pd.read_excel(r'/Users/mohaksehgal/Documents/Work/TC Incentive/AB 90+/MARCH 20/AB 90+ TC Incentive.xlsx')

AB_90_TC_Incentive=AB90Incentive[['TC NAME','PAYOUT']]

for i in range(0,len(Final_salary_sheet['NAMES'])):
    for j in range(0,len(IDFC_Salary['FOS'])):
        if Final_salary_sheet.loc[i,'NAMES']==IDFC_Salary.loc[j,'FOS']:
            Final_salary_sheet.loc[i,'IDFC-HL']=IDFC_Salary.loc[j,'FOS INCENTIVES']

for i in range(0,len(Final_salary_sheet['NAMES'])):
    for j in range(0,len(LTIDFCTW['FOS'])):
        if Final_salary_sheet.loc[i,'NAMES']==LTIDFCTW.loc[j,'FOS']:
            Final_salary_sheet.loc[i,'L&T']=LTIDFCTW.loc[j,'FINAL_PAYOUT']
            
for i in range(0,len(Final_salary_sheet['NAMES'])):
    for j in range(0,len(AB_BL['FOS_NAME'])):
        if Final_salary_sheet.loc[i,'NAMES']==AB_BL.loc[j,'FOS_NAME']:
            Final_salary_sheet.loc[i,'ABFL']=AB_BL.loc[j,'INCENTIVE']
            
for i in range(0,len(Final_salary_sheet['NAMES'])):
    for j in range(0,len(L_T_TC_Incentive['TC NAME'])):
        if Final_salary_sheet.loc[i,'NAMES']==L_T_TC_Incentive.loc[j,'TC NAME']:
            Final_salary_sheet.loc[i,'L&T']=L_T_TC_Incentive.loc[j,'PAYOUT']
            
for i in range(0,len(Final_salary_sheet['NAMES'])):
    for j in range(0,len(IDFC_TW_TC_Incentive['TC NAME'])):
        if Final_salary_sheet.loc[i,'NAMES']==IDFC_TW_TC_Incentive.loc[j,'TC NAME']:
            Final_salary_sheet.loc[i,'IDFC-TW']=IDFC_TW_TC_Incentive.loc[j,'PAYOUT']
            
for i in range(0,len(Final_salary_sheet['NAMES'])):
    for j in range(0,len(AB_90_TC_Incentive['TC NAME'])):
        if Final_salary_sheet.loc[i,'NAMES']==AB_90_TC_Incentive.loc[j,'TC NAME']:
            Final_salary_sheet.loc[i,'ABFL']=AB_90_TC_Incentive.loc[j,'PAYOUT']
            
for i in range(0,len(Final_salary_sheet['NAMES'])):
    for j in range(0,len(AB_BL_TC_Incentive['TC NAME'])):
        if Final_salary_sheet.loc[i,'NAMES']==AB_BL_TC_Incentive.loc[j,'TC NAME']:
            Final_salary_sheet.loc[i,'ABFL']=AB_BL_TC_Incentive.loc[j,'PAYOUT']
            
Final_salary_sheet.to_excel(r'/Users/mohaksehgal/Documents/Work/P&L/P&L Automate/Salary sheet.xlsx',index=False)

## P&L

Profit=pd.read_excel(r'/Users/mohaksehgal/Documents/Work/P&L/Dummy Files/Dummy New_Profit.xls', sheet_name='P&L Summary')

P=pd.read_excel(r'/Users/mohaksehgal/Documents/Work/P&L/Expense Sheet/MARCH 20/Final Expense File..xlsx')

QQ=pd.DataFrame(P[P['MONTH']=="MAR'20"].groupby('Process Expense')['TOTAL EXPENSE'].sum()).reset_index(drop=False)

for i in range(0,len(Profit['Process Expense'])):
    for j in range(0,len(QQ['Process Expense'])):
        if Profit.loc[i,'Process Expense']==QQ.loc[j,'Process Expense']:
            Profit.loc[i,'Expense']=QQ.loc[j,'TOTAL EXPENSE']
            
Profit.fillna(0,inplace=True)

Profit.to_excel(r'/Users/mohaksehgal/Documents/Work/P&L/P&L Automate/Expense.xlsx',index=False)

AS=QQ[(QQ['Process Expense']=='ASSETS') | (QQ['Process Expense']=='SECURITY DEPOSIT')]

AS.to_excel(r'/Users/mohaksehgal/Documents/Work/P&L/P&L Automate/Assets & SD.xlsx',index=False)

Expenseby=pd.DataFrame(P[P['MONTH']=="MAR'20"].groupby('EXPENSE BY')['TOTAL EXPENSE'].sum()).reset_index(drop=False)

Expenseby.to_excel(r'/Users/mohaksehgal/Documents/Work/P&L/P&L Automate/EXPENSEBY.xlsx',index=False)



