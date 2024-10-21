## подключение всей фигни
import os
from pathlib import Path
from zipfile import ZipFile

## определяется константа, которая хранит имя zip-файла, с которым мы будем работать.
ZIP_FILENAME = "croco-blitz-source.zip"


## определение функции read_zipped_file(), которая будет ответственна за чтение содержимого zip-файла
def read_zipped_file():
## получение текущей директории
    current_folder = os.path.dirname(os.path.realpath(__file__))
## Открываем zip-файл
    with ZipFile(Path(current_folder) / 'src' / ZIP_FILENAME) as archive:
## получаем список всей фигни в архиве через цикл
        for f in archive.namelist():
## в продакшен!
            print(f)


if __name__ == "__main__":
    read_zipped_file()
