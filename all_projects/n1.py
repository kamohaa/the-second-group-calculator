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