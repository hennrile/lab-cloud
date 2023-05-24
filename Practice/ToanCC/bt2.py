# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 11:18:54 2023

@author: US
"""

n = 1001
x = [k/(n/2) for k in range (0,n)]
s = 0
for k in range(1,n):
    s = s + x[k]**2*(x[k]-x[k-1])
print(s)