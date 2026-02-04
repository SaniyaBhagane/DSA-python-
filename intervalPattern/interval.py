# 57. Merge Intervals
# https://leetcode.com/problems/merge-intervals/description/
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
# class Solution:
#     def countDays(self, days: int, meetings: List[List[int]]) -> int:
#         busy = [False] * (days + 1)   # 1-based indexing
#         # Mark meeting days
#         for start, end in meetings:
#             for d in range(start, end + 1):
#                 busy[d] = True
#         # Count free days
#         free_days = 0
#         for d in range(1, days + 1):
#             if not busy[d]:
#                 free_days += 1        
#         return free_days
# Example Walkthrough
# days = 10
# meetings = [[2,3], [5,7]]
# Marked days:
# Day:   1 2 3 4 5 6 7 8 9 10
# Busy:  F T T F T T T F F F
# Free days:
# Days: 1, 4, 8, 9, 10
# Count = 5

# Approach: Sort all meeting intervals by start day. Merge overlapping intervals and calculate the total number of days occupied by meetings.Subtract the occupied days from the total number of days to get days without meetings.
# Complexity: Time: O(n log n)  Space: O(1)
# class Solution:
#     def countDays(self, days: int, meetings: List[List[int]]) -> int:
#         meetings.sort()
#         used_days = 0
#         start, end = meetings[0]
#         for i in range(1, len(meetings)):
#             s, e = meetings[i]
#             if s <= end:           # overlapping meetings
#                 end = max(end, e)
#             else:                  # non-overlapping
#                 used_days += end - start + 1
#                 start, end = s, e
#         # add last merged interval
#         used_days += end - start + 1        
#         return days - used_days
# Example Walkthrough
# Input
# days = 10
# meetings = [[1,3],[2,5],[7,7]]
# Step 1: Sort
# [[1,3],[2,5],[7,7]]
# Step 2: Merge Intervals
# Merge [1,3] & [2,5] → [1,5]
# Days used = 5 - 1 + 1 = 5
# [7,7] → single day
# Days used = 1
# Total used days = 6
# Step 3: Count Free Days
# Free days = 10 - 6 = 4
# Output: 4

# Approach 2: First, sort and merge overlapping meeting intervals to avoid double counting. Then count free days before the first meeting, between merged meetings, and after the last meeting. The sum of these gaps gives the total days without meetings.
# Complexity: Time: O(n log n + m)  Space: O(n) where m is the number of merged intervals
# class Solution:
#     def countDays(self, days: int, meetings: List[List[int]]) -> int:
#         meetings.sort(key=lambda x: x[0])
#         # Step 1: Merge meetings
#         res = [meetings[0]]
#         for i in range(1, len(meetings)):
#             start, end = meetings[i]
#             last_end = res[-1][1]
#             if start <= last_end:
#                 res[-1][1] = max(last_end, end)
#             else:
#                 res.append([start, end])
#         # Step 2: Count free days
#         gap = 0
#         # Days before first meeting
#         gap += res[0][0] - 1
#         # Days between meetings
#         for i in range(1, len(res)):
#             gap += res[i][0] - res[i - 1][1] - 1
#         # Days after last meeting
#         gap += days - res[-1][1]        
#         return gap
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

# -----------------------------------------------------------------------------------------------------------------------
# 57. Insert Interval
# https://leetcode.com/problems/insert-interval/description/
# Approach: Insert the new interval into the list, then sort all intervals by start time. After sorting, iterate through the intervals and merge any overlapping ones by comparing the current interval with the last merged interval, producing the final merged list.
# Complexity: Time: O(n log n)  Space: O(n)
# class Solution:
#     def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
#         # Step 1: add new interval
#         intervals.append(newInterval)
#         # Step 2: sort intervals
#         intervals.sort(key=lambda x: x[0])
#         # Step 3: merge intervals
#         res = []
#         for interval in intervals:
#             if not res or interval[0] > res[-1][1]:
#                 res.append(interval)
#             else:
#                 res[-1][1] = max(res[-1][1], interval[1])        
#         return res
# Walkthrough Example
# intervals = [[1,3],[6,9]]
# newInterval = [2,5]
# Step 1: Add
# [[1,3],[6,9],[2,5]]
# Step 2: Sort
# [[1,3],[2,5],[6,9]]
# Step 3: Merge
# [1,3] + [2,5] → [1,5]
# [6,9] → no overlap
# Result: [[1,5],[6,9]]


# Approach: Since the intervals are already sorted and non-overlapping, scan the list once. First, add all intervals that end before the new interval starts. Then merge all overlapping intervals with the new interval by updating its start and end, and finally append the remaining intervals after it.
# Complexity: Time: O(n)  Space: O(n)
# class Solution:
    # def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    #     res = []
    #     i = 0
    #     n = len(intervals)
    #     # 1️ intervals before newInterval
    #     while i < n and intervals[i][1] < newInterval[0]:
    #         res.append(intervals[i])
    #         i += 1
    #     # 2️ overlapping intervals
    #     while i < n and intervals[i][0] <= newInterval[1]:
    #         newInterval[0] = min(newInterval[0], intervals[i][0])
    #         newInterval[1] = max(newInterval[1], intervals[i][1])
    #         i += 1
    #     # add merged interval
    #     res.append(newInterval)
    #     # 3️ intervals after newInterval
    #     while i < n:
    #         res.append(intervals[i])
    #         i += 1
    #     return res
# Example Walkthrough (Step-by-Step)
# Input
# intervals = [[1,3],[6,9]]
# newInterval = [2,5]
# Phase 1: Before newInterval
# [1,3] → 3 < 2  → stop
# res = []
# Phase 2: Overlap
# [1,3] overlaps [2,5]
# newInterval → [1,5]
# [6,9] does NOT overlap → stop
# res = [[1,5]]
# Phase 3: After newInterval
# add [6,9]
# Output: [[1,5],[6,9]]

# -----------------------------------------------------------------------------------
# 1288. Remove Covered Intervals
# https://leetcode.com/problems/remove-covered-intervals/description/
# Approach: For each interval, check whether it is completely covered by any other interval. If an interval is not covered, count it. Finally, return the count of non-covered intervals.
# Complexity: Time: O(n²)  Space: O(1)
# class Solution:
#     def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
#         count = 0
#         for i in range(len(intervals)):
#             c, d = intervals[i]
#             isCovered = False
#             for j in range(len(intervals)):
#                 if i == j:
#                     continue
#                 a, b = intervals[j]
#                 if a <= c and b >= d:
#                     isCovered = True
#                     break
#             if not isCovered:
#                 count += 1                
#         return count
# Example Walkthrough
# Input: intervals = [[1,4],[3,6],[2,8]]
# Interval [1,4]
# Compared with [3,6] → 3 ≤ 1 
# Compared with [2,8] → 2 ≤ 1  NOT covered
# Interval [3,6]
# Compared with [2,8] → 2 ≤ 3 AND 8 ≥ 6  Covered
# Interval [2,8]
# No interval fully covers it  NOT covered
# Intervals remaining: [1,4], [2,8]
# Output: 2

# Approach: Sort intervals by start time (and by end time descending for ties). Then iterate through the sorted list, if the current interval’s end is ≤ maxEnd, it is covered; otherwise, count it and update maxEnd.
# Complexity: Time: O(n log n)  Space: O(1)
# class Solution:
#     def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
#         # Sort by start ↑, end ↓
#         intervals.sort(key=lambda x: (x[0], -x[1]))
#         count = 0
#         maxEnd = 0
#         for start, end in intervals:
#             if end > maxEnd:
#                 count += 1
#                 maxEnd = end
#             # else: covered, skip
#         return count
# Example Walkthrough
# Input: intervals = [[1,4],[3,6],[2,8]]
# After Sorting
# [[1,4],[2,8],[3,6]]
# Scan
# [1,4] → end 4 > 0 → count = 1, maxEnd = 4
# [2,8] → end 8 > 4 → count = 2, maxEnd = 8
# [3,6] → end 6 ≤ 8 → covered → skip
# Output = 2

#-----------------------------------------------------------------------------------------------------------------------
# 731. My Calander II
# https://leetcode.com/problems/my-calendar-ii/description/
# Approach: For every new booking, simulate each time unit in its range and count how many existing bookings already cover that time. If at any point the overlap count reaches two (meaning adding this booking would create a triple booking), reject it. Otherwise, add the booking to the list.
# Complexity: Time: O(n * d)  Space: O(n) where d is the average duration of bookings
class MyCalendarTwo:
    def __init__(self):
        self.bookings = []

    def book(self, start: int, end: int) -> bool:
        # Try every time point in the new interval
        for t in range(start, end):
            overlapCount = 0
            for s, e in self.bookings:
                if s <= t < e:
                    overlapCount += 1
                    if overlapCount == 2:
                        return False #triple booking detected
        self.bookings.append([start, end])
        return True
# Example Walkthrough
# Operations
# book(10, 20) → True
# book(15, 25) → True
# book(17, 22) → False
# Step-by-step
# book(10, 20)
# No existing bookings
# Added safely
# book(15, 25)
# Overlaps with [10,20] → overlap count = 1
# Double booking allowed
# Added safely
# book(17, 22)
# At time t = 17:
# [10,20] overlaps
# [15,25] overlaps
# overlap count = 2 → adding new makes 3
# Rejected