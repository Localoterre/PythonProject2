from input_functions import input_text_from_console, read_from_file, read_with_pandas
from output import output_text_to_console, write_to_file

def main():
    # Вводимо текст з консолі
    text_from_console = input_text_from_console()
    output_text_to_console("Введений текст: " + text_from_console)

    # Читаємо з файлу за допомогою вбудованих можливостей Python
    file_path = "example.txt"  # Замініть шлях на шлях до вашого файлу
    data_from_file = read_from_file(file_path)
    output_text_to_console("Зміст файлу: " + data_from_file)

    # Читаємо з файлу за допомогою бібліотеки pandas
    csv_file_path = "example.csv"  # Замініть шлях на шлях до вашого CSV файлу
    data_with_pandas = read_with_pandas(csv_file_path)
    output_text_to_console("Дані з файлу (за допомогою pandas):")
    output_text_to_console(str(data_with_pandas))
    # Записуємо введений текст у файл
    file_path_to_write = "output.txt"
    write_to_file(file_path_to_write, "Введений текст: " + text_from_console)

if __name__ == "__main__":
    main()
