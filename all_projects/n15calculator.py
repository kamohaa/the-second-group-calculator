def str_stat():

    # ввод строки
    string = input("Введите строку: ")

    # длина строки
    length = len(string)

    # кол-во цифр
    digit = 0
    for char in string:
        if char.isdigit():
            digit += 1

    # кол-во символов в вверхнем регистре
    upper = 0
    for char in string:
        if char.isupper():
            upper += 1

    # кол-во символов в нижнем регистре
    lower = 0
    for char in string:
        if char.islower():
            lower += 1

    # кол-во непечатаемых символов
    space = 0
    for char in string:
        if char.isspace():
            space += 1
    # вывод информации
    print("Длина строки: ", length)
    print("Количество цифр: ", digit)
    print("Количество символов в вверхнем регистре: ", upper)
    print("Количество символов в нижнем регистре: ", lower)
    print("Количество пробельных символов: ", space)


    if __name__ == "__main__":
        str_stat()