def isAnagram(s: str, t: str) -> bool:
    def count_words(s):
        counter_dict = {}
        for char in s:
            if char in counter_dict.keys():
                counter_dict[char] += 1
            else:
                counter_dict[char] = 1
        return counter_dict

    if count_words(s) == count_words(t):
        return True

    return False


print(isAnagram("anagram", "nagaram"))
print(isAnagram("rat", "car"))

# Example 1:
#
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
#
# Input: s = "rat", t = "car"
# Output: false
