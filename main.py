from stats import get_num_words, get_num_chars, sorted_list
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        contents = f.read()
    return contents

def main():
    print("============ BOOKBOT ============")
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    contents = get_book_text(file_path)
    # contents = get_book_text("books/frankenstein.txt")
    print("Analyzing book found at {file_path}...")

    num_words = get_num_words(contents)
    print(f"Found {num_words} total words")

    char_num_dict = sorted_list(contents)
    for item in char_num_dict:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")

    print("============= END ===============")
if __name__ == '__main__':
    main()