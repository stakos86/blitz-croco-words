from View_files_in_zip import *
from open_pptx_file import *

def main() -> None:
    extract_pptx_from_zip('/Users/Stanislav_Egorov/Documents/GitHub/blitz-croco-words/src/croco-blitz-source.zip'
                      ,'','croco-blitz-source_test1')

    presentation_path=extract_path

    extracted_words = extract_words_from_pptx(str(presentation_path))

    write_txt('words.txt', extracted_words)
