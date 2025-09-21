class TrieNode:
    def __init__(self):
        self.children = {}   # char -> TrieNode
        self.end = False     # marks end of word

class WordDictionary: # TLE

    def __init__(self):
        self.store = []
        

    def addWord(self, word: str) -> None:
        # Time Complexity: O(1) per call.
        # Space Complexity: O(m) per word added, where m is the length of the word.
        self.store.append(word)
        

    def search(self, word: str) -> bool:
        # Time Complexity: O(N * L) in the worst case, where
        #   N is the number of words in the store and L is the average word length.
        # Space Complexity: O(1) additional space.
        for w in self.store:
            if len(w) != len(word):
                continue
            i = 0
            while i < len(w):
                if w[i] == word[i] or word[i] == '.':
                    i += 1
                else:
                    break
            
            if i == len(w):
                return True

        return False
        



# Test cases (canonical)
wd = WordDictionary()
wd.addWord("bad")
wd.addWord("dad")
wd.addWord("mad")
print("Test 1:", wd.search("pad"))  # Expected: False
print("Test 2:", wd.search("bad"))  # Expected: True
print("Test 3:", wd.search(".ad"))  # Expected: True
print("Test 4:", wd.search("b.."))  # Expected: True

# More tests
wd2 = WordDictionary()
for w in ["apple", "app", "apex", "bat", "batch", "bath"]:
    wd2.addWord(w)
print("Test 5:", wd2.search("app"))    # Expected: True
print("Test 6:", wd2.search("appl"))   # Expected: False
print("Test 7:", wd2.search("a..le"))  # Expected: True  ("apple")
print("Test 8:", wd2.search("ba.."))   # Expected: True  ("batch","bath")
print("Test 9:", wd2.search("b.t"))    # Expected: True  ("bat")
print("Test 10:", wd2.search("...."))  # Expected: True  (e.g., "apex","bath")
