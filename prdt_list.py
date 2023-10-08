# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 19:17:53 2023

@author: hp
"""

def prdtList(list1):
    prdt = 1
    for i in list1:
        prdt = prdt * i 
    return prdt 
list2 = [1,2,3,4,5]
print("list is" ,list2)
result = prdtList(list2)
print("result is " ,result)