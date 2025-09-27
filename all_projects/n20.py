def long_add_op():
    #функция сложения
    s = int(input("Введите ваше число: "))
    print()
    #return


def long_sub_opp():
    #функция вычитания
    s = int(input("Введите ваше число: "))
    print()
    #return

def long_mul_op():
    #функция умножения
    s = int(input("Введите ваше число: "))
    print()
    #return
23


def menu():
    while True:
        print()
        print("Меню длинной арифметики:")
        print()
        print("1. Сложение;")
        print("2. Вычитание;")
        print("3. Умножение;")
        print("4. Выход.")
        print()

        try:
            catalog = int(input("Выберите пункт, чтобы продолжить: "))
        except ValueError:
            print()
            print("Ошибка! Введите число от 1 до 4")
            continue


        if catalog == 1:
            print()
            print("Вы выбрали раздел 1: 'Сложение'")
            long_add_op()
        elif catalog == 2:
            print()
            print("Вы выбрали раздел 2: 'Вычитание'")
            long_sub_opp()
        elif catalog == 3:
            print()
            print("Вы выбрали раздел 3: 'Умножение'")
            long_mul_op()
        elif catalog == 4:
            print()
            print("Вы выбрали раздел 4: 'Выход'")
            break
        else:
            print()
            print("Такого пункта в меню нет...")

if __name__ == "__main__":
    menu()