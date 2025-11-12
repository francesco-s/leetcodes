class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
        Multiplies two non-negative integers represented as strings.

        Time Complexity: O(m * n), where m and n are the lengths of num1 and num2.
        Space Complexity: O(m + n), for the result array.
        """
        if "0" in [num1, num2]:
            return "0"

        res = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]

        for i in range(len(num1)):
            for j in range(len(num2)):
                res[i + j] += int(num1[i]) * int(num2[j])
                res[i + j + 1] += res[i + j] // 10
                res[i + j] %= 10

        while len(res) > 1 and res[-1] == 0:
            res.pop()

        return "".join(map(str, res[::-1]))


# Test cases
solution = Solution()

# Test case 1 (example - simple)
num1_1, num2_1 = "2", "3"
res1 = solution.multiply(num1_1, num2_1)
print(f"Test case 1: {res1}")  # Expected: "6"

# Test case 2 (example - larger numbers)
num1_2, num2_2 = "123", "456"
res2 = solution.multiply(num1_2, num2_2)
print(f"Test case 2: {res2}")  # Expected: "56088"

# Test case 3 (multiply by zero)
num1_3, num2_3 = "123", "0"
res3 = solution.multiply(num1_3, num2_3)
print(f"Test case 3: {res3}")  # Expected: "0"

# Test case 4 (multiply by one)
num1_4, num2_4 = "456", "1"
res4 = solution.multiply(num1_4, num2_4)
print(f"Test case 4: {res4}")  # Expected: "456"

# Test case 5 (both single digits)
num1_5, num2_5 = "9", "9"
res5 = solution.multiply(num1_5, num2_5)
print(f"Test case 5: {res5}")  # Expected: "81"

# Test case 6 (larger test)
num1_6, num2_6 = "987", "43"
res6 = solution.multiply(num1_6, num2_6)
print(f"Test case 6: {res6}")  # Expected: "42441"

# Test case 7 (zero times zero)
num1_7, num2_7 = "0", "0"
res7 = solution.multiply(num1_7, num2_7)
print(f"Test case 7: {res7}")  # Expected: "0"

# Test case 8 (different lengths)
num1_8, num2_8 = "99", "999"
res8 = solution.multiply(num1_8, num2_8)
print(f"Test case 8: {res8}")  # Expected: "98901"
