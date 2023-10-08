# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 20:15:16 2023

@author: hp
"""

def remduplicate(list) :
    newlist = [] 
    for num in list:
        if num not in newlist:
            newlist.append(num)
    return newlist 
L1 = [ 12 , 34 , 43 , 65 , 78 , 12 , 65 ]
print("List before removing duplicates" , L1)
print( "List After removing duplicates " , remduplicate(L1)) 


# list1 = [ 19 , 20 , 35 , 20 , 54 , 20] 
# print("List with duplicate values\n" ,list1)

# newlist = [] # empty list 

# for i in list1:
#     if i not in newlist:
#         newlist.append(i)
    
# print("List with distinct values\n" , newlist)