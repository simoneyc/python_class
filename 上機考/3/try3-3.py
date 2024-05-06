# -*- coding: utf-8 -*-
"""
Created on Sun May  5 21:49:15 2024

@author: simone
"""

f = open("data.txt","r")
s = f.readline()
#print(s)

words = s.replace("!", "").replace(".", "").replace(",", "").lower().split()

str_dict = {}
for word in words:
    if word in str_dict:
        str_dict[word] += 1
    else:
        str_dict[word] = 1
print(str_dict)