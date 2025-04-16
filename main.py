from stats import count_words, count_chars, list_conv

path = "./books/frankenstein.txt" 

def get_book_text(file_path):
    with open(file_path) as fhandle:
        file_contents = fhandle.read()
        return file_contents        

def main():
    # print(get_book_text("./books/frankenstein.txt"))
    words = count_words(get_book_text(path))
    chars = list_conv(count_chars(get_book_text(path)))
    return words, chars 

words, chars = main()
print("============ BOOKBOT ============")
print(f"Analyzing book found at {path[1:]}...")
print("----------- Word Count -----------")
print(f"Found {words} total words")
print("--------- Character Count ---------")
print(chars)
