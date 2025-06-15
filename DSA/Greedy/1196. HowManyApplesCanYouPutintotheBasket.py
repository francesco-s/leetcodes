import heapq


class Solution:
    def maxNumberOfApplesHeap(self, weight):
        heapq.heapify(weight)
        apples = units = 0
        max_units = 5000

        while weight:
            max_units -= heapq.heappop(weight)
            if max_units < 0:
                break
            apples += 1
        
        return apples
    
    def maxNumberOfApples(self, weight):
        cum_sum = 5000
        num_apples = 0

        weight.sort()
        for w in weight:
            cum_sum -= w
            if cum_sum < 0:
                break
            num_apples += 1

        return num_apples


# Test cases
solution = Solution()

# Test case 1
apples1 = [100, 150, 200, 200, 2000]
result1 = solution.maxNumberOfApples(apples1)
print(f"Test case 1: {result1}")  # Expected: 5

# Test case 2
apples2 = [900, 1000, 800, 700, 600, 500]
result2 = solution.maxNumberOfApples(apples2)
print(f"Test case 2: {result2}")  # Expected: 6