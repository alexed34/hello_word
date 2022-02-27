s1 = 'a?a'
s2 = 'aba?abf'
ls1 = len(s1)
ls2 = len(s2)
dl = ls2 - ls1
for j in range(dl + 1):
    check = True
    text = s2[j: j + ls1]
    for i in range(len(text)):
        if text[i] == s1[i] or text[i] == '?' or s1[i] == '?':
            continue
        else:
            check = False
            break
    if check:
        break
# else:
#     print('no')
print(['no', 'yes'][check])
