def count_words(book_string):
    return len(book_string.split())

letters_dict = {}
def count_chars(book_string):
    words = book_string.split()
    for word in words:
        for char in word:
            char = char.lower()
            if char.isalpha():   
                if char not in letters_dict: letters_dict[char] = 1
                else: letters_dict[char] += 1
    return letters_dict
