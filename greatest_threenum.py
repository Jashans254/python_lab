# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 19:11:49 2023

@author: hp
"""

#find greatest among 3 no.
a=int(input("Enter num1: "))
b=int(input("Enter num2: "))
c=int(input("Enter num3: "))
if(a>b):
    if(a>c):
        print("num1 is greatest")
    else:
        print("num3 is greatest")
elif(b>a) : 
    if(b>c):
         print("num2 is greatest")
    else:
        print("num3 is greatest")
elif(c>a):
    if(c>b):
        print("num3 is greatest")   
elif(a==b):
    if(b==c):
        print("All no. are equal to each other ")         
else:
    print("Enter valid no.")
    
    
    