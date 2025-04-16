from stats import count_words, count_chars
def get_book_text(file_path):
    with open(file_path) as fhandle:
        file_contents = fhandle.read()
        return file_contents        

def main():
    # print(get_book_text("./books/frankenstein.txt"))
    words = f"{count_words(get_book_text("./books/frankenstein.txt"))} words found in the document"  
    chars = f"{count_chars(get_book_text("./books/frankenstein.txt"))}"  
    return words, chars 

print(main())
