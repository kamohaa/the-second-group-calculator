def str_simple_ops():
    #функция простых операции со строками
    s = input("Введите вашу строку: ")
    print()
    #return


def str_showcenter_op():
    #функция вывода строки по центру
    s = input("Введите вашу строку: ")
    print()
    #return


def str_words_op():
    #функция кол-во слов и кол-во уникальных слов
    s = input("Введите вашу строку: ")
    print()
    #return

def str_stat_op():
    #функция статистики по символам строки
    s = input("Введите вашу строку: ")
    print()
    #return



def menu():
    while True:
        print()
        print("Меню калькулятора строк:")
        print()
        print("1. Простые операции со строками;")
        print("2. Вывод строки по центру;")
        print("3. Количество слов и количество уникальных слов;")
        print("4. Статистика по символам строки;")
        print("5. Выход.")
        print()

        try:
            catalog = int(input("Выберите пункт, чтобы продолжить: "))
        except ValueError:
            print()
            print("Ошибка! Введите число от 1 до 5")
            continue


        if catalog == 1:
            print()
            print("Вы выбрали раздел 1: 'Простые операции со строками'")
            str_simple_ops()
        elif catalog == 2:
            print()
            print("Вы выбрали раздел 2: 'Вывод строки по центру'")
            str_showcenter_op()
        elif catalog == 3:
            print()
            print("Вы выбрали раздел 3: 'Количество слов и количество уникальных слов'")
            str_words_op()
        elif catalog == 43:
            print()
            print("Вы выбрали раздел 4: 'Статистика по символам строки'")
            str_stat_op()
        elif catalog == 5:
            print()
            print("Вы выбрали раздел 5: 'Выход'")
            break
        else:
            print()
            print("Такого пункта в меню нет...")

if __name__ == "__main__":
    menu()