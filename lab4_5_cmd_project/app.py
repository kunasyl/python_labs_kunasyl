"""
Задачи:
1. Нужно поставить начальную директорию с диска C:/
2. Создать команду “ls” или “dir” для показа всех существующих директорий в находящейся папке
3. Сделать переход между директориями через команду “cd Название папки“ и “cd ..“ чтобы выйти назад, в противном случае вывести Exception что не найдена директория
4. Сделать Команды для создание, удаление, переименование Папок и Файлов
5. Сделать просмотр файлов как .txt, .md и других расширений
6. Придумать интерфейс и логику для данной задачи, чтобы она выглядела как стандартный CMD
БОНУС: Можете добавить другой функционал который сможете придумать, зависеть от вашей креативности.(Например, доступ к командной строке по Роли пользователя. Админ может делать все эти комманды через свою же консоль, а обычный Пользователь не может этого сделать).
"""

import os, sys

def init():
    os.chdir("C:\\")

    while True:
        main_path = os.getcwd()
        input_data = input(f"{main_path} >> ")
        command = input_data.split(maxsplit=1)[0]

        if command == 'q':
            sys.exit(0)

        path = "".join(input_data.split(maxsplit=1)[1:])

        if command in ("ls", "dir"):
            print(os.listdir(main_path))

        if command == "cd":
            try:
                folders = path.split("\\")

                for folder in folders:
                    if folder == "..":
                        main_path = os.path.abspath('..')
                    else:
                        main_path = f"{main_path}\\{folder}"

                    os.chdir(f"{main_path}\\")
                
            except FileNotFoundError:
                print("Path is incorrect")

        if command == "cat":
            try:
                open(f"{main_path}\\{path}", 'w').close()
            except OSError:
                print('Failed creating the file')

        if command == "mkdir":
            os.mkdir(f"{main_path}\\{path}")
        
        if command == "rm":
            try:
                if os.path.exists(f"{main_path}\\{path}") and os.path.isfile(f"{main_path}\\{path}"):
                    os.remove(path)
                    print('File successfully deleted')
                else:
                    print('File does not exist')
            except OSError:
                print('Error deleting a file')

        if command == "rmdir":
            try:
                if os.path.exists(f"{main_path}\\{path}") and os.path.isdir(f"{main_path}\\{path}"):
                    os.rmdir(f"{main_path}\\{path}")
                    print('Directory successfully deleted')
                else:
                    print('Incorrect path')
            except OSError:
                print('Error deleting a diractory')

        if command == "mv":
            [src, dest] = path.split(maxsplit=1)
            try:
                if os.path.exists(f"{main_path}\\{src}"):
                    os.rename(src, dest)
                else:
                    print('Incorrect path')
            except OSError:
                print('Error renaming the file')

        if command == "read":
            if os.path.exists(f"{main_path}\\{path}"):
                fl = open(f"{main_path}\\{path}", "r")
                fl_data = fl.readlines()
                for line in fl_data:
                    print(line)
                fl.close()
            else:
                print('File does not exist')

        if command == "write":
            if os.path.exists(f"{main_path}\\{path}"):
                print("Please enter data: ")
                data = input()
                fl = open(f"{main_path}\\{path}", "a")
                fl.writelines(data)
                fl.close()
            else:
                print('File does not exist')


if __name__ == '__main__':
    init()