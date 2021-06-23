#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 08:52:14 2020

@author: mohaksehgal
"""


import pandas as pd
import numpy as np

Pervious=pd.read_excel(r"/Users/mohaksehgal/Documents/Work/MIS/L_T/MARCH 20/L_T PAID FILE 25 MAR 20.xlsx")

Ondate=pd.read_excel(r"/Users/mohaksehgal/Documents/Work/MIS/L_T/MARCH 20/L_T PAID FILE 26 MAR 20.xlsx")


LP=list(Pervious['AGREEMENTID'])
LO=list(Ondate['AGREEMENTID'])

for i in range(0,len(LP)):
    if LP[i] not in LO:
        print(LP[i])
