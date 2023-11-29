import os
import zipfile

# Функция для запаковки всех данных в папке в zip-архив
def pack_data():
    # Получение пути к папке, где находится исполняемый файл
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Создание zip-архива с именем "data.zip"
    zip_filename = os.path.join(current_dir, 'data.zip')
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        # Рекурсивно добавляем все файлы и папки в zip-архив
        for root, dirs, files in os.walk(current_dir):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, current_dir))

# Функция для разархивации zip-файла с именем "data.zip" в папку, где находится исполняемый файл
def unpack_data():
    # Получение пути к папке, где находится исполняемый файл
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Путь к zip-файлу
    zip_filename = os.path.join(current_dir, 'data.zip')

    # Разархивация zip-файла
    with zipfile.ZipFile(zip_filename, 'r') as zipf:
        zipf.extractall(current_dir)

# Пример использования функций
pack_data()  # Запаковка данных в zip-архив
 # Разархивация zip-архива
