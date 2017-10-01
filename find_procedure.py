# Задание
# мне нужно отыскать файл среди десятков других
# я знаю некоторые части этого файла (на память или из другого источника)
# я ищу только среди .sql файлов
# 1. программа ожидает строку, которую будет искать (input())
# после того, как строка введена, программа ищет её во всех файлах
# выводит список найденных файлов построчно
# выводит количество найденных файлов
# 2. снова ожидает ввод
# поиск происходит только среди найденных на этапе 1
# 3. снова ожидает ввод
# ...
# Выход из программы программировать не нужно.
# Достаточно принудительно остановить, для этого можете нажать Ctrl + C

# Пример на настоящих данных

# python3 find_procedure.py
# Введите строку: INSERT
# ... большой список файлов ...
# Всего: 301
# Введите строку: APPLICATION_SETUP
# ... большой список файлов ...
# Всего: 26
# Введите строку: A400M
# ... большой список файлов ...
# Всего: 17
# Введите строку: 0.0
# Migrations/000_PSE_Application_setup.sql
# Migrations/100_1-32_PSE_Application_setup.sql
# Всего: 2
# Введите строку: 2.0
# Migrations/000_PSE_Application_setup.sql
# Всего: 1

# не забываем организовывать собственный код в функции

import os

migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))


def find_sql(files):
    sql_files = []
    for file in files:
        if file.endswith('.sql'):
            sql_files.append(file)
    return sql_files


def find_str_infile(sql_files, find_str):
    find_files = []
    for file in sql_files:
        with open(os.path.join(migrations, file)) as f:
            for line in f:
                if find_str in line:
                    find_files.append(file)
                    break
    return find_files


def print_list_of_files(find_files):
    for file in find_files:
        print('\n'.join(find_files))
    print('Всего {}'.format(len(find_files)))


if __name__ == '__main__':
    files = os.listdir(migrations)
    sql_files = find_sql(files)
    while True:
        find_str = input('Введите строку: ')
        find_files = find_str_infile(sql_files, find_str)
        print_list_of_files(find_files)
        sql_files = find_files.copy()
        find_files.clear()
