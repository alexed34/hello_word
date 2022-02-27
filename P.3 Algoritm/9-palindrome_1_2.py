"""
	number = 59
	Перевернем число 59 -> 95
	Если 59 == 95 
тогда: стоп 
иначе: идем дальше
	Сложим два числа:
	number = 59 + 95 = 154
	Перевернем число 154 -> 451
	Если 154 == 451 
тогда: стоп 
иначе: идем дальше
	Сложим два числа:
	number = 154+451=605
	Перевернем число 605 -> 506
	Если 605 == 506 
тогда: стоп 
иначе: идем дальше
	number = 605+506=1111
"""
count_1 = 0
count_2 = 0

def palindrome_search_1(number):
    global count_1
    while True:
        count_1+=1
##        numberStr1 = str(number) #переводим в строку число №1
##        numberStr2 = numberStr[::-1] #переворачиваем и получаем число №2
##        number = int(numberStr1)+int(numberStr2) #переводим в числа и суммируем
        numberStr = str(number) #переводим в строку
        number += int(numberStr[::-1]) #переворачиваем, переводим в число и суммируем с исходным
        # сравним исходное число с его перевертышем
        if str(number) == str(number)[::-1]:
            break
    return number

def palindrome_search_2(number):
    global count_2    #Объявляем переменную count_2 доступной в функции
    count_2 += 1       #Увеличиваем счетчик на 1
    numberStr = str(number)  #Переводим число в строку
    if numberStr == numberStr[::-1]:# Если строка равна перевернутой
        return number        #Тогда возвращаем палиндром
    # Получаем сумму оригинала и перевернутого чисел
    #number += int(numberStr[::-1])
    #вызываем рекурсию
    return palindrome_search_2(number+int(numberStr[::-1]))


print(palindrome_search_1(89),count_1)
print(palindrome_search_2(89),count_2)
