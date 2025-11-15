from typing import List


class Solution:

    def countBits(self, n: int) -> List[int]:
        """
        Count the number of 1-bits in binary representation of each number from 0 to n.
        
        Time Complexity: O(n log n) - for each number, we count bits in O(log n)
        Space Complexity: O(1) - excluding the output array
        """
        res = []
        
        for num in range(n + 1):
            ones = 0
            curr = num
            while curr:
                ones += curr & 1
                curr >>= 1
            res.append(ones)

        return res


# Test cases
solution = Solution()

# Test case 1 (example)
n1 = 2
res1 = solution.countBits(n1)
print(f"Test case 1: {res1}")  # Expected: [0,1,1]

# Test case 2 (example)
n2 = 5
res2 = solution.countBits(n2)
print(f"Test case 2: {res2}")  # Expected: [0,1,1,2,1,2]

# Test case 3 (zero)
n3 = 0
res3 = solution.countBits(n3)
print(f"Test case 3: {res3}")  # Expected: [0]

# Test case 4 (one)
n4 = 1
res4 = solution.countBits(n4)
print(f"Test case 4: {res4}")  # Expected: [0,1]

# Test case 5 (larger number)
n5 = 8
res5 = solution.countBits(n5)
print(f"Test case 5: {res5}")  # Expected: [0,1,1,2,1,2,2,3,1]

# Test case 6 (power of 2)
n6 = 4
res6 = solution.countBits(n6)
print(f"Test case 6: {res6}")  # Expected: [0,1,1,2,1]

# Test case 7 (larger example)
n7 = 10
res7 = solution.countBits(n7)
print(f"Test case 7: {res7}")  # Expected: [0,1,1,2,1,2,2,3,1,2,2]
