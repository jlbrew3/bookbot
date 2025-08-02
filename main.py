from stats import get_num_words, char_dict, sort_dict
import sys

def get_book_text(filepath):
    with open(filepath) as b:
        book_text = b.read()
        return book_text

def main():
    if(len(sys.argv) == 1):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        num_words = get_num_words(get_book_text(sys.argv[1]))
        print(f"Found {num_words} total words")
        char_list = []
        char_list = sort_dict(char_dict(get_book_text(sys.argv[1])))
        for item in char_list:
            if(item["char"].isalpha()):
                print(item["char"] + ": " + str(item["num"]))

main()