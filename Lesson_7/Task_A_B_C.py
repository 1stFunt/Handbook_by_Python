# A - Напишите списочное выражения для получения квадратов чисел из диапазона [a, b]
a, b = 1, 5
# Идеальное решение:
print([i ** 2 for i in range(int(input()), int(input()) + 1)])
# Фактически решение по условию должно выглядеть так:
[i ** 2 for i in range(a, b + 1)]
# a и b указывать не нужно, как и print()

# B - Таблица умножения 2.0
# Вашему решению будет предоставлена единственная переменная n — необходимый размер таблицы умножения.
# Идеальное решение:
n = int(input())
print([[i * j for i in range(1, n + 1)] for j in range(1, n + 1)])
# Фактическое решение по условиям: 
[[i * j for i in range(1, n + 1)] for j in range(1, n + 1)]

# C - Вашему решению будет предоставлена строка sentence слов, разделённых пробелами.
# Напишите списочное выражения для генерации списка длин слов.
sentence = "Мама мыла раму"
# Идеальное решение:
print([len(i) for i in input().split(" ")])
# Фактическое решение по условияем:
[len(i) for i in sentence.split(" ")]