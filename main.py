def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_dict = get_char_dict(text)
    dict_list = create_char_list(char_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in dict_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item["char"]}' was found {item["num"]} times")


def sort_on(dict_list):
    return dict_list["num"]


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_words(text):
    words = text.split()
    return len(words)


def get_char_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def create_char_list(dict):
    sorted_list = []
    for char in dict:
        sorted_list.append({"char": char, "num":dict[char]})
        sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list
    

main()


