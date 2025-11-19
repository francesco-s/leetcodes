class Solution:
    def hammingWeight(self, n):
        """
        Returns the number of '1' bits in the binary representation of n.

        Time Complexity: O(32) = O(1), since n is a 32-bit integer.
        Space Complexity: O(1), uses constant extra space.
        """
        res = 0

        while n:
            res += n & 1
            n = n >> 1

        return res


# Test cases
solution = Solution()

# Test case 1 (example)
n1 = 0b00000000000000000000000000001011  # 11 in decimal
res1 = solution.hammingWeight(n1)
print(f"Test case 1: {res1}")  # Expected: 3

# Test case 2 (example)
n2 = 0b00000000000000000000000010000000  # 128 in decimal
res2 = solution.hammingWeight(n2)
print(f"Test case 2: {res2}")  # Expected: 1

# Test case 3 (example)
n3 = 0b11111111111111111111111111111101  # 4294967293 in decimal
res3 = solution.hammingWeight(n3)
print(f"Test case 3: {res3}")  # Expected: 31

# Test case 4 (all zeros)
n4 = 0
res4 = solution.hammingWeight(n4)
print(f"Test case 4: {res4}")  # Expected: 0

# Test case 5 (all ones)
n5 = 0b11111111111111111111111111111111  # 4294967295 in decimal
res5 = solution.hammingWeight(n5)
print(f"Test case 5: {res5}")  # Expected: 32

# Test case 6 (single bit)
n6 = 1
res6 = solution.hammingWeight(n6)
print(f"Test case 6: {res6}")  # Expected: 1

# Test case 7 (mixed bits)
n7 = 0b00000000000000000000000000000111  # 7 in decimal
res7 = solution.hammingWeight(n7)
print(f"Test case 7: {res7}")  # Expected: 3
