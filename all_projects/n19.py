def long_multiply():
    num1 = input("Введите первое число: ")
    num2 = input("Введите второе число: ")
    a = []
    for i in num1:
        try:
            a.append(int(i))
        except ValueError:
            print("Ошибка: введите число")
            return
    b = []
    for i in num2:
        try:
            b.append(int(i))
        except ValueError:
            print("Ошибка: введите число")
            return
    m, n = len(a), len(b)
    arr = [0] * (m + n)
    for i in range(m)[::-1]:
        c = 0
        for j in range(n)[::-1]:
            ar = a[i] * b[j] + arr[i + j + 1] + c
            c = ar // 10
            arr[i + j + 1] = ar % 10
        arr[i + j] += c
    while len(arr) > 1 and arr[0] == 0:
        arr = arr[1:]

    print("Результат умножения: ", ''.join(map(str, arr)))
long_multiply()