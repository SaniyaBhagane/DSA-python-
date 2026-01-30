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
# class Solution:
#     def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
#         res = []
#         for i in range(len(firstList)):
#             s1, e1 = firstList[i]
#             for j in range(len(secondList)):
#                 s2, e2 = secondList[j]
#                 # Same overlap condition
#                 if e1 >= s2 and e2 >= s1:
#                     res.append([max(s1, s2), min(e1, e2)])        
#         return res
# Example Walkthrough
# firstList  = [[0,2],[5,10]]
# secondList = [[1,5],[8,12]]
# [0,2] ∩ [1,5] → [1,2]
# [0,2] ∩ [8,12] → no overlap
# [5,10] ∩ [1,5] → [5,5]
# [5,10] ∩ [8,12] → [8,10]
# Result: [[1,2], [5,5], [8,10]]

# Approach 2: Use two pointers to traverse both interval lists. If two intervals overlap, add their intersection.Move the pointer of the interval that ends first to find the next possible overlap.
# Complexity: Time: O(n + m)  Space: O(1)
# class Solution:
#     def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
#         i, j = 0, 0
#         res = []
#         while i < len(firstList) and j < len(secondList):
#             s1, e1 = firstList[i]
#             s2, e2 = secondList[j]
#             # Check overlap
#             if e1 >= s2 and e2 >= s1:
#                 res.append([max(s1, s2), min(e1, e2)])
#             # Move the pointer of the interval that ends first
#             if e1 < e2:
#                 i += 1
#             else:
#                 j += 1
#         return res
# Example Walkthrough
# firstList  = [[0,2],[5,10],[13,23],[24,25]]
# secondList = [[1,5],[8,12],[15,24],[25,26]]
# first	second	overlap	added
# [0,2]	[1,5]	yes	[1,2]
# [5,10]	[1,5]	yes	[5,5]
# [5,10]	[8,12]	yes	[8,10]
# [13,23]	[15,24]	yes	[15,23]
# [24,25]	[15,24]	yes	[24,24]
# [24,25]	[25,26]	yes	[25,25]

# -------------------------------------------------------------------------------------------------------------------------
# 3169. Count days without Interval
# https://leetcode.com/problems/count-days-without-interval/description/
# Approach: Create an array representing each day and mark days that fall within any meeting. After marking all meetings, count how many days remain unmarked. Those unmarked days are the days without meetings.
# Complexity: Time: O(n + d)  Space: O(d) where d is the range of days
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        busy = [False] * (days + 1)   # 1-based indexing
        # Mark meeting days
        for start, end in meetings:
            for d in range(start, end + 1):
                busy[d] = True
        # Count free days
        free_days = 0
        for d in range(1, days + 1):
            if not busy[d]:
                free_days += 1        
        return free_days
# Example Walkthrough
# days = 10
# meetings = [[2,3], [5,7]]
# Marked days:
# Day:   1 2 3 4 5 6 7 8 9 10
# Busy:  F T T F T T T F F F
# Free days:
# Days: 1, 4, 8, 9, 10
# Count = 5

# Approach 2: First, sort and merge overlapping meeting intervals to avoid double counting. Then count free days before the first meeting, between merged meetings, and after the last meeting. The sum of these gaps gives the total days without meetings.
# Complexity: Time: O(n log n + m)  Space: O(n) where m is the number of merged intervals
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])
        # Step 1: Merge meetings
        res = [meetings[0]]
        for i in range(1, len(meetings)):
            start, end = meetings[i]
            last_end = res[-1][1]
            if start <= last_end:
                res[-1][1] = max(last_end, end)
            else:
                res.append([start, end])
        # Step 2: Count free days
        gap = 0
        # Days before first meeting
        gap += res[0][0] - 1
        # Days between meetings
        for i in range(1, len(res)):
            gap += res[i][0] - res[i - 1][1] - 1
        # Days after last meeting
        gap += days - res[-1][1]        
        return gap
# Example Walkthrough
# days = 10
# meetings = [[2,3],[5,7]]
# After merging:
# [[2,3],[5,7]]
# Free days:
# Before first meeting → day 1 → 1
# Between meetings → day 4 → 1
# After last meeting → days 8,9,10 → 3
# ✅ Total free days = 5