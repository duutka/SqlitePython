import sqlite
# Выполняем запрос
# Сюда необходимо вводить Фамилию
print("Введите фамилию автора, которого вы хотите найти")
author = str(input())
sqlite.selectAuthor(author)
