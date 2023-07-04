# S - Шифр Цезаря, также известный как шифр сдвига, код Цезаря — один из самых простых и наиболее широко 
# известных методов шифрования. Он назван в честь римского полководца Гая Юлия Цезаря, использовавшего 
# его для секретной переписки со своими генералами.
# Давайте реализуем эту систему шифрования. 
# Однако для простоты мы будем сдвигать только латинские символы по кругу.
# Чтение размера сдвига из ввода
shift = int(input())

# Чтение текста из файла public.txt
with open('public.txt', 'r') as f:
    text = f.read()

# Сдвиг символов в тексте
shifted_text = ''
for ch in text:
    if ch.isalpha():
        # Хранение информации о регистре буквы
        is_upper = ch.isupper()
        # Приведение буквы к нижнему регистру
        ch = ch.lower()
        # Сдвиг буквы
        ch = chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
        # Возвращение буквы к нужному регистру
        if is_upper:
            ch = ch.upper()
    shifted_text += ch
# Запись зашифрованного текста в файл private.txt
with open('private.txt', 'w') as f:
    f.write(shifted_text)

"""
S - Вы скорее всего знаете, что существуют не только текстовые файлы. 
Различные форматы данных предусматривают специальное кодирование. 
Например, BMP изображения хранят некоторую заголовочную информацию и цвета всех пикселей в виде чисел.
Давайте поработаем с такими данными. Нам дают файл в некотором формате, назовем его NUM. 
Он содержит список 2-байтных чисел. Для простоты будем считать, что отрицательных чисел не существует.
Напишите программу, которая вычисляет сумму всех записанных в файле чисел в 2-байтном диапазоне.
Формат ввода - В файле numbers.num содержатся числа в указанном формате.
Формат вывода - Одно число — сумма всех чисел в файле на 2-байтном диапазоне.
Примечание - Для простоты файлы в примерах записаны в HEX формате. В этом виде файл представляется 
как последовательность четырехзначных шестнадцатеричных чисел.
В первом примере записано 5 шестнадцатеричных чисел: 1, 2, 3, 4, 5. Их сумма равна 15.
Во втором — 255 и 257. Их сумма равна 512.
Файл из примеров в изначальном виде можно загрузить здесь: * Первый пример * Второй пример
Если вы хотите изучить принцип хранения целых чисел в ЭВМ, советуем почитать про прямой, 
обратный и дополнительный коды.
Ввод:
0001 0002 0003 0004 0005
Вывод:
15
"""
import struct

# Открываем файл numbers.num для чтения в бинарном режиме
with open('numbers.num', 'r', encoding="b") as f:
    # Инициализируем переменную sum нулем
    sum = 0
    # Читаем из файла 2 байта (по условию задачи это 2-байтное число)
    # и сразу переводим их в целое число
    while True:
        number_bytes = f.read(2)
        # Если мы дошли до конца файла, то number_bytes == b''
        if number_bytes == b'':
            break
        # Переводим байты в число, используя модуль struct
        number = struct.unpack('>h', number_bytes)[0]
        # Добавляем число к сумме
        sum += number
    # Выводим результат
    print(sum)