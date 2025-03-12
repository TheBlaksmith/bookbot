get_book_text = ""

with open("./books/frankenstein.txt") as f:
    get_book_text = f.read()

all_words = get_book_text.split()
num_words = len(all_words)

