raw_input = input()
used = set()
for i in raw_input.split():
    n = int(i)
    if n in used:
        print('YES')
    else:
        print('NO')
        used.add(n)

w


