class Solution:
    def reverseBits(self, n: int) -> int:
        """
        Reverse bits of a 32-bit unsigned integer.

        TC: O(1) - fixed 32 iterations
        SC: O(1) - constant space
        """
        res = 0

        for i in range(32):
            bit = (n >> i) & 1
            res += bit << (31 - i)

        return res

    def reverseBits2(self, n):
        """
        Reverse bits using generator expression.

        TC: O(1) - fixed 32 iterations
        SC: O(1) - constant space
        """
        return sum(((n >> i) & 1) << (31 - i) for i in range(32))


# Test cases
solution = Solution()

# Test case 1 (example)
n1 = 0b00000010100101000001111010011100  # 43261596
res1 = solution.reverseBits(n1)
print(f"Test case 1: {res1}")  # Expected: 964176192

# Test case 2 (example)
n2 = 0b11111111111111111111111111111101  # 4294967293
res2 = solution.reverseBits(n2)
print(f"Test case 2: {res2}")  # Expected: 3221225471

# Test case 3 (all zeros)
n3 = 0b00000000000000000000000000000000  # 0
res3 = solution.reverseBits(n3)
print(f"Test case 3: {res3}")  # Expected: 0

# Test case 4 (single bit set)
n4 = 0b00000000000000000000000000000001  # 1
res4 = solution.reverseBits(n4)
print(f"Test case 4: {res4}")  # Expected: 2147483648

# Test case 5 (single bit at high position)
n5 = 0b10000000000000000000000000000000  # 2147483648
res5 = solution.reverseBits(n5)
print(f"Test case 5: {res5}")  # Expected: 1

# Test case 6 (alternating bits)
n6 = 0b10101010101010101010101010101010  # 2863311530
res6 = solution.reverseBits(n6)
print(f"Test case 6: {res6}")  # Expected: 1431655765

# Test case 7 (simple pattern)
n7 = 0b00000000000000000000000000001011  # 11
res7 = solution.reverseBits(n7)
print(f"Test case 7: {res7}")  # Expected: 3489660928
