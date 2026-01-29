# 56. Merge Intervals
# https://leetcode.com/problems/merge-intervals/
# Approach: Compare every interval with every other interval and merge any overlapping ones. Repeat this process until no more overlaps remain.
# Complexity: Time: O(n²)  Space: O(n)
# class Solution:
#     def merge(self, intervals):
#         merged = True
#         while merged:
#             merged = False
#             res = []
#             used = [False] * len(intervals)
#             for i in range(len(intervals)):
#                 if used[i]:
#                     continue
#                 start, end = intervals[i]
#                 for j in range(i + 1, len(intervals)):
#                     if used[j]:
#                         continue
#                     s, e = intervals[j]
#                     # check overlap
#                     if not (end < s or e < start):
#                         start = min(start, s)
#                         end = max(end, e)
#                         used[j] = True
#                         merged = True
#                 used[i] = True
#                 res.append([start, end])
#             intervals = res        
#         return intervals
# Example Walkthrough
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Compare [1,3] and [2,6] → overlap → merge → [1,6]
# [8,10] and [15,18] → no overlap
# Result: [[1,6],[8,10],[15,18]]

# Approach: If intervals are sorted by start time, overlapping intervals will appear next to each other. We iterate once, merging when the current interval overlaps with the last merged one.
# Complexity: Time: O(n log n)  Space: O(n)
class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]
        for start, end in intervals[1:]:
            last_end = merged[-1][1]
            if start <= last_end:              # overlap
                merged[-1][1] = max(last_end, end)
            else:                              # no overlap
                merged.append([start, end])
        return merged
# Example Walkthrough
# Input: [[1,3],[2,6],[8,10],[15,18]]
# After sorting: [[1,3],[2,6],[8,10],[15,18]]
# Current	Last Merged	Action
# [2,6]	[1,3]	overlap → merge → [1,6]
# [8,10]	[1,6]	no overlap → add
# [15,18]	[8,10]	no overlap → add
# Output: [[1,6],[8,10],[15,18]]