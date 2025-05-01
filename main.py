import sys
from stats import num_of_words
from stats import count_characters
from stats import sort
from stats import print_sorted_counts


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}")
        print("----------- Word Count ----------")
        
        num_words = num_of_words(get_book_text(sys.argv[1]))
        print(f"Found {num_words} total words")

        counts = count_characters(get_book_text(sys.argv[1]))
        sorted_chars = sort(counts)
        print("--------- Character Count -------")
        print_sorted_counts(sorted_chars)

        print("============= END ===============")


if __name__ == '__main__':
    main()
