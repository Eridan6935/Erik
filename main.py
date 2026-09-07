""""
    -[x] создать репозиторий проекта
    -[ ] реализовать цикл приложения
    -[ ] реализовать хранилище задач
"""
from random import choice
from tkinter.font import names

is_running = True
collection = ['task1, task2, task3'] #list
print("Добро пожаловать")
while is_running:
    print("1 - посмотреть задачи |\n"
          "2 - добавить задачу |\n"
          "3 - редактирование и удаление |\n"
          "4 - удаление задачи |\n"
          "5 - выход \n")
    choice_user = input("Введите свой выбор")
    match str(choice_user):
        case '1':
            for key,item in enumerate(collection):
                print(key + 1 , item)
        case '2':
            names_task = input("Введение имя задачи")
            collection.append(names_task)
        case '3':
            for key,item in enumerate(collection):
                print(key + 1 , item)
            select_edit = int(input("Введите номер задчи для редактирования"))
            edit_name = input("Укажите новое имя задачи")
            collection[select_edit - 1] = edit_name
        case '4':
            for key, item in enumerate(collection):
              print(key + 1, item)
            select_edit = int(input("Введите номер задчи для редактирования"))
            edit_name = input("Укажите новое имя задачи")
            collection.pop(select_edit - 1)
        case '5':
            is_running = False
            print("До свидания!")
        case _:
            print("Такого тут нету!")








# if __name__ == '__main__':
