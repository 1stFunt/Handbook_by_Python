# P - Формат ввода
# В каждой строке записано описание придорожной местности.
# Конец ввода обозначается пустой строкой.
# Формат вывода
# Определите список увиденного рядом с зайками без повторений.
# Порядок вывода не имеет значения.
# Примечание
# Считается, что объект находится рядом, если он записан справа или слева от требуемого.
set_rabbit = set()
while True:
    rabbit = input()
    temp = rabbit.split(" ")
    index = 0
    for r in temp:
        if r == "зайка":
            index = temp.index(r)
            set_rabbit.add(temp[index - 1] if temp[index] != temp[0] else "")
            set_rabbit.add(temp[index + 1] if temp[index] != temp[-1] else "")
            temp.remove(temp[index])
    if rabbit == "":
        break
for i in set_rabbit:
    if i != "":
        print(i)

# Q - Теория шести рукопожатий — социологическая теория, согласно которой любые два человека на Земле разделены не более, 
# чем пятью уровнями общих знакомых (и, соответственно, шестью уровнями связей). Формальная математическая формулировка 
# теории: диаметр графа знакомств не превышает 6. Мы не станем так сильно углубляться в дружественные связи и пока нам 
# хватит только двух уровней. Напишите программу, которая по списку дружественных пар для каждого человека определяет 
# список «друзей 2-го уровня».
# Формат ввода
# В каждой строке записывается два имени.
# Окончанием ввода служит пустая строка.
# Формат вывода
# Выведите список всех людей и их «друзей 2-го уровня» в формате «Человек: Друг1, Друг2, ...».
# Список людей и друзей в каждой строке требуется вывести в алфавитном порядке без повторений.
string = input()
friendship = dict()

while string != '': 
    secondname = string.split(' ')
    if secondname[0] not in friendship.keys():
        friendship[secondname[0]] = {secondname[1]}
    else:
        friendship[secondname[0]].add(secondname[1])
    if secondname[1] not in friendship.keys():
        friendship[secondname[1]] = {secondname[0]}
    else:
        friendship[secondname[1]].add(secondname[0])
    string = input()

friend_result = {key: set() for key in friendship.keys()}
for i in friendship.keys():
    for j in friendship[i]:
        temp = friendship[j].copy()
        temp.discard(i)
        temp.difference_update(friendship[i])
        friend_result[i] = friend_result[i].union(temp)
        
sort_res = sorted(friend_result.items(), key=lambda secondname: secondname[0])
for i in sort_res:
    print(f"{i[0]}: {', '.join(sorted(i[1]))}")

# R - На пиратской карте отмечено N точек, в которых зарыты сокровища. Каждая точка задана координатами (x, y)
# Координаты указаны в километрах. Команда Капитана Крюка хочет составить маршрут, чтобы собрать как можно больше кладов. 
# Однако есть ограничение: для любых двух соседних точек маршрута (xi, yi) и (xj, yj) координаты xi и xj могут различаться 
# только последней цифрой, как и координаты yi, yj тоже могут различаться только последней цифрой. Например, после точки (15, 10) 
# они могут отправиться в точку (18, 16), а вот из точки (14, 68) в точку (19, 71) пройти уже не получится, ведь 68 и 71 
# различаются не только последней цифрой. Из точки (5, 12) в точку (13, 14) попасть тоже нельзя, так как числа 5 и 13 отличаются 
# в разряде десятков. По заданным координатам определите, какое максимальное количество точек сможет добавить в свой маршрут 
# Капитан Крюк.
# Формат вывода
# Выведите одно число — максимальное количество точек, которое Капитан Крюк сможет посетить по маршруту, построенному 
# по описанным правилам.
# Формат ввода
# В первой строке указано число N < 10^5 — количество точек, отмеченных на карте сокровищ. 
# В следующих N строках содержатся пары координат: x, y координаты i - ой точки. Координаты — целые числа 
# не меньше нуля и не больше 10^9. Гарантируется, что совпадающих точек в списке нет.
num = int(input())
coordinates = [list(map(int, input().split(" "))) for i in range(num)]
dct = {}
for i in range(num):
    tuple = (coordinates[i][0] // 10, coordinates[i][1] // 10)
    if tuple not in dct:
        dct[tuple] = 0
    dct[tuple] += 1
print(max(dct.values()))        