def main():
    text = get_text('./books/frankenstein.txt')
    print(text)
    num_words = get_number_of_words(text)
    print(f"Text contains {num_words} words")

def get_text(file_path):
    with open(file_path) as f:
        return f.read()

def get_number_of_words(str):
    words = str.split()
    return len(words)

if __name__ == '__main__':
    main()
