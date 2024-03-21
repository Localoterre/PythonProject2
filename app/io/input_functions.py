import pandas as pd

def input_text_from_console():
    """
    Зчитує текст з консолі.

    Повертає:
    str: Текст, введений користувачем у консолі.
    """
    text = input("Введіть текст: ")
    return text


def read_from_file(file_path):
    """
    Зчитує дані з файлу за допомогою вбудованих можливостей Python.

    Параметри:
    file_path (str): Шлях до файлу, з якого потрібно зчитати дані.

    Повертає:
    str: Дані, зчитані з файлу.
    """
    try:
        with open(file_path, 'r') as file:
            data = file.read()
        return data
    except FileNotFoundError:
        return "Файл не знайдено."


def read_with_pandas(file_path):
    """
    Зчитує дані з файлу за допомогою бібліотеки pandas.

    Параметри:
    file_path (str): Шлях до файлу, з якого потрібно зчитати дані.

    Повертає:
    pandas.DataFrame або str: Об'єкт DataFrame з даними з файлу, якщо файл існує, або повідомлення про помилку,
    якщо файл не знайдено.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        return "Файл не знайдено."


# Приклад використання функцій
if __name__ == "__main__":
    # Вводимо текст з консолі
    text_from_console = input_text_from_console()
    print("Введений текст:", text_from_console)

    # Зчитуємо з файлу за допомогою вбудованих можливостей Python
    file_path = "example.txt"  # Замініть шлях на шлях до вашого файлу
    data_from_file = read_from_file(file_path)
    print("Зміст файлу:", data_from_file)

    # Зчитуємо з файлу за допомогою бібліотеки pandas
    csv_file_path = "example.csv"  # Замініть шлях на шлях до вашого CSV файлу
    data_with_pandas = read_with_pandas(csv_file_path)
    print("Дані з файлу (за допомогою pandas):")
    print(data_with_pandas)