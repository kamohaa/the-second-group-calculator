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

            except ValueError as e:
                print(f"Ошибка: {e}")

        elif action == 3:
            try:
                a = int(input("Введите значение (0 или 1): "))
                if a not in [0, 1]:
                    raise ValueError("Ошибка: введите 0 или 1 для значения")

                result = int(not a)
                print(f"NOT {a} = {result}")

            except ValueError as e:
                print(f"Ошибка: {e}")

    except ValueError as e:
        print(f"Ошибка: {e}")
