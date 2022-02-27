b = '?bf'
a = 'aba?abf'
t = 0
for i in range(len(a)):
    if a[i] == b[0] or a[i] == '?' or b[0] == '?':
        print(a[i], i, end='  -  ')
        for k in range(len(b)):
            if i + k < len(a) and a[i + k] == b[k] or a[i + k] == '?' or b[k] == '?':
                t += 1
            else:
                break
        if t == len(b):
            print('yes')
            exit()
        t = 0
print('no')
