Below is a clear list of when to use a **Heap, Stack, Queue, and HashMap**—with practical examples and typical use cases often seen on coding challenge platforms like LeetCode.

---

## **When to Use a Heap (Min-Heap / Max-Heap)**

**Typical Scenarios:**

- **Priority Queues:** When you need to quickly retrieve the minimum or maximum element in a dynamic dataset.
- **Top-K Problems:** Finding the k largest or smallest elements in an array without fully sorting it.
- **Graph Algorithms:** Algorithms like Dijkstra’s or A\* require a heap to efficiently select the node with the smallest cost.
- **Merging Sorted Lists:** Efficiently merging k sorted lists without repeatedly sorting the entire collection.

**LeetCode Examples:**

- **[Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)** (Medium) – Find the kth largest number.
- **[Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)** (Hard) – Merge multiple sorted linked lists.
- **[Network Delay Time](https://leetcode.com/problems/network-delay-time/)** (Medium) – Compute the shortest time for signals to reach all nodes.
- **[Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)** (Hard) – Find the maximum in each sliding window.

---

## **When to Use a Stack (LIFO)**

**Typical Scenarios:**

- **Backtracking and Depth-First Search (DFS):** Stacks are used to keep track of function calls or recursive states.
- **Expression Evaluation:** Checking for balanced parentheses or evaluating Reverse Polish Notation.
- **Undo/Redo Mechanisms:** Maintaining a history of operations to revert actions.

**LeetCode Examples:**

- **[Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)** (Easy) – Verify if parentheses are balanced.
- **[Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/)** (Medium) – Evaluate mathematical expressions in RPN.
- **[Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)** (Medium) – Use a monotonic stack to determine the next warmer day.
- **[Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/)** (Hard) – Calculate the largest rectangle in a histogram using a monotonic stack.

---

## **When to Use a Queue (FIFO) or a Deque**

**Typical Scenarios:**

- **Breadth-First Search (BFS):** Processing nodes level by level in graphs or trees.
- **Sliding Windows:** Managing elements in a fixed-size window for efficient updates.
- **Real-Time Data Buffers:** When order of processing (first-in-first-out) is essential.

**LeetCode Examples:**

- **[Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)** (Medium) – Perform a BFS on a tree.
- **[Rotting Oranges](https://leetcode.com/problems/rotting-oranges/)** (Medium) – Simulate the spread of rot using BFS.
- **[Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)** (Hard) – Use `deque` to efficiently find the maximum in each window.
- **[Design Circular Queue](https://leetcode.com/problems/design-circular-queue/)** (Medium) – Implement a circular queue.

_Note:_ In Python, you can use:

- `queue.Queue()` for a thread-safe FIFO.
- `collections.deque()` for fast O(1) appends and pops from both ends.

---

## **When to Use a HashMap (Dictionary in Python)**

**Typical Scenarios:**

- **Fast Lookups:** When you need constant time O(1) access to values based on a key.
- **Frequency Counting:** Counting occurrences of elements in an array.
- **Duplicate Detection:** Quickly identifying duplicates.
- **Caching / Memoization:** Storing and retrieving computed results to avoid redundant work.

**LeetCode Examples:**

- **[Two Sum](https://leetcode.com/problems/two-sum/)** (Easy) – Find two numbers that add up to a target value.
- **[Group Anagrams](https://leetcode.com/problems/group-anagrams/)** (Medium) – Group strings that are anagrams of each other.
- **[Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)** (Medium) – Find the longest substring without duplicate characters.
- **[LRU Cache](https://leetcode.com/problems/lru-cache/)** (Medium) – Implement a Least Recently Used cache using an ordered dictionary.

_Note:_ In Python, you can also use:

- `collections.defaultdict()` for automatic initialization of dictionary keys.
- `collections.Counter()` for counting frequencies.
- `collections.OrderedDict()` when you need to preserve the order of insertion.

---

## **Summary Table**

| Data Structure           | When to Use                                                             | Typical Time Complexity          |
| ------------------------ | ----------------------------------------------------------------------- | -------------------------------- |
| **Heap (Min/Max Heap)**  | Priority queues, top-k problems, graph algorithms, merging sorted lists | O(log N) for insert/extract      |
| **Stack (LIFO)**         | Backtracking, DFS, expression evaluation, undo/redo                     | O(1) for push/pop                |
| **Queue (FIFO) / Deque** | BFS, sliding window problems, real-time buffers                         | O(1) for appends/pops with deque |
| **HashMap (Dictionary)** | Fast lookup, frequency counting, caching, duplicate detection           | O(1) average for get/set         |

---

## **Conclusion**

- **Heap:** Use when you need to quickly retrieve the minimum or maximum element, especially in dynamic priority queue scenarios.
- **Stack:** Use when the order of operations follows a Last-In-First-Out principle, such as in DFS or parsing expressions.
- **Queue/Deque:** Use when the order of processing should be First-In-First-Out, ideal for BFS and sliding window problems.
- **HashMap:** Use when fast lookups are crucial, such as counting frequencies, caching, or detecting duplicates.
