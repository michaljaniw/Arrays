arr = [[0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0]]

for i in range(5):  
    for j in range(5):  
        arr[i][j] = (i + 1) * (j + 1)  


for i in arr:
    print(" ".join(map(str, i)))