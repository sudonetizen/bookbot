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

def list_conv(dictionary):
    dictionary = dict(sorted(dictionary.items(), reverse=True, key=lambda item: item[1]))
    dict_list = "\n".join([f"{key}: {value}" for key, value in dictionary.items()])
    return dict_list
