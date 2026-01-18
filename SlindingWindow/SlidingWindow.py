# Max Sum Subarray of size K
# https://www.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1
# Approach: Check every possible subarray of size k, calculate its sum, and keep updating the maximum sum found. Since we recompute the sum for each window from scratch, this approach is simple but not optimal.
# Complexity Analysis: Time=>0(n*n) space=> O(1)
# class Solution:
#     def maxSubarraySum(self, arr, k):
#         n = len(arr)
#         maxSum = float('-inf')
#         for i in range(0, n - k + 1):
#             currSum = 0
#             for j in range(i, i + k):
#                 currSum += arr[j]
#             maxSum = max(maxSum, currSum)
#         return maxSum
# Example Walkthrough
# Input:
# arr = [2, 1, 5, 1, 3, 2]
# k = 3
# Step 1: First subarray (index 0 → 2)
# [2, 1, 5] → sum = 8
# maxSum = 8
# Step 2: Second subarray (index 1 → 3)
# [1, 5, 1] → sum = 7
# maxSum = 8
# Step 3: Third subarray (index 2 → 4)
# [5, 1, 3] → sum = 9
# maxSum = 9
# Step 4: Fourth subarray (index 3 → 5)
# [1, 3, 2] → sum = 6
# maxSum = 9
# Final Answer => Maximum subarray sum of size 3 = 9

# Approach 2: First calculate the sum of the first k elements. Then slide the window one step at a time by adding the new element entering the window and removing the element leaving it. Keep updating the maximum sum during this process
# Complexity Analysis: Time=>0(n) space=> O(1)
# class Solution:
#     def maxSubarraySum(self, arr, k):
#         n = len(arr)
#         # Step 1: sum of first window
#         windowSum = sum(arr[:k])
#         maxSum = windowSum
#         # Step 2: slide the window
#         for i in range(k, n):
#             windowSum += arr[i]        # add new element
#             windowSum -= arr[i - k]    # remove old element
#             maxSum = max(maxSum, windowSum)
#         return maxSum
# Example Walkthrough
# Input: arr = [2, 1, 5, 1, 3, 2]   k = 3
# Step 1: First window
# [2, 1, 5] → sum = 8
# max_sum = 8
# Step 2: Slide window
# Remove 2, add 1 → [1, 5, 1] → sum = 7
# Remove 1, add 3 → [5, 1, 3] → sum = 9  ← max
# Remove 5, add 2 → [1, 3, 2] → sum = 6
# Answer = 9

# ---------------------------------------------------------------------------------------
# 2461. Maximum Sum of Distinct Subarrays of Length K
# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/
# Approach: Generate all subarrays of length k, check if all elements are distinct using a list, and if yes, calculate the sum. Track the maximum valid sum. This is slow because we re-check uniqueness every time.
# Complexity Analysis: Time=>0(n*n) space=> O(1)
# class Solution:
#     def maximumSubarraySum(self, nums, k):
#         n = len(nums)
#         maxSum = 0
#         for i in range(n - k + 1):
#             temp = []
#             currSum = 0
#             valid = True
#             for j in range(i, i+k):
#                 if nums[j] in temp:
#                     valid = False
#                     break
#                 temp.append(nums[j])
#                 currSum += nums[j]
#             if valid:
#                 maxSum = max(maxSum, currSum)
#         return maxSum
# Example Walkthrough=> nums = [1,5,4,2,9,9,9], k = 3
# [1,5,4] → distinct ✅ sum = 10
# [5,4,2] → distinct ✅ sum = 11
# [4,2,9] → distinct ✅ sum = 15 ← max
# [2,9,9] → duplicate ❌
# [9,9,9] → duplicate ❌
# Answer = 15

# Approach 2: Use a sliding window of size k and a frequency map to track counts of elements. If any element’s count becomes greater than 1, shrink the window from the left. When the window size is exactly k and all elements are unique, update the max sum.
# Complexity Analysis: Time=>0(n) space=> O(n)
# class Solution:
#     def maximumSubarraySum(self, nums, k):
#         freq = {}
#         left = 0
#         currSum = 0
#         maxSum = 0
#         for right in range(len(nums)):
#             freq[nums[right]] = freq.get(nums[right], 0) + 1
#             currSum += nums[right]
#             # If duplicate appears, shrink window
#             while freq[nums[right]]> 1:
#                 freq[nums[left]] -= 1
#                 currSum -= nums[left]
#                 if freq[nums[left]] == 0:
#                     del freq[nums[left]]
#                 left += 1
#             # Window size exactly k
#             if right - left + 1 == k:
#                 maxSum = max(maxSum, currSum)
#                 # Slide window forward
#                 freq[nums[left]] -= 1
#                 currSum -= nums[left]
#                 if freq[nums[left]] == 0:
#                     del freq[nums[left]]
#                 left += 1
#         return maxSum
# Example Walkthrough => nums = [1,5,4,2,9,9,9], k = 3
# [1,5,4] → freq valid → sum = 10
# [5,4,2] → sum = 11
# [4,2,9] → sum = 15 ✅
# Duplicate 9 → shrink until unique again
# Final Answer = 15  

# -----------------------------------------------------------------------------------------------------
# 209. Minimum Size Subarray Sum
# https://leetcode.com/problems/minimum-size-subarray-sum/description/
# Approach: Check every possible subarray, calculate its sum, and track the smallest length whose sum ≥ target. This works but repeats sum calculations unnecessarily, making it inefficient for large inputs.
# Complexity Analysis: Time=>0(n*n) space=> O(1)
# class Solution:
#     def minSubArrayLen(self, target: int, nums: list[int]) -> int:
#         n = len(nums)
#         min_len = float('inf')
#         for i in range(n):
#             curr_sum = 0
#             for j in range(i, n):
#                 curr_sum += nums[j]
#                 if curr_sum >= target:
#                     min_len = min(min_len, j - i + 1)
#                     break
#         return 0 if min_len == float('inf') else min_len

# Approach 2: Use two pointers to maintain a sliding window.Expand the window to increase the sum and shrink it when the sum ≥ target to minimize the window size efficiently.
# Complexity Analysis: Time=>0(n) space=> O(1)
# class Solution:
#     def minSubArrayLen(self, target: int, nums: list[int]) -> int:
#         left = 0
#         curr_sum = 0
#         min_len = float('inf')
#         for right in range(len(nums)):
#             curr_sum += nums[right]
#             while curr_sum >= target:
#                 min_len = min(min_len, right - left + 1)
#                 curr_sum -= nums[left]
#                 left += 1
#         return 0 if min_len == float('inf') else min_len
# Example Walkthrough
# Input: target = 7   nums = [2,3,1,2,4,3]
# Sliding Window Steps:
# Expand → sum = 8 → window [2,3,1,2]
# Shrink from left → try smaller windows
# Best window found → [4,3]
# Output: 2

# ------------------------------------------------------------------------------------------------------
# 219. Contains Duplicates II:
# https://leetcode.com/problems/contains-duplicate-ii/description/
# Approach: For each index i, we look ahead up to k positions and check whether the same number appears again within this range. A set is used to track elements in the current window so duplicates can be detected quickly. If any duplicate is found within distance k, we return True; otherwise, after all checks, return False.
# Complexity Analysis: Time Complexity: O(n × k) Space Complexity: O(k) 
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        n = len(nums)
        for i in range(n):
            seen = set()
            for j in range(i, min(i+k-1), n):
                if nums[j] in seen:
                    return True
                seen.add(nums[j])
        return False
# Example Walkthrough
# Input: nums = [1, 2, 3, 1], k = 3
# i = 0, window indices 0 → 3
# seen = {}
# j = 0 → add 1 → {1}
# j = 1 → add 2 → {1,2}
# j = 2 → add 3 → {1,2,3}
# j = 3 → 1 already in set → duplicate found → return True
# So the function stops early and returns True.

# Approach 2: We maintain a sliding window of at most k elements using a set. As we move forward, we remove the element that goes out of the window and check if the current element already exists in the set. If it does, a duplicate within distance k is found.
# Complexity Analysis: Time:O(n)    Space:O(k)
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        n = len(nums)
        window = set()
        for i in range(n):
            if j - i > k:
                window.remove(nums[i])
                i +=1
            if nums[j] in window:
                return True
            window.add(nums[j])
        return False  
# Example Walkthrough
# Input: nums = [1, 2, 3, 1], k = 3
# Step	j	window	Action
# 1 	0	{}	    add 1 → {1}
# 2	    1	{1}	    add 2 → {1,2}
# 3	    2	{1,2}	add 3 → {1,2,3}
# 4	    3	{1,2,3}	1 already present → return True

# -----------------------------------------------------------------------------------
# 643. Maximun Average Subarray I
#  https://leetcode.com/problems/maximum-average-subarray-i/description/
# Approach: Check every subarray of size k, calculate its sum, and keep track of the maximum sum found. Finally, divide the maximum sum by k to get the maximum average.
# Complexity Analysis: Time: O(n × k)  Space: O(1)
class Solution:
    def findMaxAverage(self, nums, k):
        maxSum = float('-inf')
        for i in range(len(nums) - k + 1):
            currSum = 0 
            for j in range(i, i+1):
                currSum += nums[j]
            maxSum = max(maxSum, currSum)
        return maxSum / k
# Example Walkthrough: nums = [1,12,-5,-6,50,3], k = 4
# Subarray [1,12,-5,-6] → sum = 2
# Subarray [12,-5,-6,50] → sum = 51
# Subarray [-5,-6,50,3] → sum = 42
# Max sum = 51, average = 51 / 4 = 12.75

# Approach: First calculate the sum of the first k elements. Then slide the window by adding the next element and removing the leftmost element. Track the maximum window sum and divide by k at the end.
# Complexity Analysis: Time: O(n)   Space: O(1)
class Solution:
    def findMaxAverage(self, nums, k):
        windowSum = sum(nums[::k])
        maxSum = windowSum
        for i in range(k, len(nums)):
            windowSum += nums[i] # add next element
            windowSum -= nums[i-k] # remove leftmost element
            maxSum = max(maxSum, windowSum)
        return maxSum / k
# Example Walkthrough: nums = [1,12,-5,-6,50,3], k = 4
# Initial window [1,12,-5,-6] → sum = 2
# Slide → [12,-5,-6,50] → sum = 51 (max)
# Slide → [-5,-6,50,3] → sum = 42
# Max sum = 51, average = 12.75