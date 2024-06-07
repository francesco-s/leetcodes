import math


def reverse(x: int) -> int:
    rev = int(str(abs(x))[::-1])
    if rev > pow(2, 31) - 1:
        return 0
    elif rev < pow(-2, 31):
        return 0
    elif x > 0:
        return rev
    else:
        return -rev


print(reverse(-123))
print(reverse(123))
print(reverse(120))
