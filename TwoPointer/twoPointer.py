# -------------------------------------------------------------------------------------------------
# 1. TWO SUM

# BRUTEFORCE : Two pointers
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
#         return []  # Fallback (problem guarantees a solution)

# APPROACH 2: One-pass Hash Table
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         hashmap={}
#         for i, num in enumerate(nums):
#             value=target-num
#             if value in hashmap:
#                 return[hashmap[value], i]
#             hashmap[num]=i

# -------------------------------------------------------------------------------------------------------------
# 125. VALID PALINDROME
# https://leetcode.com/problems/valid-palindrome/
# APPROACH: We use two pointers starting from the beginning and end of the string and skips any non-alphanumeric characters. When both pointers point to valid characters, they are compared in a case-insensitive way. If all such character pairs match while moving inward, the string is a palindrome; otherwise, it returns False immediately.
# COMPLEXITY ANALYSIS:
# Time Complexity: O(N), where N is the length of the input string.
# Space Complexity: O(1), as we are using only a constant amount of extra space
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         left, right = 0, len(s) - 1
#         while left < right:
#             # Move left pointer to the right until we find an alphanumeric character
#             while left < right and not s[left].isalnum():
#                 left += 1
#             # Move right pointer to the left until we find an alphanumeric character
#             while left < right and not s[right].isalnum():
#                 right -= 1
#             # Compare characters in a case-insensitive manner
#             if s[left].lower() != s[right].lower():
#                 return False        
#             # Move both pointers towards the center
#             left += 1
#             right -= 1
#         return True

# APPROACH 2: We first cleans the string by removing non-alphanumeric characters and converting all letters to lowercase to ensure case-insensitive comparison. It then uses two pointers starting from both ends of the cleaned string to compare characters. If any pair does not match, it returns `False`; otherwise, if all pairs match, the string is confirmed to be a palindrome and returns `True`.
# COMPLEXITY ANALYSIS:  
# Time Complexity: O(N), where N is the length of the input string.
# Space Complexity: O(N), as we are creating a new cleaned string
# class Solution:
#     def isPalindrome(self, s: str) -> bool:   
#         cleaned_s = ''.join(char.lower() for char in s if char.isalnum())
#         left, right = 0, len(cleaned_s) - 1
#         while left < right:
#             if cleaned_s[left] != cleaned_s[right]:
#                 return False
#             left += 1
#             right -= 1
#         return True

# -------------------------------------------------------------------------------------------------------------