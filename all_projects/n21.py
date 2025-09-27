import math
#'Калькулятор чисел'
def numbers_ops():
    def calc_simple():
        try:
            a = int(input("Введите первое число: "))

            b = int(input("Введите второе число: "))

            operation = input("Введите операцию (+, -, *, /): ")

            if operation == '+':
                result = a + b
                print(f"{a} + {b} = {result}")
            elif operation == '-':
                result = a - b
                print(f"{a} - {b} = {result}")
            elif operation == '*':
                result = a * b
                print(f"{a} * {b} = {result}")
            elif operation == '/':
                if b == 0:
                    print("Ошибка: деление на ноль!")
                else:
                    result = a / b
                    print(f"{a} / {b} = {result}")
            else:
                print("Ошибка: неверная операция! Допустимые операции: +, -, *, /")
        except ValueError:
            print("Ошибка: введите целое число!")

    def calc_extended():
        while True:
            print("\nВыберите операцию:")
            print("1. Возведение в степень")
            print("2. Остаток от деления")
            print("3. Нахождение корня")
            print("4. Выход")
            operation = input("Введите номер операции (1, 2, 3 или 4 для выхода): ")
            if operation == '4':
                print("Выход из программы.")
                break
            if operation not in ['1', '2', '3']:
                print("Ошибка: введите 1, 2, 3 или 4 для выхода!")
                continue
            if operation == '1':
                while True:
                    try:
                        num = float(input("Введите основание: "))
                        degree = float(input("Введите показатель степени: "))
                        result = num ** degree
                        print("Результат: ", result)
                        break
                    except ValueError:
                        print("Ошибка: введите числа")
            elif operation == '2':
                while True:
                    try:
                        dividend = float(input("Введите делимое: "))
                        divisor = float(input("Введите делитель: "))
                        if divisor == 0:
                            print("Ошибка: деление на ноль невозможно!")
                            continue
                        result = dividend % divisor
                        print("Результат: ", result)
                        break
                    except ValueError:
                        print("Ошибка: введите числа")
            elif operation == '3':
                while True:
                    try:
                        num = float(input("Введите число: "))
                        if num < 0:
                            print("Ошибка: нельзя извлечь корень из отрицательного числа!")
                            continue
                        result = num ** 0.5
                        print(f"Результат: ", result)
                        break
                    except ValueError:
                        print("Ошибка: введите число")

    def calc_degrees():
        while True:
            print("\nВведите номер действия: ")
            print("1. sin")
            print("2. cos")
            print("3. Выход")
            operation = input("Введите номер операции (1, 2 или 3 для выхода): ")
            if operation == '3':
                print("Выход из программы.")
                break
            if operation not in ['1', '2', '3']:
                print("Ошибка: введите 1, 2 или 3 для выхода!")
                continue
            if operation == '1':
                while True:
                    try:
                        degrees = int(input("Введите угол в градусах: "))
                        radians = math.radians(degrees)
                        result = math.sin(radians)
                        print("Результат: ", result)
                        break
                    except ValueError:
                        print("Ошибка: введите число")
            if operation == '2':
                while True:
                    try:
                        degrees = int(input("Введите угол в градусах: "))
                        radians = math.radians(degrees)
                        result = math.cos(radians)
                        print(result)
                        break
                    except ValueError:
                        print("Ошибка: введите число")

    def menu_logic():
        def calc_10_2():
            try:
                number = int(input("Введите целое положительное число: "))
                if number <= 0:
                    raise ValueError("Ошибка: введите положительное число")

                result = bin(number)[2:]  # убираем "0b" в начале
                print(f"Число {number} в двоичной системе = {result}")

            except ValueError:
                print("Ошибка: введите число от 0 до бесконечности!")

        def calc_10_16():
            try:
                number = int(input("Введите целое положительное число: "))

                if number < 0:
                    print("Ошибка: число должно быть положительным!")
                    return

                hex_number = hex(number)

                print(f"Число {number} в шестнадцатеричной системе: {hex_number[2:].upper()}")

            except ValueError:
                print("Ошибка: введите целое число!")

        def calc_10_8():
            try:
                number = int(input("Введите целое положительное число: "))

                if number < 0:
                    print("Ошибка: число должно быть положительным!")
                    return

                oct_number = oct(number)

                print(f"Число {number} в восьмеричной системе: {oct_number[2:]}")

            except ValueError:
                print("Ошибка: введите целое число!")

        # Вывод меню
        print("Меню перевода чисел:")
        print("1. Перевод 10СИ -> 2СИ")
        print("2. Перевод 10СИ -> 16СИ")
        print("3. Перевод 10СИ -> 8СИ")

        # Считывание выбора пользователя
        choice = input("Выберите действие (1, 2 или 3): ")

        # Выполнение действия в зависимости от выбора
        if choice == '1':
            # Вызов функции перевода из 10СИ в 2СИ
            calc_10_2()
        elif choice == '2':
            # Вызов функции перевода из 10СИ в 16СИ
            calc_10_16()
        elif choice == '3':
            # Вызов функции перевода из 10СИ в 8СИ
            calc_10_8()
        else:
            print("Неверный выбор!")

    def check_brackets():
        """
        #Проверяет, правильно ли расставлены круглые скобки в строке.
        #:param formula: строка с математическим выражением
        #:return: "ДА" если скобки сбалансированы, "НЕТ" если нет
        """

        formula = input("Введите математическое выражение: ")

        if '(' not in formula and ')' not in formula:
            print("Ошибка: в строке нет скобок!")
            return

        balance = 0
        for char in formula:
            if char == '(':
                balance += 1
            elif char == ')':
                balance -= 1
                if balance < 0:
                    print("НЕТ - закрывающая скобка раньше открывающей. Попробуйте еще раз.")
                    return

        if balance == 0:
            print("ДА")
        else:
            print("НЕТ - не все скобки закрыты. Попробуйте еще раз.")

        return
        # функция 10

    def calc_radians():
        print("Выберите действие:")
        print("1 - sin(x)")
        print("2 - cos(x)")

        try:
            action = int(input("Ваш выбор: "))
            if action not in [1, 2]:
                raise ValueError("Ошибка: выбрано неверное действие")

            angle = float(input("Введите угол в радианах: "))

            if action == 1:
                result = math.sin(angle)
                print(f"sin({angle}) = {result}")
            elif action == 2:
                result = math.cos(angle)
                print(f"cos({angle}) = {result}")

        except ValueError:
            print("Ошибка: введите число!")

    def calc_logic():
        print("Выберите действие:")
        print("1 - and")
        print("2 - or")
        print("3 - not")

        try:
            action = int(input("Ваш выбор: "))
            if action not in [1, 2, 3]:
                raise ValueError("Ошибка: выбрано неверное действие")

            if action == 1 or action == 2:
                try:
                    a = int(input("Введите первое значение (0 или 1): "))
                    b = int(input("Введите второе значение (0 или 1): "))
                    if a not in [0, 1] or b not in [0, 1]:
                        raise ValueError("Ошибка: введите 0 или 1 для значений")

                    if action == 1:
                        result = a and b
                        print(f"{a} AND {b} = {result}")
                    elif action == 2:
                        result = a or b
                        print(f"{a} OR {b} = {result}")

                except ValueError:
                    print("Ошибка: Введите значение 0 или 1!")

            elif action == 3:
                try:
                    a = int(input("Введите значение (0 или 1): "))
                    if a not in [0, 1]:
                        raise ValueError("Ошибка: Введите значение 0 или 1!")

                    result = int(not a)
                    print(f"NOT {a} = {result}")
                except ValueError:
                    print("Ошибка: Введите значение 0 или 1!")



        except ValueError:
            print("Ошибка: укажите число от 1 до 3!")

    def menu_numbers():
        while True:
            """
            Главное меню калькулятора чисел.
            Показывает список действий и запускает соответствующую функцию.
            """
            print("\n" + "=" * 50)
            print("           КАЛЬКУЛЯТОР ЧИСЕЛ")
            print("=" * 50)
            print("1. Простые операции")
            print("2. Расширенные операции")
            print("3. Тригонометрические действия с градусами")
            print("4. Тригонометрические действия с радианами")
            print("5. Логические операции")
            print("6. Перевод чисел в различные системы счисления")
            print("7. Проверка скобок")
            print("8. Выход")
            print("=" * 50)

        # Запрос действия
            choice = input("Выберите действие (1-8): ").strip()

        # Обработка выбора
            if choice == '1':
                print("Вы выбрали: Простые операции")
                calc_simple()  # ← Функция от участника №1
            elif choice == '2':
                print("Вы выбрали: Расширенные операции")
                calc_extended()  # ← Функция от участника №2
            elif choice == '3':
                print("Вы выбрали: Тригонометрия в градусах")
                calc_degrees()  # ← Функция от участника №3
            elif choice == '4':
                print("Вы выбрали: Тригонометрия в радианах")
                calc_radians()  # ← Функция от участника №4
            elif choice == '5':
                print("Вы выбрали: Логические операции")
                calc_logic()  # ← Функция от участника №5
            elif choice == '6':
                print("Вы выбрали: Перевод чисел в СС")
                menu_logic()  # ← Функция от участника №9
            elif choice == '7':
                print("Вы выбрали: Проверка скобок")
                check_brackets()  # ← Функция от участника №10
            elif choice == '8':
                print()
                print("Вы выбрали раздел 8: 'Выход'")
                break
            else:
                print("Ошибка: введите число от 1 до 8")

    menu_numbers()
#'Калькулятор строк'
def string_ops():

    def str_simple_ops():
        op = input("Введите операцию (+ или *): ").strip()

        if op == "+":
            s1 = input("Введите первую строку: ")
            s2 = input("Введите вторую строку: ")

            result = s1 + s2
            print("Результат сложения строк:", result)
            return
        elif op == "*":
            s = input("Введите строку: ")
            try:
                n = int(input("Введите число: "))
            except ValueError:
                print("Ошибка: число должно быть целым. ")
                return
            result = s * n
            print("Результат умножения строки:", result)
            return
        else:
            print("Ошибка: операция должна быть '+' или '*'")

    def str_showcenter_op():
        input_string = input("Введите строку: ")

        terminal_width = 80
        terminal_height = 25

        vertical_center = terminal_height // 2

        horizontal_padding = (terminal_width - len(input_string)) // 2

        print("\n" * vertical_center)

        print(" " * horizontal_padding + input_string)

        remaining_lines = terminal_height - vertical_center - 1
        if remaining_lines > 0:
            print("\n" * remaining_lines)

    def str_words_op2():
        input_string = input("Введите строку: ")

        words = input_string.split()

        total_words = len(words)

        unique_words = len(set(word.lower() for word in words))

        print(f"Количество слов: {total_words}")
        print(f"Количество уникальных слов: {unique_words}")

    def str_stat_op():

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

    while True:
        print("\n" + "=" * 50)
        print("           КАЛЬКУЛЯТОР СТРОК")
        print("=" * 50)
        print("1. Простые операции со строками;")
        print("2. Вывод строки по центру;")
        print("3. Количество слов и количество уникальных слов;")
        print("4. Статистика по символам строки;")
        print("5. Выход.")
        print("=" * 50)

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
            str_words_op2()
        elif catalog == 4:
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
#'Длинная арифметика'
def str_words_op():

    def long_multiply():
        num1 = input("Введите первое число: ")
        num2 = input("Введите второе число: ")
        a = []
        for i in num1:
            try:
                a.append(int(i))
            except ValueError:
                print("Ошибка: введите число")
                return
        b = []
        for i in num2:
            try:
                b.append(int(i))
            except ValueError:
                print("Ошибка: введите число")
                return
        m, n = len(a), len(b)
        arr = [0] * (m + n)
        for i in range(m)[::-1]:
            c = 0
            for j in range(n)[::-1]:
                ar = a[i] * b[j] + arr[i + j + 1] + c
                c = ar // 10
                arr[i + j + 1] = ar % 10
                arr[i + j] += c
        while len(arr) > 1 and arr[0] == 0:
            arr = arr[1:]

        print("Результат умножения: ", ''.join(map(str, arr)))

    def long_add_op():
        a = input("Введите первое число: ").strip()
        b = input("Введите второе число: ").strip()
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)
        carry = 0
        result = []
        for i in range(max_len - 1, -1, -1):
            try:
                s = int(a[i]) + int(b[i]) + carry
                result.append(str(s % 10))
                carry = s // 10
            except ValueError:
                print("Ошибка: введите число")
                return
        if carry:
            result.append(str(carry))

        print("Результат:", ''.join(result[::-1]).lstrip('0') or '0')

    def long_sub_op():
        def subtract_positive(num1, num2):
            len1, len2 = len(num1), len(num2)
            if len1 < len2 or (len1 == len2 and num1 < num2):
                result = subtract_positive(num2, num1)
                return f"-{result}" if result != "0" else "0"

            digits1 = [int(d) for d in num1][::-1]
            digits2 = [int(d) for d in num2][::-1]
            digits2.extend([0] * (len(digits1) - len(digits2)))

            result_2 = []
            borrow = 0  # *для вычитания столбиком*
            for i in range(len(digits1)):
                diff = digits1[i] - digits2[i] - borrow
                if diff < 0:
                    diff += 10
                    borrow = 1
                else:
                    borrow = 0
                result_2.append(diff)

            while len(result_2) > 1 and result_2[-1] == 0:
                result_2.pop()

            result_str = ''.join(str(d) for d in result_2[::-1])
            return result_str

        def add_positive(num1, num2):
            digits1 = [int(d) for d in num1][::-1]
            digits2 = [int(d) for d in num2][::-1]

            max_len = max(len(digits1), len(digits2))
            digits1.extend([0] * (max_len - len(digits1)))
            digits2.extend([0] * (max_len - len(digits2)))

            result_1 = []
            carry = 0

            for i in range(max_len):
                total = digits1[i] + digits2[i] + carry
                result_1.append(total % 10)
                carry = total // 10
            if carry > 0:
                result_1.append(carry)
            result_str = ''.join(str(d) for d in result_1[::-1])
            return result_str

        user_num1 = input("Введите первое число: ")
        user_num2 = input("Введите второе число: ")

        try:

            sign1 = -1 if user_num1.startswith('-') else 1
            sign2 = -1 if user_num2.startswith('-') else 1

            num1_clean = user_num1.lstrip('-')
            num2_clean = user_num2.lstrip('-')
            num1_clean = num1_clean.lstrip('0') or '0'
            num2_clean = num2_clean.lstrip('0') or '0'


            if sign1 == 1 and sign2 == 1:
                print(subtract_positive(num1_clean, num2_clean))
            elif sign1 == 1 and sign2 == -1:
                print(add_positive(num1_clean, num2_clean))
            elif sign1 == -1 and sign2 == 1:
                result = add_positive(num1_clean, num2_clean)
                print(f"-{result}" if result != "0" else "0")
            elif sign1 == -1 and sign2 == -1:
                print(subtract_positive(num2_clean, num1_clean))

        except ValueError:
            print("Ошибка: введите только числа")


    while True:
        print()
        print("\n" + "=" * 50)
        print("           КАЛЬКУЛЯТОР ДЛИННОЙ АРИФМЕТИКИ")
        print("=" * 50)
        print("1. Сложение;")
        print("2. Вычитание;")
        print("3. Умножение;")
        print("4. Выход.")
        print("=" * 50)
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
            long_sub_op()
        elif catalog == 3:
            print()
            print("Вы выбрали раздел 3: 'Умножение'")
            long_multiply()
        elif catalog == 4:
            print()
            print("Вы выбрали раздел 4: 'Выход'")
            break
        else:
            print()
            print("Такого пункта в меню нет...")
#'Основное меню'
def menu():
    while True:
        print()
        print("Добро пожаловать в универсальный калькулятор! Выберите из меню желаемый калькулятор: ")
        print("\n" + "=" * 50)
        print("           КАЛЬКУЛЯТОР!")
        print("=" * 50)
        print("Меню калькулятора:")
        print()
        print("1. Калькулятор чисел;")
        print("2. Калькулятор строк;")
        print("3. Длинная арифметика;")
        print("4. Выход;")
        print("=" * 50)

        try:
            catalog = int(input("Выберите пункт, чтобы продолжить: "))
        except ValueError:
            print()
            print("Ошибка! Введите число от 1 до 4")
            continue


        if catalog == 1:
            print()
            print("Вы выбрали раздел 1: 'Калькулятор чисел'")
            numbers_ops()
        elif catalog == 2:
            print()
            print("Вы выбрали раздел 2: 'Калькулятор строк'")
            string_ops()
        elif catalog == 3:
            print()
            print("Вы выбрали раздел 3: 'Длинная арифметика'")
            str_words_op()
        elif catalog == 4:
            print()
            print("Вы выбрали раздел 4: 'Выход'")
            break
        else:
            print()
            print("Такого пункта в меню нет...")

if __name__ == "__main__":
    menu()