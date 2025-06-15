from collections import deque


class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        self.window_sum = 0

    def next(self, val: int) -> float:
        if len(self.queue) >= self.size:
            self.window_sum -= self.queue.popleft()
        self.queue.append(val)
        self.window_sum += val

        return self.window_sum / len(self.queue)

    def getdq(self) -> deque:
        return self.queue


class MovingAverage2:

    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        self.count = 0

    def next(self, val: int) -> float:
        self.count += 1
        if self.count > self.size:
            self.queue.popleft()
        self.queue.append(val)

        return sum(self.queue) / len(self.queue)

    def getdq(self) -> deque:
        return self.queue


# ["MovingAverage", "next", "next", "next", "next"]
# significa che faccio la media sono dal secondo step (cioè quando ho il primo uno)
# movingAverage.next(1); // return 1.0 = 1 / 1
# movingAverage.next(10); // return 5.5 = (1 + 10) / 2
# movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
# movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3

obj = MovingAverage(3)

# param_1 = obj.next(3)
# print(param_1)
param_1 = obj.next(1)
param_1 = obj.next(10)
param_1 = obj.next(3)
param_1 = obj.next(5)

print(obj.getdq())
