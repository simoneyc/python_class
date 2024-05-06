# -*- coding: utf-8 -*-
"""
Created on Sat May  4 21:09:50 2024

@author: simone
"""

s = 'Twinkle, twinkle, little star! How I wonder what you are, \
    Up above the world so high, \
        Like a diamond in the sky. \
            When the blazing sun is gone, \
                When he nothing shines upon, \
                    Then you show your little light, \
                        Twinkle, twinkle all the night.'

s = s.replace(',','').replace('.','').replace('!','').lower()
words = s.split()

word_dict = {}
for word in words:
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1

print(word_dict)