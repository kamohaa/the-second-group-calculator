import math


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

    except ValueError as e:
        print(f"Ошибка: {e}")
