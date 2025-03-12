from stats import count_characters, sort_characters

with open("./books/frankenstein.txt") as f:
    book = f.read()

character_counts = count_characters(book)

sorted_chars = sort_characters(character_counts)

# Print the report
print("============ BOOKBOT ============")
print("Analyzing book found at books/frankenstein.txt...")
print("----------- Word Count ----------")
# Count words by splitting the text
words = book.split()
print(f"Found {len(words)} total words")
print("--------- Character Count -------")

# Print each character and its count
for char_dict in sorted_chars:
    char = char_dict["char"]
    count = char_dict["count"]
    # Only print alphabetic characters
    if char.isalpha():
        print(f"{char}: {count}")

print("============= END ===============")