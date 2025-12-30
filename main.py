from stats import get_num_words, get_num_chars, return_sorted_list
import sys

def get_book_text(filename):
    with open(filename) as f:
        book_text = f.read()
    return book_text

def print_dictionary(sorted_list, word_count, filename):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filename}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for lst in sorted_list:
        for char, count in lst.items():
            if char.isalpha():
                print(f"{char}: {count}")

def main():

    # Validate arg
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Store arg
    filename = sys.argv[1]

    try:
        book_text = get_book_text(filename)
    except (FileNotFoundError, PermissionError, IsADirectoryError, UnicodeDecodeError, OSError) as e:
        print(f"Error reading '{filename}': {e}")
        sys.exit(1)

    word_count = get_num_words(book_text)
    dictionary_of_chars = get_num_chars(book_text)

    sorted_list = return_sorted_list(dictionary_of_chars)

    print_dictionary(sorted_list, word_count, filename)


if __name__ == '__main__':
    main()