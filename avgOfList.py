# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 18:04:24 2023

@author: hp
"""

n = int(input("Enter the number of elements to be inserted:"))
a = []
for i in range(0 , n):
    elem = int(input("Enter value of element:" ))
    a.append(elem)
print("list = ", a)
avg = sum(a)/n # len(a) can also be used instead of n 
print("Average of list elements = " , avg)
