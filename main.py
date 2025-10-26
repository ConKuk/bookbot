from stats import get_num_words_in_text, num_letters_in_text, sort_letter_counts
import sys

def get_book_text(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def main(book_path: str):
    book_text = get_book_text(book_path)
    num_words = get_num_words_in_text(book_text)    
    letters = num_letters_in_text(book_text)
    sorted_letters = sort_letter_counts(letters)

    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print(f"----------- Word Count ----------\n"
        + f"Found {num_words} total words\n"
        + f"--------- Character Count -------\n"
        )
    for sorted_letter in sorted_letters:
        if sorted_letter["char"].isalpha():
            print(f"{sorted_letter['char']}: {sorted_letter['num']}")
    
    print(f"============= END ===============")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    main(sys.argv[1])