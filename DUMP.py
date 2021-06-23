#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 16:00:18 2020

@author: mohaksehgal
"""


import pandas as pd
import numpy as np

M=pd.read_excel(r'/Users/mohaksehgal/Documents/Work/Dump/MARCH 20 DUMP/DUMP REPORT 16 MAR 20.xlsx')

M2=M.loc[:,['PROCESS','Call Date','Agent ID','Status','LOAN NO.']]

M2.to_excel(r'/Users/mohaksehgal/Documents/Work/DUMP/Master File.xlsx',index=False)