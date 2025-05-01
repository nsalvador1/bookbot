def num_of_words(book_text):
    word_count = 0
    for word in book_text.split():
        word_count += 1
    return word_count


def count_characters(book_text):
    char_counts = {}
    for char in book_text.lower():
        if char.isalpha():
            char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts


def sort_on(dict):
    return dict["num"]


def sort(char_counts_dict):
    sorted_counts = [{"char": char, "num": count} for char, count in char_counts_dict.items()]
    sorted_counts.sort(reverse=True, key=sort_on)
    return sorted_counts


def print_sorted_counts(sorted_counts):
    for item in sorted_counts:
        print(f"{item["char"]}: {item["num"]}")
