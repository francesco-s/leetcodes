class TimeMap:

    def __init__(self):
        # SC: O(N), where N is the total number of set operations (unique key-timestamp pairs)
        self.key_time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # TC: O(1)
        # SC: O(1) per set operation
        if key not in self.key_time_map:
            self.key_time_map[key] = {}
        self.key_time_map[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        # TC: O(T), where T is the timestamp value (worst case)
        # SC: O(1)
        if key not in self.key_time_map.keys():
            return ""
        for t in reversed(range(1, timestamp + 1)):
            if t in self.key_time_map[key]:
                return self.key_time_map[key][t]
        return ""

# Test cases

# Test case 1
timeMap1 = TimeMap()
timeMap1.set("foo", "bar", 1)
result1_1 = timeMap1.get("foo", 1)
print(f"Test case 1.1: {result1_1}")  # Expected: "bar"

result1_2 = timeMap1.get("foo", 3)
print(f"Test case 1.2: {result1_2}")  # Expected: "bar"

timeMap1.set("foo", "bar2", 4)
result1_3 = timeMap1.get("foo", 4)
print(f"Test case 1.3: {result1_3}")  # Expected: "bar2"

result1_4 = timeMap1.get("foo", 5)
print(f"Test case 1.4: {result1_4}")  # Expected: "bar2"

# Test case 2
timeMap2 = TimeMap()
timeMap2.set("love", "high", 10)
timeMap2.set("love", "low", 20)
result2_1 = timeMap2.get("love", 5)
print(f"Test case 2.1: {result2_1}")  # Expected: ""

result2_2 = timeMap2.get("love", 10)
print(f"Test case 2.2: {result2_2}")  # Expected: "high"

result2_3 = timeMap2.get("love", 15)
print(f"Test case 2.3: {result2_3}")  # Expected: "high"

result2_4 = timeMap2.get("love", 20)
print(f"Test case 2.4: {result2_4}")  # Expected: "low"

result2_5 = timeMap2.get("love", 25)
print(f"Test case 2.5: {result2_5}")  # Expected: "low"
