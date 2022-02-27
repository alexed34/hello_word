words = ['a', 'bb', 'ccc', 'a', 'bb', 'aaa', 'a']
now_words = []
for i in words:
    if i in now_words:
        number = 1
        name = i
        while True:
            now_name = i + str(number)
            if now_name in now_words:
                number += 1
            else:
                now_words.append(now_name)
                print(now_name)
                break

    else:
        now_words.append(i)
        print('ok')
print(now_words)