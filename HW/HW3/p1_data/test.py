# -*- coding: utf-8 -*-
city = {}
city2 = {}
earthquake = {}
def distance(m1, m2, n1, n2):
    return abs(m1-n1) + abs(m2-n2)
def citycount(data):
    num1 = data[0]
    num2 = data[1]
    min = num1
    c = ''
    for i in city:
        l = city[i]
        d = distance(l[0], l[1], num1, num2)
        if d < min:
            min = d
            c = i
    city2[c].append(data)
f1 = open('cityCoordinate.txt' ,'r', encoding='UTF-8') 
f1.readline()
for line in f1.readlines():
    line = line.replace(':', ' ').replace(',', ' ').split()
    city[line[0]] = [float(line[2]), float(line[1])]
    city2[line[0]] = []
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

while 1 :
    num = int(input('0.縣市查詢 1.縣市地震查詢 2.歷年地震資訊 3.強度表 4.深度表 5.經緯度查詢法 6.退出\n'))
    if num == 0:
        for i in city:
            print(i)
    elif num == 1:
        choice = input()
        data = city2[choice]
        for i in range(len(data)):
            print(f'{i+1}:{data[i]}')
    elif num == 2:
        for index, (key, value) in enumerate(earthquake.items(), start=1):
            tmp = ", ".join(str(item) for item in value)
            print(f'{index}:[{key}, {tmp}]')
    elif num == 6:
        break