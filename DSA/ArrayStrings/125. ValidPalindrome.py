class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Placeholder for the actual implementation
        new_string = ""
                
        for char in s.lower():
            if char in "qwertyuiopasdfghjklzxcvbnm1234567890":
                new_string += char

        return new_string == new_string[::-1]

# Test cases
solution = Solution()

# Test case 1
s1 = "A man, a plan, a canal: Panama"
result1 = solution.isPalindrome(s1)
print(f"Test case 1: {result1}")  # Expected: True

# Test case 2
s2 = "race a car"
result2 = solution.isPalindrome(s2)
print(f"Test case 2: {result2}")  # Expected: False

# Test case 3
s3 = ""
result3 = solution.isPalindrome(s3)
print(f"Test case 3: {result3}")  # Expected: True