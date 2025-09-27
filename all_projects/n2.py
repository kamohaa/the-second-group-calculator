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
calc_extended()