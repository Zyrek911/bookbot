import sys
from stats import *

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_text = f.read()
    return file_text

def main():
    if len(sys.argv) == 2:
        req_path = sys.argv[1]
        book_text = get_book_text(req_path)
        total_words = word_count(book_text)
        total_char = report_sort(book_text)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {req_path}")
        print("----------- Word Count ----------")
        print(f"Found {total_words} total words")
        print("--------- Character Count -------")
        for char_dict in total_char:
            print(f"{char_dict["char"]}: {char_dict["num"]}")
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)    
main()