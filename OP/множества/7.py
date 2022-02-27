'''Условие:
Вам дан массив чисел.
Ваша задача –разделить его на 2 массива, сумма элементов первого из которых строго больше суммы элементов второго.
При этом нужно минимизировать количество элементов в первом массиве.
Подсказка: числа могут повторяться, используйте multiset.'''

a = [1, 2, 3]
summa = sum(a)
len_a = len(a)
# n = int(input())
# a = []
# summa = 0
# for i in range(n):
#     n1 = int(input())
#     summa += n1
#     a.append(n1)
# print(summa)
# print(a)

a = sorted(a, reverse=True)
print(a)
first_sum = 0
count = 0
for i in a:
    first_sum += i
    count += 1
    if first_sum *2 > summa:
        break
print(count)





