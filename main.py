def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")

    chars_dict = get_chars_dict(text)
    print(f"Character count: {chars_dict}")

def get_chars_dict(text):
    text = text.lower()
    chars = {}
    for char in text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as file:
        return file.read()

main()
