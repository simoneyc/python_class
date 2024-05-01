import numpy as np

with open("data.txt", "r") as file:
    data = file.readlines()

M,N = map(int, data[0].split())

image = np.array([[int(num) for num in string.strip().split()] for string in data[1:M+1]])

m,n = map(int, data[M+2].split())
mask = np.array([[int(num) for num in string.strip().split()] for string in data[M+3:M+3+m]]) # 中間卡了一行'\n'

convolution = np.zeros((M - m + 1, N - n + 1)) # 設定output大小

for i in range(M - m + 1): 
    for j in range(N - n + 1):
        convolution[i, j] = int(np.sum(image[i:i+m, j:j+n] * mask))
print(convolution.astype(int))