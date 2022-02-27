n = int(input())
d =  {}
for i in range(n):
    a, b = input().split()
    d[a] = b
    d[b] = a
n2 = input()
print(d[n2])
