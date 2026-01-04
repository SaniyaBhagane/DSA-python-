# --------------------ARRAYS --------------------

# 485. Max Consecutive Ones
# https://leetcode.com/problems/max-consecutive-ones/

# Approach => In a loop keep count of 1s, then reset count when 0 is encountered. Keep track of max count in res variable. 
# COMPLEXITY ANALYSIS:
# Time Complexity: O(N), where N is the number of elements in the input array.  
# Space Complexity: O(1), as we are using only a constant amount of extra space
# class Solution:
#     def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
#         count = 0
#         res = 0
#         for i in nums:
#             if i == 1:
#                 count += 1
#                 res = max(count, res)
#             else:
#                 count = 0
#         return res
# => The above approach can be optimized slightly by updating maxCount only when 0 is encountered.

# Approach 2 => In a loop keep count of 1s, then when 0 is encountered update maxCount and reset count. Finally return the maximum of maxCount and count to account for the case when array ends with 1s.
# COMPLEXITY ANALYSIS:
# Time Complexity: O(N), where N is the number of elements in the input array.  
# Space Complexity: O(1), as we are using only a constant amount of extra space
# class Solution:
#     def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
#         count = 0
#         maxCount = 0
#         for i in nums:
#             if i == 1:
#                 count += 1
#             else:
#                 maxCount = max(maxCount, count)
#                 count = 0
#         return max(maxCount, count)        
# --------------------------------------------------------------------------


# 1295. Find Numbers with Even Number of Digits
# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

# Approach 1 => Count digits by repeatedly dividing number by 10 until it becomes 0.
# COMPLEXITY ANALYSIS:
# Time Complexity: O(N * M), where N is the number of elements in the input array and M is the average number of digits in each number.
# Space Complexity: O(1), as we are using only a constant amount of extra space 
# class Solution:
#     def findNumbers(self, nums: List[int]) -> int:
#         count = 0
#         for i in nums:
#             digit_count = 0
#             num = i
#             while num > 0:
#                 num //= 10
#                 digit_count += 1
#             if digit_count % 2 == 0:
#                 count += 1
#         return count

# Approach 2 => Convert number to string and check length of string is even or not.
# COMPLEXITY ANALYSIS:
# Time Complexity: O(N * M), where N is the number of elements in the input array and M is the average number of digits in each number.
# Space Complexity: O(1), as we are using only a constant amount of extra space
# class Solution:
#     def findNumbers(self, nums: List[int]) -> int:    
#         count = 0
#         for i in nums:
#             if len(str(i)) % 2 == 0:
#                 count += 1
#         return count

# Approach 3 => For this problem: 2 digits: 10 to 99,4 digits: 1000 to 9999, 6 digits: 100000 (maximum allowed by constraints). Each number is checked against these ranges.If it falls into any of them, it must have an even number of digits.
# COMPLEXITY ANALYSIS:
# Time Complexity: O(N), where N is the number of elements in the input array.
# Space Complexity: O(1), as we are using only a constant amount of extra space
# class Solution:
#     def findNumbers(self, nums: List[int]) -> int:
#         counter = 0

#         for num in nums:
#             if len(str(num)) % 2 == 0:
#                 counter += 1
#         return counter

# Approach 4 => Using logarithm to count digits digits = floor(log10(num)) + 1 
# COMPLEXITY ANALYSIS:
# Time Complexity: O(N), where N is the number of elements in the input array.
# Space Complexity: O(1), as we are using only a constant amount of extra space
# class Solution:
#     def findNumbers(self, nums: List[int]) -> int:
#         counter = 0
#         for num in nums:
#             digits = int(math.log10(num)) + 1
#             if digits % 2 == 0:
#                 counter += 1
#         return counter

# --------------------------------------------------------------------------

# 724. Find Pivot Index
# https://leetcode.com/problems/find-pivot-index/

# Brute Force Approach => For each index, calculate left sum and right sum by iterating through the array. If they are equal, return that index.
# COMPLEXITY ANALYSIS:
# Time Complexity: O(N^2), where N is the number of elements in the input array.
# Space Complexity: O(1), as we are using only a constant amount of extra space
# class Solution:
#     def pivotIndex(self, nums: List[int]) -> int:
#         n = len(nums)

#         for i in range(n):
#             leftSum = sum(nums[:i])
#             rightSum = sum(nums[i+1:])

#             if leftSum == rightSum:
#                 return i

#         return -1


# Approach => Calculate total sum of array. In a loop keep track of left sum and right sum (right sum = total sum - left sum - current element). If at any index left sum equals right sum, return that index.
# COMPLEXITY ANALYSIS:
# Time Complexity: O(N), where N is the number of elements in the input array.  
# Space Complexity: O(1), as we are using only a constant amount of extra space
# class Solution:
#     def pivotIndex(self, nums: List[int]) -> int:
#         left_sum = 0
#         right_sum = sum(nums)
#         for i in range(len(nums)):
#             right_sum -= nums[i]
#             if left_sum == right_sum: 
#                 return i
#             left_sum += nums[i]
#         return -1              

#Approach 2 => Using enumerate to loop through array while keeping track of index. 
# (enumarate gives both index and value)
# COMPLEXITY ANALYSIS:  
# Time Complexity: O(N), where N is the number of elements in the input array.
# Space Complexity: O(1), as we are using only a constant amount of extra space
# class Solution:
#     def pivotIndex(self, nums: List[int]) -> int: 
#         left_sum = 0
#         right_sum = sum(nums)
#         for index, value in enumerate(nums):
#             right_sum -= value
#             if left_sum == right_sum:
#                 return index
#             left_sum += value
#         return -1
# 
#--------------------------------------------------------------------------

# 118. Pascal's Triangle
# https://leetcode.com/problems/pascals-triangle/