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