'''Задача No3.
Запросы.
Условие:На вход программе даётся N слов.
Далее даётся ещё m запросов.
Необходимо узнать, сколько слово из запроса встречается в исходных N словах.
Формат входных данных: На вход даётся число N, N слов, число M и M запросов.
Формат выходных данных: Выведете, сколько встречается раз в N словах каждое слово из запроса.'''

n = int(input())
d = {}
for i in range(n):
    word = input()
    if word in d:
        d[word] += 1
    else:
        d[word] = 1

m = int(input())
m_list = []
for i in range(m):
    word = input()
    m_list.append(word)
for word in m_list():
    if word in d:
        print(d[word])
    else:
        print(0)

print(d)

