def calc_10_2():
    try:
        number = int(input("Введите целое положительное число: "))
        if number <= 0:
            raise ValueError("Ошибка: введите положительное число")

        result = bin(number)[2:]  # убираем "0b" в начале
        print(f"Число {number} в двоичной системе = {result}")

    except ValueError as e:
        print(f"Ошибка: {e}")
