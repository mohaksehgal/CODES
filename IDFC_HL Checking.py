#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 08:31:02 2020

@author: mohaksehgal
"""


import pandas as pd
import numpy as np

Pervious=pd.read_excel(r"/Users/mohaksehgal/Documents/Work/MIS/IDFC/MARCH 20/IDFC_PAID FILE_30MARCH20.xlsx")

Ondate=pd.read_excel(r"/Users/mohaksehgal/Documents/Work/MIS/IDFC/MARCH 20/IDFC_PAID FILE_31MARCH20.xlsx")


LP=list(Pervious['AGREEMENTID'])
LO=list(Ondate['AGREEMENTID'])

for i in range(0,len(LP)):
    if LP[i] not in LO:
        print(LP[i])