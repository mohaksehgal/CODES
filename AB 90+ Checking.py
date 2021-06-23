#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 14:14:16 2020

@author: mohaksehgal
"""


import pandas as pd
import numpy as np

Pervious=pd.read_excel(r"/Users/mohaksehgal/Documents/Work/MIS/AB/90+/MARCH 20/ABFL_90+ PAID FILE 13 MARCH 20.xlsx")
Ondate=pd.read_excel(r"/Users/mohaksehgal/Documents/Work/MIS/AB/90+/MARCH 20/ABFL_90+ PAID FILE 31 MARCH 20.xlsx")

LP=list(Pervious['AGREEMENTID'])
LO=list(Ondate['AGREEMENTID'])

for i in range(0,len(LP)):
    if LP[i] not in LO:
        print(LP[i])