class Solution:
    
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        right = 0
        left = len(s) - 1

        while right < left:
            while right < left and not s[right].isalnum():
                right += 1
            while right < left and not s[left].isalnum():
                left -= 1

            if s[right].lower() != s[left].lower():
                return False

            right += 1
            left -= 1

        return True
    

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
s3 = " "
result3 = solution.isPalindrome(s3)
print(f"Test case 3: {result3}")  # Expected: True

# Test case 4
s4 = "a"
result4 = solution.isPalindrome(s4)
print(f"Test case 4: {result4}")  # Expected: True

# Test case 5
s5 = "Madam"
result5 = solution.isPalindrome(s5)
print(f"Test case 5: {result5}")  # Expected: True

# Test case 6
s6 = "0P"
result6 = solution.isPalindrome(s6)
print(f"Test case 6: {result6}")  # Expected: False
