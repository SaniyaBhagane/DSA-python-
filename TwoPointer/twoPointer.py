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

# 344. Reverse String
# https://leetcode.com/problems/reverse-string/ 

# Approach => Use two pointers, one at start and one at end. Swap characters at these pointers and move them towards each other until they meet or cross.
# COMPLEXITY ANALYSIS:
# Time Complexity: O(N), where N is the number of characters in the input array.
# Space Complexity: O(1), as we are using only a constant amount of extra space
# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         i = 0
#         j = len(s)-1
#         while i < j:
#             temp = s[j]
#             s[j] = s[i]
#             s[i] = temp
#             i += 1
#             j -= 1

# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         i = 0
#         j = len(s) - 1

#         while i < j:
#             s[i], s[j] = s[j], s[i]
#             i += 1
#             j -= 1

# --------------------------------------------------------------------------
# 977. Squares of a Sorted Array
# https://leetcode.com/problems/squares-of-a-sorted-array/
# Approach => Two pointers compare squares from both ends of the array and append the larger square to a new list. Because the largest values are added first, the list is built in reverse (descending) order. The final list is reversed once to obtain the correctly sorted squares array.
# COMPLEXITY ANALYSIS:
# Time Complexity: O(N), where N is the number of elements in the input array.
# Space Complexity: O(N), as we are using an additional array to store the results
# class Solution:
#     def sortedSquares(self, nums: List[int]) -> List[int]:
#         squared = []
#         left,right = 0, len(nums) -1
#         while left <= right:
#             leftSquared = nums[left] * nums[left]
#             rightSquared= nums[right] * nums[right]
#             if leftSquared > rightSquared:
#                 squared.append(leftSquared)
#                 left+=1
#             else:
#                 squared.append(rightSquared)
#                 right-=1
#         return squared[::-1] 

# Approach 2: Two pointers are used to compare absolute values, and the larger square is placed directly at the correct position from the end of the result array. Pointers move inward until all elements are processed, producing a sorted squares array without any extra reversal step.
# COMPLEXITY ANALYSIS:
# Time Complexity: O(N), where N is the number of elements in the input array.
# Space Complexity: O(N), as we are using an additional array to store the results
# class Solution:
    # def sortedSquares(self, nums: List[int]) -> List[int]:
    #     res = [0] * len(nums)
    #     i = 0 
    #     j = len(nums) - 1
    #     k = len(nums) - 1
    #     while i <= j:
    #         if abs(nums[i]) > abs(nums[j]):
    #             res[k] = nums[i] * nums[i]
    #             i += 1
    #         else:
    #             res[k] = nums[j] * nums[j]
    #             j -= 1 
    #         k -= 1
    #     return res

# -------------------------------------------------------------------------------------------------------------
# 680. Valid Palindrome II
# https://leetcode.com/problems/valid-palindrome-ii/

# APPROACH 1: Try deleting each character one at a time and check whether the resulting string is a palindrome. If any deletion produces a palindrome, return true; otherwise, return false.
# COMPLEXITY ANALYSIS:
# Time Complexity: O(N^2), where N is the length of the input string.
# Space Complexity: O(1), as we are using only a constant amount of extra space
# class Solution:
    # def validPalindrome(self, s: str) -> bool:
        # def is_pal(st):
        #     return st == st[::-1]

        # for i in range(len(s)):
        #     if is_pal(s[:i] + s[i+1:]):
        #         return True
        # return False

# APPROACH 2: Use recursion with two pointers and a flag to track whether a character has already been deleted. When a mismatch occurs, recursively try skipping either the left or right character if no deletion has been used yet. If all characters match within this constraint, the string is a valid palindrome.
# COMPLEXITY ANALYSIS:
# Time Complexity: O(N), where N is the length of the input string.
# Space Complexity: O(N), due to the recursion stack in the worst case
# class Solution:
    # def validPalindrome(self, s: str) -> bool:
    #     def validPalindrome(s):
            # def dfs(l, r, deleted):
            #     if l >= r:
            #         return True
            #     if s[l] == s[r]:
            #         return dfs(l+1, r-1, deleted)
            #     if deleted:
            #         return False
            #     return dfs(l+1, r, True) or dfs(l, r-1, True)
            # return dfs(0, len(s)-1, False)
            
# Approach 3: Use two pointers from both ends of the string. When a mismatch occurs, skip either the left or right character once and check if the remaining substring is a palindrome. If either case is valid, return true.
# COMPLEXITY ANALYSIS:
# Time Complexity: O(N), where N is the length of the input string.
# Space Complexity: O(1), as we are using only a constant amount of extra space
# class Solution:
    # def validPalindrome(self, s: str) -> bool:
    #     i = 0
    #     j = len(s) - 1
    #     def palindromehelper(i, j):
    #         while i < j:
    #             if (s[i] != s[j] ):
    #                 return False
    #             i += 1
    #             j -= 1
    #         return True
    #     while i < j:
    #         if s[i] != s[j]:
    #             return palindromehelper(i+1, j) or palindromehelper(i, j - 1)
    #         else : 
    #              i += 1
    #              j -= 1
    #     return True
# abbxa
# i   j
#  i j
#  ij
            
#-------------------------------------------------------------------------------------------------------------