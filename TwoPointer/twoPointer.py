# -------------------------------------------------------------------------------------------------
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

# https://neetcode.io/problems/valid-word-abbreviation/question?list=neetcode250
# 408. Valid Word Abbreviation
# Approach: Try to expand the abbreviation into all possible original strings and check if any of them matches the given word, or simulate every possible interpretation of the numbers by rebuilding the word step by step.
# COMPLEXITY ANALYSIS:
# Time Complexity: O(2^M), where M is the number of digit groups in the abbreviation.
# Space Complexity: O(M), due to the recursion stack in the worst case
#class Solution:
    # def validWordAbbreviation(self, word: str, abbr: str) -> bool:
    #     def expand(abbr):
    #         res = ""
    #         i = 0
    #         while i < len(abbr):
    #             if abbr[i].isalpha():
    #                 res += abbr[i]
    #                 i += 1
    #             else:
    #                 if abbr[i] == '0':
    #                     return ""   # invalid leading zero
    #                 num = 0
    #                 while i < len(abbr) and abbr[i].isdigit():
    #                     num = num * 10 + int(abbr[i])
    #                     i += 1
    #                 res += "#" * num   # placeholder
    #         return res
    #     expanded = expand(abbr)
    #     if len(expanded) != len(word):
    #         return False

    #     for i in range(len(word)):
    #         if expanded[i] != "#" and expanded[i] != word[i]:
    #             return False
    #     return True

# APPROACH: Use two pointers to traverse the word and abbreviation. When encountering a digit in the abbreviation, convert it to an integer and skip that many characters in the word. If characters match, move both pointers forward. If a mismatch occurs, return False. If both pointers reach the end simultaneously, return True.
# COMPLEXITY ANALYSIS:
# Time Complexity: O(N + M), where N is the length of the word and M is the length of the abbreviation.
# Space Complexity: O(1), as we are using only a constant amount of extra space
# class Solution:
#     def validWordAbbreviation(self, word: str, abbr: str) -> bool:
#         i = 0  # Pointer for word
#         j = 0  # Pointer for abbr
#           while i < len(word) and j < len(abbr):
#             #   If characters match, move both pointers
#             if abbr[j].isalpha():
#                 if word[i] != abbr[j]:
#                     return False
#                 i += 1
#                 j += 1
#             else:
#                 # If we encounter a digit, calculate the full number
#                 if abbr[j] == '0':
#                     return False  # Leading zeros are not allowed
#                 num = 0
#                 while j < len(abbr) and abbr[j].isdigit():
#                     num = num * 10 + int(abbr[j])
#                     j += 1
#                 i += num  # Skip 'num' characters in word
#         return i == len(word) and j == len(abbr)

# -------------------------------------------------------------------------------------------------------------
# 88. Merge Sorted Array
# https://leetcode.com/problems/merge-sorted-array/

# Approach 1: Add elements of nums2 to nums1 and sort the combined array[num1].
# COMPLEXITY ANALYSIS:
# Time Complexity: O((m + n) log(m + n)), where m and n are the lengths of nums1 and nums2 respectively.
# Space Complexity: O(1), as we are modifying nums1 in place
# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2:
#                  List[int], n: int) -> None:
#         nums1[:] = sorted(nums1[:m] + nums2)

# Approach 2: Use two pointers starting from the start of both arrays to compare elements and merge them into nums1.

# Approach 3: Use pointers at the end of nums1, nums2, and the merged array. Compare elements from the back and place the larger one at the end of nums1, moving pointers backward until all elements are merged.
# COMPLEXITY ANALYSIS:
# Time Complexity: O(m + n), where m and n are the lengths of nums1 and nums2 respectively.
# Space Complexity: O(1), as we are modifying nums1 in place
# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         i = m - 1
#         j = n - 1
#         k = m + n - 1
#         while i >= 0 and j >= 0:
#             if nums1[i] > nums2[j]:
#                 nums1[k] = nums1[i]
#                 i -= 1
#             else:
#                 nums1[k] = nums2[j]
#                 j -= 1
#             k -= 1
#         # Copy remaining elements of nums2 if any
#         while j >= 0:
#             nums1[k] = nums2[j]
#             j -= 1
#             k -= 1

# -------------------------------------------------------------------------------------------------------------
# 2824. Count Pairs Whose Sum is Less than Target
# https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/

# Approach: Check each number in the array which every other element to find how many numbers can pair with it to form a sum less than the target.
# COMPLEXITY ANALYSIS:
# Time Complexity: O(N^2), where N is the number of elements in the input array.
# Space Complexity: O(1), as we are using only a constant amount of extra space
# class Solution:
#     def countPairs(self, nums: List[int], target: int) -> int:
#         count = 0
#         n = len(nums)
#         for i in range(n):
#             for j in range(i + 1, n):
#                 if nums[i] + nums[j] < target:
#                     count += 1
#         return count

# Approach 2: The array is first sorted. Two pointers are used—one at the start and one at the end. If the sum of nums[i] + nums[j] is less than the target, then all elements between i and j form valid pairs with nums[i], so we add (j - i) to the count and move i forward. Otherwise, we move j backward to reduce the sum.
# COMPLEXITY ANALYSIS:
# Time Complexity: O(N log N), where N is the number of elements in the input array due to sorting.
# Space Complexity: O(1), as we are using only a constant amount of extra space
# class Solution:
#     def countPairs(self, nums: List[int], target: int) -> int:
#         nums.sort()
#         i = 0 
#         j = len(nums) - 1
#         count = 0
#         while i < j:
#             curr_sum = nums[i] + nums[j]
#             if curr_sum < target:
#                 count += (j - i)
#                 i += 1
#             else:
#                 j -= 1
#         return count

# -------------------------------------------------------------------------------------------------------------
# 1. TWO SUM
# https://leetcode.com/problems/two-sum/

# BRUTEFORCE : Check each number in the array which every other element to find the pair that sums to the target.
# COMPLEXITY ANALYSIS:
# Time Complexity: O(N^2), where N is the number of elements in the input array.
# Space Complexity: O(1), as we are using only a constant amount of extra space
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
#         return []  # Fallback (problem guarantees a solution)

# APPROACH 2: Use a hashmap to store the complement of each number (target - num) and its index. As we iterate through the array, we check if the current number exists in the hashmap. If it does, we have found the two numbers that sum to the target.
# COMPLEXITY ANALYSIS:
# Time Complexity: O(N), where N is the number of elements in the input array.
# Space Complexity: O(N), as we are using a hashmap to store elements
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         hashmap={}
#         for i, num in enumerate(nums):
#             value=target-num
#             if value in hashmap:
#                 return[hashmap[value], i]
#             hashmap[num]=i
#         return []  # Fallback (problem guarantees a solution)

# -------------------------------------------------------------------------------------------------------------
# 167. TWO SUM II - INPUT ARRAY IS SORTED
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

# APPROACH: Use two pointers, one starting at the beginning and the other at the end of the array. Calculate the sum of the elements at these pointers. If the sum equals the target, return their indices. If the sum is less than the target, move the left pointer to the right to increase the sum. If the sum is greater than the target, move the right pointer to the left to decrease the sum. Repeat this process until the target sum is found.
# COMPLEXITY ANALYSIS:
# Time Complexity: O(N), where N is the number of elements in the input array.
# Space Complexity: O(1), as we are using only a constant amount of extra space
# class Solution:
    # def twoSum(self, numbers: List[int], target: int) -> List[int]:
    #     i = 0
    #     j = len(numbers) - 1
    #     while i < j:
    #         sum = numbers[i]+numbers[j]
    #         if sum == target: 
    #             return [i + 1, j + 1]
    #         elif sum < target:
    #             i += 1
    #         elif sum > target: 
    #             j -= 1
    
# -------------------------------------------------------------------------------------------------------------
# 15. 3SUM
# https://leetcode.com/problems/3sum/

# Approach 1: First, sort the array and fix one element at a time. For each fixed element, use two pointers (left and right) to find pairs whose sum with the fixed element equals zero. Move pointers based on the sum and skip duplicates to ensure unique triplets.
# COMPLEXITY ANALYSIS:
# Time Complexity: O(N^2), where N is the number of elements in the input
# Space Complexity: O(1), as we are using only a constant amount of extra space
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()                 # Step 1: Sort the array
#         res = []
#         n = len(nums)
#         for f in range(n):
#             # Step 2: Skip duplicate fixed elements
#             if f > 0 and nums[f] == nums[f - 1]:
#                 continue
#             i, j = f + 1, n - 1     # Step 3: Two pointers for remaining array
#             while i < j:
#                 total = nums[f] + nums[i] + nums[j]
#                 if total < 0:       # Step 4: Sum too small → move left pointer
#                     i += 1
#                 elif total > 0:     # Step 5: Sum too large → move right pointer
#                     j -= 1
#                 else:
#                     # Step 6: Found valid triplet
#                     res.append([nums[f], nums[i], nums[j]])
#                     i += 1
#                     j -= 1
#                     # Step 7: Skip duplicates for second and third elements
#                     while i < j and nums[i] == nums[i - 1]:
#                         i += 1
#                     while i < j and nums[j] == nums[j + 1]:
#                         j -= 1
#         return res


# Approach 2:After sorting the array, fix one element and reduce the problem to a 2Sum search on the remaining part of the array. The helper function uses two pointers to find valid pairs while skipping duplicates. This modular approach clearly shows how 3Sum is built on top of 2Sum.
# COMPLEXITY ANALYSIS:
# Time Complexity: O(N^2), where N is the number of elements in the input
# Space Complexity: O(1), as we are using only a constant amount of extra space
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()                 # Step 1: Sort array
#         res = []
#         def twoSumHelper(f):
#             i, j = f + 1, len(nums) - 1  # Step 4: Two pointers
#             while i < j:
#                 total = nums[f] + nums[i] + nums[j]
#                 if total < 0:
#                     i += 1
#                 elif total > 0:
#                     j -= 1
#                 else:
#                     # Step 5: Found valid triplet
#                     res.append([nums[f], nums[i], nums[j]])
#                     i += 1
#                     j -= 1
#                     # Step 6: Skip duplicates
#                     while i < j and nums[i] == nums[i - 1]:
#                         i += 1
#                     while i < j and nums[j] == nums[j + 1]:
#                         j -= 1
#         for f in range(len(nums)):
#             # Step 2: Skip duplicate fixed elements
#             if f > 0 and nums[f] == nums[f - 1]:
#                 continue
#             # Step 3: Reduce problem to 2Sum
#             twoSumHelper(f)
#         return res

# -------------------------------------------------------------------------------------------------------------
# SORT TWO COLORS
# Approach: First, sort the array so that all 0s come before 1s. Then count the number of 0s and 1s using built-in functions and return their counts.
# COMPLEXITY ANALYSIS:
# Time Complexity: O(N log N), where N is the number of elements in the input array due to sorting.
# # Space Complexity: O(1), as we are using only a constant amount of extra space
# class Solution:
#     def sortColors(self, nums: List[int]) -> int:
#         nums.sort()
#         return nums.count(0), nums.count(1)

# Approach 2: Use two pointers starting from both ends of the array. Move the left pointer forward until a 1 is found and move the right pointer backward until a 0 is found, then swap them. Continue until both pointers meet, resulting in all 0s on the left and 1s on the right.
# COMPLEXITY ANALYSIS:
# Time Complexity: O(N), where N is the number of elements in the input array.
# Space Complexity: O(1), as we are using only a constant amount of extra space 
# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         i = 0
#         j = len(nums) = 1
#         count0 = 0
#         count1 = 0
#         while i <= j:
#             if nums[i] == 0:
#                 count0 += 1
#                 i += 1
#             elif nums[j] == 1:
#                 count1 += 1
#                 j -= 1
#             else:
#                 nums[i], nums[j] = nums[j], nums[i]
#                 j -= 1
#         return count0, count1

# --------------------------------------------------------------------------------------------------------------
# 75. SORT COLORS II
# https://leetcode.com/problems/sort-colors-ii/
# COMPLEXITY ANALYSIS: Time: O(n)  Space: O(1)
# Approach: Use three pointers: i to track the position for 0s, j to track the position for 2s, and k to traverse the array. While traversing, swap 0s to the left and 2s to the right, and move past 1s without swapping. This single-pass approach sorts the array in-place using constant extra space.
# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         i = 0
#         j = len(nums) - 1
#         k = 0
#         while (k <= j ):
#             if nums[k] == 1:
#                 k += 1
#             elif nums[k] == 2:
#                 nums[j], nums[k] = nums[k], nums[j]
#                 j -= 1
#             else:
#                 nums[i], nums[k] = nums[k], nums[i]
#                 k += 1
#                 i += 1

# ----------------------------------------------------------------------------------------------------------------------------
# 19. REMOVE NTH NODE FORM THE END OF THE LIST
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
# Approach 1: Traverse linked list to calculate its total length, then compute position of the node to remove from beginning. Traverse again to that position and delete the node by adjusting pointers. This approach is simple but requires two passes.
# COMPLEXITY ANALYSIS: Time: O(n) Space: O(1)
# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         dummy = ListNode(0)
#         dummy.next = head
#         length = 0 # Step 1: Count length
#         curr = head
#         while curr:
#             length += 1
#             curr = curr.next
#         curr = dummy  # Step 2: Find node before target
#         for _ in range(length - n):
#             curr = curr.next
#         curr.next = curr.next.next # Step 3: Remove node
#         return dummy.next

# Approach 2: Use a dummy node to handle edge cases like deleting the head. Move a fast pointer n steps ahead, then move both fast and slow pointers together until fast reaches the end. The slow pointer will be just before the node to delete, which is then removed.
# COMPLEXITY ANALYSIS: Time: O(n) Space: O(1)
# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         dummy = ListNode(0)
#         dummy.next = head
#         fast = head
#         slow = dummy    
#         for _ in range(n):  # Move fast pointer n steps ahead
#             fast = fast.next
#         while fast:  # Move both pointers until fast reaches end
#             fast = fast.next
#             slow = slow.next
#         slow.next = slow.next.next     # Remove nth node from end
#         return dummy.next

# ---------------------------------------------------------------------------------------------------------------
# 246. Strobogrammatic Number
# Approach: Reverse the number and rotate each digit using valid strobogrammatic mappings. If any digit is invalid, return false immediately. Finally, compare the rotated number with the original to determine if it is strobogrammatic.
# COMPLEXITY ANALYSIS: Time: O(n) Space: O(n)
# def isStrobogrammatic(num: str) -> bool: 
#     rotate = {'0':'0', '1':'1', '8':'8', '9':'6', '6':'9'}
#     rotated = ''
#     for ch in reversed(num):
#         if ch not in rotate:
#             return False
#         rotated += rotate[ch]
#     return rotated == num

# Approach 2: Use two pointers starting from the beginning and end of the string. Maintain a mapping of valid strobogrammatic digit pairs (0↔0, 1↔1, 8↔8, 6↔9, 9↔6). At each step, verify that the left digit maps correctly to the right digit. If any check fails, it’s not strobogrammatic.
# COMPLEXITY ANALYSIS: Time: O(n) Space: O(1)
# def isStrobogrammatic(num: str) -> bool:
#     pairs = {'0':'0', '1':'1', '8':'8', '6':'9', '9':'6'}
#     i, j = 0, len(num) - 1
#     while (i<= j):
#         if num[j] not in pairs or pairs[num[i]] != num[j]:
#             return False
#         i += 1
#         j -= 1
#     return True

# ---------------------------------------------------------------------------------------------------------------
# 2486. Append Characters to string to make subsequence
# https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/description/
# Approach : For each character in t, scan the remaining part of s to find a match. If a character cannot be matched, it must be appended to s. The number of unmatched characters is the answer.
# COMPLEXITY ANALYSIS: Time: O(|s| × |t|) Space: O(1)
# class Solution:
#     def appendCharacters(self, s: str, t: str) -> int:
#         i = 0  # pointer for s
#         count = 0
#         for ch in t:
#             found = False
#             while i < len(s):
#                 if s[i] == ch:
#                     found = True
#                     i += 1
#                     break
#                 i += 1
#             if not found:
#                 count += 1
#         return count

# Approach 2: Use two pointers, i for string s and j for string t, and traverse through s while trying to match characters of t in order. When characters match, move both pointers forward; otherwise, move only the pointer in s. After traversal, the number of characters left unmatched in t, calculated as len(t) − j, is the number of characters that need to be appended.
# COMPLEXITY ANALYSIS: Time: O(|s| + |t|) Space: O(1)
# class Solution:
#     def appendCharacters(self, s: str, t: str) -> int:
#         i = 0
#         j = 0
#         while i < len(s) and j < len(t):
#             if s[i] == t[j]:
#                 j += 1
#             i += 1
#         return len(t) - j

# --------------------------------------------------------------------------------------------
# 1650. Lowest Common Ancestor of a Binary Tree (III)
# https://neetcode.io/problems/lowest-common-ancestor-of-a-binary-tree-iii/question?list=neetcode250

# Approach: Store all ancestors of node p in a set by moving upward using parent pointers.Then move upward from node q; the first node that appears in the set is the Lowest Common Ancestor (LCA).This works because the LCA is the first common node in both ancestor paths.
# COMPLEXITY ANALYSIS: Time: O(h) Space: O(h)  (where h is the height of the tree)
# class Solution:
#     def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
#         ancestors = set()
#         while p:  # Store all ancestors of p
#             ancestors.add(p)
#             p = p.parent
#         while q: # Traverse ancestors of q
#             if q in ancestors:
#                 return q
#             q = q.parent
#         return None