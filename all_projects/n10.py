def check_brackets(formula: str) -> str:
    """
    Проверяет, правильно ли расставлены круглые скобки в строке.
    :param formula: строка с математическим выражением
    :return: "ДА" если скобки сбалансированы, "НЕТ" если нет
    """
    formula = input("Введите математическое выражение: ")

    balance = 0
    for char in formula:
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
            if balance < 0:
                print("НЕТ")
                return

    if balance == 0:
        print("ДА")
    else:
        print("НЕТ")
