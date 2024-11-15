from pyaspeller import YandexSpeller

if __name__ == "__main__":
    spisok = ["Колакал", "малако"]
    speller = YandexSpeller()
    result = speller.spelled(' '.join(spisok))
    print(result)