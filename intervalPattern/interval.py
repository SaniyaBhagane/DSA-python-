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
# class Solution:
#     def merge(self, intervals):
#         intervals.sort(key=lambda x: x[0])
#         merged = [intervals[0]]
#         for start, end in intervals[1:]:
#             last_end = merged[-1][1]
#             if start <= last_end:              # overlap
#                 merged[-1][1] = max(last_end, end)
#             else:                              # no overlap
#                 merged.append([start, end])
#         return merged
# Example Walkthrough
# Input: [[1,3],[2,6],[8,10],[15,18]]
# After sorting: [[1,3],[2,6],[8,10],[15,18]]
# Current	Last Merged	Action
# [2,6]	[1,3]	overlap → merge → [1,6]
# [8,10]	[1,6]	no overlap → add
# [15,18]	[8,10]	no overlap → add
# Output: [[1,6],[8,10],[15,18]]

# -------------------------------------------------------------------------------------------------------------------------------
# 986. Interval List Intersections
# https://leetcode.com/problems/interval-list-intersections/description/
# Approach: For each interval in the first list, check it against every interval in the second list. If the two intervals overlap, compute their intersection and add it to the result. Return all such intersections.
# Complexity: Time: O(n × m)  Space: O(1)
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        for i in range(len(firstList)):
            s1, e1 = firstList[i]
            for j in range(len(secondList)):
                s2, e2 = secondList[j]
                # Same overlap condition
                if e1 >= s2 and e2 >= s1:
                    res.append([max(s1, s2), min(e1, e2)])        
        return res
# Example Walkthrough
# firstList  = [[0,2],[5,10]]
# secondList = [[1,5],[8,12]]
# [0,2] ∩ [1,5] → [1,2]
# [0,2] ∩ [8,12] → no overlap
# [5,10] ∩ [1,5] → [5,5]
# [5,10] ∩ [8,12] → [8,10]
# Result: [[1,2], [5,5], [8,10]]

# Approach 2: