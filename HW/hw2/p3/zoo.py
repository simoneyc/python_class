class Animal:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id

class Zoo:
    def __init__(self):
        self.prairie = []
        self.desert = []
        self.arctic = []
        self.jungle = []

        self.NA = []
        self.NB = []
        self.NC = []
        self.ND = []
        self.NE = []
        self.dir = {'A':self.NA,'B':self.NB,'C':self.NC,'D':self.ND,'E':self.NE}

    def add_animal(self, block_name, animal):
        # 檢查是否符合
        # 根據區塊名稱將動物添加到相應的列表中
        if self.check(block_name, animal):
             
            if block_name == "prairie": #草原
                    self.prairie.append(animal)
                    print(animal.name, "added to prairie.")
            elif block_name == "desert": #沙漠
                    self.desert.append(animal)
                    print(animal.name, "added to desert.")
            elif block_name == "arctic": #北極
                    self.arctic.append(animal)
                    print(animal.name, "added to arctic.")
            elif block_name == "jungle": #叢林
                    self.jungle.append(animal)
                    print(animal.name, "added to jungle.")
        else:
            print(animal.name, "cannot join", block_name)
    
    def display_block(self, block_name):
        # 根據區塊名稱顯示該區塊中的所有動物
        print("Animals in", block_name + ":")
        if block_name == "prairie":
            for animal in self.prairie:
                print(animal.name+", Age: "+animal.age+",label:"+animal.id)
        elif block_name == "desert":
            for animal in self.desert:
                print(animal.name+", Age: "+animal.age+",label:"+animal.id)
        elif block_name == "arctic":
            for animal in self.arctic:
                print(animal.name+", Age: "+animal.age+",label:"+animal.id)
        elif block_name == "jungle":
            for animal in self.jungle:
                print(animal.name+", Age: "+animal.age+",label:"+animal.id)
    
    def species_characteristics(self,data):
        # 處理標籤對應資訊
        i = 0
        for d in data:
            if i == 0:
                i = 1
            else:    
                self.dir[f'{data[0]}'].append(d)

    def check(self, block_name, animal):
        if block_name == "prairie":
            block = self.prairie
        if block_name == "desert":
            block = self.desert
        if block_name == "arctic":
            block = self.arctic
        if block_name == "jungle":
            block = self.jungle
        for item in block:
            if item.id in self.dir[animal.id]:
                return False
        return True

