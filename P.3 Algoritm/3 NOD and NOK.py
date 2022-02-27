import sys
import time
sys.setrecursionlimit(200)
# def recursion(x):
#     print('Вызов №', x)
#     if x == 30:
#         return x
#     recursion(x+1)
#
# def print_list(x):
#     print(x.pop())
#     if len(x) == 0:
#         return '5'
#     print_list(x)
#
# def summ(x):
#     print(x)
#     if len(x)==1:
#         return x.pop()
#     return summ(x[:len(x)-1])+x.pop()
#
# print( summ( [ 1,1,31,213,312,1,3,2 ] ) )

def progressive(x):
    division = 2
    divisions = []
    while x != 1:
        while x%division == 0:
            divisions.append(division)
            x /= division
        division += 1
    return divisions


# print(progressive(12))
def nod_0(a,b):
    divisions_a = progressive(a)
    divisions_b = progressive(b)
    p = []
    for number in divisions_a:
        if number in divisions_b:
            p.append(number)
            divisions_b.remove(number)
    result = 1
    # print(p)
    for number in p:
        result *= number
    return result


def nok_0(a,b):
    divisions_a = progressive(a)
    divisions_b = progressive(b)
    # print(divisions_a)
    # print(divisions_b)
    p = []
    for number in divisions_a:

        if number not in divisions_b:
            p.append(number)
        else:

            count = divisions_a.count(number) - divisions_b.count(number)
            if count > 0 and count > p.count(number):
                p.append(number)
        # print(p)
    p = p + divisions_b
    result = 1
    # print(p)
    for number in p:
        result *= number
    return result


# print(progressive(180))
# print(progressive(100))
# print(nod_0(180,100))






def nod_1(a,b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def nod_2(a,b):
    while b != 0:
        r = b
        b = a % b
        a = r
    return a



def nod_3(a, b):
    if b == 0:
        return a
    return nod_3(b, a % b)
# print(nod_3(87,33))

def nod_4(a,b):
    return a if b==0 else nod_4(b,a%b)

start_time = time.time()
print(nod_4(33004444444,19004444444))
print(f'{(time.time() - start_time)}')