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
