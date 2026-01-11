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

# Approach => Start with first row as [1]. For each subsequent row, start and end with 1. Each middle element is sum of two elements above it from previous row.
# COMPLEXITY ANALYSIS:
# Time Complexity: O(N^2), where N is the number of rows in the triangle.  
# Space Complexity: O(1), as we are using only a constant amount of extra space

# WORKFLOW: 1️. Start with the first row
# Initialize the result with [[1]] since every Pascal’s Triangle begins with 1.
# 2. Generate remaining rows
# Repeat numRows - 1 times to build the rest of the triangle.
# 3️. Pad previous row with zeros
# Add 0 at the beginning and end of the last row to handle edge values easily.
# 4. Create the new row
# Add adjacent elements from the padded row to form the next row.
# 5️. Store the row
# Append the newly formed row to the result list.
# 6️. Return the triangle
# After all rows are generated, return the final list.

# class Solution:
#     def generate(self, numRows: int) -> List[List[int]]:
#         res = [[1]]
#         row = []
#         for _ in range(numRows-1):
#             dummyRow = [0] + res[-1] + [0]
#             for i in range(len(res[-1]) + 1):
#                 row.append(dummyRow[i] + dummyRow[i+1])
#             res.append(row)
#         return res

# --------------------------------------------------------------------------
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

# ------------------------------------LINKED LIST--------------------------------------
# 707. Design a Linked list
# 
# Approach: The linked list is implemented by maintaining a head pointer and a size variable to track the number of nodes. For accessing a value, the list is traversed from the head up to the required index. Insertion at the head is done by creating a new node and pointing it to the current head, while insertion at the tail requires traversing to the last node and attaching the new node. Insertion at a specific index is handled by stopping at the previous node and adjusting pointers to insert the new node in between. Deletion works similarly by bypassing the node at the given index and reconnecting the surrounding nodes. The size is updated after every insertion or deletion to keep the structure consistent.
# COMPLEXITY ANALYSIS: Time => get, addAtTail, addAtIndex, deleteAtIndex:O(n) ddAtHead: O(1)

# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None

# class MyLinkedList:
#     def __init__(self):
#         self.head = None
#         self.size = 0

#     def get(self, index: int) -> int:
#         if index < 0 or index >= self.size:
#             return -1
#         curr = self.head
#         for _ in range(index):
#             curr = curr.next
#         return curr.val        

#     def addAtHead(self, val: int) -> None:
#         newNode = Node(val)
#         newNode.next = self.head
#         self.head = newNode
#         self.size += 1 

#     def addAtTail(self, val: int) -> None:
#         newNode = Node(val)
#         if not self.head:
#             self.head = newNode
#         else:
#             curr = self.head
#             while curr.next:
#                 curr = curr.next
#             curr.next = newNode
#         self.size += 1
        
#     def addAtIndex(self, index: int, val: int) -> None:
#         if index < 0 or index > self.size:
#             return
#         if index == 0:
#             self.addAtHead(val)
#             return
#         curr = self.head
#         for _ in range(index - 1):
#             curr = curr.next
#         newNode = Node(val)
#         newNode.next = curr.next
#         curr.next = newNode
#         self.size += 1

#     def deleteAtIndex(self, index: int) -> None:
#         if index < 0 or index >= self.size:
#             return
#         if index == 0:
#             self.head = self.head.next
#         else:
#             curr = self.head
#             for _ in range(index - 1):
#                 curr = curr.next
#             curr.next = curr.next.next
#         self.size -= 1
