import pandas as pd  # Імпорт бібліотеки pandas

def output_text_to_console(text):
    """
    Виводить текст у консоль.

    Параметри:
    text (str): Текст, який потрібно вивести у консоль.
    """
    print(text)


def write_to_file(file_path, data):
    """
    Записує дані до файлу за допомогою вбудованих можливостей Python.

    Параметри:
    file_path (str): Шлях до файлу, в який потрібно записати дані.
    data (str): Дані, які потрібно записати у файл.
    """
    with open(file_path, 'w') as file:
        file.write(data)


# Приклад використання функцій
if __name__ == "__main__":
    # Приклад виводу тексту у консоль
    output_text_to_console("Це приклад виводу тексту у консоль.")

    # Приклад запису до файлу
    file_path = "output.txt"  # Замініть шлях на шлях до вашого файлу
    data_to_write = "Це приклад запису до файлу за допомогою вбудованих можливостей Python."
    write_to_file(file_path, data_to_write)
