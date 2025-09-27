def long_sub():
    num1 = input("Введите первое число: ")
    num2 = input("Введите второе число: ")

    sign1 = -1 if num1.startswith('-') else 1
    sign2 = -1 if num2.startswith('-') else 1

    num1_clean = num1.lstrip('-')
    num2_clean = num2.lstrip('-')
    num1_clean = num1_clean.lstrip('0') or '0'
    num2_clean = num2_clean.lstrip('0') or '0'

    if sign1 == 1 and sign2 == 1:
        return subtract_positive(num1_clean, num2_clean)
    elif sign1 == 1 and sign2 == -1:
        return add_positive(num1_clean, num2_clean)
    elif sign1 == -1 and sign2 == 1:
        result = add_positive(num1_clean, num2_clean)
        return f"-{result}" if result != "0" else "0"
    elif sign1 == -1 and sign2 == -1:
        return subtract_positive(num2_clean, num1_clean)

def subtract_positive(num1, num2):
    len1, len2 = len(num1), len(num2)
    if len1 < len2 or (len1 == len2 and num1 < num2):
        result = subtract_positive(num2, num1)
        return f"-{result}" if result != "0" else "0"

    digits1 = [int(d) for d in num1][::-1]
    digits2 = [int(d) for d in num2][::-1]
    digits2.extend([0] * (len(digits1) - len(digits2)))

    result = []
    borrow = 0 #*для вычитания столбиком*
    for i in range (len(digits1)):
        diff = digits1[i] - digits2[i] - borrow
        if diff <0:
            diff += 10
            borrow = 1
        else:
            borrow = 0
        result.append(diff)

    while len(result) > 1 and result[-1] == 0:
        result.pop()

    result_str = ''.join(str(d) for d in result[::-1])
    return result_str
def add_positive(num1, num2):
    digits1 = [int(d) for d in num1][::-1]
    digits2 = [int(d) for d in num2][::-1]

    max_len = max(len(digits1), len(digits2))
    digits1.extend([0] * (max_len - len(digits1)))
    digits2.extend([0] * (max_len - len(digits2)))

    result = []
    carry = 0

    for i in range(max_len):
        total = digits1[i] + digits2[i] + carry
        result.append(total % 10)
        carry = total // 10
        if carry > 0:
            result.append(carry)
        result_str = ''.join(str(d) for d in result[::-1])
        return result_str
if __name__ == '__main__':
    result = long_sub()
    prnt("Результат: ", result)