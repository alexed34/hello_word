a = 'aba?abf'
b = '?baqq'
ls1 = len(a)
ls2 = len(b)
dl = ls1 - ls2
for q in range(dl + 1):
    curr_ok = True
    for i in range(ls2):
        if b[i] == '?' or a[q + i] == '?':
            continue
        if b[i] != a[q + i]:
            curr_ok = False
            break
    if curr_ok:
        print('yes')
        break
    elif q == dl:
        print('noy')
