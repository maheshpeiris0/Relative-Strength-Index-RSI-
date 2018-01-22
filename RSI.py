# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 15:12:39 2018

@author: peirmah
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

file_path = r'Z:\Tech Smart Beta Project\Python\ML\Technical Models\BP.csv'

df = pd.read_csv(file_path)
df['Date'] = pd.to_datetime(df['Date'])

k = []
q = []
Average_Gain =[]
Average_Loss = []
RSI = []

def daily_return(share_price):
    ptc_return = share_price[1:]/share_price[:-1].values -1

    z = ptc_return.iloc[0:14,] 

    for i in range(len(z)):

        if z[i+1]>0:
            k.append(z[i+1])
        else:
            q.append(z[i+1])

    Average_Gain.append(abs(np.mean(k)))
    Average_Loss.append(abs(np.mean(q)))

    print(len(ptc_return))
    print(Average_Gain)


    w = 0
    v = 0
    for i in range(len(ptc_return)-13):

        if ptc_return[i+14] >0:

            Average_Gain.append(((Average_Gain[w])*13 +ptc_return[i+14])/14)
            Average_Loss.append(abs(((Average_Loss[v])*14 + 0)/14))
            w+=1
            v+=1
        else:
            
            Average_Loss.append(abs(((Average_Loss[v])*13 +ptc_return[i+14])/14))
            Average_Gain.append(((Average_Gain[w])*14 +0)/14)
            v+=1
            w+=1
            
    
            
    
    for i in range(len(Average_Loss)):
        RSI.append((100/(1+(Average_Gain[i]/Average_Loss[i]))))
        
        

    print(RSI)
            
            
        
        
daily_return(df['Adj Close'])


