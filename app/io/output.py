# Функція для виводу тексту у консоль
def output_text_to_console(text):
    print(text)


# Функція для запису до файлу за допомогою вбудованих можливостей Python
def write_to_file(file_path, data):
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