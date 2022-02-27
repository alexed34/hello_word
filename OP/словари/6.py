n = [1, 3, 2, 3, 2, 3, 2 ]
m = 6
dict1 = {}
dict1 = dict1.fromkeys(range(m+1), 0)
for i in n:
    dict1[i] +=1
summa = 0
n2 = 0
for i in dict1:
    if i == m - i:
        n2 = (i*(i - 1))//2
        print(i, n)
    else:
        n = dict1[i] * dict1[m - i]
        print(i, n)
        summa += n

print(summa//2 + n2)


