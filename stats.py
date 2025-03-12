def count_characters(text):
    char_counts = {}
    lowercase_text = text.lower()
    for char in lowercase_text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

book = ""
letter_count = {}
with open("./books/frankenstein.txt") as f:
    book = f.read()
character_counts = count_characters(book)
