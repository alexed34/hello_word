import numpy as np

arr = np.random.randint(0,10,6) # 1- мин число 0, 2- макс число 10 , 3- колличество чисел
print(arr)
def buble(n, arr):
    count = 0
    for i in range(1,n):
        for j in range(n-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                count += 1
    for i in range(n):
        print(f'{i + 1} - {arr[i]}')



buble(6, arr)
