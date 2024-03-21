"""
Решение номера 1 препрофессионального экзамена.
Программа получает на вход файл с таблицей, ищет все ошибки с содержанием числа 55, заменяет поля этих ошибок на DONE и
меняет дату на 0000-00-00, после записывает все в новый файл.
"""

from csv import reader, writer

# Первая часть задания
with open("game.txt", 'r', encoding='utf-8') as data_file:  # Открытие файла на чтение
    data = list(reader(data_file, delimiter='$'))  # Создание списка со значениями из таблицы
    header_line = data.pop(0)  # Получение заголовка таблицы
    for x in range(1, len(data)):  # Линейный поиск ошибки с содержанием числа 55
        if '55' in data[x][2]:  # Проверка на нахождение числа 55 в поле
            print(f'У персонажа {data[x][1]} в игре {data[x][0]} нашлась ошибка с кодом: {data[x][2]}. '
                  f'Дата фиксации: {data[x][3]}')  # Вывод всех строк с ошибкой

# Вторая часть задания
with open('game.txt', 'r', encoding='utf-8') as data_file:  # Открытие файла на чтение
    for z in range(1, len(data)):  # Линейный поиск ошибки с содержание числа 55
        if '55' in data[z][2]:  # Проверка на нахождение числа 55 в поле
            data[z][2] = 'Done'  # Замена ошибки на Done
            data[z][3] = '0000-00-00'  # Замена даты на 0000-00-00

with open('game_new.csv', 'w', encoding='utf-8') as data_file:  # Открытие файла на запись
    writing = writer(data_file, delimiter='$')
    writing.writerow(header_line)  # Запись заголовка в новый файл
    writing.writerows(data)  # Запись новых значений из  файла 'game.txt'




