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