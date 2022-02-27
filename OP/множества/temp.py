a = [1, 3, 5, 7, 9, 16, 2]
b =[2, 4, 8, 1, 6, 15]
a = set(a)
a.symmetric_difference_update(b)
print(a)
# print(b)
#b = set(b)
print(a.isdisjoint(b) )