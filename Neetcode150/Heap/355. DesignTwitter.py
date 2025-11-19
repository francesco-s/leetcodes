import heapq
from collections import defaultdict
from typing import List


class Twitter:
    def __init__(self):
        self.timer = 0
        self.tweets = defaultdict(list)  # userId -> [(timestamp, tweetId), ...]
        self.following = defaultdict(set)  # userId -> {followeeId, ...}

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Time Complexity: O(1)
        Space Complexity: O(1) per tweet (total O(T) for all tweets)
        """
        self.timer += 1
        self.tweets[userId].append((-self.timer, tweetId))  # max-heap

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Time Complexity: O(1)
        Space Complexity: O(1) per follow relationship
        """
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.following[followerId].discard(followeeId)

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Time Complexity: O(N log N), where N is the total number of tweets from userId and their followees.
        Space Complexity: O(N) for the heap.
        """
        all_tweets = []
        all_tweets.extend(self.tweets[userId])
        for followee in self.following[userId]:
            all_tweets.extend(self.tweets[followee])

        heapq.heapify(all_tweets)

        feed = []
        for _ in range(10):
            if all_tweets:
                _, tweetId = heapq.heappop(all_tweets)
                feed.append(tweetId)
            else:
                break
        return feed


# Test cases (mirror the canonical example)
tw = Twitter()

tw.postTweet(1, 5)
print("Test 1:", tw.getNewsFeed(1))  # Expected: [5]

tw.follow(1, 2)
tw.postTweet(2, 6)
print("Test 2:", tw.getNewsFeed(1))  # Expected: [6, 5]

tw.unfollow(1, 2)
print("Test 3:", tw.getNewsFeed(1))  # Expected: [5]

# More tests
tw2 = Twitter()
tw2.postTweet(1, 10)
tw2.postTweet(1, 11)
tw2.postTweet(2, 20)
tw2.follow(3, 1)
tw2.follow(3, 2)
print("Test 4:", tw2.getNewsFeed(3))  # Expected: [20, 11, 10] (up to 10 most recent)

tw3 = Twitter()
for i in range(15):
    tw3.postTweet(1, 100 + i)
print("Test 5:", len(tw3.getNewsFeed(1)))  # Expected: 10

tw4 = Twitter()
tw4.postTweet(1, 1)
tw4.follow(1, 1)  # no-op effectively
print("Test 6:", tw4.getNewsFeed(1))  # Expected: [1]
tw4.unfollow(1, 1)  # should be a no-op (cannot unfollow self per constraints)
print("Test 7:", tw4.getNewsFeed(1))  # Expected: [1]
