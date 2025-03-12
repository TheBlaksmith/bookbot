import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

from stats import count_characters, sort_characters

with open(sys.argv[1]) as f:
    book = f.read()

character_counts = count_characters(book)

sorted_chars = sort_characters(character_counts)

# Print the report
print("============ BOOKBOT ============")
print(f"Analyzing book found at {sys.argv[1]}")
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