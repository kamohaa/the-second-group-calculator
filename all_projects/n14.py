def str_words():
    input_string = input("Введите строку: ")
    
    words = input_string.split()

    total_words = len(words)

    unique_words = len(set(word.lower() for word in words))

    print(f"Количество слов: {total_words}")
    print(f"Количество уникальных слов: {unique_words}")

if __name__ == "__main__":
    str_words()