# -*- coding: utf-8 -*-
"""
Created on Sat May  4 20:50:47 2024

@author: simone
"""

A = ['B']
B = ['A','C','D']
C = ['B','E','F']
D = ['B','E']
E = ['C','D']
F = ['A','C']

NA = ['C','E']
NB = ['F']
NC = ['A','D']
ND = []
NE = []
NF = []

a = list((set(A) | set(B)) - set(A) - set(NA) - {'A'})
b = list((set(B) | set(A) | set(C) | set(D)) - set(B) - set(NB) - {'B'})    
c = list((set(C) | set(B) | set(E) | set(F)) - set(C) - set(NC) - {'C'})
d = list((set(D) | set(B) | set(E)) - set(D) - set(ND) - {'D'}) 
e = list((set(E) | set(C) | set(D)) - set(E) - set(NE) - {'E'})
f = list((set(F) | set(A) | set(C)) - set(F) - set(NF) - {'F'})
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)