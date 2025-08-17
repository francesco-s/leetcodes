class Codec:

    def encodeNonAscii(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        return '😀'.join(strs)

    def decodeNonAscii(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        return s.split('😀')
    

    def encode(self, strs):
        encoded_string = ''
        for s in strs:
            # Append the length, the delimiter, and the string itself.
            encoded_string += str(len(s)) + '/:' + s

        print(encoded_string)
        return encoded_string

    def decode(self, s):
        decoded_strings = []
        i = 0
        while i < len(s):
            delim = s.find('/:', i)
            length = int(s[i:delim])
            str_ = s[delim+2 : delim+2+length]
            decoded_strings.append(str_)
            i = delim + 2 + length
        return decoded_strings

# Test cases
codec = Codec()

# Test case 1
strs1 = ["lint", "code", "love", "you"]
encoded1 = codec.encode(strs1)
decoded1 = codec.decode(encoded1)
print(f"Test case 1: {decoded1}")  # Expected: ["lint", "code", "love", "you"]

# Test case 2
strs2 = ["we", "say", ":", "yes"]
encoded2 = codec.encode(strs2)
decoded2 = codec.decode(encoded2)
print(f"Test case 2: {decoded2}")  # Expected: ["we", "say", ":", "yes"]

# Test case 3
strs3 = []
encoded3 = codec.encode(strs3)
decoded3 = codec.decode(encoded3)
print(f"Test case 3: {decoded3}")  # Expected: []

# Test case 4
strs4 = [""]
encoded4 = codec.encode(strs4)
decoded4 = codec.decode(encoded4)
print(f"Test case 4: {decoded4}")  # Expected: [""]

# Test case 5
strs5 = ["a", "", "b"]
encoded5 = codec.encode(strs5)
decoded5 = codec.decode(encoded5)
print(f"Test case 5: {decoded5}")  # Expected: ["a", "", "b"]
