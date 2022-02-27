
print("Давай поиграем. Я загадал слово, тебе нужно его отгадать по буквам")
word = "росомаха"
letters = []
attempts = 3
while attempts > 0:
    victory = True
    letter = input("Введите букву ")

    letters.append(letter)
    #print(letters)
    for char in word:
        if char in letters:
            print(char, end=" ")
        else:
            print("*", end=" ")
            victory = False
    print()
    if letter not in word:
        attempts = attempts - 1
        print("Такой буквы в слове нет. У тебя осталось попыток: " + str(attempts))
    if attempts == 0:
        print("Ты проиграл!")
    if victory == True:
        print("Ты победил!")
        break

