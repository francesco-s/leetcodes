class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Find the length of the longest substring containing the same letter 
        after replacing at most k characters using sliding window technique.
        
        Time Complexity: O(n) where n is length of string
        Space Complexity: O(1) since we have at most 26 characters (constant space)
        """
        left, right = 0, 0  # Two pointers for sliding window
        max_freq = 0        # Maximum frequency of any character in current window
        
        # Initialize frequency map for all unique characters
        chars_freq = dict()
        for char in set(s):
            chars_freq[char] = 0
        
        while right < len(s):
            # Expand window by including character at right pointer
            chars_freq[s[right]] += 1
            
            # Update max frequency seen so far (never decreases)
            # This is key optimization - we don't recalculate max_freq when shrinking
            max_freq = max(max_freq, chars_freq[s[right]])
            
            # Calculate current window size
            window_size = right - left + 1
            
            # Check if current window is invalid
            # window_size - max_freq = number of characters that need to be replaced
            if window_size - max_freq > k:
                # Shrink window from left - remove leftmost character
                chars_freq[s[left]] -= 1
                left += 1
                # Note: we don't decrease max_freq here (key insight!)
            
            # Move right pointer to expand window for next iteration (expand the window)
            right += 1
        
        # At end of loop, right points one position beyond last character
        # So right - left gives us the length of the longest valid window found
        return right - left

# Test cases
solution = Solution()

# Test case 1
s1 = "ABAB"
k1 = 2
result1 = solution.characterReplacement(s1, k1)
print(f"Test case 1: {result1}")  # Expected: 4

# Test case 2
s2 = "AABABBA"
k2 = 1
result2 = solution.characterReplacement(s2, k2)
print(f"Test case 2: {result2}")  # Expected: 4

# Test case 3
s3 = "ABCDE"
k3 = 1
result3 = solution.characterReplacement(s3, k3)
print(f"Test case 3: {result3}")  # Expected: 2

# Test case 4
s4 = "AAAA"
k4 = 2
result4 = solution.characterReplacement(s4, k4)
print(f"Test case 4: {result4}")  # Expected: 4

# Test case 5
s5 = "ABCDABCD"
k5 = 2
result5 = solution.characterReplacement(s5, k5)
print(f"Test case 5: {result5}")  # Expected: 4

# Test case 6
s6 = "A"
k6 = 1
result6 = solution.characterReplacement(s6, k6)
print(f"Test case 6: {result6}")  # Expected: 1
