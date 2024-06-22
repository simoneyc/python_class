from zoo import Animal
from zoo import Zoo


f = open('data.txt','r') #read txt

zoo = Zoo()


#特徵
for i in  range(5):  
    data = f.readline()
    data =data.split()
    zoo.species_characteristics(data)

print(zoo.dir) #查詢動物資訊表

# 動物添加功能

num = f.readline()
num = int(num) 

for i in range(num) :
    data = f.readline()
    data = data.split()
    zoo.add_animal(data[0],Animal(data[1],data[2],data[3])) 


# 園區顯示功能
block_name = ["prairie","desert","arctic","jungle"]
for block in block_name:
    zoo.display_block(block)


f.close()