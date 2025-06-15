def isPalindrome2(x: int) -> bool:
    return str(x) == str(x)[::-1]


def isPalindrome(x: int) -> bool:
    x_reverted = 0
    i = 1

    if x // 10 == 0:
        return True

    while x > x_reverted:
        x_reverted = x_reverted * 10 + x % 10 
        if x_reverted == 0:
            i *= 10
        x //= 10

    if x_reverted > x and x_reverted >= 10:
        x_reverted //= 10
    
    return x * i == x_reverted



print(isPalindrome(121))
print(isPalindrome(-121))
print(isPalindrome(124))
print(isPalindrome(1234))
print(isPalindrome(1221))
print(isPalindrome(1127211))
print(isPalindrome(10))
print(isPalindrome(1))
print(isPalindrome(101))
print(isPalindrome(21120))
