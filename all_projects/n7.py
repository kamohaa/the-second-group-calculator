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