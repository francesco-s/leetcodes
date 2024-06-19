class Solution:
    def checkIfPangram3(sentence: str) -> bool:
        return len(set(sentence)) == 26

    def checkIfPangram2(sentence: str) -> bool:
        char_counter = {}
        for char in sentence:
            char_counter[char] = True

        print(char_counter)

        return sum(char_counter.values()) == 26

    def checkIfPangram(sentence: str) -> bool:
        seen = 0

        for char in sentence:
            mapped_index = ord(char) - ord('a')
            bit = 1 << mapped_index
            seen |= bit
        return seen == (1 << 26) - 1


print(Solution.checkIfPangram3("thequickbrownfoxjumpsoverthelazydog"))
print(Solution.checkIfPangram2("thequickbrownfoxjumpsoverthelazydog"))
print(Solution.checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))

print(Solution.checkIfPangram3("leetcode"))
print(Solution.checkIfPangram2("leetcode"))
print(Solution.checkIfPangram("leetcode"))
