# -*- coding: utf-8 -*-
"""
Created on Sat May  4 20:58:52 2024

@author: simone
"""

# 測試
#        [0][0]       [1][0]        [2][0]       [2][1]     [2][2]       [3][0]  [3][1]  [3][2]  
num = [["59647042"], ["01260528"], ["01616970", "69921388", "53451508"], ["710", "042", "633"]]
invoice = ["91132057", "53977042", "69565958", "13359685", "52822508", "64268088", "95756107", "67921388", "15269483", "31208591", "85601171", "31697745", "94191710", "87883887", "33598443", "01260528", "01626970"]

prize_cnt = {'特別獎':0,'特獎':0,'頭獎':0,'二獎':0,'三獎':0,'四獎':0,'五獎':0,'六獎':0,'沒中獎':0}

for inv in invoice:
    if inv == num[0][0]:
        prize_cnt['特別獎'] += 1
        pass
    elif inv == num[1][0]:
        prize_cnt['特獎'] += 1
        pass
    elif inv in num[2]:
        prize_cnt['頭獎'] += 1
        pass
    elif inv[1:] == num[2][0][1:] or inv[1:] == num[2][1][1:] or inv[1:] == num[2][2][1:]:
        prize_cnt['二獎'] += 1
        pass
    elif inv[2:] == num[2][0][2:] or inv[2:] == num[2][1][2:] or inv[2:] == num[2][2][2:]:
        prize_cnt['三獎'] += 1
        pass
    elif inv[3:] == num[2][0][3:] or inv[3:] == num[2][1][3:] or inv[3:] == num[2][2][3:]:
        prize_cnt['四獎'] += 1
        pass
    elif inv[4:] == num[2][0][4:] or inv[4:] == num[2][1][4:] or inv[4:] == num[2][2][4:]:
        prize_cnt['五獎'] += 1
        pass
    elif inv[5:] == num[2][0][5:] or inv[5:] == num[2][1][5:] or inv[5:] == num[2][2][5:] or (inv[5:] in num[3]):
        prize_cnt['六獎'] += 1
        pass
    else:
        prize_cnt['沒中獎'] += 1
        pass

print(prize_cnt)