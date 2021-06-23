import pandas as pd
import numpy as np


A=pd.read_excel(r"/Users/mohaksehgal/Documents/Work/MIS/IDFC/JUN 21/IDFC_ALLOCATION_21JUN21.xlsx")
B=pd.read_excel(r"/Users/mohaksehgal/Documents/Work/MIS/IDFC/JUN 21/IDFC_PAID FILE_22JUN21.xlsx")
B1=pd.DataFrame(B.groupby('AGREEMENTID')['PAID AMOUNT'].sum()).reset_index()

for i in range(0,len(A['AGREEMENTID'])):
    for k in range(0,len(B['AGREEMENTID'])):
        if A.loc[i,'AGREEMENTID']==B.loc[k,'AGREEMENTID'] and B.loc[k,'AGAINST']!='FORECLOSE' and B.loc[k,'AGAINST']!='SETTLEMENT':
            for j in range(0,len(B1['AGREEMENTID'])):
                if A.loc[i,'AGREEMENTID']==B1.loc[j,'AGREEMENTID']:
                    if A.loc[i,'BKT']!='BKT0' and A.loc[i,'BKT']!='BKT12' and A.loc[i,'BKT']!='BKT1' and A.loc[i,'BKT']!='BKT10':
                        a=(int(A.loc[i,'BKT'][-1])+1)*A.loc[i,'EMI']
                        b=A.loc[i,'EMI']+A.loc[i,'EMI']
                        if B1.loc[j,'PAID AMOUNT']>=a or B1.loc[j,'PAID AMOUNT']>=A.loc[i,'POS']:
                                A.loc[i,'STATUS']='NM'
                        elif B1.loc[j,'PAID AMOUNT']>=b and B1.loc[j,'PAID AMOUNT']<a and B1.loc[j,'PAID AMOUNT']<A.loc[i,'POS']:
                            A.loc[i,'STATUS']='RB'
                        elif B1.loc[j,'PAID AMOUNT']>=A.loc[i,'EMI'] and B1.loc[j,'PAID AMOUNT']<b:
                            A.loc[i,'STATUS']='SB'
                        elif B1.loc[j,'PAID AMOUNT']<A.loc[i,'EMI']:
                            A.loc[i,'STATUS']='PART PAID'
                    elif A.loc[i,'BKT']=='BKT1':
                        b=A.loc[i,'EMI']+A.loc[i,'EMI']
                        if B1.loc[j,'PAID AMOUNT']>=b or B1.loc[j,'PAID AMOUNT']>=A.loc[i,'POS']:
                            A.loc[i,'STATUS']='NM'
                        elif B1.loc[j,'PAID AMOUNT']>=A.loc[i,'EMI'] and B1.loc[j,'PAID AMOUNT']<b:
                            A.loc[i,'STATUS']='SB'
                        elif B1.loc[j,'PAID AMOUNT']<A.loc[i,'EMI']:
                            A.loc[i,'STATUS']='PART PAID'
                    elif A.loc[i,'BKT']=='BKT12' or A.loc[i,'BKT']=='BKT10':
                        c=(int(A.loc[i,'BKT'][-2:])+1)*A.loc[i,'EMI']
                        d=A.loc[i,'EMI']+A.loc[i,'EMI']
                        if B1.loc[j,'PAID AMOUNT']>=c or B1.loc[j,'PAID AMOUNT']>=A.loc[i,'POS']:
                            A.loc[i,'STATUS']='NM'
                        elif B1.loc[j,'PAID AMOUNT']>=d and B1.loc[j,'PAID AMOUNT']<c:
                            A.loc[i,'STATUS']='RB'
                        elif B1.loc[j,'PAID AMOUNT']>=A.loc[i,'EMI'] and B1.loc[j,'PAID AMOUNT']<d:
                            A.loc[i,'STATUS']='SB'
                        elif B1.loc[j,'PAID AMOUNT']<A.loc[i,'EMI']:
                            A.loc[i,'STATUS']='PART PAID'
                    elif A.loc[i,'BKT']=='BKT0':
                        if B1.loc[j,'PAID AMOUNT']<A.loc[i,'EMI']:
                            A.loc[i,'STATUS']='PART PAID'
                        else:
                            A.loc[i,'STATUS']='SB'
        elif A.loc[i,'AGREEMENTID']==B.loc[k,'AGREEMENTID'] and B.loc[k,'AGAINST']=='FORECLOSE':
            A.loc[i,'STATUS']='FORECLOSE'
        elif A.loc[i,'AGREEMENTID']==B.loc[k,'AGREEMENTID'] and B.loc[k,'AGAINST']=='SETTLEMENT':
            A.loc[i,'STATUS']='SETTLEMENT'
        elif A.loc[i,'AGREEMENTID']==B.loc[k,'AGREEMENTID'] and B.loc[k,'AGAINST']=='LOAN CANCELED':
            A.loc[i,'STATUS']='LOAN CANCELED'
            
A['STATUS'].fillna('FLOW',inplace=True)

for i in range(0,len(A['AGREEMENTID'])):
    for j in range(0,len(B1['PAID AMOUNT'])):
        if A.loc[i,'AGREEMENTID']==B1.loc[j,'AGREEMENTID']:
            A.loc[i,'TOTAL PAID']=B1.loc[j,'PAID AMOUNT']

M=pd.DataFrame(A.groupby(['BKT','STATE'])['POS'].sum()).reset_index()

M.rename({'POS':'TOTAL_POS'},axis=1,inplace=True)

R=pd.DataFrame(A.groupby(['BKT','STATE'])['AGREEMENTID'].count()).reset_index()

F=M.merge(R,how='outer')

F.rename({'AGREEMENTID':'TOTAL_CASES'},axis=1,inplace=True)

R1=pd.DataFrame(A.groupby(['BKT','STATE','STATUS'])['AGREEMENTID'].count()).reset_index()

P=F.copy()

P=P.iloc[:,:3]

P['FLOW']=np.nan
P['SB']=np.nan
P['RB']=np.nan
P['NM']=np.nan
P['PART PAID']=np.nan
P['FORECLOSE']=np.nan
P['SETTLEMENT']=np.nan
P['LOAN CANCELED']=np.nan

COL=P.columns

for i in range(0,len(R1['BKT'])):
    for j in range(0,len(P['FLOW'])):
        for k in range(0,len(COL)):
            if ((R1.loc[i,['BKT','STATE']]==P.loc[j,['BKT','STATE']]).all()) and R1.loc[i,'STATUS']==COL[k]:
                P.loc[j,COL[k]]=R1.loc[i,'AGREEMENTID']

F=F.merge(P,how='outer')

F.fillna(0,inplace=True)

F.rename({'FLOW':'FLOW_CASES','SB':'SB_CASES','RB':'RB_CASES','FORECLOSE':'FORECLOSE_CASES','SETTLEMENT':'SETTLEMENT_CASES','NM':'NM_CASES','PART PAID':'PART_PAID_CASES','LOAN CANCELED':'LOAN_CANCELED_CASES'},axis=1,inplace=True)

R2=pd.DataFrame(A.groupby(['BKT','STATE','STATUS'])['POS'].sum()).reset_index()

for i in range(0,len(R2['BKT'])):
    for j in range(0,len(P['FLOW'])):
        for k in range(0,len(COL)):
            if ((R2.loc[i,['BKT','STATE']]==P.loc[j,['BKT','STATE']]).all()) and R2.loc[i,'STATUS']==COL[k]:
                P.loc[j,COL[k]]=R2.loc[i,'POS']
                
F=F.merge(P,how='outer')

F.rename({'FLOW':'FLOW_POS','SB':'SB_POS','RB':'RB_POS','FORECLOSE':'FORECLOSE_POS', 'NM':'NM_POS','SETTLEMENT':'SETTLEMENT_POS','PART PAID':'PART_PAID_POS','LOAN CANCELED':'LOAN_CANCELED_POS'},axis=1,inplace=True)

F.fillna(0,inplace=True)

for i in range(0,len(F['FLOW_CASES'])):
    F.loc[i,'FLOW_POS%']=round((F.loc[i,'FLOW_POS']/F.loc[i,'TOTAL_POS'])*100,2)
    F.loc[i,'SB_POS%']=round((F.loc[i,'SB_POS']/F.loc[i,'TOTAL_POS'])*100,2)
    F.loc[i,'RB_POS%']=round((F.loc[i,'RB_POS']/F.loc[i,'TOTAL_POS'])*100,2)
    F.loc[i,'FORECLOSE_POS%']=round((F.loc[i,'FORECLOSE_POS']/F.loc[i,'TOTAL_POS'])*100,2)
    F.loc[i,'SETTLEMENT_POS%']=round((F.loc[i,'SETTLEMENT_POS']/F.loc[i,'TOTAL_POS'])*100,2)
    F.loc[i,'NM_POS%']=round((F.loc[i,'NM_POS']/F.loc[i,'TOTAL_POS'])*100,2)
    F.loc[i,'PART_PAID_POS%']=round((F.loc[i,'PART_PAID_POS']/F.loc[i,'TOTAL_POS'])*100,2)
    F.loc[i,'LOAN_CANCELED%']=round((F.loc[i,'LOAN_CANCELED_POS']/F.loc[i,'TOTAL_POS'])*100,2)

TP=pd.DataFrame(A.groupby(['BKT','STATE'])['TOTAL PAID'].sum()).reset_index()

F=F.merge(TP,how='outer')

for i in range(0,len(F['SB_POS'])):
    F.loc[i,'PERFORMANCE']=F.loc[i,'SB_POS%']+F.loc[i,'RB_POS%']+F.loc[i,'FORECLOSE_POS%']+F.loc[i,'NM_POS%']+F.loc[i,'SETTLEMENT_POS%']+F.loc[i,'LOAN_CANCELED%']
    F.loc[i,'Additional_Performance']=F.loc[i,'RB_POS%']+F.loc[i,'NM_POS%']

F.rename({'TOTAL_CASES':'COUNT','PART_PAID_CASES':'PP_CASES','FORECLOSE_CASES':'FC_CASES','SETTLEMENT_CASES':'SC_CASES',
         'PART_PAID_POS':'PP_POS','FORECLOSE_POS':'FC_POS','SETTLEMENT_POS':'SC_POS','FORECLOSE_POS%':'FC_POS%',
         'SETTLEMENT_POS%':'SC_POS%','PART_PAID_POS%':'PP_POS%','PERFORMANCE':'POS_RES%'},axis=1,inplace=True)

F.replace(0,np.nan,inplace=True)

F.to_excel(r'/Users/mohaksehgal/Documents/Work/MIS/IDFC/JUN 21/MIS IDFC.xlsx',index=False)   

F.replace(np.nan,0,inplace=True)

F.to_excel(r'/Users/mohaksehgal/Documents/Work/Billing/IDFC/IDFC Jun 21/Performance IDFC.xlsx',index=False) 

for i in range(0,len(A['AGREEMENTID'])):
    s=0
    for j in range(0,len(B['AGREEMENTID'])):
        if (A.loc[i,'AGREEMENTID']==B.loc[j,'AGREEMENTID']) and (A.loc[i,'STATUS']=='NM' or A.loc[i,'STATUS']=='FORECLOSE' or A.loc[i,'STATUS']=='SETTLEMENT') and (B.loc[j,'MODE']!='ECS'):
            s=s+B.loc[j,'PAID AMOUNT']
        elif (A.loc[i,'AGREEMENTID']==B.loc[j,'AGREEMENTID']) and (A.loc[i,'STATUS']=='SB') and (B.loc[j,'MODE']!='ECS'):
            s=s+B.loc[j,'PAID AMOUNT']
        elif (A.loc[i,'AGREEMENTID']==B.loc[j,'AGREEMENTID']) and (A.loc[i,'STATUS']=='RB'):
            s=s+B.loc[j,'PAID AMOUNT']
    A.loc[i,'Billing PAID AMT.']=s

for i in range(0,len(A['STATE'])):
    if A.loc[i,'STATUS']=='SB':
        if A.loc[i,'Billing PAID AMT.']>A.loc[i,'EMI']:
            A.loc[i,'Billing PAID AMT.']=A.loc[i,'EMI']

A.to_excel(r'/Users/mohaksehgal/Documents/Work/Billing/IDFC/IDFC Jun 21/MASTER FILE IDFC.xlsx',index=False)

A.to_excel(r'/Users/mohaksehgal/Documents/Work/TC Performance/IDFC/Jun 21/MASTER FILE IDFC.xlsx',index=False)

A.to_excel(r'/Users/mohaksehgal/Documents/Work/MIS/IDFC/JUN 21/MASTER FILE IDFC.xlsx',index=False)

A.to_excel(r'/Users/mohaksehgal/Documents/Work/FOS Salary/IDFC/JUN 21/MASTER FILE IDFC.xlsx',index=False)



## TL-Wise Performace


M=pd.DataFrame(A.groupby(['BKT','TL'])['POS'].sum()).reset_index()

M.rename({'POS':'TOTAL_POS'},axis=1,inplace=True)

R=pd.DataFrame(A.groupby(['BKT','TL'])['AGREEMENTID'].count()).reset_index()

F=M.merge(R,how='outer')

F.rename({'AGREEMENTID':'TOTAL_CASES'},axis=1,inplace=True)

R1=pd.DataFrame(A.groupby(['BKT','TL','STATUS'])['AGREEMENTID'].count()).reset_index()

R1=pd.DataFrame(A.groupby(['BKT','TL','STATUS'])['AGREEMENTID'].count()).reset_index()

P=F.copy()

P=P.iloc[:,:2]

P['FLOW']=np.nan
P['SB']=np.nan
P['RB']=np.nan
P['NM']=np.nan
P['PART PAID']=np.nan
P['FORECLOSE']=np.nan
P['SETTLEMENT']=np.nan
P['LOAN CANCELED']=np.nan 

COL=P.columns

for i in range(0,len(R1['BKT'])):
    for j in range(0,len(P['BKT'])):
        for k in range(0,len(COL)):
            if ((R1.loc[i,['BKT','TL']]==P.loc[j,['BKT','TL']]).all()) and R1.loc[i,'STATUS']==COL[k]:
                P.loc[j,COL[k]]=R1.loc[i,'AGREEMENTID']
                
F=F.merge(P,how='outer')

F.fillna(0,inplace=True)

F.rename({'FLOW':'FLOW_CASES','SB':'SB_CASES','RB':'RB_CASES','FORECLOSE':'FORECLOSE_CASES','SETTLEMENT':'SETTLEMENT_CASES','NM':'NM_CASES','PART PAID':'PART_PAID_CASES','LOAN CANCELED':'LOAN_CANCELED_CASES'},axis=1,inplace=True)

R2=pd.DataFrame(A.groupby(['BKT','TL','STATUS'])['POS'].sum()).reset_index()

for i in range(0,len(R2['BKT'])):
    for j in range(0,len(P['BKT'])):
        for k in range(0,len(COL)):
            if ((R2.loc[i,['BKT','TL']]==P.loc[j,['BKT','TL']]).all()) and R2.loc[i,'STATUS']==COL[k]:
                P.loc[j,COL[k]]=R2.loc[i,'POS']

F=F.merge(P,how='outer')

F.rename({'FLOW':'FLOW_POS','SB':'SB_POS','RB':'RB_POS','FORECLOSE':'FORECLOSE_POS', 'NM':'NM_POS','SETTLEMENT':'SETTLEMENT_POS','PART PAID':'PART_PAID_POS','LOAN CANCELED':'LOAN_CANCELED_POS'},axis=1,inplace=True)

F.fillna(0,inplace=True)

for i in range(0,len(F['FLOW_CASES'])):
    F.loc[i,'FLOW_POS%']=round((F.loc[i,'FLOW_POS']/F.loc[i,'TOTAL_POS'])*100,2)
    F.loc[i,'SB_POS%']=round((F.loc[i,'SB_POS']/F.loc[i,'TOTAL_POS'])*100,2)
    F.loc[i,'RB_POS%']=round((F.loc[i,'RB_POS']/F.loc[i,'TOTAL_POS'])*100,2)
    F.loc[i,'FORECLOSE_POS%']=round((F.loc[i,'FORECLOSE_POS']/F.loc[i,'TOTAL_POS'])*100,2)
    F.loc[i,'SETTLEMENT_POS%']=round((F.loc[i,'SETTLEMENT_POS']/F.loc[i,'TOTAL_POS'])*100,2)
    F.loc[i,'NM_POS%']=round((F.loc[i,'NM_POS']/F.loc[i,'TOTAL_POS'])*100,2)
    F.loc[i,'PART_PAID_POS%']=round((F.loc[i,'PART_PAID_POS']/F.loc[i,'TOTAL_POS'])*100,2)
    F.loc[i,'LOAN_CANCELED%']=round((F.loc[i,'LOAN_CANCELED_POS']/F.loc[i,'TOTAL_POS'])*100,2)

TP=pd.DataFrame(A.groupby(['BKT','TL'])['TOTAL PAID'].sum()).reset_index()

F=F.merge(TP,how='outer')

for i in range(0,len(F['SB_POS'])):
    F.loc[i,'PERFORMANCE']=F.loc[i,'SB_POS%']+F.loc[i,'RB_POS%']+F.loc[i,'FORECLOSE_POS%']+F.loc[i,'NM_POS%']+F.loc[i,'SETTLEMENT_POS%']+F.loc[i,'LOAN_CANCELED%']

for i in range(0,len(F['SB_CASES'])):
    F.loc[i,'Additional_Performance']=F.loc[i,'RB_POS%']+F.loc[i,'NM_POS%']
    
F.replace(0,np.nan,inplace=True)

F.to_excel(r'/Users/mohaksehgal/Documents/Work/MIS/IDFC/JUN 21/MIS TL-WISE.xlsx',index=False)


            
