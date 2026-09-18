import sys
import platform
from platform import processor

list_os = []

os_name = platform.system()
os_version = platform.version()
os_arch = platform.architecture()[0]
build = os_version[:5]
processor_name = processor()
py_ver = platform.python_version()

list_task = [
    os_name,
    os_version,
    os_arch,
    build,
    processor_name,
    py_ver
]

for task in range(len(list_task)):
    list_os.append(list_task[task])

is_running = True

collection = ['task1', 'task2', 'task3']

print("Добро пожаловать")

while is_running:
    print("1 - посмотреть задачи |\n"
          "2 - добавить задачу |\n"
          "3 - редактирование задачи |\n"
          "4 - удаление задачи |\n"
          "5 - информация о системе |\n"
          "6 - выход \n")

    choice_user = input("Введите свой выбор: ")

    match str(choice_user):

        case '1':
            for key, item in enumerate(collection):
                print(key + 1, item)

        case '2':
            names_task = input("Введите имя задачи: ")
            collection.append(names_task)

        case '3':
            for key, item in enumerate(collection):
                print(key + 1, item)

            select_edit = int(
                input("Введите номер задачи для редактирования: ")
            )

            edit_name = input("Укажите новое имя задачи: ")

            collection[select_edit - 1] = edit_name

        case '4':
            for key, item in enumerate(collection):
                print(key + 1, item)

            select_delete = int(
                input("Введите номер задачи для удаления: ")
            )

            collection.pop(select_delete - 1)

        case '5':
            print("Информация о системе:")
            print("ОС:", list_os[0])
            print("Версия ОС:", list_os[1])
            print("Разрядность:", list_os[2])
            print("Build:", list_os[3])
            print("Процессор:", list_os[4])
            print("Версия Python:", list_os[5])

        case '6':
            is_running = False
            print("До свидания!")

        case _:
            print("Такого тут нету!")
