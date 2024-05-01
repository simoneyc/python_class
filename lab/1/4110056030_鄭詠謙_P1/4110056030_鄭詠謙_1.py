# -*- coding: utf-8 -*-

A = ['B']
B = ['A','C','D']
C = ['B','E','F']
D = ['B','E']
E = ['C','D']
F = ['A','C']

NA = ['C','E']
NB = ['F']
NC = ['A','D']


a = list((set(A) | set(B)) - set(A) - set(NA) - {'A'})
print(f'A = {a}')
b = list((set(B) | set(A) | set(C) | set(D)) - set(B) - set(NB) - {'B'})
print(f'B = {b}')
c = list((set(C) | set(B) | set(E) | set(F)) - set(C) - set(NC) - {'C'})
print(f'C = {c}')
d = list((set(D) | set(B) | set(E)) - set(D) - {'D'})
print(f'D = {d}')
e = list((set(E) | set(C) | set(D)) - set(E) - {'E'})
print(f'E = {e}')
f = list((set(F) | set(A) | set(C)) - set(F) - {'F'})
print(f'F = {f}')




