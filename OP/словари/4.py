d = {'Hello':3,  'world': 2, 'Tasks': 1  }
aa = sorted(d, key=d.get)
print(aa)