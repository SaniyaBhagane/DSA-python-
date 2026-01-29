# 56. Merge Intervals
# https://leetcode.com/problems/merge-intervals/
# Approach: Compare every interval with every other interval and merge any overlapping ones. Repeat this process until no more overlaps remain.
# Complexity: Time: O(n²)  Space: O(n)
class Solution:
    def merge(self, intervals):
        merged = True
        while merged:
            merged = False
            res = []
            used = [False] * len(intervals)
            for i in range(len(intervals)):
                if used[i]:
                    continue
                start, end = intervals[i]
                for j in range(i + 1, len(intervals)):
                    if used[j]:
                        continue
                    s, e = intervals[j]
                    # check overlap
                    if not (end < s or e < start):
                        start = min(start, s)
                        end = max(end, e)
                        used[j] = True
                        merged = True
                used[i] = True
                res.append([start, end])
            intervals = res        
        return intervals
# Example Walkthrough
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Compare [1,3] and [2,6] → overlap → merge → [1,6]
# [8,10] and [15,18] → no overlap
# Result: [[1,6],[8,10],[15,18]]