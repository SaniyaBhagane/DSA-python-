# 1929: CONCATENATION OF ARRAY
# BRUTEFORCE: Using + Operator
# class Solution:
#     def getConcatenation(self, nums: List[int]) -> List[int]:
#         return nums + nums  # Concatenate the list with itself

# APPROACH 2: Using Loop and Append Method
# class Solution:
#     def getConcatenation(self, nums: List[int]) -> List[int]:
#         result = []
#         for num in nums:
#             result.append(num)  # Add each element from nums
#         for num in nums:
#             result.append(num)  # Add each element again
#         return result

# APPROACH 3: Using Loop and Changing Element Value
# class Solution:
#     def getConcatenation(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         result = [0] * (2 * n)  # Create a new list of size 2n
#         for i in range(n):
#             result[i] = nums[i]      # Copy the first part
#             result[i + n] = nums[i]  # Copy the second part
#         return result

# APPROACH 4: Using Extend Method
# class Solution:
#     def getConcatenation(self, nums: List[int]) -> List[int]:
#         nums.extend(nums)  # Extend the list with itself
#         return nums

# APPROACH 5: Using * Operator
# class Solution:
#     def getConcatenation(self, nums: List[int]) -> List[int]:
#         return nums * 2  # Repeat the list twice


# -------------------------------------------------------------------------------------------------
# 217: CONTAINS DUPLICATES

# BRUTEFORCE APPROACH
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         nums.sort()
#         for i in range(1, len(nums)):
#             if nums[i] == nums[i-1]:
#                 return True
#         return False
    
# APPROACH 2 => USING SETS
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         num_set = set()

#         for n in nums:
#             if n in num_set:
#                 return True
#             num_set.add(n)
        
#         return False

# APPROACH 3 => USING SETS AND CONSIDERING LENGTH
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         return True if len(set(nums)) < len(nums) else False


# -------------------------------------------------------------------------------------------------
# 242: VALID ANAGRAM

# BRUTEFIRCE: SORTING
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         sorted_s = sorted(s)
#         sorted_t = sorted(t)
#         if sorted_s == sorted_t: 
#             return True
#         return False

# APPROACH 2: Hash Table
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         count = defaultdict(int)
#         # Count the frequency of characters in string s
#         for x in s:
#             count[x] += 1
#         # Decrement the frequency of characters in string t
#         for x in t:
#             count[x] -= 1        
#         # Check if any character has non-zero frequency
#         for val in count.values():
#             if val != 0:
#                 return False       
#         return True

# APPROACH 3: Hash Table (26-length Array Counting)
# OPTIMAL
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         count = [0] * 26        
#         # Count the frequency of characters in string s
#         for x in s:
#             count[ord(x) - ord('a')] += 1
#         # Decrement the frequency of characters in string t
#         for x in t:
#             count[ord(x) - ord('a')] -= 1        
#         # Check if any character has non-zero frequency
#         for val in count:
#             if val != 0:
#                 return False        
#         return True
    
    
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


# -------------------------------------------------------------------------------------------------
# 14. LONGEST COMMON PREFIX


# -------------------------------------------------------------------------------------------------
