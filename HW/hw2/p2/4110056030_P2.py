# 讀檔
with open('input.txt','r') as file:
    lines = file.readlines()

# init
# 字典存
student_data = {}
temp_id = None
temp_text = ""

# 每行字
for line in lines:
    line = line.strip()
    if line.startswith("###"):
        if temp_id is not None:
            student_data[temp_id] = temp_text
        temp_id = line[3:]
        temp_text = ""
    else:
        # 把字加進去
        temp_text += line + "\n"

# 把最後一個丟進去
if temp_id is not None:
    student_data[temp_id] = temp_text

# sort按學號
sort_id = dict(sorted(student_data.items(),key=lambda item: int(item[0])))

# 輸出
with open('output.txt', 'w') as output_file:
    for student_id, text in sort_id.items():
        output_file.write(student_id + "\n")
        output_file.write(text.strip() + "\n\n")
