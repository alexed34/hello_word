'''Парадокс дня рождения, также называемый
Проблема дня рождения, удивительно высокая
вероятность того, что два человека получат
тот же день рождения даже в небольшой группе людей.
В группе из 70 человек вероятность 99,9%
двух человек, у которых совпадают дни рождения. Но даже
в группе из 23 человек 50 процентов
шанс совпадающего дня рождения. Эта программа предназначена для
формирует несколько вероятностных экспериментов для определения
проценты для групп разного размера. Мы называем эти типы экспериментов
ции, в которых мы проводим несколько случайных испытаний, чтобы понять
вероятные исходы, эксперименты Монте-Карло.
Вы можете узнать больше о парадоксе дня рождения на https://en.wikipedia
.org / wiki / Birthday_problem.'''

import datetime, random


def getBirthdays(numberOfBirthdays:int)->list:
    """Returns a list of number random date objects for birthdays."""
    birthdays = []
    for i in range(numberOfBirthdays):
        # The year is unimportant for our simulation, as long as all
        # birthdays have the same year.
        startOfYear = datetime.date(2020, 1, 1)

        # Get a random day into the year:
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays


def getMatch(birthdays: list)->datetime:
    """Возвращает объект даты дня рождения, который встречается более одного раза.
     в списке дней рождения."""
    if len(birthdays) == len(set(birthdays)):
        return None  # All birthdays are unique, so return None.

    # Compare each birthday to every other birthday:
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1:]):
            # print(birthdayA, birthdayB)
            if birthdayA == birthdayB:
                return birthdayA  # Return the matching birthday.


# Display the intro:
print('''Парадокс дня рождения, автор Эла Свигарта al@inventwithpython.com

Парадокс дня рождения показывает нам, что в группе из N человек шансы
То, что у двоих из них совпадают дни рождения, на удивление велико.
Эта программа выполняет моделирование методом Монте-Карло (т. Е. Повторяющееся случайное
моделирования), чтобы изучить эту концепцию.

(На самом деле это не парадокс, это просто удивительный результат.)
''')

# Set up a tuple of month names in order:
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True:  # Keep asking until the user enters a valid amount.
    print('Сколько дней рождения мне создать? (Макс 100)')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = int(response)
        break  # User has entered a valid amount.
print()

# Generate and display the birthdays:
print('Здесь', numBDays, 'дней рождений:')
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        # Display a comma for each birthday after the first birthday.
        print(', ', end='')
    monthName = MONTHS[birthday.month - 1]
    dateText = f'{monthName} {birthday.day}'
    print(dateText, end='')
print()
print()

# Определите, совпадают ли два дня рождения.
match = getMatch(birthdays)

# Display the results:
print('In this simulation, ', end='')
if match != None:
    monthName = MONTHS[match.month - 1]
    dateText = '{} {}'.format(monthName, match.day)
    print('multiple people have a birthday on', dateText)
else:
    print('there are no matching birthdays.')
print()

# Run through 100,000 simulations:
print('Generating', numBDays, 'random birthdays 100,000 times...')
input('Press Enter to begin...')

print('Let\'s run another 100,000 simulations.')
simMatch = 0  # How many simulations had matching birthdays in them.
for i in range(100_000):
    # Report on the progress every 10,000 simulations:
    if i % 10_00 == 0:
        print(i, 'simulations run...')
    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) != None:
        simMatch = simMatch + 1
print('100,000 simulations run.')

# Display simulation results:
probability = round(simMatch / 100_000 * 100, 2)
print('Из 100000 симуляций ', numBDays, 'людей, там было')
print('совпадающий день рождения в этой группе', simMatch, 'раз. Это означает')
print('что', numBDays, 'у людей есть', probability, '% шанс')
print('совпадающий день рождения в их группе.')
print('Это, наверное, больше, чем вы думаете!')