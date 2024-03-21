import pandas as pd

# Функція для вводу тексту з консолі
def input_text_from_console():
    text = input("Введіть текст: ")
    return text


# Функція для зчитування з файлу за допомогою вбудованих можливостей Python
def read_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
        return data
    except FileNotFoundError:
        return "Файл не знайдено."


# Функція для зчитування з файлу за допомогою бібліотеки pandas
def read_with_pandas(file_path):
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