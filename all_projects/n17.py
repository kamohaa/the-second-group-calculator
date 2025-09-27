def long_add_op():
    a = input("Введите первое число: ").strip()
    b = input("Введите второе число: ").strip()
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)
    carry = 0
    result = []
    for i in range(max_len - 1, -1, -1):
        try:
            s = int(a[i]) + int(b[i]) + carry
            result.append(str(s % 10))
            carry = s // 10
        except ValueError:
            print("Ошибка: введите число")
            return
    if carry:
        result.append(str(carry))