import sys
from stats import count_words, count_chars, list_conv

def get_book_text(file_path):
    with open(file_path) as fhandle:
        file_contents = fhandle.read()
        return file_contents        

def main(path):
    words = count_words(get_book_text(path))
    chars = list_conv(count_chars(get_book_text(path)))
    return words, chars 

try:
    words, chars = main(sys.argv[1])
except:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

print("============ BOOKBOT ============")
print(f"Analyzing book found at {sys.argv[1][1:]}...")
print("----------- Word Count -----------")
print(f"Found {words} total words")
print("--------- Character Count ---------")
print(chars)
