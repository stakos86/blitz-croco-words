from View_files_in_zip import *
from open_pptx_file import *
from pyaspeller import YandexSpeller



def main() -> None:
    extract_pptx_from_zip('/Users/Stanislav_Egorov/Documents/GitHub/blitz-croco-words/src/croco-blitz-source.zip'
                          , '', 'croco-blitz-source_test1')

    presentation_path = '/Users/Stanislav_Egorov/Documents/GitHub/blitz-croco-words/croco-blitz-source_test1'

    extracted_words = extract_words_from_pptx(str(presentation_path))

    speller = YandexSpeller()
    result = speller.spelled(' '.join(extracted_words))

    write_txt('words.txt', result.split())


if __name__ == '__main__':
    main()
