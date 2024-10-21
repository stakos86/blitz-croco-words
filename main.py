import os
import zipfile

print(os.path.abspath(__file__))

with zipfile.ZipFile('/Users/Stanislav_Egorov/Documents/GitHub/blitz-croco-words/src/croco-blitz-source.zip', 'r') as zip_file:
    # Получаем список файлов
    file_list = zip_file.namelist()

    print("Список файлов в архиве:")
    for file in file_list:
        print(file)
