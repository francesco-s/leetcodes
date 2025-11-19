class Solution:
    def isHappy(self, n: int) -> bool:
        """
        Determines if a number is a happy number.

        Time Complexity (TC): O(log n) per iteration, since sum_of_square processes each digit.
        In the worst case, the process may repeat for a bounded number of steps (since numbers eventually cycle or reach 1), so overall TC is O(k * log n), where k is the number of steps (bounded by a small constant for all n).

        Space Complexity (SC): O(log n): each number has log(n) digits max.
        """
        visited = set()

        def sum_of_square(n):
            square = 0
            while n > 0:
                square += (n % 10) ** 2
                n //= 10
            return square

        while n != 1:
            n = sum_of_square(n)
            if n in visited:
                return False
            visited.add(n)

        return True


# Test cases
solution = Solution()

# Test case 1 (example - happy number)
n1 = 19
res1 = solution.isHappy(n1)
print(f"Test case 1: {res1}")  # Expected: True

# Test case 2 (example - not happy)
n2 = 2
res2 = solution.isHappy(n2)
print(f"Test case 2: {res2}")  # Expected: False

# Test case 3 (already 1)
n3 = 1
res3 = solution.isHappy(n3)
print(f"Test case 3: {res3}")  # Expected: True

# Test case 4 (happy number)
n4 = 7
res4 = solution.isHappy(n4)
print(f"Test case 4: {res4}")  # Expected: True

# Test case 5 (not happy)
n5 = 20
res5 = solution.isHappy(n5)
print(f"Test case 5: {res5}")  # Expected: False

# Test case 6 (happy number)
n6 = 100
res6 = solution.isHappy(n6)
print(f"Test case 6: {res6}")  # Expected: True

# Test case 7 (not happy - cycles to 4)
n7 = 4
res7 = solution.isHappy(n7)
print(f"Test case 7: {res7}")  # Expected: False

# Test case 8 (happy number)
n8 = 10
res8 = solution.isHappy(n8)
print(f"Test case 8: {res8}")  # Expected: True
