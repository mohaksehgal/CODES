#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 10:57:56 2020

@author: mohaksehgal
"""


import pandas as pd
import numpy as np

Pervious=pd.read_excel(r"/Users/mohaksehgal/Documents/Work/MIS/IDFC TW/MARCH 20/IDFC_TW PAID FILE 25 MARCH 20.xlsx")

Ondate=pd.read_excel(r"/Users/mohaksehgal/Documents/Work/MIS/IDFC TW/MARCH 20/IDFC_TW PAID FILE 30 MARCH 20.xlsx")


LP=list(Pervious['AGREEMENTID'])
LO=list(Ondate['AGREEMENTID'])

for i in range(0,len(LP)):
    if LP[i] not in LO:
        print(LP[i])

