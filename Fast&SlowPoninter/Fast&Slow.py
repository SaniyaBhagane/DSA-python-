# 202. Happy Number
# https://leetcode.com/problems/happy-number/description/

# Approach: Repeatedly replace the number with the sum of squares of its digits and store each intermediate result in a list. If the number becomes 1, it is a happy number. If any number repeats, a cycle is detected, meaning it will never reach 1, so return false.
# COMPLEXITY ANALYSIS: Time = O(k²)  Space = O(k)
# class Solution:
#     def sumOfSquareOfDigits(self, n):
#         total = 0
#         while n > 0:
#             dig = n % 10
#             total += dig * dig
#             n //= 10
#         return total

#     def isHappy(self, n: int) -> bool:
#         seen = []
#         while n != 1:
#             if n is seen:
#                 return False
#             seen.append(n)
#             n = self.sumOfSquareOfDigits(n)
#         return True
# Example Walkthrough 
# Input: n = 19
# Step 1:
# seen = []
# n = 19
# Digits: 1, 9
# Sum of squares = 1² + 9² = 82
# seen = [19]
# n = 82
# Step 2:
# n = 82
# Digits: 8, 2
# Sum of squares = 8² + 2² = 68
# seen = [19, 82]
# n = 68
# Step 3:
# n = 68
# Digits: 6, 8
# Sum of squares = 6² + 8² = 100
# seen = [19, 82, 68]
# n = 100
# Step 4:
# n = 100
# Digits: 1, 0, 0
# Sum of squares = 1² = 1
# n = 1
# Final Result: Since the number becomes 1, the function returns True (Happy Number).

# Approach 2: We repeatedly replace the number with the sum of squares of its digits. One pointer (slow) moves one step at a time, while another pointer (fast) moves two steps at a time. If the number is happy, the fast pointer will eventually reach 1. If the number is not happy, both pointers will meet at the same number, which means a cycle exists and the number will never reach 1.
# Complexity Analysis: Time: O(log n) per iteration  Space: O(1) (no extra memory)
# class Solution:
#     def sumOfSquareOfDigits(self, n):
#         total = 0
#         while n > 0:
#             dig = n % 10
#             total += dig * dig
#             n //= 10
#         return total
#     def isHappy(self, n: int) -> bool:
#         slow = fast = n
#         while True:
#             slow = self.sumOfSquareOfDigits(slow)
#             fast = self.sumOfSquareOfDigits(
#                 self.sumOfSquareOfDigits(fast)
#             )
#             if fast == 1:
#                 return True
#             if slow == fast:
#                 return False
# Example Walkthrough:
# Input: n = 19
# Initial:
# slow = 19
# fast = 19
# Step 1:
# slow = sumSq(19) = 1² + 9² = 82
# fast = sumSq(sumSq(19))
#      = sumSq(82)
#      = 8² + 2² = 68
# slow = 82
# fast = 68
# Step 2:
# slow = sumSq(82) = 8² + 2² = 68
# fast = sumSq(sumSq(68))
#      = sumSq(100)
#      = 1² = 1
# slow = 68
# fast = 1
# Final Result:
# Since fast pointer reaches 1, the number is a Happy Number and the function returns True.

# ------------------------------------------------------------------
# 876. Middle of the LinkedList
# https://leetcode.com/problems/middle-of-the-linked-list/description/
# Approach : First count the total number of nodes. Then traverse again until you reach the middle node (length // 2) and return it.
# Complexity: Time: O(n) Space: O(1)
# class Solution:
#     def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]: 
#         length = 0
#         curr = head
#         while curr:
#             length += 1
#             curr = curr.next
#         curr = head
#         for _ in range(length // 2):
#             curr = curr.next
#         return curr
# Example Walkthrough
# Input:
# 1 → 2 → 3 → 4 → 5
# Step	slow	fast
# 1	2	3
# 2	3	5
# fast.next becomes None, loop stops → slow = 3 (middle)

# Approach 2: To find the middle of a linked list, we can use two pointers starting at the head. The slow pointer moves one step at a time while the fast pointer moves two steps. When the fast pointer reaches the end of the list, the slow pointer will be at the middle node, which is returned as the result.
# Complexity: Time: O(n) Space: O(1)
# class Solution:
    # def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     slow = fast = head
    #     while fast and fast.next:
    #         slow = slow.next
    #         fast = fast.next.next
    #     return slow
#  Example Walkthrough
# Input: 1 → 2 → 3 → 4 → 5 → 6
# Step	slow	fast
# 1	2	3
# 2	3	5
# 3	4	None
# Loop ends → slow = 4
# Output: 4 (second middle, as required)

# ------------------------------------------------------------------------
# 141. Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/description/
# Apprach : Traverse the linked list and store each visited node in a set (or list). If you ever encounter a node that is already present, it means the list has a cycle. If you reach None, then no cycle exists.
# Complexity: Time: O(n) Space: O(n)
# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         visited = set()
#         curr = head
#         while curr:
#             if curr in visited:
#                 return True
#             visited.add(curr)
#             curr = curr.next
#         return False 
# Example Walkthrough
# Input:
# 1 → 2 → 3 → 4
#      ↑       ↓
#      ← ← ← ←
# Visit node 1 → store it
# Visit node 2 → store it
# Visit node 3 → store it
# Visit node 4 → store it
# Next node is 2 again → already visited → cycle detected
# Output: True

# Approach 2: Use two pointers starting from the head: a slow pointer that moves one step and a fast pointer that moves two steps. If the list has a cycle, the fast pointer will eventually meet the slow pointer. If the fast pointer reaches the end (None), there is no cycle.
# Complexity: Time: O(n) Space: O(1)
# Definition for singly-linked list.
# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         slow = fast = head
#         while fast != None and fast.next != None:
#             slow = slow.next
#             fast = fast.next.next
#             if (slow == fast):
#                 return True
#         return False 
# Example Walkthrough (Cycle Exists)
# Input:
# 1 → 2 → 3 → 4
#      ↑       ↓
#      ← ← ← ←
# Step	slow	fast
# 1	2	3
# 2	3	1
# 3	4	3
# 4	1	1
# Pointers meet → cycle detected → return True