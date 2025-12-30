def get_num_words(book_text):
    """Returns the total count of words in the string."""
    words = book_text.split()
    return len(words)

def get_num_chars(book_text):
    """Creates a dictionary of unique characters and their occurrence counts."""
    dictionary = {}
    for char in book_text.lower():
        dictionary[char] = dictionary.get(char, 0) + 1

    return dictionary

def sort_on(item):
    """Helper function to tell the sort method to use the 'value' (index 1 of the tuple)."""
    return item[1]

def return_sorted_list(dictionary):
    """Converts a dictionary into a list of single-entry dictionaries, sorted by frequency."""
    dictionary_list = sorted(dictionary.items(), key=sort_on, reverse=True)
    return [{char: value} for char, value in dictionary_list]