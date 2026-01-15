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

# Approach 2: We repeatedly replace the number with the sum of squares of its digits. One pointer (slow) moves one step at a time, while another pointer (fast) moves two steps at a time. If the number is happy, the fast pointer will eventually reach 1. If the number is not happy, both pointers will meet at the same number, which means a cycle exists and the number will never reach 1. This is called Floyd’s Cycle Detection Algorithm and is preferred because it detects cycles without extra memory.
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
# Approach : Traverse the linked list and store each visited node in a set (or list). If you ever encounter a node that is already present, it means the list has a cycle. If you reach None, then no cycle exists.
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

# Approach 2: Use two pointers starting from the head: a slow pointer that moves one step and a fast pointer that moves two steps. If the list has a cycle, the fast pointer will eventually meet the slow pointer. If the fast pointer reaches the end (None), there is no cycle. This is called Floyd’s Cycle Detection Algorithm and is preferred because it detects cycles without extra memory.
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

# --------------------------------------------------
# 142. Linked List Cycle II
# https://leetcode.com/problems/linked-list-cycle-ii/description/

# Approach: Traverse the linked list and store each visited node in a set. The first node that repeats is the start of the cycle. If the list ends, there is no cycle.
# Complexity: Time: O(n) Space: O(n)
# class Solution:
#     def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         visited = set()
#         curr = head
#         while curr:
#             if curr in visited:
#                 return curr
#             visited.add(curr)
#             curr = curr.next
#         return None
# Example Walkthrough (Brute Force)
# 1 → 2 → 3 → 4
#      ↑       ↓
#      ← ← ← ←
# Visit 1 → store
# Visit 2 → store
# Visit 3 → store
# Visit 4 → store
# Visit 2 again → already visited → cycle starts at 2

# Approach 2: Use slow and fast pointers to detect a cycle. Once they meet, place one pointer at the head and move both one step at a time. The node where they meet again is the start of the cycle.
# Complexity: Time: O(n) Space: O(1)
# class Solution:
#     def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         slow = fast = head
#         while fast and fast.next: # Step 1: Detect cycle
#             slow = slow.next
#             fast = fast.next.next
#             if slow == fast:
#                 break
#         if not fast or not fast.next:
#             return None 
#         n1 = slow # Step 2: Find cycle start
#         n2 = head
#         while n1 != n2:
#             n1 = n1.next
#             n2 = n2.next
#         return n1
# Example Walkthrough (Optimal)
# 1 → 2 → 3 → 4
#      ↑       ↓
#      ← ← ← ←
# Step 1: Detect cycle
# slow and fast meet at node 4 → cycle confirmed
# Step 2: Find cycle start
# n1 = meeting point (4)
# n2 = head (1)
# Move both one step at a time
# They meet at node 2 → cycle starts here

# -----------------------------------------------------------------
# FIND LENGTH OF LOOP: [GFG]
# Approach: Use slow & fast pointers to detect a cycle. Once they meet, keep one pointer fixed. Move the other pointer until it comes back to the same node, counting steps → that count is the loop length
# Mention Floyd’s Cycle Detection + loop traversal — it shows strong linked list understanding and is highly valued in interviews
# Complexity: Time: O(n) Space: O(1)
# class Solution:
#     def countNodesinLoop(self, head):
#         slow = fast = head
#         while fast and fast.next: # Step 1: Detect loop
#             slow = slow.next
#             fast = fast.next.next
#             if slow == fast:
#                 return self.loopLength(slow)
#         return 0
#     def loopLength(self, node):
#         count = 1
#         curr = node.next
#         while curr != node:
#             count += 1
#             curr = curr.next
#         return count
# Example Walkthrough (Optimal)
# 1 → 2 → 3 → 4 → 5
#      ↑           ↓
#      ← ← ← ← ← ←
# slow & fast meet at node 4 → loop exists
# Start counting from 4 → 5 → 2 → 3 → 4
# Total nodes = 4

# ----------------------------------------------------------------------------------------
# Split A Circular Linked list into two halves [GFG]:
# Approach: We use slow and fast pointers to find the middle of the circular linked list. Once the middle is found, we split the list into two halves and carefully update pointers so both halves remain circular. Finally, we return the heads of the two circular linked lists.
# COMPLEXITY ANALYSIS: Time= O(n)   Space= O(1)
# class Solution:
#     def splitList(self, head):
#         if not head or head.next == head:
#             return head, None  # Only one node
#         slow = head
#         fast = head.next
#         while fast != head and fast.next != head:  # Find middle using slow & fast
#             slow = slow.next
#             fast = fast.next
#             if fast.next != head:
#                 fast = fast.next
#         head1 = head  # Heads of the two lists
#         head2 = slow.next
#         fast.next = head2  # Make second list circular
#         slow.next = head1 # Make first list circular
#         return head1, head2 # Return pair of heads
# Example Walkthrough
# Input Circular List: 1 → 2 → 3 → 4 → 5 → back to 1
# Step 1: Find middle
# slow moves one step, fast moves two steps
# When fast reaches near the head again, slow is at 3
# slow = 3
# fast = 5
# Step 2: Split the list
# First list head = 1
# Second list head = slow.next = 4
# Step 3: Make both lists circular
# First Circular List:
# 1 → 2 → 3 → back to 1
# Second Circular List:
# 4 → 5 → back to 4
# Step 4: Return result
# (head1, head2) = (1, 4)

# -----------------------------------------------------------------------------
# 287. Find the Duplicate Number
# https://leetcode.com/problems/find-the-duplicate-number/description/
# # Approach: We iterate through the array and keep track of numbers we’ve already seen using a set. If a number appears again, it means it’s the duplicate, so we return it immediately.This avoids nested loops and makes detection fast.
# COMPLEXITY ANALYSIS: Time= O(n)   Space= O(n)
# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         visited = set()
#         for num in nums:
#             if num in visited:
#                 return num
#             visited.add(num)
#         return -1
# Example Walkthrough
# Input: nums = [1, 3, 4, 2, 2]
# Step-by-step: visited = {}
# Read 1 → not in set → add → {1}
# Read 3 → not in set → add → {1, 3} 
# Read 4 → not in set → add → {1, 3, 4}
# Read 2 → not in set → add → {1, 2, 3, 4}
# Read 2 → already in set ✅ → return 2
# Output: 2

# Approach 2: Treat the array like a linked list where index → nums[index]. Because one number is duplicated, a cycle is guaranteed. Using slow and fast pointers, we first detect the cycle, then find the entry point — which is the duplicate number.
# COMPLEXITY ANALYSIS: Time= O(n)   Space= O(1)
# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         # Phase 1: Detect cycle
#         slow = 0
#         fast = 0
#         while True:
#             slow = nums[slow]
#             fast = nums[nums[fast]]
#             if slow == fast:
#                 break
#         # Phase 2: Find entry point of cycle (duplicate)
#         n1 = 0
#         n2 = slow
#         while n1 != n2:
#             n1 = nums[n1]
#             n2 = nums[n2]
#         return n1
# Example Walkthrough=> Input:nums = [1, 3, 4, 2, 2]
# Phase 1: Detect Cycle
# Step	slow = nums[slow]	fast = nums[nums[fast]]
# start	0	0
# 1	1	3
# 2	3	4
# 3	2	4
# 4	4	4 ← meet
# Cycle detected ✔️
# Phase 2: Find Duplicate
# n1 = 0  n2 = slow = 4
# Move both one step at a time:
# n1	n2
# nums[0] = 1	nums[4] = 2
# nums[1] = 3	nums[2] = 4
# nums[3] = 2	nums[4] = 2 ← meet
# ✅ Duplicate = 2

# -------------------------------------------------------------------------
# 234. Palindrome LinkedList:
# https://leetcode.com/problems/palindrome-linked-list/description/
# Approach: Traverse the linked list and store all values in a list. Then use two pointers (start & end) to check if the list reads the same forward and backward. If all values match → palindrome.
# COMPLEXITY ANALYSIS: Time= O(n)   Space= O(n)
# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         arr = []
#         # Store values in list
#         while head:
#             arr.append(head.val)
#             head = head.next
#         # Two-pointer check
#         i, j = 0, len(arr) - 1
#         while i < j:
#             if arr[i] != arr[j]:
#                 return False
#             i += 1
#             j -= 1
#         return True
# Example Walkthrough= Input: 1 → 2 → 2 → 1
# Convert to list → [1, 2, 2, 1]
# Compare:
# 1 == 1 ✅
# 2 == 2 ✅
# All matched → Palindrome

# Approach 2: We use slow and fast pointers to find the middle of the linked list. Then we reverse the second half and compare it with the first half node by node. If all values match, the linked list is a palindrome.
# COMPLEXITY ANALYSIS: Time= O(n)   Space= O(1)
# class Solution:
#     def reverseLL(self, curr):
#         prev = None
#         while curr:
#             nxt = curr.next      # store next
#             curr.next = prev     # reverse link
#             prev = curr          # move prev
#             curr = nxt           # move curr
#         return prev
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         if not head or not head.next:
#             return True
#         # Step 1: Find middle using slow & fast
#         slow = fast = head
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#         # Step 2: Reverse second half
#         p2 = self.reverseLL(slow)
#         p1 = head
#         # Step 3: Compare both halves
#         while p2:
#             if p1.val != p2.val:
#                 return False
#             p1 = p1.next
#             p2 = p2.next
#         return True
# Example Walkthrough=> Input: 1 → 2 → 2 → 1
# Step 1: Find middle
# slow stops at second 2
# Step 2: Reverse second half
# 2 → 1 becomes 1 → 2
# Step 3: Compare
# 1 == 1 ✅
# 2 == 2 ✅
# ➡️ Palindrome → True

# 2130. Maximum Twin SUm of a Linked List
# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
# Approach: Traverse the linked list and store all node values in a list. Then use two pointers on the list—one from the start and one from the end—to compute twin sums and track the maximum.
# COMPLEXITY ANALYSIS: Time= O(n)   Space= O(n)
# class Solution:
#     def pairSum(self, head: Optional[ListNode]) -> int:
#         arr = []
#         curr = head
#         while curr:
#             arr.append(curr.val)
#             curr = curr.next
#         i, j = 0, len(arr) -1
#         max_sum = 0
#         while i < j:
#             max_sum = max(max_sum, arr[i] + arr[j])
#             i +=1
#             j -= 1
#         return max_sum    
# Example Walkthrough => Input: 5 → 4 → 2 → 1
# Convert to list → arr = [5, 4, 2, 1]
# Twin pairs:
# arr[0] + arr[3] = 5 + 1 = 6
# arr[1] + arr[2] = 4 + 2 = 6
# Maximum twin sum = 6

# Approach 2: Use slow and fast pointers to find the middle of the linked list. Reverse the second half of the list, then walk one pointer from the start and one from the reversed half together, computing twin sums and tracking the maximum.
# COMPLEXITY ANALYSIS: Time= O(n)   Space= O(1)
# class Solution:
#     def pairSum(self, head: Optional[ListNode]) -> int:
#         slow = fast = head 
#         while fast and fast.next:  # Step 1: Find middle
#             slow = slow.next
#             fast = fast.next.next
#         # Step 2: Reverse second half
#         prev = None 
#         curr = slow
#         while curr:
#             nxt = curr.next
#             curr.next = prev
#             prev = curr
#             curr = nxt
#          # Step 3: Compute max twin sum
#         max_sum = 0
#         p1, p2 = head, prev
#         while p2:
#             max_sum = max(max_sum, p1.val + p2.val)
#             p1 = p1.next
#             p2 = p2.next
#         return max_sum
# Walkthrough (Example) Input: head = [5, 4, 2, 1]
# Twin pairs:
# Node 0 & Node 3 → 5 + 1 = 6
# Node 1 & Node 2 → 4 + 2 = 6
# Steps:
# Use slow/fast pointers → slow stops at 2 (middle).
# Reverse second half → 1 → 2
# Compare pairs:
# 5 + 1 = 6
# 4 + 2 = 6
# Maximum twin sum = 6

#---------------------------------------------------------------------------------------------------------------------------
# 457. Circular Array Loop

# Approach 1: For every index, we try to simulate the movement step by step.We keep track of the indices visited only for that starting index. If we ever revisit a previously visited index with the same direction, it means we found a cycle.
# Complexity Analysis: Time: O(n²) Space: O(n)
# class Solution:
#     def circularArrayLoop(self, nums):
#         n = len(nums)
#         for i in range(n):
#             visited = set()
#             curr = i
#             direction = nums[i] > 0
#             while True:
#                 if (nums[curr] > 0) != direction:
#                     break
#                 if curr in visited:
#                     return True
#                 visited.add(curr)
#                 next_idx = (curr + nums[curr]) % n
#                 if next_idx == curr:
#                     break
#                 curr = next_idx
#         return False


# Approach 2: Visited Marking Optimization => This improves brute force by remembering already explored indices globally. Once a path is confirmed invalid, we mark those indices so we don’t reprocess them again.
# Complexity Analysis: Time: O(n) Space: O(n)
# class Solution:
#     def circularArrayLoop(self, nums):
#         n = len(nums)
#         visited = [False] * n
#         for i in range(n):
#             if visited[i]:
#                 continue
#             curr = i
#             direction = nums[i] > 0
#             path = set()
#             while True:
#                 if visited[curr] or (nums[curr] > 0) != direction:
#                     break
#                 if curr in path:
#                     return True
#                 path.add(curr)
#                 visited[curr] = True
#                 next_idx = (curr + nums[curr]) % n
#                 if next_idx == curr:
#                     break
#                 curr = next_idx
#         return False
# Example Walkthrough=> nums = [-1, 2]
# Index 0: self-loop → invalid → mark visited
# Index 1: self-loop → invalid → mark visited
# ✔ No valid cycle

# Approach 3: Treat the array like a linked list, where each index points to the next index. Use: Slow pointer → moves 1 step Fast pointer → moves 2 steps. If there is a cycle, both pointers will eventually meet (Floyd’s Cycle Detection) 
# Complexity Analysis: Time: O(n) Space: O(1)
# class Solution:
#     def circularArrayLoop(self, nums):
#         n = len(nums)
#         def next_idx(i):
#             return (i + nums[i]) % n
#         for i in range(n):
#             slow = fast = i
#             direction = nums[i] > 0
#             while True:
#                 slow_next = next_idx(slow)
#                 fast_next = next_idx(fast)
#                 fast_next2 = next_idx(fast_next)
#                 if (nums[slow] > 0) != direction or \
#                    (nums[fast] > 0) != direction or \
#                    (nums[fast_next] > 0) != direction:
#                     break
#                 slow = slow_next
#                 fast = fast_next2
#                 if slow == fast:
#                     if slow == next_idx(slow):
#                         break
#                     return True
#         return False
# Example Walkthrough => nums = [2, -1, 1, 2, 2]
# From index 0:
# slow: 0 → 2 → 3
# fast: 0 → 3 → 0
# They meet ✔ → valid cycle