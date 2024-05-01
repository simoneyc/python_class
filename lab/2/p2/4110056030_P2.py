class stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

def check(input_string):
    _stack = stack()
    for char in input_string:
        if char in "([{":
            _stack.push(char)
        elif char in ")]}":
            if _stack.is_empty():
                return False
            else:
                top = _stack.pop()
                if (char == ")" and top != "(") or (char == "]" and top != "[") or (char == "}" and top != "{"):
                    return False
    return _stack.is_empty()

# 讀取測資檔案
with open("data.txt", "r") as file:
    lines = file.readlines()

# 去除換行符號
lines = [line.strip() for line in lines]

# 測試每一行括號匹配情況並輸出結果
for line in lines[1:]:  # 第一行為測資個數，不需要處理
    print(check(line))
