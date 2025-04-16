from stats import count_words
def get_book_text(file_path):
    with open(file_path) as fhandle:
        file_contents = fhandle.read()
        return file_contents        

def main():
    # print(get_book_text("./books/frankenstein.txt"))
    return f"{count_words(get_book_text("./books/frankenstein.txt"))} words found in the document"

print(main())
