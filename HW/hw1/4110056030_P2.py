def check_prize(invoice, num):
    # 創建獎項次數的字典
    prize_count = {'特別獎': 0, '特獎': 0, '頭獎': 0, '二獎': 0, '三獎': 0, '四獎': 0, '五獎': 0, '六獎': 0, '沒中獎': 0}
    
    # 對每張發票進行檢查
    for inv in invoice:
        # 檢查是否中特別獎
        if inv == num[0][0]:
            prize_count['特別獎'] += 1
            pass
        # 檢查是否中特獎
        elif inv == num[1][0]:
            prize_count['特獎'] += 1
            pass
        # 檢查是否中頭獎
        elif inv in num[2]:
            prize_count['頭獎'] += 1
            pass
        # 檢查是否中二獎
        elif inv[1:] == num[2][0][1:] or inv[1:] == num[2][1][1:] or inv[1:] == num[2][2][1:]:
            prize_count['二獎'] += 1
            pass
        # 檢查是否中三獎
        elif inv[2:] == num[2][0][2:] or inv[2:] == num[2][1][2:] or inv[2:] == num[2][2][2:]:
            prize_count['三獎'] += 1
            pass
        # 檢查是否中四獎
        elif inv[3:] == num[2][0][3:] or inv[3:] == num[2][1][3:] or inv[3:] == num[2][2][3:]:
            prize_count['四獎'] += 1
            pass
        # 檢查是否中五獎
        elif inv[4:] == num[2][0][4:] or inv[4:] == num[2][1][4:] or inv[4:] == num[2][2][4:]:
            prize_count['五獎'] += 1
            pass
        # 檢查是否中六獎
        elif inv[5:] == num[2][0][5:] or inv[5:] == num[2][1][5:] or inv[5:] == num[2][2][5:] or (inv[5:] in num[3]):
            prize_count['六獎'] += 1
            pass
        # 若都沒中獎，則視為沒中獎
        else:
            prize_count['沒中獎'] += 1
            pass
    return prize_count

# 測試
#        [0][0]       [1][0]        [2][0]       [2][1]     [2][2]       [3][0]  [3][1]  [3][2]  
num = [["59647042"], ["01260528"], ["01616970", "69921388", "53451508"], ["710", "042", "633"]]
invoice = ["53977042", "67921388", "01260528", "91132057"]


result = check_prize(invoice, num)
print(result)
