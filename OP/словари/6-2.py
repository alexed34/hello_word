import time
tim1 = time.time()

n = [1, 3, 2, 3, 2, 3, 2 ]
m = 6
# n = [1, 3, 2, 3, 2, 3, 2 ]
# m = 5
s = 0
s2 = 0
for i in range(len(n)):
    for a in n[i:]:
        #print(n[i:])
        if a == m//2 and n[i] + a == m:
            # print(n[i])
            s2 += 1
        elif n[i] + a == m:
            s +=1

print(s+ (s2//2) )
