# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 10:05:11 2019

@author: arriba
"""

y = 1
print('*')
    
for row in range(2,6):
    asc = '*'
    output_ = ''
    col = 1
    while col <= row :
        output_= output_ + asc
        col = col + 1
        
    y = y + 1 
    print(output_)
    
