class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Time Complexity (TC):
            - Building frequency arrays for s1 and the first window: O(n + 26) ≈ O(n)
            - Sliding the window across s2 (m - n steps), each update is O(1): O(m - n)
            - Total: O(m + n) ≈ O(m)
        Space Complexity (SC):
            - Two fixed-size arrays of length 26: O(26) = O(1)
        """
                
        def ascii_calculator(s: str):
            res = [0] * 26
            for char in s:
                res[ord(char) - ord('a')] += 1
            return res

        n, m = len(s1), len(s2)
        if n > m:
            return False

        s1_ascii = ascii_calculator(s1)
        window = ascii_calculator(s2[:n])

        if window == s1_ascii:
            return True

        for i in range(n, m):
            # Update sliding window counts
            window[ord(s2[i]) - ord('a')] += 1
            window[ord(s2[i - n]) - ord('a')] -= 1

            if window == s1_ascii:
                return True

        return False


    def checkInclusionSort(self, s1: str, s2: str) -> bool:
        """
        Time Complexity (TC):
            - Sorting s1 once: O(s1_len log s1_len)
            - For each window (s2_len - s1_len + 1 windows):
                Sorting substring of size s1_len: O(s1_len log s1_len)
            - Total: O((s2_len - s1_len + 1) * s1_len log s1_len)
                    ≈ O((m - n) * n log n)
        Space Complexity (SC):
            - Sorting requires O(n) space for each substring
            - Overall: O(n)
        """

        def sort(s: str):
            return ''.join(sorted(s))

        s1_len = len(s1)
        s2_len = len(s2)
        sorted_s1 = sort(s1)

        for i in range(s2_len - s1_len + 1):
            # Sort every substring of length s1_len
            if sorted_s1 == sort(s2[i : i + s1_len]):
                return True

        return False






# Test cases
solution = Solution()

# Test case 1
s1_1 = "ab"
s2_1 = "eidbaooo"
result1 = solution.checkInclusion(s1_1, s2_1)
print(f"Test case 1: {result1}")  # Expected: True

# Test case 2
s1_2 = "ab"
s2_2 = "eidboaoo"
result2 = solution.checkInclusion(s1_2, s2_2)
print(f"Test case 2: {result2}")  # Expected: False

# Test case 3
s1_3 = "adc"
s2_3 = "dcda"
result3 = solution.checkInclusion(s1_3, s2_3)
print(f"Test case 3: {result3}")  # Expected: True

# Test case 4
s1_4 = "hello"
s2_4 = "ooolleoooleh"
result4 = solution.checkInclusion(s1_4, s2_4)
print(f"Test case 4: {result4}")  # Expected: False

# Test case 5
s1_5 = "abc"
s2_5 = "bbbca"
result5 = solution.checkInclusion(s1_5, s2_5)
print(f"Test case 5: {result5}")  # Expected: False

# Test case 6
s1_6 = "trinitrophenylmethylnitramine"
s2_6 = "dinitrophenylhydrazinetrinitrophenylmethylnitramine"
result6 = solution.checkInclusion(s1_6, s2_6)
print(f"Test case 6: {result6}")  # Expected: True
