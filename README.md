# LeetCode Solutions

![LeetCode](https://img.shields.io/badge/LeetCode-Practice-orange)
![Python](https://img.shields.io/badge/Python-3.x-blue)

A collection of my solutions to LeetCode problems, implemented primarily in **Python**. This repository serves as a personal coding journal to improve problem-solving skills, strengthen Data Structures & Algorithms concepts, and prepare for coding interviews.

## About

This repository contains solutions to LeetCode problems that I solve regularly. Each solution is written with a focus on:

* Clean and readable code
* Optimal approaches whenever possible
* Interview-oriented problem solving
* Consistent coding practices

## Topics Covered

### Data Structures

* Arrays
* Strings
* Linked Lists
* Stacks
* Queues
* Hash Maps
* Trees
* Binary Search Trees
* Heaps
* Graphs
* Tries

### Algorithms

* Binary Search
* Two Pointers
* Sliding Window
* Recursion
* Backtracking
* Dynamic Programming
* Greedy Algorithms
* Graph Traversal (BFS/DFS)
* Union Find
* Bit Manipulation

## Repository Structure

```text
leetcode_solutions/
│
├── Arrays/
├── Strings/
├── LinkedList/
├── Trees/
├── Graphs/
├── DynamicProgramming/
├── BinarySearch/
└── ...
```

*(Folder structure may vary as more solutions are added.)*

## Example Solution Format

```python
class Solution:
    def twoSum(self, nums, target):
        mp = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in mp:
                return [mp[diff], i]

            mp[num] = i
```

## Goals

* Solve LeetCode problems consistently
* Improve algorithmic thinking
* Prepare for technical interviews
* Build a strong DSA foundation
* Track coding progress publicly

## LeetCode Profile

Feel free to connect and follow my progress:

🔗 LeetCode: https://leetcode.com/

## Future Improvements

* Add time and space complexity analysis
* Add explanations for each problem
* Organize problems by topic
* Add multiple approaches for important problems
* Automate solution uploads using LeetCode Sync

## Contributions

This repository is primarily for personal learning and tracking progress. Suggestions and improvements are always welcome.

## Author

**Anush Rao**

* AIML Student @ NMAM Institute of Technology
* AI & Machine Learning Enthusiast
* Competitive Programming Learner

GitHub: https://github.com/Anush1214

---

⭐ If you find this repository useful, consider giving it a star.
