import math
def check_brackets(formula: str) -> str: # функция 10
    """
    Проверяет, правильно ли расставлены круглые скобки в строке.
    :param formula: строка с математическим выражением
    :return: "ДА" если скобки сбалансированы, "НЕТ" если нет
    """
    balance = 0

    for char in formula:
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
            if balance < 0:
                return "НЕТ"

    return "ДА" if balance == 0 else "НЕТ"

def calc_radians():        # функция 4
    print("Выберите действие:")
    print("1 - sin(x)")
    print("2 - cos(x)")
    action = int(input("Ваш выбор: "))

    angle = float(input("Введите угол в радианах: "))

    if action == 1:
        result = math.sin(angle)
        print(f"sin({angle}) = {result}")
    elif action == 2:
        result = math.cos(angle)
        print(f"cos({angle}) = {result}")
    else:
        print("Ошибка: выбрано неверное действие")



def calc_logic():         # функция 5
    print("Выберите действие:")
    print("1 - and")
    print("2 - or")
    print("3 - not")
    action = int(input("Ваш выбор: "))

    if action == 1:
        a = int(input("Введите первое значение (0 или 1): "))
        b = int(input("Введите второе значение (0 или 1): "))
        result = a and b
        print(f"{a} AND {b} = {result}")
    elif action == 2:
        a = int(input("Введите первое значение (0 или 1): "))
        b = int(input("Введите второе значение (0 или 1): "))
        result = a or b
        print(f"{a} OR {b} = {result}")
    elif action == 3:
        a = int(input("Введите значение (0 или 1): "))
        result = int(not a)
        print(f"NOT {a} = {result}")
    else:
        print("Ошибка: выбрано неверное действие")


def menu_numbers():
    """
    Главное меню калькулятора чисел.
    Показывает список действий и запускает соответствующую функцию.
    """
    print("\n" + "="*50)
    print("           КАЛЬКУЛЯТОР ЧИСЕЛ")
    print("="*50)
    print("1. Простые операции")
    print("2. Расширенные операции")
    print("3. Тригонометрические действия с градусами")
    print("4. Тригонометрические действия с радианами")
    print("5. Логические операции")
    print("6. Перевод чисел в различные системы счисления")
    print("7. Проверка скобок")
    print("="*50)

    # Запрос действия
    choice = input("Выберите действие (1-7): ").strip()

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
    else:
        print("Ошибка: введите число от 1 до 7")


menu_numbers()