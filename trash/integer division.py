# целочисленное деление без / // *

def division(number: int, by: int) -> int:
    res = 0
    sign = 1 if (number < 0 and by < 0) or (number > 0 and by > 0) else -1
    number = abs(number)
    by = abs(by)
    while number > 0:
        number -= by
        if number >= 0:
            res += 1
    return res if sign == 1 else -res


assert division(6, -3) == 6 // -3
assert division(-6, -3) == -6 // -3
assert division(-6, 3) == -6 // 3
assert division(6, 3) == 6 // 3
assert division(10, 2) == 10 // 2
assert division(5, 2) == 5 // 2
assert division(22, 2) == 22 // 2
assert division(22, 1) == 22 // 1
assert division(100, 2) == 100 // 2
assert division(0, 2) == 0 // 2
