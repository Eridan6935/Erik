import os

# Глобальный список для хранения задач в оперативной памяти
tasks = []
FILENAME = "tasks.txt"


def load_tasks_from_file():
    """Загрузка задач из текстового файла формата txt."""
    if os.path.exists(FILENAME):
        with open(FILENAME, "r", encoding="utf-8") as file:
            for line in file:
                task = line.strip()
                if task:
                    tasks.append(task)
        print(f"[+] Успешно загружено задач из файла: {len(tasks)}")
    else:
        print("[!] Файл с задачами не найден. Будет создан новый при сохранении.")


def save_tasks_to_file():
    """Сохранение задач в текстовый файл формата txt."""
    with open(FILENAME, "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(f"{task}\n")
    print("[+] Задачи успешно сохранены в файл tasks.txt!")


def show_tasks():
    """Отформатированный вывод коллекции задач с удобным отображением."""
    print("\n--- СПИСОК ЗАДАЧ ---")
    if not tasks:
        print("Список задач пуст.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    print("--------------------\n")


def add_task():
    """Функция добавления новой задачи."""
    new_task = input("Введите новую задачу: ").strip()
    if new_task:
        tasks.append(new_task)
        print(f"[+] Задача '{new_task}' успешно добавлена!")
    else:
        print("[!] Ошибка: текст задачи не может быть пустым.")


def edited_task():
    """Функция изменения (редактирования) существующей задачи."""
    show_tasks()
    if not tasks:
        return

    try:
        task_num = int(input("Введите номер задачи для изменения: "))
        if 1 <= task_num <= len(tasks):
            old_task = tasks[task_num - 1]
            updated_text = input(f"Введите новый текст задачи (было '{old_task}'): ").strip()
            if updated_text:
                tasks[task_num - 1] = updated_text
                print(f"[+] Задача №{task_num} успешно изменена!")
            else:
                print("[!] Ошибка: новый текст не может быть пустым.")
        else:
            print("[!] Ошибка: задачи с таким номером не существует.")
    except ValueError:
        print("[!] Ошибка: введите корректное число.")


def deleted_task():
    """Функция удаления задачи."""
    show_tasks()
    if not tasks:
        return

    try:
        task_num = int(input("Введите номер задачи для удаления: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"[+] Задача '{removed_task}' успешно удалена!")
        else:
            print("[!] Ошибка: задачи с таким номером не существует.")
    except ValueError:
        print("[!] Ошибка: введите корректное число.")


def main():
    """Главная функция со структурой while и match-case."""
    load_tasks_from_file()

    while True:
        print("\n=== TASK MANAGER (v0.0.7) ===")
        print("1. Посмотреть список задач")
        print("2. Добавить задачу")
        print("3. Изменить задачу")
        print("4. Удалить задачу")
        print("5. Сохранить и выйти")

        choice = input("Выберите действие (1-5): ").strip()

        # Использование конструкции match-case
        match choice:
            case "1":
                show_tasks()
            case "2":
                add_task()
            case "3":
                edited_task()  # Вызов внецикловой функции редактирования
            case "4":
                deleted_task()  # Вызов внецикловой функции удаления
            case "5":
                save_tasks_to_file()
                print("Завершение работы программы. До свидания!")
                break
            case _:
                print("[!] Неверный выбор! Пожалуйста, введите цифру от 1 до 5.")


# Вызов главной функции в конце скрипта
if __name__ == "__main__":
    main()
