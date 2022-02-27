import pytest





books = ["Гарри Поттер", "Властелин Колец", "Дядя Федор, пёс и кот"]
length = len(books)
for i in range(length):
    print(f"{i + 1}. {books[i]}")
