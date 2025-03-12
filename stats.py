def count_characters(text):
    char_counts = {}
    lowercase_text = text.lower()
    for char in lowercase_text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_characters(char_counts):
    # Create a list of dictionaries
    chars_list = []
    for char, count in char_counts.items():
        chars_list.append({"char": char, "count": count})
    
    # Define a sorting function
    def sort_on(dict):
        return dict["count"]
    
    # Sort the list from greatest to least
    chars_list.sort(reverse=True, key=sort_on)
    
    return chars_list

book = ""
letter_count = {}
with open("./books/frankenstein.txt") as f:
    book = f.read()
character_counts = count_characters(book)
