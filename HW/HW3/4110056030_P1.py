import matplotlib.pyplot as plt
from datetime import datetime
city3 = {}
city2 = {}
earthquake = {}
strenth = {} # 3
depth = {}
time = 0

def save():
    global time
    f1 = open('cityCoordinate.txt' ,'r', encoding='UTF-8') 
    f1.readline()
    for line in f1.readlines():
        line = line.replace(':', ' ').replace(',', ' ').split()
        city3[line[0]] = [float(line[2]), float(line[1])]
        city2[line[0]] = []
        depth[line[0]] = []
    f1.close()
    f2 = open('earthQuake.txt', 'r', encoding='UTF-8')
    f2.readline()
    for line in f2.readlines():
        line = line.split()
        if line != list() :
            time = str(line[0])
            time += (' ' + line[1])
            tmp = [float(line[_]) for _ in range(2, len(line))]
            earthquake[time] = tmp
            citycount(tmp)
    f2.close()

    power = [0,0,0,0,0,0,0,0,0]
    for key, value in city2.items():
        # print(value)
        for num in value:
            p = round(num[2])
            power[p] += 1
        strenth[key] = power
        power = [0,0,0,0,0,0,0,0,0]

def fun_0():
    with open("cityCoordinate.txt", "r", encoding="utf-8") as file:
        # 讀取檔案內容
        lines = file.readlines()
        # 列印縣市名稱
        for line in lines[1:]:  # 跳過第一行的標題
            city = line.split(":")[0]  # 使用冒號分割獲取縣市名稱部分
            print(city)
    

def distance(m1, m2, n1, n2):
    return abs(m1-n1) + abs(m2-n2)

def citycount(data):
    global time
    num1 = data[0]
    num2 = data[1]
    min = num1
    c = ''
    for i in city3:
        l = city3[i]
        d = distance(l[0], l[1], num1, num2)
        if d < min:
            min = d
            c = i
    city2[c].append(data)
    depth[c].extend([[time, data[3]]])
    i = 0

def fun_1():
    city_name = input()
    data = city2[city_name]
    for i in range(len(data)):
        print(f'{i+1}:{data[i]}')
    

def fun_2():
    with open("earthQuake.txt", 'r', encoding="utf-8") as file:
        # 跳過文件的第一行，因為它包含列名
        next(file)
        # 逐行讀取文件的其餘部分
        index = 1
        for line in file:
            # 去除每一行中的空格並以tab分割
            parts = line.strip().split('\t')
            # 將地震時間和數據部分分開
            earthquake_time, data = parts[0], parts[1:]
            # 格式化數據部分
            int_data = [float(d) for d in data]
            data = [earthquake_time] + int_data
            if len(data) < 2:
                break
            info = f"{index}:{data}"
            print(info)
            index += 1

def fun_3():
    city_name = input()
    data = strenth[city_name]
    print(data)
    # 橫軸座標
    x = range(len(data))
    # 劃出長條圖
    plt.bar(x, data)
    # 添加圖表標題
    plt.title('earthquake_history')
    # 顯示圖表
    plt.show()
    
def fun_4():
    city_name = input()
    data = depth[city_name][::-1]
    date = [datetime.strptime(x[0], '%Y/%m/%d %H:%M') for x in data]
    value = [x[1] for x in data]
    plt.xticks(rotation=30)
    plt.plot(date, value, linestyle='-')
    plt.title('depth table')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.show()


save()

while True:
    choice = input("0.縣市查詢 ,1.縣市地震查詢 ,3.歷年地震資訊 ,4.經緯度查詢 ,5.縣市地震深度 ,6退出: ")
    
    if choice == "0":
        fun_0()
    elif choice == "1":
        fun_1()
    elif choice == "2":
        fun_2()
    elif choice == "3":
        fun_3()
    elif choice == "4":
        fun_4()
    elif choice == "5":
        vertical = input('經度:').split()
        m1 = int(vertical[0])
        m2 = int(vertical[1])
        horizontal = input('緯度:').split()
        n1 = int(horizontal[0])
        n2 = int(horizontal[1])
        for i in earthquake:
            if m1 <= earthquake[i][0] <= m2 and n1 <= earthquake[i][1] <= n2:
                string = ", ".join(str(item) for item in earthquake[i])
                print(f"['{i}', {string}]")
        
    elif choice == "6":
        break
    else:
        print("Invalid choice")
