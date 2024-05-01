import matplotlib.pyplot as plt

# 讀入file
data_file = "data.txt"
with open(data_file, "r", encoding="utf-8") as file:
    lines = file.readlines()

date = []
data1 =[]
data2 = []

for line in lines:
    if line.startswith("-"):
        company = ""
    if "各日成交資訊" in line:
        parts = line.split()
        company = parts[1]

    if line.strip():
        if line.startswith("日期"):
            continue

        parts = line.split()
        if len(parts) < 5:
            continue
        
        if company == '2330':
            data1.append(float(parts[4]))
            date.append(parts[0])
        if company == '2303':
            data2.append(float(parts[4]))

plt.figure(figsize=(12, 6)) #調整視窗大小
plt.plot(date,data1,'s-',label="2330")
plt.plot(date,data2,'o-',label="2303")
plt.xlabel("Date")
plt.ylabel("Closing Price")
plt.title('Stock Price Trends')
plt.grid(True) # 加上網格
plt.legend(loc = "best")
plt.show()