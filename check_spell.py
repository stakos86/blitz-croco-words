from pyaspeller import YandexSpeller

if __name__ == "__main__":
    spisok = list["Колакал", "малако"]
    speller = YandexSpeller()
    result = speller.spelled(spisok)
    print(result)