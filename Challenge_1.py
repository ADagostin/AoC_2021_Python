# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
Measurements = open ("C:\\Users\\dagostia\\Desktop\\C1_Measurements.txt","r")
Measurements2 = [int(i) for i in Measurements.read().split()]
output=0
for i in range(0,len(Measurements2)-1):
    if Measurements2[i]< Measurements2[i+1]:
        output+=1
print (output)