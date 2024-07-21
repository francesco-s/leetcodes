# Example 1:
#
# Input
# ["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
# [[], [100], [80], [60], [70], [60], [75], [85]]
# Output
# [null, 1, 1, 1, 2, 1, 4, 6]
#
# Explanation
# StockSpanner stockSpanner = new StockSpanner();
# stockSpanner.next(100); // return 1
# stockSpanner.next(80);  // return 1
# stockSpanner.next(60);  // return 1
# stockSpanner.next(70);  // return 2
# stockSpanner.next(60);  // return 1
# stockSpanner.next(75);  // return 4, because the last 4 prices (including today's price of 75) were less than or equal to today's price.
# stockSpanner.next(85);  // return 6
from collections import deque


class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        count = 1

        while self.stack and self.stack[-1][0] <= price:
            count += self.stack.pop()[1]

        self.stack.append([price, count])

        return count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

stockSpanner = StockSpanner()
print(stockSpanner.next(100))
print(stockSpanner.next(80))
print(stockSpanner.next(60))
print(stockSpanner.next(70))
print(stockSpanner.next(60))
print(stockSpanner.next(75))
print(stockSpanner.next(85))
# [null, 1, 1, 1, 2, 1, 4, 6]

print()

stockSpanner = StockSpanner()
print(stockSpanner.next(31))
print(stockSpanner.next(41))
print(stockSpanner.next(48))
print(stockSpanner.next(59))
print(stockSpanner.next(79))
# [null,1,1,2,3,4]
