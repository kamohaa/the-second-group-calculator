import math
def calc_degrees():
    while True:
        print("\nВведите номер действия: " )
        print("1. sin")
        print("2. cos")
        print("3. Выход")
        operation = input("Введите номер операции (1, 2 или 3 для выхода): ")
        if operation == '3':
            print("Выход из программы.")
            break
        if operation not in ['1', '2','3']:
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

calc_degrees()