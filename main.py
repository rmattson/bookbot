def main():
    book = './books/frankenstein.txt'
    text = get_text(book)
    num_words = get_number_of_words(text)
    chars = count_characters(text)
    print(f"--- Begin report of {book} ---")
    print(f"Text contains {num_words} words\n")
    char_list = [[k, v] for k, v in chars.items() if k.isalpha()]
    char_list.sort(key=lambda x: x[1], reverse=True)
    for item in char_list:
        print(f"The '{item[0]}' character was found {item[1]} times")
    print(f"--- End report ---")

def get_text(file_path):
    with open(file_path) as f:
        return f.read()

def get_number_of_words(str):
    words = str.split()
    return len(words)

def count_characters(str):
    chars = {}
    for c in str:
        c = c.lower()
        if not c in chars:
            chars[c] = 1
        else:
            chars[c] += 1
    return chars

if __name__ == '__main__':
    main()
