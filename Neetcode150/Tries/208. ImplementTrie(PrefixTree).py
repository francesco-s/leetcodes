class TrieNode:
    def __init__(self):
        self._is_end = False
        self.links = [None] * 26

    def contains_key(self, ch: str) -> bool:
        return self.links[ord(ch) - ord("a")] is not None

    def get(self, ch: str):
        return self.links[ord(ch) - ord("a")]

    def put(self, ch: str, node: 'TrieNode'):
        self.links[ord(ch) - ord("a")] = node

    def set_end(self):
        self._is_end = True

    @property
    def is_end(self):
        return self._is_end


class Trie:

    def __init__(self):
        # TC: O(1)
        # SC: O(1)
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # TC: O(L) where L is the length of word
        # SC: O(L) in worst-case for the created nodes
        node = self.root
        for ch in word:
            if not node.contains_key(ch):
                node.put(ch, TrieNode())
            node = node.get(ch)
        node.set_end()

    def search_prefix(self, word: str) -> TrieNode:
        # TC: O(L)
        # SC: O(1)
        node = self.root
        for ch in word:
            if node.contains_key(ch):
                node = node.get(ch)
            else:
                return None
        return node

    def search(self, word: str) -> bool:
        # TC: O(L)
        # SC: O(1)
        node = self.search_prefix(word)
        return node is not None and node.is_end

    def startsWith(self, prefix: str) -> bool:
        # TC: O(L)
        # SC: O(1)
        node = self.search_prefix(prefix)
        return node is not None


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


# Test cases (mirror canonical example)
trie = Trie()
trie.insert("apple")
print("Test 1:", trie.search("apple"))    # Expected: True
print("Test 2:", trie.search("app"))      # Expected: False
print("Test 3:", trie.startsWith("app"))  # Expected: True
trie.insert("app")
print("Test 4:", trie.search("app"))      # Expected: True

# More tests
trie2 = Trie()
for w in ["cat", "car", "care", "dog"]:
    trie2.insert(w)
print("Test 5:", trie2.search("cat"))       # Expected: True
print("Test 6:", trie2.search("ca"))        # Expected: False
print("Test 7:", trie2.startsWith("ca"))    # Expected: True
print("Test 8:", trie2.startsWith("care"))  # Expected: True
print("Test 9:", trie2.search("care"))      # Expected: True
print("Test 10:", trie2.search("career"))   # Expected: False
